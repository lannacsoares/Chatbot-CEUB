# Guia da frente C · Classificador

> **Em resumo:** esta frente escreve as perguntas de exemplo e treina o classificador que decide o tipo de cada pergunta (geral, pessoal com a consulta, ou fora do escopo). Entrega o modelo salvo e as métricas para a frente D usar no servidor.

## O que esta função faz

- Define os tipos de pergunta e escreve o conjunto de exemplos com as quatro pessoas (01-03).
- Treina uma linha de base e um modelo maior, e mede o acerto por tipo (02-03, T-005).
- Decide, com o grupo, o que fazer quando o classificador tem pouca confiança.

## As tarefas desta função

| Tarefa | Especificação |
|---|---|
| 01-03 Perguntas de exemplo do classificador | `specs/01-03-perguntas-de-exemplo-do-classificador.md` |
| 02-03 Treino do classificador | `specs/02-03-treino-do-classificador.md` |

## Antes de começar uma tarefa

1. Leia `.blueprint/state.md` e a especificação da tarefa.
2. Leia `docs/ai-features.md` (AI-02) e `docs/requirements.md` (FR-11, NFR-08).
3. As perguntas só têm o jeito de perguntar: nenhum nome, matrícula ou dado real de alguém (NFR-10).
4. Separe o conjunto de teste antes de treinar e não o use para ajustar nada.

## Quando a tarefa termina

1. Escreva o resultado em "Como testar" da especificação, com a tabela de acerto por tipo, e diga ao grupo.
2. Registre a sessão em `.blueprint/journal/sessions/`.
3. Entregue à frente D o arquivo do modelo e como carregá-lo, e o que ele devolve (tipo e confiança).

## O que esta função não decide

- A meta de acerto: o grupo combina antes do treino.
- Mudar os tipos de pergunta depois de a frente A ou B já ter trabalhado com eles: avise a frente D e a pessoa.
- Cortar o treino: ele é parte fixa do projeto (D-004).
