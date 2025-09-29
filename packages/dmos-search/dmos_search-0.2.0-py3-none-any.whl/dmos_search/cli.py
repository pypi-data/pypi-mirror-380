import json
import textwrap
import webbrowser
from typing import Any, Dict, List, Optional, Tuple

import click
from ddgs import DDGS

DEFAULT_WIDTH = 88
WINDOW_TEXT = "( opens in a new window)"
MAX_SNIPPET_CHARS = 500


def _wrap_snippet(snippet: str) -> str:
    """Wrap snippet text to DEFAULT_WIDTH preserving indentation."""
    if not snippet:
        return ""
    cleaned = snippet.replace(WINDOW_TEXT, " ")
    cleaned = " ".join(cleaned.split())
    if len(cleaned) > MAX_SNIPPET_CHARS:
        cleaned = f"{cleaned[:MAX_SNIPPET_CHARS - 3].rstrip()}..."
    if not cleaned:
        return ""
    return textwrap.fill(
        cleaned,
        width=DEFAULT_WIDTH,
        initial_indent="   ",
        subsequent_indent="   ",
        replace_whitespace=False,
    )


def _fetch_results(
    query: str,
    limit: int,
    region: str,
    safesearch: str,
    timeout: int,
) -> Tuple[List[Dict[str, Any]], bool]:
    """Query DuckDuckGo via ddgs and return structured results plus a flag for TLS fallback."""
    last_exc: Optional[Exception] = None
    for verify in (True, False):
        try:
            with DDGS(timeout=timeout, verify=verify) as ddgs:
                results = ddgs.text(
                    query,
                    region=region,
                    safesearch=safesearch,
                    max_results=limit,
                )
            return results[:limit], not verify
        except ValueError as exc:
            if verify and "Unsupported protocol version" in str(exc):
                last_exc = exc
                continue
            raise click.ClickException(f"Search failed: {exc}") from exc
        except Exception as exc:  # pragma: no cover - library-specific exceptions vary
            if verify:
                last_exc = exc
                continue
            raise click.ClickException(f"Search failed: {exc}") from exc
    if last_exc:
        raise click.ClickException(f"Search failed: {last_exc}")
    return [], False


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.argument("query", nargs=-1)
@click.option("--limit", "-l", default=10, show_default=True, type=click.IntRange(1, 50), help="Number of results to display")
@click.option("--region", default="us-en", show_default=True, help="Region code such as us-en, uk-en, de-de")
@click.option(
    "--safesearch",
    type=click.Choice(["off", "moderate", "strict"], case_sensitive=False),
    default="moderate",
    show_default=True,
    help="Safe search level",
)
@click.option(
    "--timeout",
    default=10,
    show_default=True,
    type=click.IntRange(1, 60),
    help="HTTP timeout in seconds",
)
@click.option("--json-output", is_flag=True, help="Emit raw JSON instead of formatted text")
@click.option(
    "--open",
    "open_index",
    type=click.IntRange(1, 50),
    help="Open the Nth result in the browser after printing output",
)
@click.option("--no-browser", is_flag=True, help="Prevent launching the browser even if --open is supplied")
@click.version_option(package_name="dmos-search")
def main(
    query: List[str],
    limit: int,
    region: str,
    safesearch: str,
    timeout: int,
    json_output: bool,
    open_index: Optional[int],
    no_browser: bool,
) -> None:
    """Perform a web search from the terminal."""
    if not query:
        raise click.UsageError("Provide a search query, for example: dmos-search maps API docs")

    text_query = " ".join(query).strip()
    results, insecure_tls = _fetch_results(text_query, limit=limit, region=region, safesearch=safesearch.lower(), timeout=timeout)

    if insecure_tls:
        click.secho(
            "Warning: fell back to disabling TLS certificate verification; upgrade Python/OpenSSL to restore verification.",
            fg="yellow",
            err=True,
        )

    if not results:
        click.echo("No results found.")
        return

    if json_output:
        click.echo(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        for index, item in enumerate(results, start=1):
            title = item.get("title") or "(untitled)"
            url = item.get("href") or ""
            snippet = item.get("body") or ""
            click.secho(f"{index}. {title}", fg="cyan")
            if url:
                click.secho(f"   {url}", fg="blue")
            wrapped = _wrap_snippet(snippet)
            if wrapped:
                click.echo(wrapped)
            click.echo()

    if open_index and not no_browser:
        if open_index > len(results):
            raise click.ClickException(
                f"Cannot open result {open_index}; only {len(results)} result(s) available"
            )
        url = results[open_index - 1].get("href")
        if not url:
            raise click.ClickException("Selected result does not have a valid URL to open")
        webbrowser.open(url)


if __name__ == "__main__":
    main()
