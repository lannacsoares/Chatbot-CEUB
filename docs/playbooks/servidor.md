# Guia da frente D · Servidor

> **Em resumo:** esta frente cuida do servidor, da tela, da Groq e do contêiner, e junta o que as outras três frentes entregam. Também mede o resultado e prepara a apresentação. Depende das outras frentes na fase 3.

## O que esta função faz

- Sobe o servidor FastAPI em Docker com a tela de conversa e chama a Groq (01-04, T-001 a T-003).
- Junta classificador, busca, leitor do Espaço Aluno e Groq no fluxo completo (03-01).
- Mede o chatbot contra NFR-07, NFR-08 e NFR-09 (03-02, T-007).
- Prepara e ensaia a apresentação sem slides (03-03).

## As tarefas desta função

| Tarefa | Especificação |
|---|---|
| 01-04 Servidor, tela e Groq | `specs/01-04-servidor-tela-e-groq.md` |
| 03-01 Juntar o fluxo | `specs/03-01-juntar-o-fluxo.md` |
| 03-02 Teste e medição | `specs/03-02-teste-e-medicao.md` |
| 03-03 Ensaio da apresentação | `specs/03-03-ensaio-da-apresentacao.md` |

## Antes de começar uma tarefa

1. Leia `.blueprint/state.md` e a especificação da tarefa.
2. Leia `docs/architecture.md` e `docs/wireframes.md`.
3. A chave da Groq e qualquer senha ficam em variável de ambiente, nunca em arquivo, repositório, log nem saída de teste (NFR-05).
4. O servidor não grava texto de perguntas nem de respostas em disco ou log, e a sessão do aluno vive só na memória (NFR-10).
5. Antes de 03-01, confirme com as frentes A, B e C o que cada módulo entrega e como é chamado.

## Quando a tarefa termina

1. Escreva o resultado em "Como testar" da especificação e diga ao grupo.
2. Registre a sessão em `.blueprint/journal/sessions/` e, ao fim de uma fase, um marco.
3. Avise as outras frentes do que mudou no servidor que as afeta.

## O que esta função não decide

- Trocar a Groq, a hospedagem ou a stack, ou qualquer coisa que gere custo: é da pessoa.
- O que vai para a Groq: está em D-007.
- Quem hospeda a demonstração e como a turma acessa: o grupo decide até 03-03.
