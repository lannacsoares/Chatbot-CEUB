# Ajuste dos embeddings

**Fase:** 2 · Busca, treino e consultas · **Frente:** B · Documentos · **Situação:** não iniciada

## O que faz

Ajusta o modelo de embeddings com pares de pergunta e trecho dos documentos do UniCEUB, no Kaggle ou no Colab gratuitos, com sentence-transformers. Mede quantas vezes o trecho certo aparece entre os primeiros resultados antes e depois do ajuste e refaz o índice com o modelo ajustado.

## O que não faz

- Não ajusta o modelo de linguagem da Groq (não é possível no plano gratuito).
- Não usa dado real de aluno em nenhum momento do treino (NFR-10).
- Não promete melhora: se o ajuste não melhorar a busca, esse resultado é registrado como está e discutido na apresentação.

## Pronta quando

- [ ] Os pares de pergunta e trecho foram escritos (a Groq pode rascunhar as perguntas, o grupo revisa todas) e cobrem os principais documentos.
- [ ] Os pares de teste foram separados antes do treino e não entram nele.
- [ ] O treino rodou até o fim em GPU gratuita, e o tempo gasto e a cota usada estão anotados (T-006).
- [ ] Há uma tabela antes e depois do ajuste, com o mesmo conjunto de teste (T-004).
- [ ] O modelo ajustado está salvo e o índice foi gerado de novo com ele.
- [ ] O notebook ou script de treino está no repositório, sem chaves nem senhas, para poder ser mostrado na apresentação.

## Vem de

NFR-12, D-002, D-004, T-004 e T-006.

## Como testar

A escrever na entrega.

Depende de: 02-01.
