from importlib import metadata
from importlib.metadata import PackageNotFoundError
from unittest import mock

import pytest
from pure_function_decorators.version import (
    __version__,
    get_version,
    get_version_from_metadata,
    get_version_from_pyproject,
)


def test_get_version_from_metadata() -> None:
    try:
        value = get_version_from_metadata()
    except metadata.PackageNotFoundError:
        pytest.skip("package metadata not available")
    assert value == __version__


def test_get_version_from_pyproject() -> None:
    assert get_version_from_pyproject() == __version__


def test_get_version__uses_pyproject() -> None:
    expected_version = "1.2.3"
    with (
        mock.patch(
            "pure_function_decorators.version.get_version_from_metadata",
            side_effect=PackageNotFoundError,
        ) as mocked_metadata,
        mock.patch(
            "pure_function_decorators.version.get_version_from_pyproject",
            return_value=expected_version,
        ) as mocked_pyproject,
    ):
        computed_version = get_version()
        assert computed_version == expected_version

        mocked_metadata.assert_called_once()
        mocked_pyproject.assert_called_once()


def test_get_version__uses_metadata() -> None:
    expected_version = "1.2.3"
    with (
        mock.patch(
            "pure_function_decorators.version.get_version_from_metadata",
            return_value=expected_version,
        ) as mocked_metadata,
        mock.patch(
            "pure_function_decorators.version.get_version_from_pyproject",
            side_effect=FileNotFoundError,
        ) as mocked_pyproject,
    ):
        computed_version = get_version()
        assert computed_version == expected_version

        mocked_metadata.assert_called_once()
        mocked_pyproject.assert_not_called()


def test_get_version__returns_unknown_if_both_fail() -> None:
    expected_version = "unknown"
    with (
        mock.patch(
            "pure_function_decorators.version.get_version_from_metadata",
            side_effect=PackageNotFoundError,
        ) as mocked_metadata,
        mock.patch(
            "pure_function_decorators.version.get_version_from_pyproject",
            side_effect=FileNotFoundError,
        ) as mocked_pyproject,
    ):
        computed_version = get_version()
        assert computed_version == expected_version

        mocked_metadata.assert_called_once()
        mocked_pyproject.assert_called_once()
