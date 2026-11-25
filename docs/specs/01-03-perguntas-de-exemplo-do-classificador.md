# Perguntas de exemplo do classificador

**Fase:** 1 · Provas e base · **Frente:** C · Classificador · **Situação:** em andamento

## O que faz

Cria o conjunto de perguntas com que o classificador vai ser treinado e testado, em um arquivo CSV com a pergunta e o tipo. Os tipos são: geral (documentos públicos), pessoal com a consulta (na v1: faltas, falta agendada e professor) e fora do escopo. Notas, horários, calendário e caminho de processo ficam para depois da v1 (D-008): na v1, perguntas sobre eles entram como fora do escopo. O conjunto de teste é separado antes de qualquer treino.

## O que não faz

- Não treina o classificador (02-03).
- Não usa dado real de aluno: as perguntas só têm o jeito de perguntar, como "quantas faltas eu tenho em cálculo?".
- Não usa respostas do Espaço Aluno.

## Pronta quando

- [x] Os tipos estão definidos e escritos em um lugar só (`classificador/tipos.py`).
- [ ] Há pelo menos 20 perguntas por tipo (são 5 tipos na v1: geral, faltas, falta agendada, professor e fora do escopo). O número é uma proposta do agente e pode ser ajustado pelo grupo.
- [ ] As quatro pessoas escreveram parte das perguntas, com jeitos diferentes de perguntar (formal, gíria, erros de digitação, frases curtas).
- [ ] As perguntas fora do escopo incluem casos difíceis: assuntos da faculdade que o chatbot não cobre e perguntas pessoais sobre outra pessoa.
- [ ] O conjunto de teste (cerca de 20% do total) foi separado e guardado à parte antes do treino, e ninguém o usa para ajustar nada.
- [ ] Nenhuma pergunta contém nome, matrícula ou dado real de alguém.

## Vem de

NFR-12, FR-11, NFR-08, NFR-10, D-002 e D-004.

## Como testar

Arquivos: `classificador/tipos.py` (os 5 tipos), `classificador/dados/perguntas.csv` (pergunta, tipo, autor), `classificador/verificar.py` e `classificador/separar.py`.

1. Rode `python classificador/verificar.py`. Deve mostrar o total, a contagem por tipo (com "ok" ou quantas faltam para 20), a contagem por autor e terminar com "Sem erros.". Tipo desconhecido, pergunta vazia ou repetida aparecem em "Erros" e o script sai com código 1.
2. Só depois que as quatro pessoas escreverem as suas perguntas e todos os tipos tiverem "ok": rode `python classificador/separar.py`. Deve gravar `dados/treino.csv` e `dados/teste.csv`, com cerca de 20% de cada tipo no teste, e pedir o commit do teste.
3. Rode `python classificador/separar.py` de novo. Deve dizer que o teste está congelado e não fazer nada.

**Situação em 2026-11-25:** o agente escreveu um rascunho com 10 perguntas por tipo (autor `agente`). Faltam 10 por tipo, escritas pelo grupo (cerca de 3 por pessoa por tipo, cada uma com o seu jeito de perguntar, e a pessoa coloca o próprio nome em `autor`). A separação do teste ainda não foi feita.
