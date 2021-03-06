"""Test the ``dtool diff`` command."""

import os

from click.testing import CliRunner

from . import SAMPLE_DATASETS_DIR

he_dataset_uri = "file://" + os.path.join(SAMPLE_DATASETS_DIR, "he")
she_dataset_uri = "file://" + os.path.join(SAMPLE_DATASETS_DIR, "she")
cat_dataset_uri = "file://" + os.path.join(SAMPLE_DATASETS_DIR, "cat")
lion_dataset_uri = "file://" + os.path.join(SAMPLE_DATASETS_DIR, "lion")


def test_dataset_diff_functional():

    from dtool_info.dataset import diff

    runner = CliRunner()

    result = runner.invoke(diff, [he_dataset_uri, he_dataset_uri])
    assert result.exit_code == 0

    result = runner.invoke(diff, [he_dataset_uri, she_dataset_uri])
    assert result.exit_code == 1
    assert result.output.startswith("Different identifiers")

    result = runner.invoke(diff, [cat_dataset_uri, lion_dataset_uri])
    assert result.exit_code == 2
    assert result.output.find("Different sizes") != -1

    result = runner.invoke(diff, [cat_dataset_uri, she_dataset_uri])
    assert result.exit_code == 0

    result = runner.invoke(diff, ["--full", cat_dataset_uri, she_dataset_uri])
    assert result.exit_code == 3
    assert result.output.find("Different content") != -1
