# Plano

**Projeto:** chatbot-uniceub · **Versão:** 0.1 · **Data:** 2026-11-09

> **Em resumo:** 3 fases e 11 tarefas, em 4 frentes de trabalho, uma por pessoa. A primeira fase testa o maior risco (entrar no Espaço Aluno) e prepara os documentos, as perguntas de treino e o servidor, em paralelo. A segunda treina os modelos e termina as consultas pessoais. A terceira junta tudo, mede e ensaia a apresentação. A apresentação é na primeira quinzena de dezembro; as datas abaixo são metas propostas pelo agente e devem ser ajustadas quando a data for definida.

## Como o trabalho anda

- Cada pessoa leva uma frente e faz uma tarefa dela por vez. As fases seguem em ordem; dentro de uma fase, as tarefas de frentes diferentes andam ao mesmo tempo.
- Uma tarefa é entregue com o jeito de testar: o que rodar ou abrir, e o que deve aparecer.
- A tarefa só vira "feita" quando todos os itens de "Pronta quando" da especificação estão marcados. Quem marca é a pessoa da frente, e outra pessoa do grupo confere.
- Nenhuma senha, cookie ou chave da Groq vai para arquivo, repositório ou log (NFR-05). Os testes usam só as contas do grupo (NFR-03).
- Se o tempo apertar, o que sai primeiro são as consultas do fim da lista em 02-04 (notas, horários, calendário). O treino fica (D-004).

## As quatro frentes

| Frente | O que cuida | Tarefas | Quem |
|---|---|---|---|
| A · Espaço Aluno | Login e leitura das páginas | 01-01, 02-04 | A definir pelo grupo |
| B · Documentos | PDFs, trechos, embeddings, busca e ajuste dos embeddings | 01-02, 02-01, 02-02 | A definir pelo grupo |
| C · Classificador | Perguntas de exemplo e treino do classificador | 01-03, 02-03 | A definir pelo grupo |
| D · Servidor | Servidor, tela, Groq, Docker, juntar tudo, medição e ensaio | 01-04, 03-01, 03-02, 03-03 | A definir pelo grupo |

As quatro pessoas (Lanna, Sofia, Geovanna e Erick) escolhem a frente. Na terceira fase, todos ajudam a frente D.

## Fases

| Fase | O que entrega | Pronta quando | Meta |
|---|---|---|---|
| 1 · Provas e base | Sabemos se dá para entrar no Espaço Aluno; os documentos viraram trechos; as perguntas de exemplo estão escritas; o servidor responde uma pergunta pela Groq | 01-01 a 01-04 feitas | Até 17/11 |
| 2 · Busca, treino e consultas | Busca nos documentos com embeddings ajustados, classificador treinado e consultas pessoais lendo o Espaço Aluno | 02-01 a 02-04 feitas, com os números de antes e depois | Até 29/11 |
| 3 · Juntar, medir e ensaiar | O chatbot completo, medido contra as metas de NFR-07 a NFR-09, e a apresentação ensaiada | 03-01 a 03-03 feitas | Até 6/12 |

## Tarefas

### Fase 1 · Provas e base

1. Login e leitura do Espaço Aluno: entrar com a conta de um integrante, ler faltas e professor de uma disciplina e dizer se há captcha ou verificação em dois passos (T-008). Spec: `specs/01-01-login-e-leitura-do-espaco-aluno.md`
2. Documentos em trechos: converter os PDFs públicos do UniCEUB em texto e quebrar em trechos com o documento de origem. Spec: `specs/01-02-documentos-em-trechos.md`
3. Perguntas de exemplo do classificador: escrever e separar em treino e teste as perguntas de cada tipo. Spec: `specs/01-03-perguntas-de-exemplo-do-classificador.md`
4. Servidor, tela e Groq: servidor em contêiner que recebe uma pergunta pela tela e responde pela Groq; mede limites e lê a política de dados (T-001 a T-003). Spec: `specs/01-04-servidor-tela-e-groq.md`

### Fase 2 · Busca, treino e consultas

5. Busca com embeddings prontos: gerar os vetores, montar o índice e buscar os trechos, com limite para "sem conteúdo suficiente". Spec: `specs/02-01-busca-com-embeddings-prontos.md`
6. Ajuste dos embeddings: escrever pares de pergunta e trecho, ajustar o modelo no Kaggle ou no Colab e medir antes e depois (T-004, T-006). Spec: `specs/02-02-ajuste-dos-embeddings.md`
7. Treino do classificador: comparar um modelo simples com um maior e medir o acerto por tipo (T-005). Spec: `specs/02-03-treino-do-classificador.md`
8. Consultas do Espaço Aluno: faltas, falta agendada e professor primeiro; depois notas, horários, calendário e caminho de processo, sempre só os campos necessários. Spec: `specs/02-04-consultas-do-espaco-aluno.md`

### Fase 3 · Juntar, medir e ensaiar

9. Juntar o fluxo: classificador, busca ou leitor e Groq, com fonte nas respostas, "sem conteúdo suficiente" e descarte dos dados ao fim da conversa. Spec: `specs/03-01-juntar-o-fluxo.md`
10. Teste e medição: montar as 40 perguntas de teste e as 10 fora do escopo e medir NFR-07, NFR-08, NFR-09 e T-007. Spec: `specs/03-02-teste-e-medicao.md`
11. Ensaio da apresentação: roteiro de intuição, código e funcionamento, sem slides, com plano B. Spec: `specs/03-03-ensaio-da-apresentacao.md`

## O que depende de pessoas

- **Quem leva cada frente:** o grupo escolhe. Todas as tarefas da fase 1 esperam isso.
- **Os PDFs dos documentos públicos:** a Lanna envia. A tarefa 01-02 (e, depois, 02-01 e 02-02) espera por eles.
- **A data da apresentação e as entregas semanais:** o grupo informa. As metas das fases mudam com a data.
- **O resultado de 01-01:** se não for possível entrar no Espaço Aluno, o grupo decide se o trabalho segue só com os documentos públicos. As tarefas 02-04 e a rota pessoal de 03-01 esperam por isso.
- **Quem hospeda o site na demonstração e como a turma acessa:** o grupo decide até 03-03.
- **A meta de acerto do classificador e a concordância com os números de NFR-07 a NFR-09:** o grupo combina antes de 02-03 e 03-02.
- **O que o professor aceita como treino, e o que ele quis dizer com "tokens":** a Lanna pergunta a ele. Não bloqueia nenhuma tarefa.
- **TI do UniCEUB:** a autorização do acesso ao Espaço Aluno fica pendente e pesa antes de abrir o chatbot a outros alunos.
