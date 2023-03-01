import json

from Composition import Composition
from Criteria import Criteria
from Identifier import Identifier
from Readable import Readable


def get_readable_from_json(item: dict) -> str:
    criterias = []
    for criteria in item["criteria"]:
        criterias.append(Criteria(criteria["name"], criteria["uuid"]))

    compositions = []
    for composition in item["composition"]:
        identifiers = []
        for identifier in composition["identifiers"]:
            identifiers.append(Identifier(identifier["type"], identifier["uuid"]))
        compositions.append(Composition(identifiers, composition["operator"], composition["uuid"]))

    readable = Readable(criterias, compositions)
    return readable.format()


if __name__ == '__main__':
    f = open('test.json')
    data = json.load(f)

    print(get_readable_from_json(data["item_1"]))
    print(get_readable_from_json(data["item_2"]))
    print(get_readable_from_json(data["item_3"]))
