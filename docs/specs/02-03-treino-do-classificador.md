# Treino do classificador

**Fase:** 2 · Busca, treino e consultas · **Frente:** C · Classificador · **Situação:** em andamento (script pronto, espera o teste de 01-03)

## O que faz

Treina o classificador de tipo de pergunta com o conjunto de 01-03. Na v1 usa TF-IDF com regressão logística (scikit-learn), que treina em CPU. O modelo maior (BERTimbau) fica para depois da v1 (D-008, `docs/next-steps.md`). Mede o acerto geral e por tipo no conjunto de teste, com matriz de confusão, e salva o modelo escolhido para o servidor usar.

## O que não faz

- Não usa o conjunto de teste para treinar nem para escolher parâmetros.
- Não usa dado real de aluno.
- Não responde a perguntas: só diz o tipo.

## Pronta quando

- [ ] A linha de base foi treinada e medida.
- [ ] Há uma tabela com acerto geral, acerto e F1 por tipo e a matriz de confusão, no conjunto de teste (T-005).
- [ ] O grupo combinou a meta de acerto antes do treino, e o resultado diz se ela foi atingida. Em especial, o acerto nas perguntas fora do escopo está separado, por pesar em NFR-08.
- [ ] O que o classificador faz quando tem pouca confiança está decidido e anotado (proposta: seguir o caminho que admite não saber).
- [ ] O modelo escolhido está salvo em arquivo e roda em CPU dentro do tempo de NFR-09.
- [x] O script de treino está no repositório, para ser mostrado na apresentação (`classificador/treinar.py`).

## Vem de

NFR-08, NFR-12, FR-11, D-002, D-004 e T-005.

## Como testar

1. `pip install -r classificador/requirements.txt`
2. Com `dados/treino.csv` e `dados/teste.csv` gerados por 01-03, rode `python classificador/treinar.py`. Deve mostrar o C escolhido por validação cruzada (só no treino), o acerto geral no teste, precisão, revocação e F1 por tipo, a matriz de confusão, as perguntas erradas, o tempo médio por pergunta e "Modelo salvo em models/classificador.joblib".
3. Rode `python classificador/classificar.py "quantas faltas eu tenho em cálculo?"`. Deve mostrar `faltas` e a confiança.

Modelo: TF-IDF de palavras (1 e 2 palavras) e de pedaços de 3 a 5 letras, para aguentar erros de digitação, com regressão logística. Baixa confiança (< 50%) vira `fora_do_escopo` (`classificador/classificar.py`). O limite é proposta do agente e espera o grupo (`docs/perguntas-para-o-grupo.md`, pergunta 8).

**Situação em 2026-11-25:** o fluxo foi testado numa cópia descartável, só com o rascunho de 50 perguntas. Deu 60% no teste e 0,23 ms por pergunta. Esse número não vale como resultado: o treino real espera as perguntas do grupo, a separação do teste e a meta de acerto combinada.

Depende de: 01-03.
