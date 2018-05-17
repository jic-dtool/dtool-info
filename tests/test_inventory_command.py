"""Test the inventory command."""

from click.testing import CliRunner

from . import REPORT_DATASETS_DIR


def test_inventory_functional():

    from dtool_info.inventory import inventory

    runner = CliRunner()
    result = runner.invoke(inventory, [REPORT_DATASETS_DIR])
    assert result.exit_code == 0

    expected = [
        "19.0B   olssont 3 2018-05-16 big_cats",
        "11.0B   olssont 2 2018-05-16 toys",
        "30.0B           5"
    ]
    actual = result.output.strip().split("\n")
    for e, a in zip(expected, actual):
        assert e.strip() == a.strip()


def test_inventory_html_functional():

    from dtool_info.inventory import inventory

    runner = CliRunner()
    result = runner.invoke(inventory, ["-f", "html", REPORT_DATASETS_DIR])
    assert result.exit_code == 0

    assert result.output.find("<html>") != -1
    assert result.output.find("</html>") != -1


def test_inventory_csv_functional():

    from dtool_info.inventory import inventory

    runner = CliRunner()
    result = runner.invoke(inventory, ["-f", "csv", REPORT_DATASETS_DIR])
    assert result.exit_code == 0

    expected_starts = [
        "name,size_in_bytes,creator,num_items,date,uri",
        "big_cats,19,olssont,3,2018-05-16",
        "toys,11,olssont,2,2018-05-16",
    ]
    for a, e in zip(result.output.split("\n"), expected_starts):
        assert a.startswith(e)


def test_inventory_tsv_functional():

    from dtool_info.inventory import inventory

    runner = CliRunner()
    result = runner.invoke(inventory, ["-f", "tsv", REPORT_DATASETS_DIR])
    assert result.exit_code == 0

    expected_starts = [
        "name\tsize_in_bytes\tcreator\tnum_items\tdate\turi",
        "big_cats\t19\tolssont\t3\t2018-05-16",
        "toys\t11\tolssont\t2\t2018-05-16",
    ]
    for a, e in zip(result.output.split("\n"), expected_starts):
        assert a.startswith(e)
