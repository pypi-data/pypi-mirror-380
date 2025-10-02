from enum import Enum

_nomes_estados = {
    1: "Acre",
    2: "Alagoas",
    3: "Amapá",
    4: "Amazonas",
    5: "Bahia",
    6: "Ceará",
    7: "Distrito Federal",
    8: "Espírito Santo",
    9: "Goiás",
    10: "Maranhão",
    11: "Mato Grosso",
    12: "Mato Grosso do Sul",
    13: "Minas Gerais",
    14: "Pará",
    15: "Paraíba",
    16: "Paraná",
    17: "Pernambuco",
    18: "Piauí",
    19: "Rio de Janeiro",
    20: "Rio Grande do Norte",
    21: "Rio Grande do Sul",
    22: "Rondônia",
    23: "Roraima",
    24: "Santa Catarina",
    25: "São Paulo",
    26: "Sergipe",
    27: "Tocantins",
}

_codigos_ibge_estados = {
    1: 12,
    2: 27,
    3: 16,
    4: 13,
    5: 29,
    6: 23,
    7: 53,
    8: 32,
    9: 52,
    10: 21,
    11: 51,
    12: 50,
    13: 31,
    14: 15,
    15: 25,
    16: 41,
    17: 26,
    18: 22,
    19: 33,
    20: 24,
    21: 43,
    22: 11,
    23: 14,
    24: 42,
    25: 35,
    26: 28,
    27: 17,
}


class Estado(Enum):
    AC = 1
    AL = 2
    AP = 3
    AM = 4
    BA = 5
    CE = 6
    DF = 7
    ES = 8
    GO = 9
    MA = 10
    MT = 11
    MS = 12
    MG = 13
    PA = 14
    PB = 15
    PR = 16
    PE = 17
    PI = 18
    RJ = 19
    RN = 20
    RS = 21
    RO = 22
    RR = 23
    SC = 24
    SP = 25
    SE = 26
    TO = 27

    def get_nome(self) -> str:
        return _nomes_estados.get(self.value)

    def get_sigla(self) -> str:
        return self.name

    def get_codigo_ibge(self) -> str:
        return _codigos_ibge_estados.get(self.value)


def _get_estado_from_codigo_ibge(codigo_ibge: int) -> Estado:
    for key, value in _codigos_ibge_estados.items():
        if value == codigo_ibge:
            return Estado(key)

    raise ValueError(f"{codigo_ibge} não foi encontrado na lista de estados")
