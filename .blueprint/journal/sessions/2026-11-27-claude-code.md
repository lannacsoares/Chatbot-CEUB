# Sessão de 2026-11-27 · Claude Code

**Pedido:** a Lanna quis o repositório na máquina para abrir a tela do chat.

**O que aconteceu:**
- A pasta já era um clone de `lannacsoares/Chatbot-CEUB`, 14 commits atrás. Foi atualizada com `git pull --ff-only` até `e05e809`.
- Criado `.venv` com `servidor/requirements.txt` e `.claude/launch.json` (não commitado).
- Servidor subiu na porta 8000 e a tela abriu. Nesta primeira parte, nenhum código do projeto foi alterado.

**Depois:** a Lanna configurou a `GROQ_API_KEY` com `setx`. Uma pergunta de teste ("Como funciona a prova substitutiva?") foi respondida em 2,13 s por `openai/gpt-oss-120b`.

**Pendente:** na tarefa 01-04, o esperado para essa pergunta é o chatbot dizer que não tem o regulamento. Neste teste ele afirmou regras (justificativa, limite de uma por semestre, substituição da nota) sem ter nenhum documento.

**Ajuste (tarefa 01-04, a pedido da Lanna):** as instruções em `servidor/groq_cliente.py` agora mandam responder só que não há conteúdo suficiente, sem explicar como a regra "costuma" funcionar. Com 11 perguntas próprias (fora do conjunto de teste da 03-02), as 9 respostas a perguntas acadêmicas recusaram sem inventar e as 2 fora do escopo também recusaram, inclusive uma saudação. A pedido da Lanna, enviado ao GitHub no ramo `ajuste-instrucoes-groq`, por pull request. A medição de "depois" da 03-02 não foi feita.

**Como testar:** `.\.venv\Scripts\python.exe -m uvicorn servidor.app:app --port 8000` na raiz e abrir http://localhost:8000. Deve aparecer a tela "Chatbot UniCEUB" com a saudação.
