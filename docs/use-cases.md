# Casos de uso

**Projeto:** chatbot-uniceub · **Versão:** 0.1 · **Data:** 2026-11-09

> **Em resumo:** o aluno é o único usuário. Duas jornadas não podem dar errado: consultar uma informação pessoal no Espaço Aluno (a função principal do chatbot) e receber uma resposta honesta quando o chatbot não tem conteúdo suficiente, em vez de uma resposta inventada. Cada conversa começa do zero.

## Quem usa

| Quem | O que vem fazer |
|---|---|
| Aluno do UniCEUB | Tirar dúvidas sobre as regras da faculdade e sobre as próprias informações no Espaço Aluno |

## As jornadas

| Nº | Jornada | Quem | Não pode dar errado |
|---|---|---|---|
| UC-01 | Consultar uma informação pessoal no Espaço Aluno | Aluno | sim |
| UC-02 | Fazer uma pergunta que o chatbot não sabe responder | Aluno | sim |

## UC-01 · Consultar uma informação pessoal no Espaço Aluno

**Começa quando:** o aluno abre o site do chatbot.
**Precisa de:** uma conta ativa no Espaço Aluno. Na primeira versão, só as contas do grupo.

1. O aluno entra com a própria conta do Espaço Aluno.
2. O aluno pergunta, por exemplo, "quantas faltas tenho em Inteligência Artificial?".
3. O chatbot consulta o Espaço Aluno com o acesso daquele aluno.
4. O chatbot responde na conversa com a informação que consta no Espaço Aluno.

**Termina com:** o aluno vendo uma resposta igual ao que o Espaço Aluno mostra. A conversa não é guardada: a próxima começa do zero.

**Quando não dá certo** (comportamentos propostos pelo agente)

| O que acontece | O que o sistema faz |
|---|---|
| O login não é aceito | Avisa que não conseguiu entrar e pede para tentar de novo |
| A sessão expira no meio da conversa | Avisa e pede novo login (FR-13) |
| O Espaço Aluno não responde, ou a página mudou e o chatbot não acha a informação | Diz que não conseguiu consultar agora, sem inventar um valor |
| A matéria citada não é encontrada | Diz que não encontrou essa matéria e pede para o aluno conferir o nome |

## UC-02 · Fazer uma pergunta que o chatbot não sabe responder

**Começa quando:** o aluno faz uma pergunta fora do escopo ou sobre algo que não está nos documentos nem no Espaço Aluno.
**Precisa de:** nada.

1. O aluno envia a pergunta.
2. O chatbot não encontra conteúdo suficiente para responder.
3. O chatbot diz que não tem conteúdo suficiente para responder àquela pergunta e, quando possível, indica onde o aluno pode procurar (FR-11).

**Termina com:** o aluno sabendo que o chatbot não tem a resposta. Nenhuma resposta inventada é mostrada.

**Quando não dá certo** (comportamentos propostos pelo agente)

| O que acontece | O que o sistema faz |
|---|---|
| Só parte da pergunta tem conteúdo nos documentos | Responde só o que o conteúdo sustenta e diz que o restante não foi encontrado |

## O que ficou de fora

- Pergunta geral com a fonte da resposta e sessão que expira no meio da conversa foram citadas como jornadas, mas o grupo escolheu as duas acima como as mais importantes. Elas continuam cobertas pelos requisitos FR-12 e FR-13, sem jornada detalhada.
