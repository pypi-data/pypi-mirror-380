"""Command-line interface for Mouc."""

from __future__ import annotations

import importlib
import importlib.util
from pathlib import Path
from typing import Annotated

import typer

from .exceptions import MoucError
from .graph import GraphGenerator, GraphView
from .markdown import MarkdownGenerator
from .parser import FeatureMapParser

app = typer.Typer(
    name="mouc",
    help="Mapping Outcomes User stories and Capabilities - A lightweight dependency tracking system",
    add_completion=False,
)


@app.command()
def graph(
    file: Annotated[Path, typer.Argument(help="Path to the feature map YAML file")] = Path(
        "feature_map.yaml"
    ),
    view: Annotated[
        GraphView, typer.Option("--view", "-v", help="Type of graph to generate")
    ] = GraphView.ALL,
    target: Annotated[
        str | None, typer.Option("--target", "-t", help="Target for critical path view")
    ] = None,
    tags: Annotated[list[str] | None, typer.Option("--tags", help="Tags for filtered view")] = None,
    output: Annotated[Path | None, typer.Option("--output", "-o", help="Output file path")] = None,
    style_module: Annotated[
        str | None,
        typer.Option("--style-module", help="Python module path for styling functions"),
    ] = None,
    style_file: Annotated[
        Path | None,
        typer.Option("--style-file", help="Python file path for styling functions"),
    ] = None,
) -> None:
    """Generate dependency graphs in DOT format."""
    try:
        # Validate arguments
        if view == GraphView.CRITICAL_PATH and not target:
            typer.echo("Error: Critical path view requires --target", err=True)
            raise typer.Exit(1) from None

        if view == GraphView.FILTERED and not tags:
            typer.echo("Error: Filtered view requires --tags", err=True)
            raise typer.Exit(1) from None

        if style_module and style_file:
            typer.echo("Error: Cannot specify both --style-module and --style-file", err=True)
            raise typer.Exit(1) from None

        # Load styling module if specified
        if style_module or style_file:
            _load_styling(style_module, style_file)

        # Parse the feature map
        parser = FeatureMapParser()
        feature_map = parser.parse_file(file)

        # Generate the graph
        generator = GraphGenerator(feature_map)
        dot_output = generator.generate(view, target=target, tags=tags)

        # Output the result
        if output:
            output.write_text(dot_output, encoding="utf-8")
            typer.echo(f"Graph written to {output}")
        else:
            typer.echo(dot_output)

    except MoucError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1) from None
    except Exception as e:
        typer.echo(f"Unexpected error: {e}", err=True)
        raise typer.Exit(1) from None


@app.command()
def doc(
    file: Annotated[Path, typer.Argument(help="Path to the feature map YAML file")] = Path(
        "feature_map.yaml"
    ),
    output: Annotated[Path | None, typer.Option("--output", "-o", help="Output file path")] = None,
    style_module: Annotated[
        str | None,
        typer.Option("--style-module", help="Python module path for styling functions"),
    ] = None,
    style_file: Annotated[
        Path | None,
        typer.Option("--style-file", help="Python file path for styling functions"),
    ] = None,
) -> None:
    """Generate documentation in Markdown format."""
    try:
        if style_module and style_file:
            typer.echo("Error: Cannot specify both --style-module and --style-file", err=True)
            raise typer.Exit(1) from None

        # Load styling module if specified
        if style_module or style_file:
            _load_styling(style_module, style_file)

        # Parse the feature map
        parser = FeatureMapParser()
        feature_map = parser.parse_file(file)

        # Generate the markdown
        generator = MarkdownGenerator(feature_map)
        markdown_output = generator.generate()

        # Output the result
        if output:
            output.write_text(markdown_output, encoding="utf-8")
            typer.echo(f"Documentation written to {output}")
        else:
            typer.echo(markdown_output)

    except MoucError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1) from None
    except Exception as e:
        typer.echo(f"Unexpected error: {e}", err=True)
        raise typer.Exit(1) from None


@app.command()
def status(
    target: Annotated[str, typer.Argument(help="Outcome ID to check status for")],
    file: Annotated[
        Path, typer.Option("--file", "-f", help="Path to the feature map YAML file")
    ] = Path("feature_map.yaml"),
) -> None:
    """Show status of an outcome and its dependencies."""
    typer.echo(f"Status query for '{target}' not yet implemented", err=True)
    raise typer.Exit(1)


@app.command()
def audit(
    check: Annotated[str, typer.Argument(help="Type of audit check (e.g., 'no-design-doc')")],
    tags: Annotated[list[str] | None, typer.Option("--tags", help="Filter by tags")] = None,
    file: Annotated[
        Path, typer.Option("--file", "-f", help="Path to the feature map YAML file")
    ] = Path("feature_map.yaml"),
) -> None:
    """Run audit checks on the feature map."""
    typer.echo(f"Audit check '{check}' not yet implemented", err=True)
    raise typer.Exit(1)


def _load_styling(style_module: str | None, style_file: Path | None) -> None:
    """Load user styling module or file."""
    from . import styling

    # Clear any previous registrations
    styling.clear_registrations()

    if style_module:
        # Import from module path
        importlib.import_module(style_module)
    elif style_file:
        # Import from file path
        style_path = style_file.resolve()
        spec = importlib.util.spec_from_file_location("user_styles", style_path)
        if spec is None or spec.loader is None:
            raise MoucError(f"Could not load styling file: {style_file}")
        user_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(user_module)


def main() -> int:
    """Main entry point."""
    # Typer handles sys.exit() internally
    app()
    return 0


if __name__ == "__main__":
    main()
