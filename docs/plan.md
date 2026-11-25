# Plano

**Projeto:** chatbot-uniceub · **Versão:** 0.2 · **Data:** 2026-11-11

> **Em resumo:** 3 fases e 11 tarefas, em 4 frentes de trabalho, uma por pessoa, para uma **v1 simples, só para a entrega da disciplina** (D-008). A primeira fase testa o maior risco (entrar no Espaço Aluno) e prepara os documentos, as perguntas de treino e o servidor, em paralelo. A segunda treina os modelos e termina as três consultas pessoais da v1. A terceira junta tudo, mede e ensaia a apresentação. O que ficou fora da v1 (Docker, nuvem, BERTimbau, notas, horários, calendário e outras evoluções) está em `docs/next-steps.md`. A apresentação é na primeira quinzena de dezembro; as datas abaixo são metas propostas pelo agente e devem ser ajustadas quando a data for definida.

## Como o trabalho anda

- **Atualização de 2026-11-25:** as metas de data abaixo já passaram sem nenhuma tarefa começada. Há uma entrega parcial em 27/11; a data da apresentação final ainda não foi informada, e as metas serão refeitas com ela. "Falta agendada" saiu (D-009): a v1 tem duas consultas pessoais, faltas e professor, e o classificador tem 4 tipos. As perguntas de exemplo são escritas por Erick. A demonstração roda no computador de Erick.

- Cada pessoa leva uma frente e faz uma tarefa dela por vez. As fases seguem em ordem; dentro de uma fase, as tarefas de frentes diferentes andam ao mesmo tempo.
- Uma tarefa é entregue com o jeito de testar: o que rodar ou abrir, e o que deve aparecer.
- A tarefa só vira "feita" quando todos os itens de "Pronta quando" da especificação estão marcados. Quem marca é a pessoa da frente, e outra pessoa do grupo confere.
- Nenhuma senha, cookie ou chave da Groq vai para arquivo, repositório ou log (NFR-05). Os testes usam só as contas do grupo (NFR-03).
- **Ponto de decisão até 13/11:** a tarefa 01-01 diz se dá para entrar no Espaço Aluno. Se não der, a v1 segue só com os documentos públicos e as tarefas 02-04 e a rota pessoal de 03-01 saem da v1.
- Escopo da v1 (D-008): três consultas pessoais (faltas, falta agendada e professor), classificador com TF-IDF, ajuste pequeno dos embeddings, servidor sem Docker e 20 perguntas de teste. O treino fica (D-004).
- Se o tempo apertar mesmo assim, saem primeiro a falta agendada e depois o ajuste dos embeddings além do mínimo que dá o antes e depois.

## As quatro frentes

| Frente | O que cuida | Tarefas | Quem |
|---|---|---|---|
| A · Espaço Aluno | Login e leitura das páginas | 01-01, 02-04 | Lanna |
| B · Documentos | PDFs, trechos, embeddings, busca e ajuste dos embeddings | 01-02, 02-01, 02-02 | Sophia e Lanna |
| C · Classificador | Perguntas de exemplo e treino do classificador | 01-03, 02-03 | Erick |
| D · Servidor | Servidor, tela, Groq, juntar tudo, medição e ensaio | 01-04, 03-01, 03-02, 03-03 | Geovanna e Erick |

As quatro pessoas (Lanna, Sofia, Geovanna e Erick) escolhem a frente. Na terceira fase, todos ajudam a frente D. A frente A tem uma pessoa só e é o maior risco: quem terminar a sua tarefa da fase 1 antes ajuda a frente A.

## Fases

| Fase | O que entrega | Pronta quando | Meta |
|---|---|---|---|
| 1 · Provas e base | Sabemos se dá para entrar no Espaço Aluno; os documentos viraram trechos; as perguntas de exemplo estão escritas; o servidor responde uma pergunta pela Groq | 01-01 a 01-04 feitas | Até 17/11 |
| 2 · Busca, treino e consultas | Busca nos documentos com embeddings ajustados, classificador treinado e as três consultas pessoais lendo o Espaço Aluno | 02-01 a 02-04 feitas, com os números de antes e depois | Até 22/11 |
| 3 · Juntar, medir e ensaiar | O chatbot completo da v1, medido contra as metas de NFR-07 a NFR-09, e a apresentação ensaiada | 03-01 a 03-03 feitas | Até 25/11, com folga até a data da apresentação |

