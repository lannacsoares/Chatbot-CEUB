"""Compara TF-IDF, BERTimbau + regressão e BERTimbau ajustado (D-010).

Uso: python classificador/comparar.py

1. Escolha, SÓ com o treino: validação cruzada estratificada (5 dobras) nos
   três modelos. O melhor F1 médio é o escolhido. O teste não entra aqui.
2. Medida: os três são treinados com todo o treino e medidos uma vez no
   teste congelado, para a tabela da apresentação.
3. O escolhido é salvo em models/classificador.joblib, que é o arquivo que
   classificar.py e o servidor usam.
"""

import sys
import time
from pathlib import Path

import joblib
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.pipeline import Pipeline

sys.stdout.reconfigure(encoding="utf-8")
AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
from bert import BertAjustado, EmbeddingsBert  # noqa: E402
from tipos import NOMES  # noqa: E402
from treinar import MODELO, montar, xy  # noqa: E402
from verificar import PASTA, carregar  # noqa: E402


def candidatos():
    return {
        "TF-IDF + regressão": montar().set_params(clf__C=0.5),
        "BERTimbau + regressão": Pipeline([
            ("bert", EmbeddingsBert()),
            ("clf", LogisticRegression(max_iter=3000, C=1.0, class_weight="balanced")),
        ]),
        "BERTimbau ajustado": BertAjustado(epocas=8, taxa=3e-5),
    }


def main() -> int:
    x_tr, y_tr = xy(carregar(PASTA / "treino.csv"))
    x_te, y_te = xy(carregar(PASTA / "teste.csv"))
    dobras = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    print(f"Treino: {len(x_tr)} · Teste: {len(x_te)}\n")

    print("1) Validação cruzada só no treino (F1 médio):")
    cv = {}
    for nome, modelo in candidatos().items():
        t = time.perf_counter()
        notas = cross_val_score(modelo, x_tr, y_tr, cv=dobras, scoring="f1_macro")
        cv[nome] = notas.mean()
        print(f"   {nome:<24} {notas.mean():.2f} ± {notas.std():.2f}   ({time.perf_counter() - t:.0f} s)")
    escolhido = max(cv, key=cv.get)
    print(f"   Escolhido pela validação cruzada: {escolhido}\n")

    print("2) Medida única no teste congelado:")
    rotulos = [t for t in NOMES if t in set(y_tr)]
    finais, linhas = {}, []
    for nome, modelo in candidatos().items():
        modelo.fit(x_tr, y_tr)
        t = time.perf_counter()
        prev = modelo.predict(x_te)
        ms = (time.perf_counter() - t) * 1000 / len(x_te)
        rec = dict(zip(rotulos, f1_score(y_te, prev, labels=rotulos, average=None)))
        fora = np.mean([p == "fora_do_escopo" for p, c in zip(prev, y_te) if c == "fora_do_escopo"])
        linhas.append((nome, accuracy_score(y_te, prev), f1_score(y_te, prev, average="macro"), fora, ms))
        finais[nome] = (modelo, prev)

    print(f"   {'Modelo':<24} {'Acerto':>7} {'F1':>6} {'Fora reconhecido':>17} {'ms/perg.':>9}")
    for nome, ac, f1, fora, ms in linhas:
        marca = "  <- escolhido" if nome == escolhido else ""
        print(f"   {nome:<24} {ac:>7.0%} {f1:>6.2f} {fora:>17.0%} {ms:>9.1f}{marca}")
    print("   Metas do grupo: acerto 80% · fora do escopo reconhecido 90%\n")

    modelo, prev = finais[escolhido]
    print(f"3) Detalhe do escolhido ({escolhido}):")
    print(classification_report(y_te, prev, labels=rotulos, zero_division=0))
    print("Matriz de confusão (linha = certo, coluna = previsto):")
    larg = max(map(len, rotulos))
    print(" " * (larg + 2) + " ".join(f"{r[:6]:>6}" for r in rotulos))
    for r, l in zip(rotulos, confusion_matrix(y_te, prev, labels=rotulos)):
        print(f"{r:<{larg}}  " + " ".join(f"{v:>6}" for v in l))
    for p, c, v in zip(x_te, y_te, prev):
        if c != v:
            print(f"  erro [{c} -> {v}] {p}")

    MODELO.parent.mkdir(exist_ok=True)
    joblib.dump(modelo, MODELO)
    print(f"\nSalvo em {MODELO.relative_to(AQUI.parent)} ({MODELO.stat().st_size / 1e6:.1f} MB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
