from enum import Enum


class Permission(Enum):
    READ = "read"
    WRITE = "write"

    def to_int(self) -> int:
        return 0 if self == Permission.READ else 1

    @classmethod
    def from_i32(cls, value: int) -> "Permission":
        """Convert integer code to Permission enum."""
        if value == 0:
            return cls.READ
        elif value == 1:
            return cls.WRITE
        else:
            raise ValueError(f"Invalid permission code: {value}")
