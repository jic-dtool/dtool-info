"""Test the ``dtool ls`` command."""

import os

from click.testing import CliRunner

from . import chdir_fixture  # NOQA
from . import SAMPLE_DATASETS

lion_dataset_uri = "file://" + os.path.join(SAMPLE_DATASETS, "lion")


def test_dataset_ls_functional():

    from dtoolcore import DataSet
    from dtool_info.dataset import ls

    # Create one expected line.
    lion_ds = DataSet.from_uri(lion_dataset_uri)
    expected_line = "{} - {}".format(
        lion_ds.uuid,
        lion_ds.name
    )

    runner = CliRunner()

    result = runner.invoke(ls, [SAMPLE_DATASETS])
    assert result.exit_code == 0
    assert result.output.find(expected_line) != -1


def test_works_with_relative_path(chdir_fixture):  # NOQA

    import shutil
    from dtoolcore import DataSet
    from dtool_info.dataset import ls

    lion_directory = os.path.join(SAMPLE_DATASETS, "lion")
    shutil.copytree(lion_directory, "lion")

    # Create one expected line.
    lion_ds = DataSet.from_uri(lion_dataset_uri)
    expected_line = "{} - {}".format(
        lion_ds.uuid,
        lion_ds.name
    )

    runner = CliRunner()

    result = runner.invoke(ls, ["."])
    assert result.exit_code == 0
    assert result.output.find(expected_line) != -1

#def test_dataset_ls_dataset_content_functional():
#
#    from dtoolcore import DataSet
#    from dtool_info.dataset import ls
#
#    # Create one expected output.
#    expected_lines = []
#    lion_ds = DataSet.from_uri(lion_dataset_uri)
#    for i in lion_ds.identifiers:
#        props = lion_ds.item_properties(i)
#        line = "{} - {}".format(i, props["relpath"])
#        expected_lines.append(line)
#
#    runner = CliRunner()
#
#    result = runner.invoke(ls, [lion_dataset_uri])
#    assert result.exit_code == 0
#    for lin in expected_lines:
#        assert result.output.find(line) != -1
