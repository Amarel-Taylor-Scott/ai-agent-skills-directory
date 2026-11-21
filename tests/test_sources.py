"""Verify cross-field matching, optional feeds and the packaged source catalog."""

import csv
import io
import json
from contextlib import redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

import main as cli


def source_output(*args):
    command = cli.build_parser().parse_args(["sources", *args])
    output = io.StringIO()
    with redirect_stdout(output):
        assert command.func(command) == 0
    return output.getvalue()


def test_sources_match_all_words_and_filter_optional_feeds():
    with TemporaryDirectory() as tmp:
        path = Path(tmp) / "sources.csv"
        path.write_text(
            "id,name,type,focus,browse_url,feed_url,example_url,notes\n"
            "screen,Screen,community,Lighting,https://example.org/video,,https://example.org/demo,Animation\n"
            "film,Film,publication,Lighting,https://example.org/f,https://example.org/rss,,Film releases\n",
            encoding="utf-8",
        )
        with patch.object(cli, "SOURCE_CATALOG", path):
            all_sources = json.loads(source_output("--format", "json"))
            assert [row["id"] for row in all_sources] == ["film", "screen"]
            assert all_sources[1]["feed_url"] == ""
            assert [row["id"] for row in json.loads(source_output("COMMUNITY", "animation LIGHT", "--format", "json"))] == ["screen"]
            assert json.loads(source_output("animation", "lighting", "--has-feed", "--format", "json")) == []
            assert json.loads(source_output("video", "--format", "json")) == []  # browse URL only
            listing = source_output("--has-feed")
            assert "Film" in listing and "https://example.org/rss" in listing and "Screen" not in listing


def test_shipped_source_catalog():
    with cli.SOURCE_CATALOG.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        assert reader.fieldnames == ["id", "name", "type", "focus", "browse_url", "feed_url", "example_url", "notes"]
        rows = list(reader)
    assert rows and len({row["id"] for row in rows}) == len(rows)
    assert all(row["name"] and row["browse_url"] for row in rows)
    assert len(json.loads(source_output("--format", "json"))) == len(rows)
