# Plano de testes

**Projeto:** chatbot-uniceub · **Versão:** 0.2 · **Data:** 2026-11-09

> **Em resumo:** oito itens a verificar: três vêm da decisão D-001 (serviço de modelo de IA), quatro da D-002 (busca nos documentos e treino) e um da D-003 (login no Espaço Aluno). Nenhum foi feito ainda.

## O que verificar

| # | O que verificar | Vem de | Como | Situação |
|---|---|---|---|---|
| T-001 | Os limites do plano gratuito da Groq bastam para uma resposta que usa várias ferramentas seguidas, com 4 contas de teste | D-001 | Abrir a página de limites na conta da Groq e rodar o conjunto de 40 perguntas de teste medindo erros de limite | a fazer |
| T-002 | Existe um modelo gratuito da Groq com boa chamada de ferramentas e bom português | D-001 | Testar os modelos disponíveis com perguntas dos dois tipos (gerais e pessoais) e conferir as respostas | a fazer |
| T-003 | O que a Groq diz sobre treino e retenção de dados no plano gratuito | D-001 | Ler a página oficial de dados da Groq, que não pôde ser aberta na pesquisa, antes de usar dados reais de alunos | a fazer |
| T-004 | O ajuste dos embeddings melhora a busca nos documentos do UniCEUB em relação ao modelo pronto | D-002 | Escrever pares de pergunta e trecho a partir dos PDFs, separar treino e teste, medir quantas vezes o trecho certo aparece entre os primeiros resultados antes e depois do ajuste | a fazer |
| T-005 | O classificador de tipo de pergunta acerta o suficiente, em especial nas perguntas fora do escopo | D-002 | Escrever perguntas de exemplo por tipo (sem dados reais de alunos), separar treino e teste, medir acerto geral e por tipo. A meta de acerto precisa ser combinada pelo grupo | a fazer |
| T-006 | A cota de GPU gratuita do Kaggle ou do Colab basta para o tempo de treino real | D-002 | Rodar o primeiro treino completo e anotar o tempo gasto e se a sessão caiu | a fazer |
| T-007 | O modelo de busca e o classificador respondem dentro do limite de 15 segundos (NFR-09) no lugar onde vão rodar (a definir na decisão de hospedagem) | D-002 | Subir os dois modelos nesse lugar e medir o tempo de resposta, incluindo a partida com o modelo carregado | a fazer |
| T-008 | O servidor consegue entrar no Espaço Aluno com usuário e senha, sem captcha nem verificação em dois passos, e ler as páginas de faltas, professor, notas, horários e calendário | D-003 | Com a conta de um integrante do grupo, fazer o login por um script e ler cada página; anotar o que bloqueia e quanto tempo a sessão dura | a fazer |
