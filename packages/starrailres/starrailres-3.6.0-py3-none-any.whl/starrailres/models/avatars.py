from typing import Dict, Optional

from msgspec import Struct


class AvatarType(Struct):
    id: str  # avartar id
    name: str  # avartar name
    icon: str  # avartar icon


AvatarIndex = Dict[str, AvatarType]
