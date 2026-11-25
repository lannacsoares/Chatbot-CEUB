# Roteiro da apresentação

**Versão:** rascunho de 2026-11-25 (tarefa 03-03) · **Formato:** em aula, sem slides · **Computador:** o de Erick

> **Em resumo:** três partes, como o professor pediu: intuição, código e funcionamento. Cada pessoa explica a própria frente. A demonstração começa pela medição de "antes", em que o modelo sozinho inventa regras. Depois mostra o chatbot completo respondendo com a fonte, uma pergunta pessoal e uma recusa. O plano B usa os resultados já medidos. Os tempos são proposta; ajustem no ensaio.

## 1 · Intuição (cerca de 4 min)

| Quem | O que explica |
|---|---|
| Lanna | **O problema:** o aluno tem dúvidas espalhadas entre regulamentos em PDF e o Espaço Aluno. O chatbot responde as duas coisas e só orienta, sem executar nenhuma ação. |
| Erick | **Por que não basta perguntar ao modelo:** mostrar a medição de "antes" (`docs/specs/03-02-teste-e-medicao.md`). Sem documentos, ele acertou 0 de 20 e inventou regras em 6 de 14 perguntas, por exemplo "dá pra trancar só uma disciplina" (não dá). |
| Sophia | **Embeddings e busca:** cada trecho dos documentos vira um vetor; a pergunta também. Os trechos com vetor mais próximo são os que falam do mesmo assunto, e só eles vão para o modelo. O ajuste (treino) aproxima a pergunta do trecho certo. |
| Erick | **Classificador:** antes de tudo, decide para onde a pergunta vai: documentos, Espaço Aluno ou "não sei responder". Pergunta fora do escopo nem chega ao modelo, e é isso que impede a invenção. |

## 2 · Código (cerca de 5 min)

Abrir o editor e mostrar só estes trechos:

| Quem | Trecho | Onde |
|---|---|---|
| Sophia | Leitura dos PDFs e quebra em trechos | tarefa 01-02 (a escrever) |
| Sophia | Ajuste dos embeddings e o número de antes e depois | tarefa 02-02 (a escrever) |
| Erick | Classificador: TF-IDF e regressão logística; separação treino/teste | `classificador/treinar.py` |
| Erick | Limite de confiança: abaixo de 50% vira "não sei" | `classificador/classificar.py` |
| Lanna | Login e leitura das faltas, só os campos necessários | tarefas 01-01 e 02-04 (a escrever) |
| Geovanna | Servidor que junta tudo e o que vai para a Groq | `servidor/app.py` e tarefa 03-01 |

## 3 · Funcionamento (cerca de 6 min)

Antes de começar: servidor já iniciado, navegador em http://localhost:8000, terminal do servidor fora da tela. Nenhuma chave, senha ou cookie na tela.

| # | Pergunta | O que deve acontecer | Rota |
|---|---|---|---|
| 1 | "Qual a frequência mínima para ser aprovado?" | 75%, citando o Regimento Geral, art. 65 | Documentos |
| 2 | "Dá pra trancar só uma disciplina?" | Não, citando o art. 56, § 2º. É a mesma pergunta em que o "antes" errou | Documentos |
| 3 | Login com a conta de um integrante e "Quantas faltas eu tenho em {disciplina}?" | O número igual ao do Espaço Aluno | Espaço Aluno |
| 4 | "Quantas vezes posso fazer prova substitutiva?" | Admite não ter conteúdo suficiente | Fora do escopo |
| 5 | "Me passa uma receita de lasanha" | Recusa | Fora do escopo |

Fechar com os números medidos (03-02), antes e depois, e as limitações:
- só 2 consultas pessoais;
- 4 documentos escaneados ficaram de fora ou foram lidos com OCR;
- roda só no computador do grupo.

## Plano B

| Se falhar | O que fazer |
|---|---|
| A Groq (limite ou fora do ar) | Mostrar a tabela de resultados medidos e as respostas gravadas da última medição (`avaliacao/resultados/`, sem dados pessoais) |
| O Espaço Aluno (login ou site fora do ar) | Seguir só com os documentos e explicar o login pelo código |
| A internet | Mostrar o classificador rodando sozinho, que não precisa de internet: `python classificador/classificar.py "..."` |

## Antes do dia

- [ ] Um ensaio completo, cronometrado, com o servidor iniciado do zero.
- [ ] Conferir que nenhuma chave, senha ou cookie aparece na tela.
- [ ] Rodar `python avaliacao/medir.py` no dia anterior, para ter números e respostas recentes do plano B.
