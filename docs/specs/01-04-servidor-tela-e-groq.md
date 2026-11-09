# Servidor, tela e Groq

**Fase:** 1 · Provas e base · **Frente:** D · Servidor · **Situação:** não iniciada

## O que faz

Um servidor FastAPI em contêiner Docker com uma tela simples em HTML e JavaScript. A tela tem o campo de conversa, o aviso de que quem responde é uma inteligência artificial e o aviso de privacidade (`docs/wireframes.md`). O aluno digita uma pergunta e recebe a resposta escrita pela Groq, em português. Nesta tarefa, a Groq responde sem documentos nem Espaço Aluno: é a prova de que a ponta que escreve a resposta funciona. Também mede os limites do plano gratuito e testa os modelos.

## O que não faz

- Não classifica a pergunta, não busca em documentos e não lê o Espaço Aluno (fase 2).
- Não faz o login do Espaço Aluno (03-01 junta com 01-01 e 02-04).
- Não guarda histórico: cada conversa começa do zero.

## Pronta quando

- [ ] O servidor sobe dentro de um contêiner Docker, no computador de um integrante.
- [ ] A tela de conversa envia uma pergunta e mostra a resposta da Groq em português.
- [ ] A chave da Groq vem de variável de ambiente e não está no repositório nem em log.
- [ ] Os limites do plano gratuito da Groq foram lidos na conta e anotados, e uma resposta com várias chamadas seguidas foi testada (T-001).
- [ ] Pelo menos dois modelos gratuitos com chamada de ferramentas foram comparados em português, e um foi escolhido (T-002).
- [ ] A página oficial da Groq sobre uso e retenção de dados foi lida e o que ela diz foi anotado em `docs/research.md` antes de qualquer dado real de aluno passar por ela (T-003).
- [ ] O servidor não grava texto de perguntas nem de respostas em disco ou log.

## Vem de

FR-01, NFR-01, NFR-05, NFR-06, D-001, D-005, D-006, T-001, T-002 e T-003.

## Como testar

A escrever na entrega.
