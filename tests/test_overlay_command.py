"""Test the ``dtool overlay`` command."""

import os
import json

from click.testing import CliRunner

import dtoolcore

from . import SAMPLE_DATASETS_DIR

people_dataset_uri = "file://" + os.path.join(
    SAMPLE_DATASETS_DIR,
    "people"
)


def test_overlay_list_command():

    from dtool_info.overlay import ls

    runner = CliRunner()

    result = runner.invoke(ls, [people_dataset_uri])
    assert result.exit_code == 0
    assert result.output.find("age") != -1
    assert result.output.find("gender") != -1


def test_overlay_show_command():
    from dtool_info.overlay import show

    runner = CliRunner()

    result = runner.invoke(show, [people_dataset_uri, "age"])
    assert result.exit_code == 0
    age_overlay = json.loads(result.output)

    patrick_id = dtoolcore.utils.generate_identifier("patrick.txt")
    assert age_overlay[patrick_id] == 34


def test_overlay_show_command_with_nonexisting_overlay_name():
    from dtool_info.overlay import show

    runner = CliRunner()

    result = runner.invoke(show, [people_dataset_uri, "dontexit"])
    assert result.exit_code == 11
