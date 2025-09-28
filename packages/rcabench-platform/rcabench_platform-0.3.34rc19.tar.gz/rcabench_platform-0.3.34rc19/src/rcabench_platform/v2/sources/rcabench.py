import json
from functools import partial
from pathlib import Path
from typing import Any

import networkx as nx
import pandas as pd
import polars as pl
from drain3 import TemplateMiner
from drain3.drain import LogCluster
from drain3.file_persistence import FilePersistence
from drain3.template_miner_config import TemplateMinerConfig

from ..datasets.rcabench import FAULT_TYPES, rcabench_get_service_name
from ..datasets.train_ticket import extract_path
from ..logging import logger, timeit
from ..utils.serde import load_json
from .convert import DatapackLoader, DatasetLoader, Label


def replace_time_col(lf: pl.LazyFrame, col_name: str) -> pl.LazyFrame:
    lf = lf.with_columns(pl.col(col_name)).rename({col_name: "time"})
    return lf


def unnest_json_col(lf: pl.LazyFrame, col_name: str, dtype: pl.Struct) -> pl.LazyFrame:
    lf = lf.with_columns(pl.col(col_name).str.json_decode(dtype).struct.unnest()).drop(col_name)
    return lf


def convert_metrics(src: Path) -> pl.LazyFrame:
    lf = pl.scan_parquet(src)
    original_columns: list[str] = lf.collect_schema().names()

    selected_columns = [
        "TimeUnix",
        "MetricName",
        "Value",
        "ResourceAttributes",
    ]
    additional_columns = [
        "ServiceName",
        "Attributes",
    ]
    for col in additional_columns:
        if col in original_columns:
            selected_columns.append(col)

    lf = lf.select(selected_columns)

    lf = replace_time_col(lf, "TimeUnix")

    lf = lf.rename({"MetricName": "metric", "Value": "value"})

    if "ServiceName" in original_columns:
        lf = lf.rename({"ServiceName": "service_name"})
    else:
        lf = lf.with_columns(pl.lit(None, dtype=pl.String).alias("service_name"))

    attr_cols = []

    resource_attributes = pl.Struct(
        [
            pl.Field("k8s.node.name", pl.String),
            pl.Field("k8s.namespace.name", pl.String),
            pl.Field("k8s.statefulset.name", pl.String),
            pl.Field("k8s.deployment.name", pl.String),
            pl.Field("k8s.replicaset.name", pl.String),
            pl.Field("k8s.pod.name", pl.String),
            pl.Field("k8s.container.name", pl.String),
        ]
    )
    lf = unnest_json_col(lf, "ResourceAttributes", resource_attributes)
    attr_cols += [field.name for field in resource_attributes.fields]

    if "Attributes" in original_columns:
        attributes = pl.Struct(
            [
                pl.Field("destination_workload", pl.String),
                pl.Field("source_workload", pl.String),
                pl.Field("destination", pl.String),
                pl.Field("source", pl.String),
            ]
        )
        lf = unnest_json_col(lf, "Attributes", attributes)
        attr_cols += [field.name for field in attributes.fields]

    lf = lf.rename({col: "attr." + col for col in attr_cols})

    lf = lf.sort("time")

    return lf


def convert_metrics_histogram(src: Path) -> pl.LazyFrame:
    lf = pl.scan_parquet(src).select(
        "TimeUnix",
        "MetricName",
        "ServiceName",
        "ResourceAttributes",
        "Attributes",
        "Count",
        "Sum",
        # "BucketCounts",
        # "ExplicitBounds",
        "Min",
        "Max",
        # "AggregationTemporality",
    )

    lf = replace_time_col(lf, "TimeUnix")

    lf = lf.rename(
        {
            "MetricName": "metric",
            "ServiceName": "service_name",
            "Count": "count",
            "Sum": "sum",
            "Min": "min",
            "Max": "max",
        }
    )

    lf = lf.with_columns(
        pl.col("count").cast(pl.Float64),
        pl.col("sum").cast(pl.Float64),
        pl.col("min").cast(pl.Float64),
        pl.col("max").cast(pl.Float64),
    )

    resource_attributes = pl.Struct(
        [
            pl.Field("pod.name", pl.String),
            pl.Field("service.name", pl.String),
            pl.Field("service.namespace", pl.String),
        ]
    )
    lf = unnest_json_col(lf, "ResourceAttributes", resource_attributes)
    lf = lf.rename(
        {
            "pod.name": "attr.k8s.pod.name",
            "service.name": "attr.k8s.service.name",
            "service.namespace": "attr.k8s.namespace.name",
        }
    )

    attributes = pl.Struct(
        [
            pl.Field("jvm.gc.action", pl.String),
            pl.Field("jvm.gc.name", pl.String),
            pl.Field("destination", pl.String),
            pl.Field("source", pl.String),
        ]
    )
    lf = unnest_json_col(lf, "Attributes", attributes)
    lf = lf.rename({field.name: "attr." + field.name for field in attributes.fields})

    lf = lf.sort("time")
    return lf


