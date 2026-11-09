# Teste e medição

**Fase:** 3 · Juntar, medir e ensaiar · **Frente:** D · Servidor · **Situação:** não iniciada

## O que faz

Monta o conjunto de perguntas de teste do chatbot e mede se ele atinge as metas: 40 perguntas (5 por tipo de consulta, nas 8 consultas) para precisão, 10 perguntas fora do escopo para honestidade e o tempo de resposta. Escreve os resultados e as limitações encontradas, para mostrar na apresentação.

## O que não faz

- Não usa as perguntas de teste do classificador (01-03) nem os pares de teste dos embeddings (02-02) para ajustar nada.
- Não esconde resultado ruim: o que falhar entra nas limitações.
- Não usa dados de alunos fora do grupo.

## Pronta quando

- [ ] As 40 perguntas de teste e as 10 fora do escopo estão escritas, e a resposta certa de cada uma foi conferida com a fonte (documento ou o próprio Espaço Aluno).
- [ ] O grupo concordou com as metas de NFR-07 (acertar ao menos 80%), NFR-08 (admitir não saber em ao menos 90%) e NFR-09 (até 15 segundos em ao menos 90%) ou combinou outras.
- [ ] Os três números foram medidos e estão escritos, com os erros listados.
- [ ] O tempo de resposta no computador onde a demonstração vai rodar foi medido, incluindo a partida com os modelos carregados (T-007).
- [ ] Os limites do plano gratuito da Groq não estouraram durante a medição, ou o que aconteceu está anotado (T-001).
- [ ] As limitações conhecidas estão escritas em uma lista curta para a apresentação.

## Vem de

NFR-07, NFR-08, NFR-09, NFR-11, T-001 e T-007.

## Como testar

A escrever na entrega.

Depende de: 03-01.
