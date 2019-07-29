"""Test the `dtool identifiers` command."""

import os

from click.testing import CliRunner

from . import SAMPLE_DATASETS_DIR
from . import tmp_dir_fixture  # NOQA

lion_dataset_uri = "file://" + os.path.join(SAMPLE_DATASETS_DIR, "lion")
not_dataset_uri = "file://" + SAMPLE_DATASETS_DIR


def test_status_command_on_frozen_dataset_functional():
    from dtool_info.dataset import status
    runner = CliRunner()

    result = runner.invoke(status, [lion_dataset_uri])
    assert result.exit_code == 0
    assert result.output.strip() == "frozen"


def test_status_command_on_proto_dataset_functional(tmp_dir_fixture):  # NOQA
    from dtoolcore import generate_admin_metadata, generate_proto_dataset
    from dtool_info.dataset import status

    admin_metadata = generate_admin_metadata("test_ds")
    proto_dataset = generate_proto_dataset(
        admin_metadata=admin_metadata,
        base_uri=tmp_dir_fixture
    )
    proto_dataset.create()

    runner = CliRunner()

    result = runner.invoke(status, [proto_dataset.uri])
    assert result.exit_code == 0
    assert result.output.strip() == "proto"


def test_status_command_on_not_dataset():
    from dtool_info.dataset import status
    runner = CliRunner()

    result = runner.invoke(status, [not_dataset_uri])
    assert result.exit_code != 0
