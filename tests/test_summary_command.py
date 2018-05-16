"""Test the dtool summary command."""

import os
import json

from click.testing import CliRunner

from . import SAMPLE_DATASETS_DIR

lion_dataset_uri = "file://" + os.path.join(SAMPLE_DATASETS_DIR, "lion")


def test_dataset_summary_functional():

    from dtoolcore import DataSet
    from dtool_info.dataset import summary

    # Create expected output.
    lion_ds = DataSet.from_uri(lion_dataset_uri)

    tot_size = sum([lion_ds.item_properties(i)["size_in_bytes"]
                    for i in lion_ds.identifiers])

    expected = {
        "name": lion_ds.name,
        "uuid": lion_ds.uuid,
        "number_of_items": len(lion_ds.identifiers),
        "size_in_bytes": tot_size,
        "creator_username": lion_ds._admin_metadata["creator_username"],
        "frozen_at": lion_ds._admin_metadata["frozen_at"],
    }

    runner = CliRunner()

    result = runner.invoke(summary, [lion_dataset_uri])
    assert result.exit_code == 0

    actual = json.loads(result.output)
    assert expected == actual
