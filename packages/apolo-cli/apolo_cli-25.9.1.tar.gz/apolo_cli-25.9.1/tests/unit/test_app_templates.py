import tempfile
from contextlib import asynccontextmanager, contextmanager
from typing import Any, AsyncIterator, Iterator, List
from unittest import mock

from apolo_sdk import AppTemplate
from apolo_sdk._apps import Apps

_RunCli = Any


@contextmanager
def mock_apps_list_template_versions(
    template_name: str, versions: List[str]
) -> Iterator[None]:
    """Context manager to mock the Apps.list_template_versions method."""
    with mock.patch.object(Apps, "list_template_versions") as mocked:

        @asynccontextmanager
        async def async_cm(**kwargs: Any) -> AsyncIterator[AsyncIterator[AppTemplate]]:
            async def async_iterator() -> AsyncIterator[AppTemplate]:
                for version in versions:
                    yield AppTemplate(
                        name=template_name,
                        version=version,
                        title=f"{template_name} {version}",
                        short_description=f"Version {version} of {template_name}",
                        tags=[],
                        input=None,
                        description="",
                    )

            yield async_iterator()

        mocked.side_effect = async_cm
        yield


@contextmanager
def mock_apps_list_templates(templates: List[AppTemplate]) -> Iterator[None]:
    """Context manager to mock the Apps.list_templates method."""
    with mock.patch.object(Apps, "list_templates") as mocked:

        @asynccontextmanager
        async def async_cm(**kwargs: Any) -> AsyncIterator[AsyncIterator[AppTemplate]]:
            async def async_iterator() -> AsyncIterator[AppTemplate]:
                for template in templates:
                    yield template

            yield async_iterator()

        mocked.side_effect = async_cm
        yield


@contextmanager
def mock_apps_get_template(template: AppTemplate) -> Iterator[None]:
    """Context manager to mock the Apps.get_template method."""
    with mock.patch.object(Apps, "get_template") as mocked:

        async def async_func(**kwargs: Any) -> AppTemplate:
            return template

        mocked.side_effect = async_func
        yield


@contextmanager
def mock_apps_get_template_none() -> Iterator[None]:
    """Context manager to mock the Apps.get_template method returning None."""
    with mock.patch.object(Apps, "get_template") as mocked:

        async def async_func(**kwargs: Any) -> None:
            return None

        mocked.side_effect = async_func
        yield


def test_app_template_ls_with_templates(run_cli: _RunCli) -> None:
    """Test the app_template ls command when templates are returned."""
    templates = [
        AppTemplate(
            name="stable-diffusion",
            title="Stable Diffusion",
            version="master",
            short_description="AI image generation model",
            tags=["ai", "image", "generation"],
            input=None,
            description="",
        ),
        AppTemplate(
            name="jupyter-notebook",
            title="Jupyter Notebook",
            version="1.0.0",
            short_description="Interactive computing environment",
            tags=["jupyter", "notebook", "python"],
            input=None,
            description="",
        ),
    ]

    with mock_apps_list_templates(templates):
        capture = run_cli(["app-template", "ls"])

    assert not capture.err
    assert "stable-diffusion" in capture.out
    assert "Stable Diffusion" in capture.out
    assert "master" in capture.out
    assert "AI image generation model" in capture.out
    assert "ai, image, generation" in capture.out
    assert capture.code == 0


def test_app_template_ls_no_templates(run_cli: _RunCli) -> None:
    """Test the app_template ls command when no templates are returned."""
    with mock_apps_list_templates([]):
        capture = run_cli(["app-template", "ls"])

    assert not capture.err
    assert "No app templates found." in capture.out
    assert capture.code == 0


def test_app_template_ls_quiet_mode(run_cli: _RunCli) -> None:
    """Test the app_template ls command in quiet mode."""
    templates = [
        AppTemplate(
            name="stable-diffusion",
            title="Stable Diffusion",
            version="master",
            short_description="AI image generation model",
            tags=["ai", "image", "generation"],
            input=None,
            description="",
        ),
        AppTemplate(
            name="jupyter-notebook",
            title="Jupyter Notebook",
            version="1.0.0",
            short_description="Interactive computing environment",
            tags=["jupyter", "notebook", "python"],
            input=None,
            description="",
        ),
    ]

    with mock_apps_list_templates(templates):
        capture = run_cli(["-q", "app-template", "ls"])

    assert not capture.err
    assert "stable-diffusion" in capture.out
    assert "jupyter-notebook" in capture.out
    assert "Stable Diffusion" not in capture.out  # Title should not be present
    assert capture.code == 0


