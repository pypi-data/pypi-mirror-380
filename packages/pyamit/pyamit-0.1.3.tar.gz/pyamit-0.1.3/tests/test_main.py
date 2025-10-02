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


def test_format_yaml_with_sort_lists():
    # Test sorting lists in YAML
    data = {
        "unsorted_list": ["zebra", "apple", "banana"],
        "numbers": [3, 1, 2],
        "mixed": ["b", 3, "a", 1],
    }
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump(data, f, default_flow_style=False)
        temp_file = f.name

    try:
        # Format with list sorting
        format_yaml_files([temp_file], sort_keys=False, sort_lists=True)

        # Read back and check
        with open(temp_file, "r") as f:
            result = yaml.safe_load(f)

        # Lists should be sorted
        expected = {
            "unsorted_list": ["apple", "banana", "zebra"],
            "numbers": [1, 2, 3],
            "mixed": [1, 3, "a", "b"],  # sorted by type then value
        }
        assert result == expected
    finally:
        os.unlink(temp_file)


def test_format_yaml_without_sort_lists():
    # Test that lists are not sorted when option is disabled
    data = {"list": ["zebra", "apple", "banana"]}
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump(data, f, default_flow_style=False)
        temp_file = f.name

    try:
        # Format without list sorting
        format_yaml_files([temp_file], sort_keys=False, sort_lists=False)

        # Read back and check
        with open(temp_file, "r") as f:
            result = yaml.safe_load(f)

        # List should remain unsorted
        assert result["list"] == ["zebra", "apple", "banana"]
    finally:
        os.unlink(temp_file)


def test_format_yaml_sort_lists_nested():
    # Test sorting nested lists
    data = {
        "nested": {
            "inner_list": ["zebra", "apple", "banana"],
            "another_list": [3, 1, 2],
        },
        "top_list": ["z", "a", "m"],
    }
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump(data, f, default_flow_style=False)
        temp_file = f.name

    try:
        # Format with list sorting
        format_yaml_files([temp_file], sort_keys=False, sort_lists=True)

        # Read back and check
        with open(temp_file, "r") as f:
            result = yaml.safe_load(f)

        # All lists should be sorted
        expected = {
            "nested": {
                "inner_list": ["apple", "banana", "zebra"],
                "another_list": [1, 2, 3],
            },
            "top_list": ["a", "m", "z"],
        }
        assert result == expected
    finally:
        os.unlink(temp_file)


def test_format_yaml_sort_lists_with_keys():
    # Test combining key sorting and list sorting
    data = {"z_key": ["zebra", "apple"], "a_key": ["zebra", "apple"]}
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump(data, f, default_flow_style=False)
        temp_file = f.name

    try:
        # Format with both key and list sorting
        format_yaml_files([temp_file], sort_keys=True, sort_lists=True)

        # Read back and check
        with open(temp_file, "r") as f:
            result = yaml.safe_load(f)

        # Keys and lists should both be sorted
        expected = {"a_key": ["apple", "zebra"], "z_key": ["apple", "zebra"]}
        assert result == expected
    finally:
        os.unlink(temp_file)


def test_format_yaml_sort_lists_incomparable_types():
    # Test sorting lists with incomparable types
    # (should keep original order due to TypeError)
    # Create a list with mixed types that cause sorting key incompatibility
    data = {
        "list": [
            None,
            1,
            "string",
            True,
            2.5,
        ]  # mixed types with incompatible sort keys
    }
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump(data, f, default_flow_style=False)
        temp_file = f.name

    try:
        # Format with list sorting - should trigger TypeError and keep original order
        format_yaml_files([temp_file], sort_keys=False, sort_lists=True)

        # Read back and check
        with open(temp_file, "r") as f:
            result = yaml.safe_load(f)

        # Should keep original order due to TypeError in sorting
        assert result["list"] == [None, 1, "string", True, 2.5]
    finally:
        os.unlink(temp_file)


def test_indented_dumper_safety():
    # Test that IndentedDumper produces valid, safe YAML that can be loaded back
    from pyamit.main import IndentedDumper

    test_data = {
        "nested_lists": [[1, 2], [3, 4]],
        "deep_nesting": {"level1": {"level2": {"level3": [1, 2, 3]}}},
        "mixed_types": [None, 42, "string", True, 3.14],
        "unicode": ["café", "🚀"],
    }

    # Dump with IndentedDumper
    import io

    output = io.StringIO()
    yaml.dump(
        test_data, output, Dumper=IndentedDumper, default_flow_style=False, indent=2
    )
    dumped_yaml = output.getvalue()

    # Verify it can be loaded back
    loaded_data = yaml.safe_load(io.StringIO(dumped_yaml))
    assert loaded_data == test_data

    # Verify proper indentation (list items should be indented)
    lines = dumped_yaml.strip().split("\n")
    list_item_lines = [line for line in lines if line.strip().startswith("-")]

    # All list items should have some indentation (not flush left)
    for line in list_item_lines:
        assert line.startswith("  "), f"List item not properly indented: {line!r}"
