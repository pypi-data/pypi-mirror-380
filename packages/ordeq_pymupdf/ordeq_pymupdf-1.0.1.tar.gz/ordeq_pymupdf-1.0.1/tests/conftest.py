from pathlib import Path

import pytest


@pytest.fixture
def resources_dir() -> Path:
    """
    Returns:
        the path to the resources directory
    """

    PACKAGE_DIR = Path(__file__).resolve().parent
    return PACKAGE_DIR / "resources"