def convert_traces(src: Path, filter: bool = False) -> pl.DataFrame:
    lf = pl.scan_parquet(src).select(
        "Timestamp",
        "TraceId",
        "SpanId",
        "ParentSpanId",
        "SpanName",
        "SpanKind",
        "ServiceName",
        "ResourceAttributes",
        "SpanAttributes",
        "Duration",
        "StatusCode",
    )

    lf = replace_time_col(lf, "Timestamp")

    lf = lf.rename(
        {
            "TraceId": "trace_id",
            "SpanId": "span_id",
            "ParentSpanId": "parent_span_id",
            "SpanName": "span_name",
            "ServiceName": "service_name",
            "Duration": "duration",
            "SpanKind": "attr.span_kind",
            "StatusCode": "attr.status_code",
        }
    )

    resource_attributes = pl.Struct(
        [
            pl.Field("pod.name", pl.String),
            pl.Field("service.name", pl.String),
            pl.Field("service.namespace", pl.String),
        ]
    )
    lf = unnest_json_col(lf, "ResourceAttributes", resource_attributes)
    lf = lf.rename(
        {
            "pod.name": "attr.k8s.pod.name",
            "service.name": "attr.k8s.service.name",
            "service.namespace": "attr.k8s.namespace.name",
        }
    )

    span_attributes = pl.Struct(
        [
            # "telemetry.sdk.language": "go"
            pl.Field("http.method", pl.String),
            pl.Field("http.request_content_length", pl.String),
            pl.Field("http.response_content_length", pl.String),
            pl.Field("http.status_code", pl.String),
            #
            # "telemetry.sdk.language": "java"
            pl.Field("http.request.method", pl.String),
            pl.Field("http.response.status_code", pl.String),
            #
        ]
    )
    lf = unnest_json_col(lf, "SpanAttributes", span_attributes)

    coalesce_columns = [
        ("http.request.method", "http.method"),
        ("http.response.status_code", "http.status_code"),
    ]
    lf = lf.with_columns([pl.coalesce(*cols).alias(cols[0]) for cols in coalesce_columns])
    lf = lf.drop([cols[1] for cols in coalesce_columns])

    lf = lf.with_columns(
        pl.col("http.request_content_length").cast(pl.UInt64),
        pl.col("http.response_content_length").cast(pl.UInt64),
        pl.col("http.response.status_code").cast(pl.UInt16),
    )

    lf = lf.rename(
        {
            "http.request.method": "attr.http.request.method",
            "http.response.status_code": "attr.http.response.status_code",
            "http.request_content_length": "attr.http.request.content_length",
            "http.response_content_length": "attr.http.response.content_length",
        }
    )

    if filter:
        traces_with_long_spans = lf.filter(pl.col("duration") > 2_000_000_000).select("trace_id").unique()
        lf = lf.join(traces_with_long_spans, on="trace_id", how="anti")

    lf = lf.sort("time")
    df = lf.collect()
    df = df.with_columns(
        [
            pl.when(pl.col("service_name").is_in(["loadgenerator", "ts-ui-dashboard"]))
            .then(pl.col("span_name").map_elements(extract_path, return_dtype=pl.String))
            .otherwise(pl.col("span_name"))
            .alias("span_name")
        ]
    )
    del lf

    return df


