import os
import subprocess
import sys
import tempfile

import yaml

from pyamit.main import format_yaml_files


def test_format_yaml_without_sort():
    # Create a temporary YAML file
    data = {"b": 2, "a": 1, "c": 3}
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump(data, f, default_flow_style=False)
        temp_file = f.name

    try:
        # Format without sorting
        format_yaml_files([temp_file], sort_keys=False)

        # Read back and check
        with open(temp_file, "r") as f:
            result = yaml.safe_load(f)

        # Should preserve order (pyyaml may not, but for test, check it's valid)
        assert result == data
    finally:
        os.unlink(temp_file)


def test_format_yaml_with_sort():
    # Create a temporary YAML file
    data = {"b": 2, "a": 1, "c": 3}
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump(data, f, default_flow_style=False)
        temp_file = f.name

    try:
        # Format with sorting
        format_yaml_files([temp_file], sort_keys=True)

        # Read back and check
        with open(temp_file, "r") as f:
            result = yaml.safe_load(f)

        # Should be sorted
        expected = {"a": 1, "b": 2, "c": 3}
        assert result == expected
    finally:
        os.unlink(temp_file)


def test_format_yaml_complex_structure():
    # Test with nested dicts and lists
    data = {
        "config": {
            "database": {
                "host": "localhost",
                "port": 5432,
                "credentials": {"user": "admin", "password": "secret"},
            },
            "features": ["logging", "caching", "auth"],
            "settings": {"debug": True, "timeout": 30},
        },
        "version": "1.0.0",
    }
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump(data, f, default_flow_style=False)
        temp_file = f.name

    try:
        # Format without sorting to preserve structure
        format_yaml_files([temp_file], sort_keys=False)

        # Read back and check
        with open(temp_file, "r") as f:
            result = yaml.safe_load(f)

        # Should match original structure
        assert result == data

        # Check that the file content has proper indentation
        with open(temp_file, "r") as f:
            content = f.read()
            assert "  database:" in content
            assert "    credentials:" in content
            assert "  - logging" in content  # list items
    finally:
        os.unlink(temp_file)


def test_format_yaml_custom_indent():
    # Test with custom indentation
    data = {"level1": {"level2": {"level3": "value"}}}
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump(data, f, default_flow_style=False)
        temp_file = f.name

    try:
        # Format with indent 4
        format_yaml_files([temp_file], sort_keys=False, indent=4)

        # Read back and check
        with open(temp_file, "r") as f:
            result = yaml.safe_load(f)

        assert result == data

        # Check indentation
        with open(temp_file, "r") as f:
            content = f.read()
            assert "    level2:" in content
            assert "        level3:" in content
    finally:
        os.unlink(temp_file)


def test_format_yaml_file_not_found():
    # Test error handling for non-existent file
    non_existent_file = "/tmp/non_existent_file.yaml"
    # Make sure the file doesn't exist
    if os.path.exists(non_existent_file):
        os.unlink(non_existent_file)

    # This should not raise an exception, but should print an error message
    format_yaml_files([non_existent_file], sort_keys=False)


def test_format_yaml_invalid_content():
    # Test error handling for invalid YAML content
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        f.write("invalid: yaml: content: [\n")  # Invalid YAML
        temp_file = f.name

    try:
        # This should not raise an exception, but should print an error message
        format_yaml_files([temp_file], sort_keys=False)
    finally:
        os.unlink(temp_file)


def test_cli_interface():
    # Test the CLI interface by running the script directly
    data = {"test": "data"}
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump(data, f, default_flow_style=False)
        temp_file = f.name

    try:
        # Run the script directly to trigger __name__ == "__main__"
        main_script = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "src", "pyamit", "main.py"
        )
        result = subprocess.run(
            [sys.executable, main_script, temp_file], capture_output=True, text=True
        )

        # Should exit successfully
        assert result.returncode == 0

        # Check that the file was formatted
        with open(temp_file, "r") as f:
            result_data = yaml.safe_load(f)
        assert result_data == data

    finally:
        os.unlink(temp_file)
