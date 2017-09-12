"""Test the ``dtool dataset compare`` command."""

import os

from click.testing import CliRunner

from . import SAMPLE_DATASETS

he_dataset_uri = "file://" + os.path.join(SAMPLE_DATASETS, "he")
she_dataset_uri = "file://" + os.path.join(SAMPLE_DATASETS, "she")
cat_dataset_uri = "file://" + os.path.join(SAMPLE_DATASETS, "cat")

def test_dataset_diff_functional():

    from dtool_info.dataset import diff

    runner = CliRunner()

    result = runner.invoke(diff, [he_dataset_uri, he_dataset_uri])
    assert result.exit_code == 0
