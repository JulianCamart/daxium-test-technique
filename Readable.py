from typing import List
from Composition import Composition
from Criteria import Criteria


class Readable:
    def __init__(self, criterias: List[Criteria], compositions: List[Composition]):
        self.criterias = criterias
        self.compositions = compositions

    def __get_criteria(self, uuid: str) -> Criteria:
        criteria = next((cr for cr in self.criterias if cr.uuid == uuid), None)
        if criteria is None:
            raise Exception(f"The uuid: {uuid} can not be found")
        return criteria

    def __get_composition(self, uuid: str) -> Composition:
        composition = next((co for co in self.compositions if co.uuid == uuid), None)
        if composition is None:
            raise Exception(f"The uuid: {uuid} can not be found")
        return composition

    def __get_order(self, composition: Composition, order: int = 0) -> int:
        for identifier in composition.identifiers:
            if identifier.type == "REFERENCE":
                order = self.__get_order(self.__get_composition(identifier.uuid), order + 1)
        return order

    def __flatten(self) -> str:
        flatten_text = ''
        for composition in self.compositions:
            if composition.uuid in flatten_text:
                flatten_text = flatten_text.replace(f"__{composition.uuid}__", composition.readable)
            else:
                flatten_text += composition.readable
        return flatten_text

    def format(self) -> str:
        for composition in self.compositions:
            for index, identifier in enumerate(composition.identifiers):
                if identifier.type == "CRITERIA":
                    composition.readable += self.__get_criteria(identifier.uuid).name
                if identifier.type == "REFERENCE":
                    composition.readable += f"(__{identifier.uuid}__)"
                if index < len(composition.identifiers) - 1:
                    composition.readable += ' ' + composition.operator + ' '
            composition.priority = self.__get_order(composition)
        self.compositions.sort(key=lambda x: x.priority, reverse=True)
        return self.__flatten()
