"""Test the dtool summary command."""

import os

from click.testing import CliRunner

from . import SAMPLE_DATASETS_DIR

lion_dataset_uri = "file://" + os.path.join(SAMPLE_DATASETS_DIR, "lion")


def test_dataset_uuid_functional():

    from dtoolcore import DataSet
    from dtool_info.dataset import uuid

    # Create expected output.
    lion_ds = DataSet.from_uri(lion_dataset_uri)
    expected_uuid = lion_ds.uuid

    runner = CliRunner()

    result = runner.invoke(
        uuid,
        [lion_dataset_uri])
    assert result.exit_code == 0
    assert result.output.strip() == expected_uuid
