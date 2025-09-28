import pytest

from duplicaid.config import Config
from duplicaid.local import LocalExecutor


@pytest.fixture
def local_config():
    config = Config()
    config._data = {
        "execution_mode": "local",
        "containers": {"postgres": "postgres", "backup": "db-backup"},
        "paths": {"docker_compose": "./test.yml"},
    }
    return config


def test_local_executor_basic_commands(local_config):
    executor = LocalExecutor(local_config)

    with executor:
        stdout, stderr, exit_code = executor.execute("echo hello", show_command=False)
        assert stdout == "hello"
        assert exit_code == 0


def test_local_executor_failed_command(local_config):
    executor = LocalExecutor(local_config)

    with executor:
        stdout, stderr, exit_code = executor.execute("false", show_command=False)
        assert exit_code == 1


def test_local_executor_file_exists(local_config):
    executor = LocalExecutor(local_config)

    with executor:
        assert executor.file_exists("/etc/passwd")
        assert not executor.file_exists("/nonexistent/file")


def test_local_executor_docker_commands(local_config):
    executor = LocalExecutor(local_config)

    with executor:
        stdout, stderr, exit_code = executor.execute(
            "docker --version", show_command=False
        )
        assert "Docker version" in stdout or exit_code != 0
