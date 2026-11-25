"""Confere o conjunto de perguntas de exemplo (tarefa 01-03).

Uso: python classificador/verificar.py

Mostra quantas perguntas há por tipo e por autor e aponta problemas:
tipo desconhecido, pergunta vazia ou repetida, tipo com menos do mínimo.
Sai com código 1 se houver erro, para poder rodar antes de separar o teste.
"""

import csv
import sys
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")  # acentos no terminal do Windows
sys.path.insert(0, str(Path(__file__).resolve().parent))
from tipos import NOMES  # noqa: E402

PASTA = Path(__file__).resolve().parent / "dados"
ARQUIVO = PASTA / "perguntas.csv"
MINIMO_POR_TIPO = 20  # proposta do agente na especificação; o grupo pode ajustar


def normalizar(texto: str) -> str:
    return " ".join(texto.lower().split()).rstrip("?.! ")


def carregar(caminho: Path) -> list[dict]:
    with caminho.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def main() -> int:
    linhas = carregar(ARQUIVO)
    erros, avisos = [], []
    vistas = {}

    for n, linha in enumerate(linhas, start=2):  # linha 1 é o cabeçalho
        pergunta = (linha.get("pergunta") or "").strip()
        tipo = (linha.get("tipo") or "").strip()
        if not pergunta:
            erros.append(f"linha {n}: pergunta vazia")
            continue
        if tipo not in NOMES:
            erros.append(f"linha {n}: tipo desconhecido '{tipo}' (use um de {NOMES})")
        chave = normalizar(pergunta)
        if chave in vistas:
            erros.append(f"linha {n}: repetida da linha {vistas[chave]}: {pergunta!r}")
        else:
            vistas[chave] = n

    por_tipo = Counter(l["tipo"].strip() for l in linhas)
    por_autor = Counter((l.get("autor") or "").strip() or "(sem autor)" for l in linhas)

    print(f"Total: {len(linhas)} perguntas\n")
    print("Por tipo:")
    for tipo in NOMES:
        qtd = por_tipo.get(tipo, 0)
        marca = "ok" if qtd >= MINIMO_POR_TIPO else f"faltam {MINIMO_POR_TIPO - qtd}"
        print(f"  {tipo:<16} {qtd:>3}  ({marca})")
        if qtd < MINIMO_POR_TIPO:
            avisos.append(f"{tipo} tem {qtd} perguntas; o mínimo é {MINIMO_POR_TIPO}")
    print("\nPor autor:")
    for autor, qtd in por_autor.most_common():
        print(f"  {autor:<16} {qtd:>3}")

    if avisos:
        print("\nAvisos:")
        for a in avisos:
            print(f"  - {a}")
    if erros:
        print("\nErros:")
        for e in erros:
            print(f"  - {e}")
        return 1
    print("\nSem erros.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
