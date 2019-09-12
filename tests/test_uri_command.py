"""Test the `dtool uri` command."""

import os

from click.testing import CliRunner

from . import SAMPLE_DATASETS_DIR
from . import tmp_dir_fixture  # NOQA

lion_dataset_path = os.path.join(SAMPLE_DATASETS_DIR, "lion")


def test_uri_command_functional():
    from dtool_info.dataset import uri
    runner = CliRunner()

    result = runner.invoke(uri, [lion_dataset_path])
    assert result.exit_code == 0

    output = result.output.strip()
    assert output.startswith("file://")
    assert output.endswith(lion_dataset_path)
