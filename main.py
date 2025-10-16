"""A CLI for maintaining DALIA-curated OERs."""

from dalia_dif.dif13 import read_dif13
import uuid
from pathlib import Path

import click
import pandas as pd

HERE = Path(__file__).parent.resolve()
INPUT_DIRECTORY = HERE.joinpath("curation")
INPUT_PATHS = list(INPUT_DIRECTORY.glob("*.csv"))
EXPORT_DIRECTORY = HERE.joinpath("export")
EXPORT_DIRECTORY.mkdir(exist_ok=True, parents=True)
CHART_SVG_PATH = EXPORT_DIRECTORY.joinpath("summary.svg")
CHART_PNG_PATH = EXPORT_DIRECTORY.joinpath("summary.png")
DIF13_TTL_PATH = EXPORT_DIRECTORY.joinpath("dalia-dif13.ttl")
DIF13_JSONL_PATH = EXPORT_DIRECTORY.joinpath("dalia-dif13.jsonl")
SQLITE_FTI_PATH = EXPORT_DIRECTORY.joinpath("dalia-full-text-index.sqlite")


@click.group()
def main() -> None:
    """Run the CLI."""


@main.command()
def validate() -> None:
    """Validate all CSV files in the curation directory."""
    for path in INPUT_PATHS:
        read_dif13(path)


@main.command()
def export() -> None:
    """Make exports."""
    from dalia_dif.dif13.export.charts import export_chart
    from dalia_dif.dif13.export.fti import write_sqlite_fti
    from dalia_dif.namespace import get_base_graph

    graph = get_base_graph()
    with DIF13_JSONL_PATH.open("w") as file:
        for path in INPUT_PATHS:
            for record in read_dif13(path):
                record.add_to_graph(graph)
                file.write(record.model_dump_json())

    graph.serialize(DIF13_TTL_PATH, format="turtle")

    export_chart(graph, [CHART_SVG_PATH, CHART_PNG_PATH])
    write_sqlite_fti(graph, SQLITE_FTI_PATH)


@main.command()
def lint():
    """Lint CSV files in the curation directory."""
    count = 0
    for path in INPUT_PATHS:
        df = pd.read_csv(path, sep=",")
        if "DALIA_ID" not in df.columns:
            click.secho(f"missing DALIA_ID in {path}")
            xx = ["DALIA_ID", *df.columns]
            df["DALIA_ID"] = df.index.map(lambda _: str(uuid.uuid4()))
            df = df[xx]
            df.to_csv(path, sep=",", index=False)
        count += len(df)
    click.echo(f"There are a total of {count:,} rows")


if __name__ == "__main__":
    main()
