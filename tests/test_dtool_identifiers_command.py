"""Test the `dtool identifiers` command."""

import os

from click.testing import CliRunner

from . import SAMPLE_DATASETS_DIR

lion_dataset_uri = "file://" + os.path.join(SAMPLE_DATASETS_DIR, "lion")
item_identifier = "5436437fa01a7d3e41d46741da54b451446774ca"


def test_dataset_item_properties_functional():
    from dtool_info.dataset import identifiers
    runner = CliRunner()

    result = runner.invoke(identifiers, [lion_dataset_uri])
    assert result.exit_code == 0
    assert result.output.strip() == item_identifier
