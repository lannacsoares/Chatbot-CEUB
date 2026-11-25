"""Separa o conjunto de teste, uma única vez (tarefa 01-03).

Uso: python classificador/separar.py

Lê dados/perguntas.csv e grava dados/treino.csv e dados/teste.csv,
com cerca de 20% de cada tipo no teste (separação estratificada, semente fixa).

O teste é congelado: se dados/teste.csv já existir, o script não faz nada.
Ninguém usa o teste para ajustar o classificador (02-03). Perguntas novas
escritas depois da separação vão só para o treino: rode com --novas-no-treino.
"""

import csv
import random
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from verificar import ARQUIVO, PASTA, carregar, main as verificar, normalizar  # noqa: E402

TREINO = PASTA / "treino.csv"
TESTE = PASTA / "teste.csv"
FRACAO_TESTE = 0.2
SEMENTE = 42
CAMPOS = ["pergunta", "tipo", "autor"]


def gravar(caminho: Path, linhas: list[dict]) -> None:
    with caminho.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        w.writerows({c: l.get(c, "") for c in CAMPOS} for l in linhas)


def main() -> int:
    if verificar() != 0:
        print("\nCorrija os erros antes de separar.")
        return 1

    linhas = carregar(ARQUIVO)

    if TESTE.exists():
        if "--novas-no-treino" not in sys.argv:
            print(f"\n{TESTE.name} já existe e está congelado. Nada foi feito.")
            print("Para mandar perguntas novas só para o treino: --novas-no-treino")
            return 0
        no_teste = {normalizar(l["pergunta"]) for l in carregar(TESTE)}
        treino = [l for l in linhas if normalizar(l["pergunta"]) not in no_teste]
        gravar(TREINO, treino)
        print(f"\nTreino regravado com {len(treino)} perguntas; teste intocado.")
        return 0

    rng = random.Random(SEMENTE)
    por_tipo = defaultdict(list)
    for l in linhas:
        por_tipo[l["tipo"].strip()].append(l)

    treino, teste = [], []
    for tipo, grupo in sorted(por_tipo.items()):
        rng.shuffle(grupo)
        n_teste = max(1, round(len(grupo) * FRACAO_TESTE))
        teste += grupo[:n_teste]
        treino += grupo[n_teste:]

    gravar(TREINO, treino)
    gravar(TESTE, teste)
    print(f"\nSeparado: {len(treino)} no treino, {len(teste)} no teste.")
    print("Faça commit de teste.csv agora e não o edite mais.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
