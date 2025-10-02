from importlib.metadata import version

try:
    __version__ = version("fontes_clp")
except:
    __version__ = "0.2.3"

from .common import Estado, Sexo
from .tabnet import GruposObitos, GruposCausas, TabNetObitos, TabNetMorbidades
from .ibge import IBGEPopulacao
from .sidra import Sidra, Tabela, Variavel
from .fbsp import FBSP, VariavelFBSP

__all__ = [
    "Estado",
    "Sexo",
    "GruposObitos",
    "GruposCausas",
    "TabNetObitos",
    "TabNetMorbidades",
    "IBGEPopulacao",
    "Sidra",
    "Tabela",
    "Variavel",
    "FBSP",
    "VariavelFBSP",
    "common",
    "tabnet",
    "ibge",
    "sidra",
]
