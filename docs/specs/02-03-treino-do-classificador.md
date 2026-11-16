# Treino do classificador

**Fase:** 2 · Busca, treino e consultas · **Frente:** C · Classificador · **Situação:** não iniciada

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
- [ ] O script de treino está no repositório, para ser mostrado na apresentação.

## Vem de

NFR-08, NFR-12, FR-11, D-002, D-004 e T-005.

## Como testar

A escrever na entrega.

Depende de: 01-03.
