from __future__ import annotations

import json
from typing import Any, Dict, List, Tuple

from click.testing import CliRunner
import pytest

from dmos_search import cli


class _RecordingDDGS:
    """Fake DDGS that simulates TLS fallback support."""

    def __init__(self, *, timeout: int, verify: bool) -> None:
        self.timeout = timeout
        self.verify = verify

    def __enter__(self) -> "_RecordingDDGS":
        return self

    def __exit__(self, exc_type, exc, tb) -> bool:
        return False

    def text(self, *args: Any, **kwargs: Any) -> List[Dict[str, Any]]:
        if self.verify:
            raise ValueError("Unsupported protocol version")
        return [
            {
                "title": "Fallback succeeded",
                "href": "https://example.com",
                "body": "An example result",
            }
        ]


def test_fetch_results_tls_fallback(monkeypatch: pytest.MonkeyPatch) -> None:
    created: List[_RecordingDDGS] = []

    def fake_ddgs(**kwargs: Any) -> _RecordingDDGS:
        instance = _RecordingDDGS(**kwargs)
        created.append(instance)
        return instance

    monkeypatch.setattr(cli, "DDGS", fake_ddgs)  # type: ignore[arg-type]

    results, insecure = cli._fetch_results(
        query="python",
        limit=5,
        region="us-en",
        safesearch="moderate",
        timeout=3,
    )

    assert insecure is True
    assert results[0]["title"] == "Fallback succeeded"
    # First attempt should have used strict verification, second attempt disabled it.
    assert [instance.verify for instance in created] == [True, False]


def test_cli_json_output(monkeypatch: pytest.MonkeyPatch) -> None:
    runner = CliRunner()

    payload = [
        {"title": "Example", "href": "https://example.com", "body": "Snippet"}
    ]

    monkeypatch.setattr(cli, "_fetch_results", lambda *args, **kwargs: (payload, False))

    result = runner.invoke(cli.main, ["demo", "query", "--json-output"])

    assert result.exit_code == 0
    assert json.loads(result.stdout) == payload


def test_cli_warns_on_insecure_tls_and_respects_no_browser(monkeypatch: pytest.MonkeyPatch) -> None:
    runner = CliRunner()

    payload = [
        {"title": "Example", "href": "https://example.com", "body": "Snippet"}
    ]

    monkeypatch.setattr(cli, "_fetch_results", lambda *args, **kwargs: (payload, True))

    opened: List[str] = []

    def fake_open(url: str, *args: Any, **kwargs: Any) -> bool:
        opened.append(url)
        return True

    monkeypatch.setattr(cli.webbrowser, "open", fake_open)

    result = runner.invoke(
        cli.main,
        ["query", "--open", "1", "--no-browser"],
    )

    assert result.exit_code == 0
    assert "Warning: fell back to disabling TLS" in result.stderr
    assert opened == []