def test_app_template_ls_quiet_mode_no_templates(run_cli: _RunCli) -> None:
    """Test the app_template ls command in quiet mode when no templates are returned."""
    with mock_apps_list_templates([]):
        capture = run_cli(["-q", "app-template", "ls"])

    assert not capture.err
    assert capture.out.strip() == ""
    assert capture.code == 0


def test_app_template_ls_versions_with_versions(run_cli: _RunCli) -> None:
    """Test the app_template ls-versions command when versions are returned."""
    versions = ["1.0.0", "1.1.0", "2.0.0"]

    with mock_apps_list_template_versions("stable-diffusion", versions):
        capture = run_cli(["app-template", "ls-versions", "stable-diffusion"])

    assert not capture.err
    assert "1.0.0" in capture.out
    assert "1.1.0" in capture.out
    assert "2.0.0" in capture.out
    assert "stable-diffusion" in capture.out
    assert capture.code == 0


def test_app_template_ls_versions_no_versions(run_cli: _RunCli) -> None:
    """Test the app_template ls-versions command when no versions are returned."""
    with mock_apps_list_template_versions("stable-diffusion", []):
        capture = run_cli(["app-template", "ls-versions", "stable-diffusion"])

    assert not capture.err
    assert "No versions found for app template 'stable-diffusion'" in capture.out
    assert capture.code == 0


def test_app_template_ls_versions_quiet_mode(run_cli: _RunCli) -> None:
    """Test the app_template ls-versions command in quiet mode."""
    versions = ["1.0.0", "2.0.0", "latest"]

    with mock_apps_list_template_versions("stable-diffusion", versions):
        capture = run_cli(["-q", "app-template", "ls-versions", "stable-diffusion"])

    assert not capture.err
    # In quiet mode with is_version_list=True, we should expect only version numbers
    assert (
        "stable-diffusion" not in capture.out
    )  # Template name should not be in output
    assert "1.0.0" in capture.out
    assert "2.0.0" in capture.out
    assert "latest" in capture.out
    assert capture.code == 0


def test_app_template_ls_versions_quiet_mode_no_versions(run_cli: _RunCli) -> None:
    with mock_apps_list_template_versions("stable-diffusion", []):
        capture = run_cli(["-q", "app-template", "ls-versions", "stable-diffusion"])

    assert not capture.err
    assert capture.out.strip() == ""
    assert capture.code == 0


def test_app_template_ls_versions_with_cluster_option(run_cli: _RunCli) -> None:
    """Test the app_template ls-versions command with cluster option."""
    versions = ["1.0.0"]

    # Need to patch the cluster validation first
    with mock.patch("apolo_cli.click_types.CLUSTER.convert") as convert_mock:
        convert_mock.return_value = "test-cluster"

        with mock_apps_list_template_versions("stable-diffusion", versions):
            capture = run_cli(
                [
                    "app-template",
                    "ls-versions",
                    "stable-diffusion",
                    "--cluster",
                    "test-cluster",
                ]
            )

    assert not capture.err
    assert "1.0.0" in capture.out
    assert capture.code == 0


def test_app_template_get_table_format(run_cli: _RunCli) -> None:
    """Test the app_template get command with yaml format (default)."""
    template = AppTemplate(
        name="stable-diffusion",
        title="Stable Diffusion",
        version="master",
        short_description="AI image generation model",
        description="A detailed description of Stable Diffusion",
        tags=["ai", "image-generation"],
        input={
            "type": "object",
            "properties": {
                "http": {
                    "type": "object",
                    "properties": {
                        "port": {"type": "integer", "default": 8080},
                        "host": {"type": "string", "default": "localhost"},
                    },
                }
            },
        },
    )

    with mock_apps_get_template(template):
        capture = run_cli(["app-template", "get", "stable-diffusion"])

    assert not capture.err
    assert "template_name: stable-diffusion" in capture.out
    assert "template_version: master" in capture.out
    assert "# Application template configuration for: stable-diffusion" in capture.out
    assert "port: 8080" in capture.out
    assert "host: localhost" in capture.out
    assert capture.code == 0


