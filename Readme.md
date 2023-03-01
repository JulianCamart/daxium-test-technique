# DAXIUM - CHALLENGE DEV FILTERING #

## Explications

L'objectif est d'écrire un algorithme qui va parser un fichier JSON envoyé en entrée et en sortir une représentation "humainement lisible" de sa composition.

Le JSON contient 2 types d'éléments :
  * des critères
  * des compositions

Les critères sont simples. Un UUID pour les identifier, et un nom pour les représenter.
Les compositions, comme leur nom l'indique, sont composées de plusieurs éléments. Elles regroupent des critères et/ou d'autres compositions.

Par exemple, prenons ce JSON :


```
{
    "criteria":
    [
        {
            "uuid": "9c7b4212-ad88-4817-afb4-f1ef2a21f28e",
            "name": "critère_1"
        },
        {
            "uuid": "1c944f87-b244-459b-ae42-efbcb032a1d3",
            "name": "critère_2"
        }
    ],
    "composition":
    [
        {
            "identifiers":
            [
                {
                    "uuid": "9c7b4212-ad88-4817-afb4-f1ef2a21f28e",
                    "type": "CRITERIA"
                },
                {
                    "uuid": "1c944f87-b244-459b-ae42-efbcb032a1d3",
                    "type": "CRITERIA"
                }
            ],
            "operator": "AND",
            "uuid": "d65a96f0-e90a-4289-8ad8-0eecad0492c0"
        }
    ]
}
```

Le résultat attendu sera : 

```
(critère_1 AND critère 2)
```

En effet, les seuls "identifiers" spécifiés dans la composition sont de type "CRITERIA". Mais une composition peut référencer d'autres compositions.
Par exemple : 


```
{
    "criteria":
    [
        {
            "uuid": "9c7b4212-ad88-4817-afb4-f1ef2a21f28e",
            "name": "critère_1"
        },
        {
            "uuid": "1c944f87-b244-459b-ae42-efbcb032a1d3",
            "name": "critère_2"
        }
    ],
    "composition":
    [
        {
            "identifiers":
            [
                {
                    "uuid": "9c7b4212-ad88-4817-afb4-f1ef2a21f28e",
                    "type": "CRITERIA"
                },
                {
                    "uuid": "1c944f87-b244-459b-ae42-efbcb032a1d3",
                    "type": "CRITERIA"
                }
            ],
            "operator": "AND",
            "uuid": "d65a96f0-e90a-4289-8ad8-0eecad0492c0"
        },
        {
            "identifiers":
            [
                {
                    "uuid": "9c7b4212-ad88-4817-afb4-f1ef2a21f28e",
                    "type": "CRITERIA"
                },
                {
                    "uuid": "d65a96f0-e90a-4289-8ad8-0eecad0492c0",
                    "type": "REFERENCE"
                }
            ],
            "operator": "OR",
            "uuid": "dd72e1e0-89e6-4d6d-b1ad-ef11e4740681"
        }
    ]
}
```

Le résultat attendu sera : 

```
(critère_1 OR (critère_1 AND critère 2))
```

On retrouve après "OR" la composition référencée entre parenthèses.


Voilà pour l'explication.



## Exercice

Est attendu en résultat de l'algorithme écrit, ce texte, à partir du JSON fourni ci-dessous :

> (critère_4 OR critère_3 OR (critère_5 AND critère_7 AND critère_6)) AND critère_1 AND critère_2

(L’ordre n’a pas d’importance, seule la logique en a).

Le JSON en entrée : 

```
{
    "criteria":
    [
        {
            "uuid": "9c7b4212-ad88-4817-afb4-f1ef2a21f28e",
            "name": "critère_1"
        },
        {
            "uuid": "1c944f87-b244-459b-ae42-efbcb032a1d3",
            "name": "critère_2"
        },
        {
            "uuid": "8259c681-5dd9-4304-bc48-cf93b00dbfe9",
            "name": "critère_3"
        },
        {
            "uuid": "e1cdc9fb-ab2d-4c15-9374-32b2a0de16ce",
            "name": "critère_4"
        },
        {
            "uuid": "01776afc-9332-4105-ba7e-ac2374ff2267",
            "name": "critère_5"
        },
        {
            "uuid": "9e1923df-85a6-4b55-bde3-08b7953ef48e",
            "name": "critère_6"
        },
        {
            "uuid": "32083edd-e4ab-400e-a06c-1c6d5957eecf",
            "name": "critère_7"
        }
    ],
    "composition":
    [
        {
            "identifiers":
            [
                {
                    "uuid": "4c6daaec-014a-473e-b98b-e58cc82aa081",
                    "type": "REFERENCE"
                },
                {
                    "uuid": "1c944f87-b244-459b-ae42-efbcb032a1d3",
                    "type": "CRITERIA"
                },
                {
                    "uuid": "9c7b4212-ad88-4817-afb4-f1ef2a21f28e",
                    "type": "CRITERIA"
                }
            ],
            "operator": "AND",
            "uuid": "d65a96f0-e90a-4289-8ad8-0eecad0492c0"
        },
        {
            "identifiers":
            [
                {
                    "uuid": "01776afc-9332-4105-ba7e-ac2374ff2267",
                    "type": "CRITERIA"
                },
                {
                    "uuid": "9e1923df-85a6-4b55-bde3-08b7953ef48e",
                    "type": "CRITERIA"
                },
                {
                    "uuid": "32083edd-e4ab-400e-a06c-1c6d5957eecf",
                    "type": "CRITERIA"
                }
            ],
            "operator": "AND",
            "uuid": "3723416c-83ab-48d0-b0db-aee3c1174af5"
        },
        {
            "identifiers":
            [
                {
                    "uuid": "e1cdc9fb-ab2d-4c15-9374-32b2a0de16ce",
                    "type": "CRITERIA"
                },
                {
                    "uuid": "3723416c-83ab-48d0-b0db-aee3c1174af5",
                    "type": "REFERENCE"
                },
                {
                    "uuid": "8259c681-5dd9-4304-bc48-cf93b00dbfe9",
                    "type": "CRITERIA"
                }
            ],
            "operator": "OR",
            "uuid": "4c6daaec-014a-473e-b98b-e58cc82aa081"
        }
    ]
}
```

Bon dev ! :-)