"""
    Helper functions for working with Datastar projects
"""

import os
import sys
from typing import Dict, List, Optional, Tuple, Any
from .frog_platform import OptilogicClient

# pylint: disable=logging-fstring-interpolation

DSTAR_IDLE_TRANSACTION_TIMEOUT = os.getenv("DSTAR_IDLE_TRANSACTION_TIMEOUT", 1800)
ATLAS_API_BASE_URL = os.getenv("ATLAS_API_BASE_URL", "https://api.optilogic.app/v0")

class Datastar:
    """
    Datastar class with helper functions for accessing Datastar projects
    """

    # This allows app key to be set once for all instances, makes utilities easier to write
    class_app_key = None

    # Helper method for setting up app key
    @classmethod
    def __set_app_key__(
        cls,
        app_key: Optional[str],
        raise_if_not_found: Optional[bool] = True
    ) -> str:
        """
        Helper method for setting up app key.

        There are 4 ways to set the app key:
        1) Passed in argument when opening a model e.g. FrogModel(app_key="my_app_key", model_name="my_model")
        2) Set via class variable (used for all instances of FrogModel, used in utilities)
        3) Via Enviroment var, in Andromeda (if running in Andromeda)
        4) Via app.key file (when running locally, place file in folder with your script)

        Args:
            app_key: Optional app key

        Returns:
            App key
        
        """
        try:
            found_app_key = app_key or cls.class_app_key or os.environ.get("OPTILOGIC_JOB_APPKEY")

            if not found_app_key:
                initial_script_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
                file_path = os.path.join(initial_script_dir, "app.key")
                if os.path.exists(file_path):
                    with open(file_path, "r", encoding="utf-8") as file:
                        found_app_key = file.read().strip()

            if not found_app_key and raise_if_not_found:
                raise ValueError("App key not found. Please provide a valid app key.")

            return found_app_key
        except Exception as e:
            # cls.log.exception(f"Error setting app key: {e}", exc_info=True)
            raise ValueError(f"Error setting app key: {e}")

    def __init__(
        self,
        project_name: Optional[str] = None,
        connection_string: Optional[str] = None,
        application_name: str = "Datastar User Library",
        app_key: Optional[str] = None
    ) -> None:
        pass


    