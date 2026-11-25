# Treino do classificador

**Fase:** 2 · Busca, treino e consultas · **Frente:** C · Classificador · **Situação:** feita (falta a conferência de outra pessoa do grupo)

## O que faz

Treina o classificador de tipo de pergunta com o conjunto de 01-03. Na v1 usa TF-IDF com regressão logística (scikit-learn), que treina em CPU. O modelo maior (BERTimbau) fica para depois da v1 (D-008, `docs/next-steps.md`). Mede o acerto geral e por tipo no conjunto de teste, com matriz de confusão, e salva o modelo escolhido para o servidor usar.

## O que não faz

- Não usa o conjunto de teste para treinar nem para escolher parâmetros.
- Não usa dado real de aluno.
- Não responde a perguntas: só diz o tipo.

## Pronta quando

- [x] A linha de base foi treinada e medida.
- [x] Há uma tabela com acerto geral, acerto e F1 por tipo e a matriz de confusão, no conjunto de teste (T-005).
- [x] O grupo combinou a meta de acerto antes do treino (80% geral e 90% fora do escopo), e o resultado diz se ela foi atingida. Em especial, o acerto nas perguntas fora do escopo está separado, por pesar em NFR-08.
- [x] O que o classificador faz quando tem pouca confiança está decidido (abaixo de 50% vira fora do escopo) e anotado (proposta: seguir o caminho que admite não saber).
- [x] O modelo escolhido está salvo em arquivo e roda em CPU (0,16 ms por pergunta) dentro do tempo de NFR-09.
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

### Primeiro treino real (2026-11-25)

80 perguntas no treino e 20 no teste (5 por tipo). Na validação cruzada, só com o treino, o melhor C foi 0,5 (F1 médio 0,69).

| Tipo | Precisão | Revocação | F1 |
|---|---|---|---|
| geral | 0,75 | 0,60 | 0,67 |
| faltas | 0,62 | 1,00 | 0,77 |
| professor | 1,00 | 0,80 | 0,89 |
| fora_do_escopo | 0,75 | 0,60 | 0,67 |

- **Acerto geral: 75%** (meta 80%, **não atingida**). **Fora do escopo reconhecido: 60%** (meta 90%, **não atingida**).
- Erros no teste:
  - duas regras sobre limite de faltas foram classificadas como `faltas`: a palavra "faltas" pesa mais que o sentido;
  - "me ajuda a fazer meu trabalho de física" virou `geral`;
  - "quanto eu tirei na prova de banco de dados" virou `faltas`;
  - "Quem ministra Programação Orientada a Objetos pra mim?" virou `fora_do_escopo`.
- Com o limite de confiança de 50%, muitas previsões caem para `fora_do_escopo`. Isso protege contra invenção, mas também manda para "não sei" perguntas válidas, como "quem da aula de IA" (42%).
- **Próximo passo:** mais perguntas de treino, escritas por pessoas, sobretudo na fronteira entre regra de faltas (`geral`) e faltas do aluno (`faltas`), e em pedidos de notas. O teste não muda. Retreinar e medir de novo com o mesmo `teste.csv`.

### Comparação com o BERTimbau (2026-11-25, D-010)

Rodar: `pip install -r classificador/requirements.txt` e `python classificador/comparar.py` (cerca de 10 minutos em CPU; na primeira vez baixa o BERTimbau, uns 420 MB).

**1. Escolha só no treino** (validação cruzada em 5 dobras, F1 médio):

| Modelo | F1 médio |
|---|---|
| TF-IDF + regressão | 0,69 ± 0,13 |
| **BERTimbau + regressão (escolhido)** | **0,83 ± 0,07** |
| BERTimbau ajustado | 0,79 ± 0,13 |

**2. Medida única no teste congelado** (20 perguntas):

| Modelo | Acerto | F1 | Fora do escopo reconhecido | ms por pergunta |
|---|---|---|---|---|
| TF-IDF + regressão | 75% | 0,75 | 60% | 0,2 |
| **BERTimbau + regressão** | **90%** | **0,90** | **80%** | 10 |
| BERTimbau ajustado | 85% | 0,85 | 60% | 10 |

- **Meta de acerto (80%): atingida.** Meta de fora do escopo reconhecido (90%): **não atingida, ficou em 80%.**
- Os 2 erros no teste:
  - "Quando começam as férias segundo o calendário acadêmico?" virou `geral`;
  - "quantas faltas posso ter no maximo numa disciplina?" virou `faltas`.
- Com 5 perguntas fora do escopo no teste, cada erro vale 20 pontos. Para medir com mais segurança, é preciso um teste maior.
- O modelo salvo funciona sem internet: o BERTimbau vem do cache. A primeira pergunta leva cerca de 20 s para carregar o modelo; depois, cerca de 10 ms por pergunta.
- Ainda erra a fronteira entre a regra de faltas e as faltas do aluno ("qual o limite de faltas" sai como `faltas`, 53%). Mais exemplos de treino nessa fronteira devem ajudar.
