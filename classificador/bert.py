"""BERTimbau no classificador (D-010).

Duas formas, as duas compatíveis com scikit-learn (fit / predict / predict_proba),
para entrar na mesma validação cruzada e no mesmo arquivo de modelo:

- EmbeddingsBert: o BERTimbau congelado transforma cada pergunta em um vetor
  (média dos vetores das palavras). Uma regressão logística é treinada em cima.
- BertAjustado: ajuste fino do BERTimbau inteiro para classificar a pergunta.

O modelo vem do Hugging Face e fica no cache do usuário, fora do projeto.
"""

import random

import numpy as np
import torch
from sklearn.base import BaseEstimator, ClassifierMixin, TransformerMixin

MODELO_BERT = "neuralmind/bert-base-portuguese-cased"
MAX_TOKENS = 48


def _semente(s: int) -> None:
    random.seed(s)
    np.random.seed(s)
    torch.manual_seed(s)


def _carregar(classe, **kw):
    """Usa a cópia do cache sem ir à internet; só baixa se ainda não existir.
    Assim a demonstração funciona sem internet (plano B)."""
    from transformers import AutoTokenizer
    try:
        tok = AutoTokenizer.from_pretrained(MODELO_BERT, local_files_only=True)
        return tok, classe.from_pretrained(MODELO_BERT, local_files_only=True, **kw)
    except OSError:
        tok = AutoTokenizer.from_pretrained(MODELO_BERT)
        return tok, classe.from_pretrained(MODELO_BERT, **kw)


def _media(saida, mascara):
    m = mascara.unsqueeze(-1).float()
    return (saida * m).sum(1) / m.sum(1).clamp(min=1e-9)


class EmbeddingsBert(BaseEstimator, TransformerMixin):
    """Pergunta -> vetor de 768 números (BERTimbau congelado, sem treino)."""

    _cache: dict = {}  # compartilhado entre cópias, acelera a validação cruzada
    _modelo = None

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        cls = EmbeddingsBert
        faltam = [t for t in dict.fromkeys(X) if t not in cls._cache]
        if faltam:
            if cls._modelo is None:
                from transformers import AutoModel
                cls._modelo = _carregar(AutoModel)
                cls._modelo[1].eval()
            tok, mod = cls._modelo
            with torch.no_grad():
                for i in range(0, len(faltam), 32):
                    lote = faltam[i:i + 32]
                    enc = tok(lote, padding=True, truncation=True,
                              max_length=MAX_TOKENS, return_tensors="pt")
                    vet = _media(mod(**enc).last_hidden_state, enc["attention_mask"])
                    for t, v in zip(lote, vet.numpy()):
                        cls._cache[t] = v
        return np.stack([cls._cache[t] for t in X])

    def __getstate__(self):
        return {}  # o arquivo salvo guarda só a regressão; o BERT vem do cache


class BertAjustado(BaseEstimator, ClassifierMixin):
    """Ajuste fino do BERTimbau para classificar o tipo da pergunta."""

    def __init__(self, epocas=8, taxa=3e-5, lote=16, semente=42):
        self.epocas, self.taxa, self.lote, self.semente = epocas, taxa, lote, semente

    def fit(self, X, y):
        from transformers import AutoModelForSequenceClassification
        _semente(self.semente)
        self.classes_ = np.array(sorted(set(y)))
        indice = {c: i for i, c in enumerate(self.classes_)}
        self.tok_, self.mod_ = _carregar(AutoModelForSequenceClassification,
                                         num_labels=len(self.classes_))
        opt = torch.optim.AdamW(self.mod_.parameters(), lr=self.taxa, weight_decay=0.01)
        X, alvo = list(X), torch.tensor([indice[c] for c in y])
        self.mod_.train()
        for _ in range(self.epocas):
            ordem = np.random.permutation(len(X))
            for i in range(0, len(X), self.lote):
                sel = ordem[i:i + self.lote]
                enc = self.tok_([X[j] for j in sel], padding=True, truncation=True,
                                max_length=MAX_TOKENS, return_tensors="pt")
                perda = self.mod_(**enc, labels=alvo[sel]).loss
                perda.backward()
                opt.step()
                opt.zero_grad()
        self.mod_.eval()
        return self

    def predict_proba(self, X):
        with torch.no_grad():
            enc = self.tok_(list(X), padding=True, truncation=True,
                            max_length=MAX_TOKENS, return_tensors="pt")
            return torch.softmax(self.mod_(**enc).logits, -1).numpy()

    def predict(self, X):
        return self.classes_[self.predict_proba(X).argmax(1)]
