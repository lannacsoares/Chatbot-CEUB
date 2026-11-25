# Servidor, tela e Groq

**Fase:** 1 · Provas e base · **Frente:** D · Servidor · **Situação:** feita (falta a conferência de outra pessoa do grupo)

## O que faz

Um servidor FastAPI, rodando direto no computador de um integrante (sem Docker na v1, D-008), com uma tela simples em HTML e JavaScript. A tela tem o campo de conversa, o aviso de que quem responde é uma inteligência artificial e o aviso de privacidade (`docs/wireframes.md`). O aluno digita uma pergunta e recebe a resposta escrita pela Groq, em português. Nesta tarefa, a Groq responde sem documentos nem Espaço Aluno: é a prova de que a ponta que escreve a resposta funciona. Também mede os limites do plano gratuito e testa os modelos.

## O que não faz

- Não classifica a pergunta, não busca em documentos e não lê o Espaço Aluno (fase 2).
- Não faz o login do Espaço Aluno (03-01 junta com 01-01 e 02-04).
- Não guarda histórico: cada conversa começa do zero.

## Pronta quando

- [x] O servidor sobe com um comando (uvicorn, em ambiente virtual Python), no computador de um integrante. Docker fica para depois da v1 (D-008).
- [x] A tela de conversa envia uma pergunta e mostra a resposta da Groq em português.
- [x] A chave da Groq vem de variável de ambiente e não está no repositório nem em log.
- [x] Os limites do plano gratuito da Groq foram lidos na conta e anotados, e uma resposta com várias chamadas seguidas foi testada (T-001).
- [x] Pelo menos dois modelos gratuitos com chamada de ferramentas foram comparados em português, e um foi escolhido (T-002).
- [x] A página oficial da Groq sobre uso e retenção de dados foi lida e o que ela diz foi anotado em `docs/research.md` antes de qualquer dado real de aluno passar por ela (T-003).
- [x] O servidor não grava texto de perguntas nem de respostas em disco ou log.

## Vem de

FR-01, NFR-01, NFR-05, NFR-06, D-001, D-005, D-006, T-001, T-002 e T-003.

## Como testar

1. Crie a chave em https://console.groq.com e, num PowerShell seu, rode `setx GROQ_API_KEY "sua-chave"`. Abra um terminal novo depois disso. A chave nunca vai para arquivo do projeto.
2. `pip install -r servidor/requirements.txt`
3. Na raiz do projeto: `uvicorn servidor.app:app --port 8000`
4. Abra http://localhost:8000 e pergunte "Como funciona a prova substitutiva?". A resposta deve vir em português, em poucos segundos, com `openai/gpt-oss-120b · N s` embaixo. Como ainda não há documentos, ela deve dizer que não tem o regulamento do UniCEUB e indicar o Espaço Aluno ou a secretaria.
5. Sem a chave, a tela deve mostrar "A chave da Groq não está configurada no servidor".
6. O terminal do servidor deve mostrar só linhas como `POST /api/perguntar ... 200`, nunca o texto da pergunta.

**Resultados (2026-11-25, conta de Erick):**

- **Modelos disponíveis (T-002):** a Groq não oferece mais o `llama-3.3-70b-versatile`. Os modelos de texto disponíveis são `openai/gpt-oss-120b`, `openai/gpt-oss-20b` e `qwen/qwen3.8-27b`. Os três foram comparados com 4 perguntas em português (`python -m servidor.comparar_modelos`).
  - **Escolhido: `openai/gpt-oss-120b`.** Admitiu não ter a regra do UniCEUB, não inventou nada e respondeu em 0,6 a 0,9 s.
  - O `gpt-oss-20b` inventou um detalhe ("evita multas").
  - O `qwen3.8-27b` errou um fato simples (disse que a Alemanha ganhou a Copa de 2002).
  - O modelo pode ser trocado pela variável `GROQ_MODELO`.
- **Limites do plano gratuito (T-001):** a Groq informou 1.000 pedidos por dia e 8.000 tokens por minuto. Uma rajada de 20 perguntas seguidas passou toda, sem bloqueio, em 13,7 s. Os tokens por minuto serão o limite real: com trechos de documentos, cada resposta deve gastar de 1.500 a 2.500 tokens, o que dá cerca de 3 a 5 respostas por minuto (estimativa). Basta para a demonstração; a rajada de 20 deve ser refeita em 03-02, já com os documentos.
- **Dados (T-003):** em `docs/research.md`. A recomendação é ligar a retenção zero (Data Controls) antes de usar dados reais do Espaço Aluno.
- **Ponta a ponta:** uma pergunta pelo servidor foi respondida em 2,0 s, e o texto da pergunta não apareceu no log.
