import re
import httpx
import pandas as pd
from typing import Sequence
from bs4 import BeautifulSoup
from collections.abc import Iterable
from fontes_clp.common.estados import Estado
from fontes_clp.tabnet.grupos import GruposObitos

_tabnet_url = (
    "http://tabnet.datasus.gov.br/cgi/tabcgi.exe?sim/cnv/ext10uf.def;"
)


class TabNetObitos():
    ano: int | Sequence[int]
    estado: Estado | Sequence[Estado]
    grupo: GruposObitos | Sequence[GruposObitos]

    def __init__(
        self,
        ano: int | Sequence[int],
        estado: Estado = Estado | Sequence[Estado],
        grupo: GruposObitos | Sequence[GruposObitos] = GruposObitos.TODAS_AS_CATEGORIAS,
    ):
        self.ano = ano
        self.estado = estado
        self.grupo = grupo

    def _get_conteudo(self) -> str:
        if isinstance(self.ano, Iterable):
            arquivos = ""
            for ano in self.ano:
                arquivos += f"&Arquivos=extuf{(ano % 100):02d}.dbf"
        else:
            arquivos = f"&Arquivos=extuf{(self.ano % 100):02d}.dbf"

        if isinstance(self.estado, Iterable):
            estado_valor = ""
            for estado in self.estado:
                estado_valor += f"&SUnidade_da_Federa%E7%E3o={estado.value}"
        else:
            estado_valor = f"&SUnidade_da_Federa%E7%E3o={self.estado.value}"

        if isinstance(self.grupo, Iterable):
            grupo_valor = ""
            for grupo in self.grupo:
                grupo_valor += f"&SGrupo_CID10={grupo.value}"
        elif isinstance(self.grupo.value, Iterable):
            grupo_valor = ""
            for grupo in self.grupo.value:
                grupo_valor += f"&SGrupo_CID10={grupo}"
        else:
            grupo_valor = f"&SGrupo_CID10={self.grupo.value}"

        return (
            "Linha=Unidade_da_Federa%E7%E3o"
            "&Coluna=Ano_do_%D3bito"
            "&Incremento=%D3bitos_p%2FOcorr%EAnc"
            f"{arquivos}"
            "&SRegi%E3o=TODAS_AS_CATEGORIAS__"
            "&pesqmes2=Digite+o+texto+e+ache+f%E1cil"
            f"{estado_valor}"
            "&SGrande_Grupo_CID10=TODAS_AS_CATEGORIAS__"
            "&pesqmes4=Digite+o+texto+e+ache+f%E1cil"
            f"{grupo_valor}"
            "&pesqmes5=Digite+o+texto+e+ache+f%E1cil"
            "&SCategoria_CID10=TODAS_AS_CATEGORIAS__"
            "&pesqmes6=Digite+o+texto+e+ache+f%E1cil"
            "&SFaixa_Et%E1ria=TODAS_AS_CATEGORIAS__"
            "&pesqmes7=Digite+o+texto+e+ache+f%E1cil"
            "&SFaixa_Et%E1ria_OPS=TODAS_AS_CATEGORIAS__"
            "&pesqmes8=Digite+o+texto+e+ache+f%E1cil"
            "&SFaixa_Et%E1ria_det=TODAS_AS_CATEGORIAS__"
            "&SFx.Et%E1ria_Menor_1A=TODAS_AS_CATEGORIAS__"
            "&SSexo=TODAS_AS_CATEGORIAS__"
            "&SCor%2Fra%E7a=TODAS_AS_CATEGORIAS__"
            "&SEscolaridade=TODAS_AS_CATEGORIAS__"
            "&SEstado_civil=TODAS_AS_CATEGORIAS__"
            "&SLocal_ocorr%EAncia=TODAS_AS_CATEGORIAS__"
            "&SAcid._Trabalho=TODAS_AS_CATEGORIAS__"
            "&formato=table"
            "&mostre=Mostra"
        )

    def get_dados(self) -> pd.DataFrame:
        with httpx.Client() as client:
            req = httpx.Request(
                "POST",
                _tabnet_url,
                content=self._get_conteudo(),
                headers={
                    "Content-Type": "application/x-www-form-urlencoded",
                }
            )
            res = client.send(req, follow_redirects=True)
            soup = BeautifulSoup(res.text, features="html.parser")
            el = soup.select('.tabdados tr > td[align="left"]')

            if isinstance(self.ano, Iterable):
                anos = sorted(list(self.ano))
            else:
                anos = [self.ano]

            if el and len(el) != 0:
                estados = []
                if isinstance(self.estado, Iterable):
                    for estado in self.estado:
                        nome_estado = re.search(estado.get_nome(), el[0].text)
                        if not nome_estado:
                            raise ValueError(
                                f"Não foi possível encontrar o estado {estado.get_nome()} nos resultados"
                            )

                        estados.append((estado.get_codigo_ibge(), estado.get_sigla()))

                    estados = sorted(estados, key=lambda x: x[0])
                    estados = [estado[1] for estado in estados]
                else:
                    nome_estado = re.search(self.estado.get_nome(), el[0].text)
                    if not nome_estado:
                        raise ValueError(
                            f"Não foi possível encontrar o estado {self.estado.get_nome()} nos resultados"
                        )

                    estados.append(self.estado.get_sigla())

                match = re.findall(r"((\d+)(\.\d+)?)+", str(el))
                if not match:
                    raise ValueError("Não foi possível encontrar o valor")

                match = match[len(anos)+1:]

                valores = []
                while len(match) != 0:
                    ivalores = []
                    for valor in match[1:len(anos)+1]:
                        ivalores.append(int(valor[0].replace(".", "")))

                    match = match[len(anos)+2:]
                    valores.append(ivalores)
            else:
                estados = []
                if isinstance(self.estado, Iterable):
                    for estado in self.estado:
                        estados.append(estado.get_sigla())
                else:
                    estados.append(self.estado.get_sigla())

                valores = [[None] * len(anos) for _ in range(len(estados))]

            df = pd.DataFrame({
                "Ano": [anos] * len(estados),
                "Estado": [[estado] * len(anos) for estado in estados],
                "Valor": valores,
            })

            return (
                df
                .explode(["Ano", "Estado", "Valor"])
                .sort_values(["Ano", "Estado"])
                .reset_index(drop=True)
            )
