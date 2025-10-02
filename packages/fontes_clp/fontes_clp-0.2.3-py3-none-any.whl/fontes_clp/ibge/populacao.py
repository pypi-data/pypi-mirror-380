import pandas as pd
from typing import Sequence, Iterable
import importlib.resources as resources
from fontes_clp.common import Estado, Sexo


class IBGEPopulacao():
    """
    Os dados apresentados aqui foram retirados diretamente das projeções mais
    recentes do IBGE, disponíveis em https://www.ibge.gov.br/estatisticas/sociais/populacao/9109-projecao-da-populacao.html
    """

    ano: int | Sequence[int]
    estado: Estado | Sequence[Estado]
    sexo: Sexo

    def __init__(
        self,
        ano: int | Sequence[int],
        estado: Estado | Sequence[Estado],
        sexo: Sexo = Sexo.AMBOS,
    ):
        self.ano = ano
        self.estado = estado
        self.sexo = sexo

    def get_dados(self) -> pd.DataFrame:
        with resources.open_binary("fontes_clp.ibge.dados", "dados.xlsx") as f:
            df = pd.read_excel(f, header=4)
            df.columns = df.iloc[0]
            df = df[1:]

            if isinstance(self.estado, Iterable):
                estados = [estado.get_sigla() for estado in self.estado]
                df = df[df["SIGLA"].isin(estados)]
            else:
                df = df[df["SIGLA"] == self.estado.get_sigla()]

            df = df[df["SEXO"] == self.sexo.get_nome()]

            if isinstance(self.ano, Iterable):
                for ano in self.ano:
                    if ano not in df.columns:
                        raise ValueError(f"{ano} não está disponível")

                df = df[["SIGLA", *self.ano]]
            else:
                if self.ano not in df.columns:
                    raise ValueError(f"{self.ano} não está disponível")

                df = df[["SIGLA", self.ano]]

            df = df.groupby("SIGLA", as_index=False).sum()
            df = df.melt(id_vars=["SIGLA"], var_name="Ano", value_name="Valor")
            df = df.rename({"SIGLA": "Estado"}, axis=1)
            df = df[["Ano", "Estado", "Valor"]]
            df = df.sort_values(["Ano", "Estado"])

            return df
