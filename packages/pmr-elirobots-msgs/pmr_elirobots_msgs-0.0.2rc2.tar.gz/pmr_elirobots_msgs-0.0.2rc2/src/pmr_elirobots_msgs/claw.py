from enum import Enum
from typing import Optional

from dataclasses_json import dataclass_json
from pydantic.dataclasses import dataclass
from pydantic.fields import Field

from pmr_elirobots_msgs.header import Header


@dataclass_json
@dataclass
class ClawCommand:
    """Position command to robot joints"""

    class ClawState(Enum):
        OPEN = 0
        CLOSE = 1

    claw: Optional[ClawState] = None

    @property
    def as_list(self):
        return [
            self.claw,
        ]

    def to_json(self, *args) -> str:
        return ""

    @classmethod
    def from_json(cls, *args):
        return cls()


@dataclass_json
@dataclass
class ClawCommandMsg:
    """Joint command with message header"""

    cmd: ClawCommand = Field(default_factory=ClawCommand)
    header: Header = Field(default_factory=Header)

    def to_json(self, *args) -> str:
        return ""

    @classmethod
    def from_json(cls, *args):
        return cls()
