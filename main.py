# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click",
#     "dalia-dif[export,fti]>=0.0.11",
#     "pystow",
#     "rdflib",
# ]
# ///

"""A CLI for maintaining DALIA-curated OERs."""

import unittest
from pathlib import Path

import click
from dalia_dif.dif13 import read_dif13

HERE = Path(__file__).parent.resolve()
INPUT_DIRECTORY = HERE.joinpath("curation")
INPUT_PATHS = list(INPUT_DIRECTORY.glob("*.csv"))
EXPORT_DIRECTORY = HERE.joinpath("export")
EXPORT_DIRECTORY.mkdir(exist_ok=True, parents=True)
CHART_SVG_PATH = EXPORT_DIRECTORY.joinpath("summary.svg")
CHART_PNG_PATH = EXPORT_DIRECTORY.joinpath("summary.png")
DIF13_TTL_PATH = EXPORT_DIRECTORY.joinpath("dalia-dif13.ttl")
DIF13_FULL_TTL_PATH = EXPORT_DIRECTORY.joinpath("dalia-dif13-full.ttl")
DIF13_JSONL_PATH = EXPORT_DIRECTORY.joinpath("dalia-dif13.jsonl")
SQLITE_FTI_PATH = EXPORT_DIRECTORY.joinpath("dalia-full-text-index.sqlite")


@click.group()
def main() -> None:
    """Run the CLI."""


@main.command()
def export() -> None:
    """Make exports."""
    from dalia_dif.dif13.export.charts import export_chart
    from dalia_dif.dif13.rdf import add_background_triples
    from dalia_dif.dif13.export.fti import write_sqlite_fti
    from dalia_dif.namespace import get_base_graph

    graph_dif13 = get_base_graph()
    with DIF13_JSONL_PATH.open("w") as file:
        for path in INPUT_PATHS:
            for record_dif13 in read_dif13(path):
                record_dif13.add_to_graph(graph_dif13)
                file.write(record_dif13.model_dump_json())
    graph_dif13.serialize(DIF13_TTL_PATH, format="turtle")

    add_background_triples(graph_dif13)
    graph_dif13.serialize(DIF13_FULL_TTL_PATH, format="turtle")

    export_chart(graph_dif13, [CHART_SVG_PATH, CHART_PNG_PATH])
    if SQLITE_FTI_PATH.is_file():
        SQLITE_FTI_PATH.unlink()
    write_sqlite_fti(graph_dif13, SQLITE_FTI_PATH)


class TestParity(unittest.TestCase):
    """Test parity."""

    def test_parity(self) -> None:
        """Test parity."""
        import rdflib
        from dalia_dif.dif13 import parse_dif13_row
        from dalia_dif.dif13.legacy import parse_dif13_row_legacy
        from pystow.utils import safe_open_dict_reader
        from rdflib.compare import isomorphic

        for path in INPUT_PATHS:
            with safe_open_dict_reader(path, delimiter=",") as reader:
                for i, row in enumerate(reader, start=1):
                    if not row:
                        continue
                    with self.subTest(path=path.name, line=i):
                        self.maxDiff = None
                        old_graph = rdflib.Graph()
                        parse_dif13_row_legacy(old_graph, i, row, path=path)

                        obj = parse_dif13_row(path.name, i, row)
                        self.assertIsNotNone(
                            obj,
                            msg=f"see old graph:\n\n{old_graph.serialize(format='ttl')}",
                        )
                        new_graph = obj.get_graph()
                        if not isomorphic(old_graph, new_graph):
                            self.assertEqual(
                                old_graph.serialize(format="ttl"),
                                new_graph.serialize(format="ttl"),
                                msg=f"\n\nfailed on {path.name} row {i}",
                            )


@main.command()
def test() -> None:
    """Test that the new output creates the same graphs as the old one."""
    TestParity().test_parity()


if __name__ == "__main__":
    main()
