from pydantic import BaseModel
from typing import List, Literal, Optional


class Node(BaseModel):
    id: str
    type: Literal["PAGE", "ACTION", "DECISION", "LOOP", "END", "DEFAULT"]
    label: List[str]


class Edge(BaseModel):
    from_: List[str]
    to: List[str]
    condition: Optional[bool]


class Graph(BaseModel):
    name: str
    nodes: List[Node]
    edges: List[Edge]
