import typer
import yaml

app = typer.Typer()


class IndentedDumper(yaml.SafeDumper):
    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)


def sort_lists_in_data(data):
    """Recursively sort lists in the data structure."""
    if isinstance(data, dict):
        return {key: sort_lists_in_data(value) for key, value in data.items()}
    elif isinstance(data, list):
        # Sort the list if all elements are of comparable types
        try:
            sorted_list = sorted(
                data,
                key=lambda x: (type(x).__name__, x)
                if isinstance(x, (str, int, float, bool))
                else str(x),
            )
            return [sort_lists_in_data(item) for item in sorted_list]
        except TypeError:
            # If items are not comparable, keep original order but still process
            # nested structures
            return [sort_lists_in_data(item) for item in data]
    else:
        return data


def format_yaml_files(
    files: list[str], sort_keys: bool = False, indent: int = 2, sort_lists: bool = False
):
    """Format and optionally sort keys and lists in YAML files."""
    for file_path in files:
        try:
            with open(file_path, "r") as f:
                data = yaml.safe_load(f)

            if sort_lists:
                data = sort_lists_in_data(data)

            with open(file_path, "w") as f:
                yaml.dump(
                    data,
                    f,
                    sort_keys=sort_keys,
                    default_flow_style=False,
                    indent=indent,
                    Dumper=IndentedDumper,
                )
        except Exception as e:
            typer.echo(f"Error processing {file_path}: {e}", err=True)


@app.command()
def format_yaml(
    files: list[str] = typer.Argument(..., help="YAML files to format"),
    sort_keys: bool = typer.Option(False, "--sort-keys", help="Sort keys in YAML"),
    indent: int = typer.Option(2, "--indent", help="Number of spaces for indentation"),
    sort_lists: bool = typer.Option(False, "--sort-lists", help="Sort lists in YAML"),
):
    """Format YAML files and optionally sort keys and lists."""
    format_yaml_files(files, sort_keys, indent, sort_lists)


if __name__ == "__main__":  # pragma: no cover
    app()  # pragma: no cover
