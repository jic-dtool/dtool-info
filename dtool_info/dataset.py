"""Commands for getting information about datasets."""

import click

from dtool_cli.cli import (
    dataset_uri_argument,
    dataset_uri_validation,
)


@click.command()
@dataset_uri_argument
@click.argument("reference_dataset_uri", callback=dataset_uri_validation)
def diff(dataset_uri, reference_dataset_uri):
    """Report the difference between two datasets.

    1. Checks that the identifiers are identicial
    2. Checks that the sizes are identical
    3. Checks that the hashes are identical

    If a differences is detected in step 1, steps 2 and 3 will not be carried
    out. Similarly if a difference is detected in step 2, step 3 will not be
    carried out.

    When checking that the hashes are identical the hashes for the first
    dataset are recalculated using the hashing algorithm of the reference
    dataset.
    """
