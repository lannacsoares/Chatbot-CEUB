# Teste e medição

**Fase:** 3 · Juntar, medir e ensaiar · **Frente:** D · Servidor · **Situação:** em andamento (perguntas e script prontos; medição final espera 03-01)

## O que faz

Monta o conjunto de perguntas de teste do chatbot e mede se ele atinge as metas: 20 perguntas (gerais e das 3 consultas pessoais da v1) para precisão; as 40 perguntas nas 8 consultas ficam para depois da v1 (D-008), 10 perguntas fora do escopo para honestidade e o tempo de resposta. Escreve os resultados e as limitações encontradas, para mostrar na apresentação.

## O que não faz

- Não usa as perguntas de teste do classificador (01-03) nem os pares de teste dos embeddings (02-02) para ajustar nada.
- Não esconde resultado ruim: o que falhar entra nas limitações.
- Não usa dados de alunos fora do grupo.

## Pronta quando

- [x] As 20 perguntas de teste e as 10 fora do escopo estão escritas, e a resposta certa de cada uma foi conferida com a fonte (documento ou o próprio Espaço Aluno). As 14 gerais foram conferidas pelo agente no texto dos documentos; as 6 pessoais são conferidas na hora, no Espaço Aluno de quem testa.
- [x] O grupo concordou com as metas de NFR-07 (acertar ao menos 80%), NFR-08 (admitir não saber em ao menos 90%) e NFR-09 (até 15 segundos em ao menos 90%) ou combinou outras.
- [ ] Os três números foram medidos e estão escritos, com os erros listados.
- [ ] O tempo de resposta no computador onde a demonstração vai rodar foi medido, incluindo a partida com os modelos carregados (T-007).
- [ ] Os limites do plano gratuito da Groq não estouraram durante a medição, ou o que aconteceu está anotado (T-001).
- [ ] As limitações conhecidas estão escritas em uma lista curta para a apresentação.

## Vem de

NFR-07, NFR-08, NFR-09, NFR-11, T-001 e T-007.

## Como testar

Arquivos: `avaliacao/perguntas_teste.csv` (20 de precisão: 14 gerais com artigo e 6 pessoais; 10 de honestidade) e `avaliacao/medir.py`.

1. Suba o servidor: `uvicorn servidor.app:app --port 8000`.
2. Em outro terminal: `python avaliacao/medir.py --disciplina "nome de uma disciplina sua"`. Para cada pergunta aparecem a resposta, o tempo e a resposta esperada com a fonte. Marque `c` (certa) ou `e` (errada).
3. No fim aparece o resumo: precisão (meta 80%), honestidade (meta 90%) e tempo (90% em até 15 s). O arquivo vai para `avaliacao/resultados/`, fora do Git, sem as respostas das perguntas pessoais (NFR-10).

### Medição de "antes" (2026-11-25, servidor de 01-04, sem documentos nem Espaço Aluno)

Marcação feita pelo agente, comparando cada resposta com o artigo; o grupo confere.

**Atenção (2026-11-27):** as instruções à Groq mudaram depois desta medição (agora o chatbot sem documentos recusa em vez de explicar). Os números e a conclusão abaixo valem para a versão anterior, a do commit `e05e809`; o conjunto de teste não foi medido de novo.

| Medida | Resultado | Meta |
|---|---|---|
| Precisão (NFR-07) | 0 de 20 (0%) | 80% |
| Honestidade (NFR-08) | 9 de 10 (90%) | 90% |
| Tempo (NFR-09) | 30 de 30 em até 15 s; mediana 3,2 s; máximo 6,0 s | 90% |

- Em 8 das 14 gerais, o chatbot admitiu não saber, como pedem as instruções.
- **Em 6 ele inventou, mesmo instruído a não inventar.**
  - G04 criou menções que não existem ("menção honrosa").
  - G07 deu prazo errado ("5 a 10 dias úteis"; o certo são 8 dias).
  - G09 disse que dá para trancar só uma disciplina (não dá).
  - G10 disse que o pré-requisito vale (não vale para reprovação só por falta).
  - G11 inventou motivos de perda de vínculo (inadimplência).
  - G12 deu critérios vagos e incompletos.
- Na honestidade, a F05 errou: inventou um caminho de menus do Espaço Aluno ("Avaliações", "Revisão de Nota").

**Conclusão para a apresentação:** sem os documentos, o modelo inventa regras com confiança, e só as instruções não bastam. É o argumento para a busca nos documentos (RAG) e para o classificador barrar o que está fora do escopo antes da Groq. A medição de "depois" é feita com o fluxo de 03-01.

Depende de: 03-01.
