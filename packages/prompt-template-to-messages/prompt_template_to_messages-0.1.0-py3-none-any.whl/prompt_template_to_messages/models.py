"""Core data models used during PT2M parsing and translation."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping, Sequence, Union


@dataclass(frozen=True)
class PT2MTag:
    """Structured representation of a PT2M tag."""

    name: str
    attrs: Mapping[str, Any]
    children: Sequence["Fragment"] = field(default_factory=tuple)

    def as_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "attrs": dict(self.attrs),
            "children": [
                child.as_dict() if isinstance(child, PT2MTag) else child for child in self.children
            ],
        }


Fragment = Union[str, PT2MTag]
