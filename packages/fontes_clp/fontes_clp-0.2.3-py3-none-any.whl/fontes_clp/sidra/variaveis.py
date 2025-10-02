from enum import Enum

_nomes_variaveis = {
    5929: "Rendimento médio mensal nominal das pessoas de 14 anos ou mais de idade ocupadas na semana de referência com rendimento de trabalho, habitualmente recebido em todos os trabalhos",
}


class Variavel(Enum):
    RENDIMENTO_MEDIO_MENSAL_NOMINAL = 5929

    def get_nome(self) -> str:
        return _nomes_variaveis.get(self.value)
