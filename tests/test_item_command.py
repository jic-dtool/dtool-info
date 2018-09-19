"""Test the dtool summary command."""

import os
import json

from click.testing import CliRunner

from . import SAMPLE_DATASETS_DIR

lion_dataset_uri = "file://" + os.path.join(SAMPLE_DATASETS_DIR, "lion")
item_identifier = "5436437fa01a7d3e41d46741da54b451446774ca"

people_dataset_uri = "file://" + os.path.join(SAMPLE_DATASETS_DIR, "people")
anna_identifier = "4162a9a650be9ab5b133bf37867eac076a871e11"


def test_dataset_item_properties_functional():

    from dtoolcore import DataSet
    from dtool_info.dataset import item

    # Create expected output.
    lion_ds = DataSet.from_uri(lion_dataset_uri)
    expected = lion_ds.item_properties(item_identifier)

    runner = CliRunner()

    result = runner.invoke(
        item,
        ["properties", lion_dataset_uri, item_identifier])
    assert result.exit_code == 0

    actual = json.loads(result.output)
    assert expected == actual


def test_dataset_item_properties_with_invalid_key_functional():

    from dtool_info.dataset import item

    runner = CliRunner()

    result = runner.invoke(
        item,
        ["properties", lion_dataset_uri, "nonsense"])
    assert result.exit_code == 20

    expected = "No such item in dataset: nonsense"
    assert expected == result.output.strip()


def test_dataset_item_fetch_functional():

    from dtoolcore import DataSet

    from dtool_info.dataset import item

    # Create expected output.
    lion_ds = DataSet.from_uri(lion_dataset_uri)
    expected = lion_ds.item_content_abspath(item_identifier)

    runner = CliRunner()

    result = runner.invoke(
        item,
        ["fetch", lion_dataset_uri, item_identifier])
    assert result.exit_code == 0
    assert expected == result.output.strip()


def test_dataset_item_overlay_functional():

    from dtool_info.dataset import item

    # Create expected output.

    runner = CliRunner()

    result = runner.invoke(
        item,
        ["overlay", "gender", people_dataset_uri, anna_identifier])
    assert result.exit_code == 0
    assert result.output.strip() == "female"

    result = runner.invoke(
        item,
        ["overlay", "dont_exist", people_dataset_uri, anna_identifier])
    assert result.exit_code == 4
    assert result.output.startswith("No such overlay in dataset")

    result = runner.invoke(
        item,
        ["overlay", "gender", people_dataset_uri, "dontexist"])
    assert result.exit_code == 5
    assert result.output.startswith("No such identifier in overlay")
