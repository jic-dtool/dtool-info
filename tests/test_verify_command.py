"""Test the ``dtool verify`` command."""

import os

from click.testing import CliRunner

import dtoolcore

from . import SAMPLE_DATASETS
from . import tmp_dir_fixture  # NOQA

lion_dataset_uri = "file://" + os.path.join(SAMPLE_DATASETS, "lion")


def test_dataset_verify_functional(tmp_dir_fixture):  # NOQA

    from dtool_info.dataset import verify

    uri = dtoolcore.copy(lion_dataset_uri, tmp_dir_fixture, "file")
    dataset = dtoolcore.DataSet.from_uri(uri)

    runner = CliRunner()

    result = runner.invoke(verify, [uri])
    assert result.exit_code == 0
    assert result.output.startswith("All good")

    extra_fpath = os.path.join(
        dataset._storage_broker._data_abspath,
        "extra.txt"
    )
    with open(extra_fpath, "w") as fh:
        fh.write("extra")

    result = runner.invoke(verify, [uri])
    assert result.exit_code == 1
    assert result.output.startswith("Unknown item: ")

    os.unlink(extra_fpath)

    item_fpath = os.path.join(
        dataset._storage_broker._data_abspath,
        "file.txt"
    )
    os.unlink(item_fpath)

    result = runner.invoke(verify, [uri])
    assert result.exit_code == 1
    assert result.output.startswith("Missing item: ")

    with open(item_fpath, "w") as fh:
        fh.write("Different content")

    result = runner.invoke(verify, [uri])
    assert result.exit_code == 0
    assert result.output.startswith("All good")

    result = runner.invoke(verify, ["--full", uri])
    assert result.exit_code == 1
    assert result.output.startswith("Altered item: ")
