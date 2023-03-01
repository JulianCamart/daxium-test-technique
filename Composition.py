from typing import List
from Identifier import Identifier


class Composition:
    def __init__(self, identifiers: List[Identifier], operator: str, uuid: str):
        self.identifiers = identifiers
        self.operator = operator
        self.uuid = uuid
        self.readable = ''
        self.priority = 0
