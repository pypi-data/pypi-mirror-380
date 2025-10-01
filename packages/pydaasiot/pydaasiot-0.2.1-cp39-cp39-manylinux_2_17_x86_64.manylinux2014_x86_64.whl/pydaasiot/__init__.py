from importlib.metadata import version as _pkg_version

try:
    from ._core import *   # esporta le API C++ esposte via pybind11
except Exception as _e:     # messaggio chiaro se manca la wheel adeguata
    raise ImportError(
        "Impossibile importare il modulo nativo 'pydaasiot._core'. "
        "Assicurati di installare una wheel compatibile con il tuo sistema."
    ) from _e

__version__ = None
try:
    __version__ = _pkg_version("pydaasiot")
except Exception:
    pass  # in dev/editable mode potrebbe non essere risolvibile
