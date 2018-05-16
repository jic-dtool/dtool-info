"""Test the report command."""

from click.testing import CliRunner

from . import REPORT_DATASETS_DIR


def test_report_functional():

    from dtool_info.report import report

    runner = CliRunner()
    result = runner.invoke(report, [REPORT_DATASETS_DIR])
    assert result.exit_code == 0

    expected = [
        "19.0B   olssont 3 2018-05-16 big_cats",
        "11.0B   olssont 2 2018-05-16 toys",
        "30.0B           5"
    ]
    actual = result.output.strip().split("\n")
    for e, a in zip(expected, actual):
        assert e.strip() == a.strip()


def test_report_html_functional():

    from dtool_info.report import report

    runner = CliRunner()
    result = runner.invoke(report, ["-f", "html", REPORT_DATASETS_DIR])
    assert result.exit_code == 0

    assert result.output.find("<html>") != -1
    assert result.output.find("</html>") != -1
