from typing import Any, List

import pytest

from apolo_sdk import Secret

from apolo_cli.formatters.secrets import SecretsFormatter, SimpleSecretsFormatter


@pytest.fixture
def secrets_list() -> List[Secret]:
    return [
        Secret(
            key="key1",
            owner="user",
            cluster_name="cluster",
            org_name="NO_ORG",
            project_name="test-project",
        ),
        Secret(
            key="key2",
            owner="user",
            cluster_name="cluster",
            org_name="test-org",
            project_name="test-project",
        ),
        Secret(
            key="key3",
            owner="anotheruser",
            cluster_name="cluster",
            org_name="NO_ORG",
            project_name="test-project",
        ),
    ]


def test_secrets_formatter_simple(secrets_list: List[Secret], rich_cmp: Any) -> None:
    fmtr = SimpleSecretsFormatter()
    rich_cmp(fmtr(secrets_list))


def test_secrets_formatter_short(secrets_list: List[Secret], rich_cmp: Any) -> None:
    fmtr = SecretsFormatter(str)
    rich_cmp(fmtr(secrets_list))