def convert_logs(src: Path) -> pl.DataFrame:
    lf = pl.scan_parquet(src).select(
        "Timestamp",
        "TraceId",
        "SpanId",
        "SeverityText",
        "ServiceName",
        "Body",
        "ResourceAttributes",
        # "LogAttributes",
    )

    lf = replace_time_col(lf, "Timestamp")

    lf = lf.rename(
        {
            "TraceId": "trace_id",
            "SpanId": "span_id",
            "ServiceName": "service_name",
            "SeverityText": "level",
            "Body": "message",
        }
    )

    lf = lf.with_columns(
        pl.col("level").str.to_uppercase(),
    )

    # Filter out ts-ui-dashboard logs
    lf = lf.filter(pl.col("service_name") != "ts-ui-dashboard")

    resource_attributes = pl.Struct(
        [
            pl.Field("pod.name", pl.String),
            pl.Field("service.name", pl.String),
            pl.Field("service.namespace", pl.String),
        ]
    )
    lf = unnest_json_col(lf, "ResourceAttributes", resource_attributes)
    lf = lf.rename(
        {
            "pod.name": "attr.k8s.pod.name",
            "service.name": "attr.k8s.service.name",
            "service.namespace": "attr.k8s.namespace.name",
        }
    )

    lf = lf.sort("time")

    # Process templates directly within convert_logs
    df = lf.collect()

    # Extract unique messages for template processing
    unique_messages = df.select("message").unique()

    if unique_messages.height > 0:
        logger.info(f"Processing {unique_messages.height} unique log messages for template extraction")

        # Process messages with Drain3
        config_path = Path("data/rcabench_dataset/drain_template/drain_ts.ini")
        persistence_path = Path("data/rcabench_dataset/drain_template/drain_ts.bin")

        template_miner = create_template_miner(config_path, persistence_path)

        message_mappings = []
        for message in unique_messages["message"].to_list():
            if message:  # Skip empty messages
                result = template_miner.add_log_message(message)
                template_id = result["cluster_id"]
                cluster = template_miner.drain.id_to_cluster.get(template_id)
                if isinstance(cluster, LogCluster):
                    log_template = cluster.get_template()
                else:
                    log_template = ""

                message_mappings.append(
                    {
                        "message": message,
                        "template_id": template_id,
                        "log_template": log_template,
                    }
                )

        del template_miner

        # Create template mapping DataFrame
        template_mapping_df = pl.DataFrame(
            message_mappings, schema={"message": pl.String, "template_id": pl.UInt16, "log_template": pl.String}
        )

        # Join with log data to add template columns
        df = (
            df.join(template_mapping_df, on="message", how="left")
            .with_columns(
                [
                    pl.col("template_id").alias("attr.template_id"),
                    pl.col("log_template").alias("attr.log_template"),
                ]
            )
            .drop(["template_id", "log_template"])
        )

        del template_mapping_df, unique_messages

    return df


def convert_conclusion(src: Path) -> pl.LazyFrame:
    # Check if file exists and has content
    if not src.exists():
        logger.warning(f"Conclusion CSV file does not exist: {src}")
        # Return empty LazyFrame with correct schema
        return pl.LazyFrame(
            schema={
                "SpanName": pl.String,
                "Issues": pl.String,
                "AbnormalAvgDuration": pl.Float64,
                "NormalAvgDuration": pl.Float64,
                "AbnormalSuccRate": pl.Float64,
                "NormalSuccRate": pl.Float64,
                "AbnormalP90": pl.Float64,
                "NormalP90": pl.Float64,
                "AbnormalP95": pl.Float64,
                "NormalP95": pl.Float64,
                "AbnormalP99": pl.Float64,
                "NormalP99": pl.Float64,
            }
        )

    try:
        lf = pl.scan_csv(
            src,
            schema={
                "SpanName": pl.String,
                "Issues": pl.String,
                "AbnormalAvgDuration": pl.Float64,
                "NormalAvgDuration": pl.Float64,
                "AbnormalSuccRate": pl.Float64,
                "NormalSuccRate": pl.Float64,
                "AbnormalP90": pl.Float64,
                "NormalP90": pl.Float64,
                "AbnormalP95": pl.Float64,
                "NormalP95": pl.Float64,
                "AbnormalP99": pl.Float64,
                "NormalP99": pl.Float64,
            },
        )
        return lf
    except Exception as e:
        logger.warning(f"Error reading conclusion CSV {src}: {e}")
        # Return empty LazyFrame with correct schema
        return pl.LazyFrame(
            schema={
                "SpanName": pl.String,
                "Issues": pl.String,
                "AbnormalAvgDuration": pl.Float64,
                "NormalAvgDuration": pl.Float64,
                "AbnormalSuccRate": pl.Float64,
                "NormalSuccRate": pl.Float64,
                "AbnormalP90": pl.Float64,
                "NormalP90": pl.Float64,
                "AbnormalP95": pl.Float64,
                "NormalP95": pl.Float64,
                "AbnormalP99": pl.Float64,
                "NormalP99": pl.Float64,
            }
        )


