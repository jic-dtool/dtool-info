"""Test the dtool summary command."""

import os
import json

from click.testing import CliRunner

from . import SAMPLE_DATASETS

lion_dataset_uri = "file://" + os.path.join(SAMPLE_DATASETS, "lion")
item_identifier = "5436437fa01a7d3e41d46741da54b451446774ca"


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


def test_dataset_item_fetch_functional():

    from dtoolcore import DataSet

    from dtool_info.dataset import item

    runner = CliRunner()

    result = runner.invoke(
        item,
        ["fetch", lion_dataset_uri, item_identifier])
    assert result.exit_code == 0
