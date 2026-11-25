"""Usa o classificador treinado (entrega da frente C para a frente D).

No servidor:
    from classificador.classificar import classificar
    tipo, confianca = classificar("quantas faltas eu tenho em cálculo?")

Devolve um dos tipos de classificador/tipos.py e a confiança (0 a 1).
Se a confiança ficar abaixo de LIMITE_CONFIANCA, devolve "fora_do_escopo",
para o chatbot admitir que não sabe em vez de inventar (FR-11, NFR-08).
O limite é proposta do agente e espera a confirmação do grupo.

No terminal, para testar: python classificador/classificar.py "sua pergunta"
"""

import sys
from functools import lru_cache
from pathlib import Path

import joblib

# O modelo salvo pode conter classes de classificador/bert.py (D-010).
sys.path.insert(0, str(Path(__file__).resolve().parent))

MODELO = Path(__file__).resolve().parent.parent / "models" / "classificador.joblib"
LIMITE_CONFIANCA = 0.5


@lru_cache(maxsize=1)
def _modelo():
    if not MODELO.exists():
        raise FileNotFoundError(
            f"{MODELO} não existe: rode python classificador/treinar.py")
    return joblib.load(MODELO)


def classificar(pergunta: str) -> tuple[str, float]:
    modelo = _modelo()
    probs = modelo.predict_proba([pergunta])[0]
    i = probs.argmax()
    tipo, confianca = modelo.classes_[i], float(probs[i])
    if confianca < LIMITE_CONFIANCA:
        return "fora_do_escopo", confianca
    return tipo, confianca


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for pergunta in sys.argv[1:] or ["quantas faltas eu tenho em cálculo?"]:
        tipo, conf = classificar(pergunta)
        print(f"{tipo:<16} {conf:.0%}  {pergunta}")
