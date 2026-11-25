"""Treino do classificador de tipo de pergunta (tarefa 02-03).

Uso: python classificador/treinar.py

1. Lê dados/treino.csv e escolhe os parâmetros por validação cruzada,
   usando SÓ o treino.
2. Treina o modelo final com todo o treino.
3. Mede uma única vez em dados/teste.csv: acerto geral, precisão, revocação
   e F1 por tipo e matriz de confusão (T-005).
4. Salva o modelo em models/classificador.joblib (fora do Git; rode o
   script de novo para gerar).

Modelo da v1 (D-008): TF-IDF de palavras e de pedaços de 3 a 5 letras (para
aguentar erros de digitação e abreviações) e regressão logística.
"""

import sys
import time
from pathlib import Path

import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.pipeline import FeatureUnion, Pipeline

sys.stdout.reconfigure(encoding="utf-8")
AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
from tipos import NOMES  # noqa: E402
from verificar import PASTA, carregar  # noqa: E402

MODELO = AQUI.parent / "models" / "classificador.joblib"


def montar() -> Pipeline:
    return Pipeline([
        ("tfidf", FeatureUnion([
            ("palavras", TfidfVectorizer(lowercase=True, strip_accents="unicode",
                                         ngram_range=(1, 2), sublinear_tf=True)),
            ("letras", TfidfVectorizer(lowercase=True, strip_accents="unicode",
                                       analyzer="char_wb", ngram_range=(3, 5),
                                       sublinear_tf=True)),
        ])),
        ("clf", LogisticRegression(max_iter=2000, class_weight="balanced")),
    ])


def xy(linhas):
    return [l["pergunta"] for l in linhas], [l["tipo"].strip() for l in linhas]


def main() -> int:
    treino_csv, teste_csv = PASTA / "treino.csv", PASTA / "teste.csv"
    if not (treino_csv.exists() and teste_csv.exists()):
        print("Falta separar o teste: rode antes python classificador/separar.py")
        return 1

    x_tr, y_tr = xy(carregar(treino_csv))
    x_te, y_te = xy(carregar(teste_csv))
    print(f"Treino: {len(x_tr)} perguntas · Teste: {len(x_te)} perguntas\n")

    # Escolha de parâmetros só com o treino (o teste não entra aqui).
    menor_tipo = min(y_tr.count(t) for t in set(y_tr))
    dobras = StratifiedKFold(n_splits=max(2, min(5, menor_tipo)), shuffle=True, random_state=42)
    busca = GridSearchCV(montar(), {"clf__C": [0.5, 1, 3, 10, 30]},
                         cv=dobras, scoring="f1_macro")
    busca.fit(x_tr, y_tr)
    print(f"Melhor C na validação cruzada (só treino): {busca.best_params_['clf__C']}"
          f" · F1 médio: {busca.best_score_:.2f}\n")
    modelo = busca.best_estimator_

    # Medida final, uma única vez, no teste.
    inicio = time.perf_counter()
    previsto = modelo.predict(x_te)
    ms = (time.perf_counter() - inicio) * 1000 / len(x_te)

    rotulos = [t for t in NOMES if t in set(y_tr) | set(y_te)]
    print(f"Acerto geral no teste: {accuracy_score(y_te, previsto):.0%}\n")
    print(classification_report(y_te, previsto, labels=rotulos, zero_division=0))
    print("Matriz de confusão (linha = tipo certo, coluna = tipo previsto):")
    larg = max(len(r) for r in rotulos)
    print(" " * (larg + 2) + " ".join(f"{r[:6]:>6}" for r in rotulos))
    for r, linha in zip(rotulos, confusion_matrix(y_te, previsto, labels=rotulos)):
        print(f"{r:<{larg}}  " + " ".join(f"{v:>6}" for v in linha))

    erros = [(p, c, v) for p, c, v in zip(x_te, y_te, previsto) if c != v]
    if erros:
        print("\nErros no teste:")
        for p, c, v in erros:
            print(f"  [{c} -> {v}] {p}")
    print(f"\nTempo médio por pergunta: {ms:.2f} ms (CPU)")

    MODELO.parent.mkdir(exist_ok=True)
    joblib.dump(modelo, MODELO)
    print(f"Modelo salvo em {MODELO.relative_to(AQUI.parent)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
