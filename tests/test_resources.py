"""Exercise resource lookup independently of ecosystem discovery."""

import csv
import io
import json
from contextlib import redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

import main as cli


def resource_output(*args):
    command = cli.build_parser().parse_args(["resources", *args])
    output = io.StringIO()
    with redirect_stdout(output):
        assert command.func(command) == 0
    return output.getvalue()


def test_search_by_kind_and_terms_across_fields():
    with TemporaryDirectory() as tmp:
        catalog = Path(tmp) / "catalog.csv"
        catalog.write_text(
            "id,kind,name,repo_url,evidence_url,license,description,tags\n"
            "z,skill,Zebra,repo,source-z,MIT,Composite layers,motion|vector\n"
            "a,skill,Alpha,repo,source-a,MIT,Composite footage,motion|video\n"
            "t,tool,Toolkit,repo,source-t,MIT,Composite images,motion\n",
            encoding="utf-8",
        )
        with patch.object(cli, "RESOURCE_CATALOG", catalog):
            rows = json.loads(resource_output("COMPOSITE", "Motion", "--kind", "skill", "--format", "json"))
            assert [row["id"] for row in rows] == ["a", "z"]
            assert rows[0]["tags"] == ["motion", "video"]
            assert "source-t" in resource_output("Toolkit", "--kind", "tool")
            assert json.loads(resource_output("zebra", "video", "--format", "json")) == []


def test_shipped_resource_catalog():
    with cli.RESOURCE_CATALOG.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        assert reader.fieldnames == ["id", "kind", "name", "repo_url", "evidence_url", "license", "description", "tags"]
        rows = list(reader)
    assert rows
    assert len({row["id"] for row in rows}) == len(rows)
    assert all(all(row.values()) and row["kind"] in {"skill", "tool"} for row in rows)
    assert len(json.loads(resource_output("--format", "json"))) == len(rows)
