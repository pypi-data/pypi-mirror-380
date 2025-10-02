from enum import Enum

_nomes_tabelas = {
    6472: "Rendimento médio mensal real e nominal das pessoas de 14 anos ou mais de idade ocupadas na semana de referência com rendimento de trabalho, habitualmente recebido em todos os trabalhos - Total, coeficiente de variação, variações em relação ao trimestre anterior e ao mesmo trimestre do ano anterior",
}


class Tabela(Enum):
    RENDIMENTO_MEDIO_MENSAL = 6472

    def get_nome(self) -> str:
        return _nomes_tabelas.get(self.value)
