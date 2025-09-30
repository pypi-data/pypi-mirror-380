import logging
import os
import sys

import click
from simple_logger.logger import get_logger

from apps.polarion.polarion_utils import find_polarion_ids, get_polarion_project_id, validate_polarion_requirements

LOGGER = get_logger(name="polarion-verify-tc-requirements")


@click.command()
@click.option(
    "--config-file-path",
    help="Provide absolute path to the config file. Any CLI option(s) would override YAML file",
    type=click.Path(),
    default=os.path.expanduser("~/.config/python-utility-scripts/config.yaml"),
)
@click.option("--project-id", "-p", help="Provide the polarion project id")
@click.option("--branch", "-b", help="Provide the github remote branch to run against", default="origin/main")
@click.option("--verbose", default=False, is_flag=True)
def has_verify(config_file_path: str, project_id: str, branch: str, verbose: bool) -> None:
    if verbose:
        LOGGER.setLevel(logging.DEBUG)
        # since the utilities are in apps.polarion.polarion_utils, we need to change log level
        # for apps.polarion.polarion_utils as well
        logging.getLogger("apps.polarion.polarion_utils").setLevel(logging.DEBUG)

    polarion_project_id = project_id or get_polarion_project_id(
        config_file_path=config_file_path, util_name="pyutils-polarion-verify-tc-requirements"
    )
    if added_ids := find_polarion_ids(polarion_project_id=polarion_project_id, string_to_match="added", branch=branch):
        LOGGER.debug(f"Checking following ids: {added_ids}")
        if tests_with_missing_requirements := validate_polarion_requirements(
            polarion_test_ids=added_ids,
            polarion_project_id=polarion_project_id,
        ):
            LOGGER.error(f"TestCases with missing requirement: {tests_with_missing_requirements}")
            sys.exit(1)


if __name__ == "__main__":
    has_verify()
