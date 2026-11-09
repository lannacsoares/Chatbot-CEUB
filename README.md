# Chatbot UniCEUB

Chatbot em site para alunos do UniCEUB tirarem dúvidas em linguagem natural: sobre as **regras da faculdade** (documentos públicos) e sobre a **própria situação no Espaço Aluno** (faltas, professores, notas, horários, calendário e caminho de processos).

Projeto em grupo da matéria de **Inteligência Artificial**.

> **Só responde e orienta.** O chatbot não executa nenhuma ação no Espaço Aluno: quem abre um processo, por exemplo, é o aluno.

## Status

🚧 **Em planejamento (fase 1 de 3).** Os documentos, a arquitetura e o plano estão prontos; ainda não há código. A primeira tarefa é [01-01 · Login e leitura do Espaço Aluno](docs/specs/01-01-login-e-leitura-do-espaco-aluno.md), que testa o maior risco do projeto.

Entrega final: primeira quinzena de dezembro de 2026, com apresentação em aula (intuição, código e funcionamento com demonstração).

## Como funciona

1. O aluno entra com usuário e senha do Espaço Aluno e faz uma pergunta.
2. Um **classificador** treinado pelo grupo decide se a pergunta é *geral*, *pessoal* ou *fora do escopo*.
3. **Geral:** uma busca por **embeddings** ajustados pelo grupo (RAG) acha os trechos mais parecidos nos documentos públicos do UniCEUB.
4. **Pessoal:** um leitor entra no Espaço Aluno com a conta de quem fez login e extrai só os campos necessários.
5. **Fora do escopo:** o chatbot diz que não tem conteúdo suficiente, em vez de inventar.
6. O modelo da **Groq** só escreve a resposta em português, a partir do que o servidor entregou, e a resposta mostra a fonte e lembra o aluno de conferir no Espaço Aluno ou na secretaria.

Detalhes em [`docs/architecture.md`](docs/architecture.md).

## Tecnologias

| Peça | Tecnologia |
|---|---|
| Servidor | Python, FastAPI |
| Tela | HTML e JavaScript, servidos pelo servidor |
| Busca nos documentos | sentence-transformers, FAISS, pdfplumber |
| Classificador | scikit-learn (e, se couber, BERTimbau) |
| Leitor do Espaço Aluno | requests, BeautifulSoup |
| Modelo de linguagem | Groq (plano gratuito) |
| Execução | Docker, no computador de um integrante |
| Treino | Kaggle ou Colab (gratuitos) |

## Regras do projeto

- **Tudo gratuito** (NFR-01): modelo de IA, hospedagem e treino.
- **Somente leitura** (NFR-04): nenhuma ação no Espaço Aluno.
- **Só as contas do grupo** (NFR-03): Lanna, Sofia, Geovanna e Erick.
- **Dados pessoais só na memória**, durante a conversa; só os campos necessários vão à Groq; nada em disco nem em log (NFR-05, NFR-10).
- **Nenhum dado real de aluno** entra no treino dos modelos.
- **Nunca** commitar senha, cookie de sessão, token ou chave da Groq. Use variáveis de ambiente (arquivos `.env` já estão no `.gitignore`).

## Documentação

| Documento | O que tem |
|---|---|
| [`docs/system-description.md`](docs/system-description.md) | O problema, o público, o objetivo e o escopo |
| [`docs/requirements.md`](docs/requirements.md) | Requisitos funcionais e não funcionais |
| [`docs/use-cases.md`](docs/use-cases.md) | As jornadas que não podem dar errado |
| [`docs/architecture.md`](docs/architecture.md) | Visão geral, fluxo de uma pergunta e dados que saem do computador |
| [`docs/ai-features.md`](docs/ai-features.md) | O que o modelo faz e o que acontece quando ele erra |
| [`docs/data-classification.md`](docs/data-classification.md) | Dados pessoais que passam pelo chatbot |
| [`docs/wireframes.md`](docs/wireframes.md) | As três telas: login, conversa e aviso de privacidade |
| [`docs/decisions.md`](docs/decisions.md) | Decisões D-001 a D-007, cada uma com o motivo |
| [`docs/research.md`](docs/research.md) | Pesquisa que embasou as decisões |
| [`docs/plan.md`](docs/plan.md) | 3 fases, 11 tarefas e 4 frentes |
| [`docs/specs/`](docs/specs/) | Uma especificação por tarefa, com "Como testar" |
| [`docs/test-plan.md`](docs/test-plan.md) | O que falta verificar |
| [`docs/playbooks/`](docs/playbooks/) | Um guia por frente de trabalho |

## Como o grupo trabalha

O projeto foi estruturado com o Blueprint. O estado atual está em [`.blueprint/state.md`](.blueprint/state.md) e o diário de sessões em [`.blueprint/journal/`](.blueprint/journal/). As instruções para agentes de IA estão em [`AGENTS.md`](AGENTS.md).

Cada pessoa leva uma frente e faz uma tarefa por vez, em ordem:

| Frente | O que cuida | Tarefas |
|---|---|---|
| A · Espaço Aluno | Login e leitura das páginas | 01-01, 02-04 |
| B · Documentos | PDFs, trechos, embeddings e busca | 01-02, 02-01, 02-02 |
| C · Classificador | Perguntas de exemplo e treino | 01-03, 02-03 |
| D · Servidor | Servidor, tela, Groq, Docker e medição | 01-04, 03-01 a 03-03 |

## Equipe

Lanna, Sofia, Geovanna e Erick.
