# Juntar o fluxo

**Fase:** 3 · Juntar, medir e ensaiar · **Frente:** D · Servidor · **Situação:** não iniciada

## O que faz

Liga todas as peças no servidor: o aluno faz login, o classificador decide o tipo da pergunta, a busca ou o leitor do Espaço Aluno trazem o conteúdo, e a Groq escreve a resposta. Pergunta geral responde com a fonte; pergunta pessoal usa só os campos necessários; fora do escopo diz que não tem conteúdo suficiente, sem chamar a Groq; pergunta mista usa as duas consultas. Ao fim da conversa, ou ao sair, descarta senha, sessão e dados.

## O que não faz

- Não guarda histórico nem dado de aluno (NFR-10).
- Não executa ações no Espaço Aluno (NFR-04).
- Não é aberto a pessoas de fora do grupo (NFR-03).

## Pronta quando

- [ ] As três rotas funcionam: geral com fonte, pessoal com o Espaço Aluno e fora do escopo sem chamar a Groq.
- [ ] Uma pergunta mista usa as duas consultas e responde com as duas partes.
- [ ] Quando a busca não acha trecho parecido o bastante, a resposta diz que não tem conteúdo suficiente e, quando possível, onde procurar (FR-11).
- [ ] A resposta geral mostra o documento de origem (FR-12), e todas mostram o aviso de que é uma inteligência artificial e o lembrete de conferir no Espaço Aluno ou na secretaria.
- [ ] Sessão expirada avisa e pede novo login (FR-13).
- [ ] Ao sair, a senha, a sessão e os campos lidos deixam de existir no servidor; nada foi para disco nem para log.
- [ ] À Groq vão só a pergunta e os trechos ou campos necessários: conferido olhando o que é enviado (D-007).
- [ ] Tudo roda dentro do contêiner Docker.

## Vem de

FR-01, FR-02, FR-10 a FR-13, NFR-02 a NFR-06, NFR-10, D-002, D-003, D-005 e D-007.

## Como testar

A escrever na entrega.

Depende de: 01-04, 02-01, 02-03 e 02-04. A tarefa 02-02 pode entrar depois, trocando o índice pelo do modelo ajustado.
