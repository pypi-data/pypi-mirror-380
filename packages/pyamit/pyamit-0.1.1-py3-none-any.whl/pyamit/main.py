import typer
import yaml

app = typer.Typer()


def format_yaml_files(files: list[str], sort_keys: bool = False, indent: int = 2):
    """Format and optionally sort keys in YAML files."""
    for file_path in files:
        try:
            with open(file_path, "r") as f:
                data = yaml.safe_load(f)
            with open(file_path, "w") as f:
                yaml.dump(
                    data,
                    f,
                    sort_keys=sort_keys,
                    default_flow_style=False,
                    indent=indent,
                )
        except Exception as e:
            typer.echo(f"Error processing {file_path}: {e}", err=True)


@app.command()
def format_yaml(
    files: list[str] = typer.Argument(..., help="YAML files to format"),
    sort_keys: bool = typer.Option(False, "--sort-keys", help="Sort keys in YAML"),
    indent: int = typer.Option(2, "--indent", help="Number of spaces for indentation"),
):
    """Format YAML files and optionally sort keys."""
    format_yaml_files(files, sort_keys, indent)


if __name__ == "__main__":  # pragma: no cover
    app()  # pragma: no cover
