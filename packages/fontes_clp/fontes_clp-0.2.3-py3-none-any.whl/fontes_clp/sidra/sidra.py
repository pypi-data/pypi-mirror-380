import json
import httpx
import pandas as pd
from typing import Sequence, Iterable
from fontes_clp.sidra.tabelas import Tabela
from fontes_clp.sidra.variaveis import Variavel
from fontes_clp.common.estados import Estado, _get_estado_from_codigo_ibge

_sidra_url = "https://apisidra.ibge.gov.br/"
_sidra_descritores_url = "https://apisidra.ibge.gov.br/DescritoresTabela"


class Sidra():
    ano: int
    estado: Estado | Sequence[Estado]
    tabela: Tabela
    variavel: Variavel

    def __init__(
        self,
        ano: int,
        estado: Estado | Sequence[Estado],
        tabela: Tabela,
        variavel: Variavel,
    ):
        self.ano = ano
        self.estado = estado
        self.tabela = tabela
        self.variavel = variavel

    def _get_periodos_disponiveis(self) -> str:
        with httpx.Client() as client:
            req = httpx.Request(
                "GET",
                f"{_sidra_descritores_url}/t/{self.tabela.value}",
                headers={
                    "Content-Type": "application/json",
                }
            )
            res = client.send(req, follow_redirects=True)
            obj = json.loads(res.text)

            if isinstance(self.ano, Iterable):
                ano_valor = [str(ano) for ano in self.ano]
            else:
                ano_valor = str(self.ano)

            periodos = []
            for periodo in obj["Periodos"]:
                original = str(periodo["Codigo"])
                codigo = original[:4]
                if codigo in ano_valor:
                    periodos.append(original)

            return periodos

    def _get_url(self) -> str:
        periodos = self._get_periodos_disponiveis()

        if isinstance(self.estado, Iterable):
            estado_valor = ",".join(
                [str(estado.get_codigo_ibge()) for estado in self.estado],
            )
        else:
            estado_valor = str(self.estado.get_codigo_ibge())

        return (
            f"{_sidra_url}/values/h/n"
            f"/t/{self.tabela.value}"
            f"/n3/{estado_valor}"
            f"/v/{self.variavel.value}"
            f"/p/{','.join(periodos)}"
        )

    def get_dados(self) -> pd.DataFrame:
        with httpx.Client() as client:
            req = httpx.Request(
                "GET",
                self._get_url(),
                headers={
                    "Content-Type": "application/json",
                }
            )
            res = client.send(req, follow_redirects=True)
            obj = json.loads(res.text)

            dados = []
            for dado in obj:
                ano = int(dado["D3C"][:4])
                estado = int(dado["D1C"])
                estado = _get_estado_from_codigo_ibge(estado).get_sigla()
                valor = float(dado["V"])

                dados.append((ano, estado, valor))

            return (
                pd.DataFrame(
                    dados,
                    columns=["Ano", "Estado", "Valor"],
                )
                .groupby(["Ano", "Estado"], as_index=False).mean()
                .sort_values(["Ano", "Estado"])
            )
