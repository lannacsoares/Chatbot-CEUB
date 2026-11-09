# Perguntas de exemplo do classificador

**Fase:** 1 · Provas e base · **Frente:** C · Classificador · **Situação:** não iniciada

## O que faz

Cria o conjunto de perguntas com que o classificador vai ser treinado e testado, em um arquivo CSV com a pergunta e o tipo. Os tipos são: geral (documentos públicos), pessoal com a consulta (faltas, falta agendada, professor, notas, horários, calendário, caminho de processo) e fora do escopo. O conjunto de teste é separado antes de qualquer treino.

## O que não faz

- Não treina o classificador (02-03).
- Não usa dado real de aluno: as perguntas só têm o jeito de perguntar, como "quantas faltas eu tenho em cálculo?".
- Não usa respostas do Espaço Aluno.

## Pronta quando

- [ ] Os tipos estão definidos e escritos em um lugar só.
- [ ] Há pelo menos 40 perguntas por tipo. O número é uma proposta do agente e pode ser ajustado pelo grupo.
- [ ] As quatro pessoas escreveram parte das perguntas, com jeitos diferentes de perguntar (formal, gíria, erros de digitação, frases curtas).
- [ ] As perguntas fora do escopo incluem casos difíceis: assuntos da faculdade que o chatbot não cobre e perguntas pessoais sobre outra pessoa.
- [ ] O conjunto de teste (cerca de 20% do total) foi separado e guardado à parte antes do treino, e ninguém o usa para ajustar nada.
- [ ] Nenhuma pergunta contém nome, matrícula ou dado real de alguém.

## Vem de

NFR-12, FR-11, NFR-08, NFR-10, D-002 e D-004.

## Como testar

A escrever na entrega.
