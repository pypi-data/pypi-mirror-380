import re
import httpx
import pandas as pd
from typing import Sequence
from bs4 import BeautifulSoup
from collections.abc import Iterable
from fontes_clp.common.estados import Estado
from fontes_clp.tabnet.grupos import GruposCausas

_tabnet_options_url = (
    "http://tabnet.datasus.gov.br/cgi/deftohtm.exe?sih/cnv/fruf.def"
)

_tabnet_url = (
    "http://tabnet.datasus.gov.br/cgi/tabcgi.exe?sih/cnv/fruf.def"
)


class TabNetMorbidades():
    ano: int | Sequence[int]
    estado: Estado | Sequence[Estado]
    grupo: GruposCausas | Sequence[GruposCausas]

    def __init__(
        self,
        ano: int | Sequence[int],
        estado: Estado = Estado | Sequence[Estado],
        grupo: GruposCausas | Sequence[GruposCausas] = GruposCausas.TODAS_AS_CATEGORIAS,
    ):
        self.ano = ano
        self.estado = estado
        self.grupo = grupo

    def _get_conteudo(self) -> str:
        with httpx.Client() as client:
            req = httpx.Request(
                "GET",
                _tabnet_options_url,
            )
            res = client.send(req, follow_redirects=True)
            soup = BeautifulSoup(res.text, features="html.parser")
            el = soup.select('select[name="Arquivos"]')
            options = el[0].find_all("option")

            values = []
            for option in options:
                value = option.get("value")
                if value:
                    values.append(value)

            arquivos = ""
            if isinstance(self.ano, Iterable):
                for ano in self.ano:
                    for mes in range(1, 13):
                        arquivo = f"fruf{(ano % 100):02d}{mes:02d}.dbf"

                        if arquivo in values:
                            arquivos += f"&Arquivos={arquivo}"
            else:
                for mes in range(1, 13):
                    arquivo = f"fruf{(self.ano % 100):02d}{mes:02d}.dbf"

                    if arquivo in values:
                        arquivos += f"&Arquivos={arquivo}"

            if isinstance(self.estado, Iterable):
                estado_valor = ""
                for estado in self.estado:
                    estado_valor += f"&SUnidade_da_Federa%E7%E3o={estado.value}"
            else:
                estado_valor = f"&SUnidade_da_Federa%E7%E3o={self.estado.value}"

            if isinstance(self.grupo, Iterable):
                grupo_valor = ""
                for grupo in self.grupo:
                    grupo_valor += f"&SGrupo_de_Causas={grupo.value}"
            elif isinstance(self.grupo.value, Iterable):
                grupo_valor = ""
                for grupo in self.grupo.value:
                    grupo_valor += f"&SGrupo_de_Causas={grupo}"
            else:
                grupo_valor = f"&SGrupo_de_Causas={self.grupo.value}"

            return (
                "Linha=Unidade_da_Federa%E7%E3o"
                "&Coluna=Ano_processamento"
                "&Incremento=Interna%E7%F5es"
                f"{arquivos}"
                "&SRegi%E3o=TODAS_AS_CATEGORIAS__"
                "&pesqmes2=Digite+o+texto+e+ache+f%E1cil"
                f"{estado_valor}"
                "&SCar%E1ter_atendimento=TODAS_AS_CATEGORIAS__"
                "&SRegime=TODAS_AS_CATEGORIAS__"
                "&pesqmes5=Digite+o+texto+e+ache+f%E1cil"
                "&SGrande_Grup_Causas=TODAS_AS_CATEGORIAS__"
                "&pesqmes6="
                f"{grupo_valor}"
                "&pesqmes7=Digite+o+texto+e+ache+f%E1cil"
                "&SCategorias_Causas=TODAS_AS_CATEGORIAS__"
                "&pesqmes8=Digite+o+texto+e+ache+f%E1cil"
                "&SFaixa_Et%E1ria_1=TODAS_AS_CATEGORIAS__"
                "&pesqmes9=Digite+o+texto+e+ache+f%E1cil"
                "&SFaixa_Et%E1ria_2=TODAS_AS_CATEGORIAS__"
                "&SSexo=TODAS_AS_CATEGORIAS__"
                "&SCor%2Fra%E7a=TODAS_AS_CATEGORIAS__"
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
