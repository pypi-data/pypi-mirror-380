from collections.abc import Mapping
from importlib.metadata import version as get_version
from logging import getLogger
from pathlib import Path

from .asset_getter import get_asset
from .constants import (
    BASE_WORKFLOW_ASSET_PATH,
)
from .constants import (
    BASE_WORKFLOW_FILE_PATH as BASE_WORKFLOW_FILE_PATH,
)
from .git_helpers import get_repo_name
from .presets import DISTRIBUTION_ARTIFACTS_DIR, LOCKFILE_ARTIFACT
from .semantic_release_config import SemanticReleaseConfiguration
from .utils import from_yaml

__version__ = get_version(__package__)

logger = getLogger(__name__)


def generate_semantic_release_config(project_repo_path: Path) -> None:
    repo_name = get_repo_name(project_repo_path)

    config = SemanticReleaseConfiguration(
        project_repo_path, LOCKFILE_ARTIFACT, repo_name, DISTRIBUTION_ARTIFACTS_DIR
    )
    config.write()


def generate_helper_script(script_path: Path) -> None:
    _create_dirs = script_path.parent.mkdir(parents=True, exist_ok=True)

    asset_path = Path(*script_path.parts[-2:])
    script: str = get_asset(asset_path)

    with script_path.open("w", encoding="utf-8") as script_file:
        script_file.write(script)


def generate_base_workflow(**kwargs: Mapping[str, str]) -> dict:
    workflow: str = get_asset(BASE_WORKFLOW_ASSET_PATH)
    yaml = from_yaml(workflow)

    env_dict = {k.upper(): v for k, v in kwargs.items()}
    yaml["env"].update(env_dict)

    return yaml
