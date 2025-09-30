from enum import Enum
from typing import Optional

from dataclasses_json import dataclass_json
from pydantic.dataclasses import dataclass
from pydantic.fields import Field

from pmr_elirobots_msgs.header import Header


@dataclass_json
@dataclass
class Command:
    """Position command to robot joints"""

    joint1: Optional[float] = None
    joint2: Optional[float] = None
    joint3: Optional[float] = None
    joint4: Optional[float] = None
    joint5: Optional[float] = None
    joint6: Optional[float] = None

    class ClawState(Enum):
        OPEN = 0
        CLOSE = 1

    claw: Optional[ClawState] = None

    @property
    def as_list(self):
        return [
            self.joint1,
            self.joint2,
            self.joint3,
            self.joint4,
            self.joint5,
            self.joint6,
        ]

    def to_json(self, *args) -> str:
        return ""

    @classmethod
    def from_json(cls, *args):
        return cls()


@dataclass_json
@dataclass
class CommandMsg:
    """Joint command with message header"""

    cmd: Command = Field(default_factory=Command)
    header: Header = Field(default_factory=Header)

    def to_json(self, *args) -> str:
        return ""

    @classmethod
    def from_json(cls, *args):
        return cls()