class RcabenchDatapackLoader(DatapackLoader):
    def __init__(self, src_folder: Path, datapack: str) -> None:
        self._src_folder = src_folder
        self._datapack = datapack
        self._service = rcabench_get_service_name(datapack)

        injection = load_json(path=self._src_folder / "injection.json")
        self._fault_type: str = FAULT_TYPES[injection["fault_type"]]
        self._injection_config = json.loads(injection["display_config"])

    def name(self) -> str:
        return self._datapack

    def labels(self) -> list[Label]:
        if self._fault_type.startswith("Network"):
            injection_point = self._injection_config.get("injection_point")
            assert isinstance(injection_point, dict)

            source_service = injection_point.get("source_service")
            target_service = injection_point.get("target_service")

            if source_service and target_service:
                return [
                    Label(level="service", name=source_service),
                    Label(level="service", name=target_service),
                ]

        return [Label(level="service", name=self._service)]

    def data(self) -> dict[str, Any]:
        ans: dict[str, Any] = {
            "env.json": self._src_folder / "env.json",
            "injection.json": self._src_folder / "injection.json",
            "conclusion.parquet": convert_conclusion(self._src_folder / "conclusion.csv"),
        }

        converters = {
            "_traces": convert_traces,
            "_logs": convert_logs,
            "_metrics": convert_metrics,
            "_metrics_sum": convert_metrics,
            "_metrics_histogram": convert_metrics_histogram,
        }

        for key, func in converters.items():
            for prefix in ("normal", "abnormal"):
                name = f"{prefix}{key}.parquet"
                ans[name] = func(self._src_folder / name)

        return ans


def create_template_miner(config_path: Path, persistence_path: Path) -> TemplateMiner:
    """Create a Drain3 template miner with file persistence and config."""
    persistence = FilePersistence(str(persistence_path))
    miner_config = TemplateMinerConfig()
    miner_config.load(str(config_path))
    return TemplateMiner(persistence, config=miner_config)


def extract_unique_log_messages(src_root: Path, datapacks: list[str]) -> pl.DataFrame:
    """Extract unique log messages from all datapacks, excluding ts-ui-dashboard service."""
    all_logs = []

    for datapack in datapacks:
        datapack_folder = src_root / datapack
        for prefix in ("normal", "abnormal"):
            log_file = datapack_folder / f"{prefix}_logs.parquet"
            if log_file.exists():
                lf = pl.scan_parquet(log_file).select("Body", "ServiceName")
                all_logs.append(lf)

    if not all_logs:
        return pl.DataFrame(schema={"Body": pl.String})

    # Combine all logs and filter out ts-ui-dashboard
    combined_lf = pl.concat(all_logs)
    unique_messages = combined_lf.filter(pl.col("ServiceName") != "ts-ui-dashboard").select("Body").unique().collect()

    return unique_messages


@timeit()
def scan_datapacks(src_root: Path) -> list[str]:
    datapacks = []
    for path in src_root.iterdir():
        if not path.is_dir():
            continue

        if not (path / "injection.json").exists():
            continue

        if not (path / "conclusion.csv").exists():
            continue

        try:
            df = pd.read_csv(path / "conclusion.csv")

            if "Issues" in df.columns and (df["Issues"] == "{}").all():
                logger.warning(f"Skipping datapack `{path}` - all Issues are empty")
                continue
        except Exception as e:
            logger.warning(f"Error reading conclusion CSV {path / 'conclusion.csv'}: {e}")
            continue

        total_size = 0
        for file in path.iterdir():
            if not file.is_file():
                continue
            total_size += file.stat().st_size
        total_size_mib = total_size / (1024 * 1024)

        if total_size_mib > 500:
            logger.warning(f"Skipping large datapack `{path.name}` with size {total_size_mib:.2f} MiB")
            continue

        mtime = path.stat().st_mtime
        datapacks.append((path.name, mtime))

    datapacks.sort(key=lambda x: x[1])

    return [name for name, _ in datapacks]


class RcabenchDatasetLoader(DatasetLoader):
    def __init__(self, src_root: Path, dataset: str) -> None:
        self._src_root = src_root
        self._dataset = dataset
        self._datapacks = scan_datapacks(src_root)

    def name(self) -> str:
        return self._dataset

    def __len__(self) -> int:
        return len(self._datapacks)

    def __getitem__(self, index: int) -> DatapackLoader:
        datapack = self._datapacks[index]
        return RcabenchDatapackLoader(src_folder=self._src_root / datapack, datapack=datapack)


def _build_service_graph(datapack_folder: Path) -> nx.Graph:
    normal_traces = pl.scan_parquet(datapack_folder / "normal_traces.parquet")
    anomal_traces = pl.scan_parquet(datapack_folder / "abnormal_traces.parquet")
    traces = pl.concat([normal_traces, anomal_traces])

    lf = traces.select(
        "span_id",
        "parent_span_id",
        "service_name",
    ).filter(pl.col("parent_span_id").is_not_null())

    lf = lf.join(
        lf.select("span_id", pl.col("service_name").alias("parent_service_name")),
        left_on="parent_span_id",
        right_on="span_id",
        how="inner",
    )

    edges_df = (
        lf.select("parent_service_name", "service_name")
        .filter(
            pl.col("parent_service_name") != pl.col("service_name")  # Exclude self-calls
        )
        .unique()
        .collect()
    )

    graph = nx.Graph()

    for parent_service, child_service in edges_df.iter_rows():
        graph.add_edge(parent_service, child_service)

    return graph