## Tarefas

### Fase 1 · Provas e base

1. Login e leitura do Espaço Aluno: entrar com a conta de um integrante, ler faltas e professor de uma disciplina e dizer se há captcha ou verificação em dois passos (T-008). Spec: `specs/01-01-login-e-leitura-do-espaco-aluno.md`
2. Documentos em trechos: converter os PDFs públicos do UniCEUB em texto e quebrar em trechos com o documento de origem. Spec: `specs/01-02-documentos-em-trechos.md`
3. Perguntas de exemplo do classificador: escrever e separar em treino e teste as perguntas de cada um dos 5 tipos da v1 (geral, faltas, falta agendada, professor e fora do escopo). Spec: `specs/01-03-perguntas-de-exemplo-do-classificador.md`
4. Servidor, tela e Groq: servidor que recebe uma pergunta pela tela e responde pela Groq, rodando direto no computador, sem Docker; mede limites e lê a política de dados (T-001 a T-003). Spec: `specs/01-04-servidor-tela-e-groq.md`

### Fase 2 · Busca, treino e consultas

5. Busca com embeddings prontos: gerar os vetores, montar o índice e buscar os trechos, com limite para "sem conteúdo suficiente". Spec: `specs/02-01-busca-com-embeddings-prontos.md`
6. Ajuste dos embeddings: escrever um conjunto pequeno de pares de pergunta e trecho, ajustar o modelo no Kaggle ou no Colab e medir antes e depois (T-004, T-006). Spec: `specs/02-02-ajuste-dos-embeddings.md`
7. Treino do classificador: TF-IDF com regressão logística e medida do acerto por tipo (T-005). Spec: `specs/02-03-treino-do-classificador.md`
8. Consultas do Espaço Aluno: faltas, falta agendada e professor, sempre só os campos necessários. Spec: `specs/02-04-consultas-do-espaco-aluno.md`

### Fase 3 · Juntar, medir e ensaiar

9. Juntar o fluxo: classificador, busca ou leitor e Groq, com fonte nas respostas, "sem conteúdo suficiente" e descarte dos dados ao fim da conversa. Spec: `specs/03-01-juntar-o-fluxo.md`
10. Teste e medição: montar as 20 perguntas de teste e as 10 fora do escopo e medir NFR-07, NFR-08, NFR-09 e T-007. Spec: `specs/03-02-teste-e-medicao.md`
11. Ensaio da apresentação: roteiro de intuição, código e funcionamento, sem slides, com plano B. Spec: `specs/03-03-ensaio-da-apresentacao.md`

## Depois da v1

Docker, hospedagem em nuvem, BERTimbau, notas, horários, calendário, caminho de processo, pergunta mista, teste de 40 perguntas, acesso pelo celular e uso por alunos de fora do grupo ficam em `docs/next-steps.md`. Nada disso é tarefa da v1.

## O que depende de pessoas

- **Quem leva cada frente:** o grupo escolhe. Todas as tarefas da fase 1 esperam isso.
- **Os PDFs dos documentos públicos:** a Lanna envia. A tarefa 01-02 (e, depois, 02-01 e 02-02) espera por eles.
- **A data da apresentação e as entregas semanais:** o grupo informa. As metas das fases mudam com a data, e as entregas semanais ainda não estão ligadas às tarefas.
- **O resultado de 01-01:** se não for possível entrar no Espaço Aluno, o grupo decide se o trabalho segue só com os documentos públicos. A tarefa 02-04 e a rota pessoal de 03-01 esperam por isso.
- **A confirmação do grupo sobre D-008:** o escopo da v1 foi decidido por Erick; o grupo confirma na revisão.
- **Quem hospeda o site na demonstração:** o grupo decide até 03-03. Na v1 a turma vê só a tela do computador.
- **A meta de acerto do classificador e a concordância com os números de NFR-07 a NFR-09:** o grupo combina antes de 02-03 e 03-02.
- **O que o professor aceita como treino, e o que ele quis dizer com "tokens":** a Lanna pergunta a ele. Não bloqueia nenhuma tarefa.
- **TI do UniCEUB:** a autorização do acesso ao Espaço Aluno fica pendente e pesa antes de abrir o chatbot a outros alunos (depois da v1).