def test_app_template_get_yaml_format(run_cli: _RunCli) -> None:
    """Test the app_template get command with YAML format."""
    template = AppTemplate(
        name="test-ping",
        title="Test Ping",
        version="latest",
        short_description="Simple ping test",
        description="",
        tags=[],
        input={
            "type": "object",
            "properties": {
                "http": {
                    "type": "object",
                    "properties": {
                        "port": {"type": "integer", "default": 8081},
                        "host": {"type": "string", "default": "test"},
                    },
                }
            },
        },
    )

    with mock_apps_get_template(template):
        capture = run_cli(["app-template", "get", "test-ping", "-o", "yaml"])

    assert not capture.err
    assert "template_name: test-ping" in capture.out
    assert "template_version: latest" in capture.out
    assert "port: 8081" in capture.out
    assert "host: test" in capture.out
    assert "# Application template configuration for: test-ping" in capture.out
    assert capture.code == 0


def test_app_template_get_yaml_format_dockerhub(run_cli: _RunCli) -> None:
    """Test the app_template get command with YAML format for dockerhub-like schema."""
    template = AppTemplate(
        name="dockerhub",
        title="DockerHub",
        version="v25.5.0",
        short_description="Access images from your private DockerHub repositories",
        description="",
        tags=[],
        input={
            "type": "object",
            "properties": {
                "dockerhub": {
                    "type": "object",
                    "properties": {
                        "username": {"type": "string"},
                        "password": {"type": "string"},
                        "registry": {
                            "type": "string",
                            "default": "https://index.docker.io/v1/",
                        },
                    },
                    "required": ["username", "password"],
                }
            },
            "required": ["dockerhub"],
        },
    )

    with mock_apps_get_template(template):
        capture = run_cli(["app-template", "get", "dockerhub", "-o", "yaml"])

    assert not capture.err
    assert "template_name: dockerhub" in capture.out
    assert "template_version: v25.5.0" in capture.out
    # Check that dockerhub is properly nested
    assert "dockerhub:" in capture.out
    assert "username: ''" in capture.out
    assert "password: ''" in capture.out
    assert "registry: https://index.docker.io/v1/" in capture.out
    assert capture.code == 0


def test_app_template_get_json_format(run_cli: _RunCli) -> None:
    """Test the app_template get command with JSON format."""
    template = AppTemplate(
        name="stable-diffusion",
        title="Stable Diffusion",
        version="master",
        short_description="AI image generation model",
        description="A detailed description",
        tags=["ai"],
        input={"type": "object", "properties": {}},
    )

    with mock_apps_get_template(template):
        capture = run_cli(["app-template", "get", "stable-diffusion", "-o", "json"])

    assert not capture.err
    assert '"template_name": "stable-diffusion"' in capture.out
    assert '"template_version": "master"' in capture.out
    assert '"input":' in capture.out
    assert capture.code == 0


def test_app_template_get_with_file_output(run_cli: _RunCli) -> None:
    """Test the app_template get command with file output."""
    template = AppTemplate(
        name="test-app",
        title="Test Application",
        version="1.0.0",
        short_description="Test app",
        description="",
        tags=[],
        input={"type": "object", "properties": {"name": {"type": "string"}}},
    )

    with tempfile.NamedTemporaryFile(
        mode="w", delete=False, suffix=".yaml"
    ) as tmp_file:
        temp_path = tmp_file.name

    try:
        with mock_apps_get_template(template):
            capture = run_cli(
                ["app-template", "get", "test-app", "-o", "yaml", "-f", temp_path]
            )

        assert not capture.err
        assert f"Template saved to {temp_path}" in capture.out
        assert capture.code == 0

        # Check file content
        with open(temp_path) as f:
            content = f.read()
            assert "template_name: test-app" in content
            assert "template_version: 1.0.0" in content
    finally:
        import os

        if os.path.exists(temp_path):
            os.unlink(temp_path)


def test_app_template_get_with_version(run_cli: _RunCli) -> None:
    """Test the app_template get command with specific version."""
    template = AppTemplate(
        name="stable-diffusion",
        title="Stable Diffusion",
        version="2.0.0",
        short_description="Version 2.0",
        description="",
        tags=[],
        input=None,
    )

    with mock_apps_get_template(template):
        capture = run_cli(["app-template", "get", "stable-diffusion", "-V", "2.0.0"])

    assert not capture.err
    assert "template_name: stable-diffusion" in capture.out
    assert "template_version: 2.0.0" in capture.out
    assert "input: {}" in capture.out
    assert capture.code == 0


def test_app_template_get_not_found(run_cli: _RunCli) -> None:
    """Test the app_template get command when template is not found."""
    with mock_apps_get_template_none():
        capture = run_cli(["app-template", "get", "nonexistent-template"])

    assert capture.err == ""
    assert "ERROR: App template 'nonexistent-template' not found" in capture.out
    assert capture.code == 1
