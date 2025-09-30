from pydantic import BaseModel
from typing import Any

def shallow_dump(state: dict[str, Any] | BaseModel) -> dict[str, Any]:
    """Convert Pydantic model to dict while preserving nested Pydantic objects.

    Args:
        state (dict[str, Any] | BaseModel): The state to convert.

    Returns:
        dict[str, Any]: The state as a dictionary with preserved nested Pydantic objects.
    """
