"""Project hooks."""
from typing import Any, Dict, Iterable, Optional

from kedro.config import OmegaConfigLoader
from kedro.framework.hooks import hook_impl
from kedro.io import DataCatalog


class ProjectHooks:
    @hook_impl
    def register_config_loader(
        self,
        conf_paths: Iterable[str],
        env: str,
        extra_params: Dict[str, Any],
    ) -> OmegaConfigLoader:
        return OmegaConfigLoader(conf_paths)

    @hook_impl
    def register_catalog(
        self,
        catalog: Optional[Dict[str, Dict[str, Any]]],
        credentials: Dict[str, Dict[str, Any]],
        load_versions: Dict[str, str],
        save_version: str,
    ) -> DataCatalog:
        return DataCatalog.from_config(
            catalog, credentials, load_versions, save_version
        )
