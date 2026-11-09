# Arquitetura

**Projeto:** chatbot-uniceub · **Versão:** 0.1 · **Data:** 2026-11-09

> **Em resumo:** um servidor Python (FastAPI), em contêiner Docker no computador de um integrante do grupo, serve uma tela de conversa. A cada pergunta, um classificador treinado pelo grupo decide se ela é geral, pessoal ou fora do escopo. Perguntas gerais usam uma busca por embeddings ajustados pelo grupo nos documentos públicos do UniCEUB; perguntas pessoais leem o Espaço Aluno de quem fez login. O modelo da Groq só escreve a resposta, a partir dos trechos ou dos campos que o servidor entregou. Senha, sessão e dados do aluno ficam só na memória do servidor e são descartados. Tudo é gratuito.

## Visão geral

| Peça | O que faz | Tecnologia | Onde roda |
|---|---|---|---|
| Tela | Login, conversa e aviso de privacidade (`docs/wireframes.md`) | HTML e JavaScript, servidos pelo próprio servidor | Navegador do aluno |
| Servidor | Recebe o login e as perguntas, junta as peças e devolve a resposta | Python, FastAPI | Contêiner Docker no computador de um integrante (D-005, D-006) |
| Classificador (AI-02) | Decide o tipo da pergunta e qual consulta pessoal | scikit-learn e, se couber, BERTimbau, treinados pelo grupo | Dentro do servidor, em CPU |
| Busca nos documentos (AI-03) | Acha os trechos mais parecidos com a pergunta | Embeddings ajustados pelo grupo (partida: `multilingual-e5-small`) e índice FAISS | Dentro do servidor, em CPU |
| Leitor do Espaço Aluno | Entra com a conta do aluno e extrai só os campos da pergunta | requests e BeautifulSoup | Dentro do servidor |
| Escritor da resposta (AI-01) | Escreve a resposta em português com o que o servidor entregou | Groq, plano gratuito, modelo aberto com chamada de ferramentas (D-001) | Serviço externo |

## Como uma pergunta é respondida

1. O aluno entra com usuário e senha do Espaço Aluno (FR-10, D-003). O servidor guarda a sessão só na memória, ligada àquela conversa.
2. O aluno envia uma pergunta. O classificador decide o tipo.
3. **Geral:** a busca acha os trechos mais parecidos nos documentos públicos. O servidor manda à Groq a pergunta e esses trechos. A resposta cita o documento de origem (FR-12). Se nenhum trecho for parecido o bastante, o chatbot diz que não tem conteúdo suficiente (FR-11).
4. **Pessoal:** o leitor entra no Espaço Aluno a partir do `/Painel`, abre a página da consulta (faltas, falta agendada, professor, notas, horários, calendário, caminho de processo), extrai só os campos necessários e o servidor manda à Groq a pergunta e esses campos (D-007). Se a sessão expirou, o chatbot avisa e pede novo login (FR-13).
5. **Fora do escopo:** o servidor responde que não tem conteúdo suficiente, sem chamar a Groq (NFR-08).
6. Pergunta que mistura os dois tipos usa as duas consultas.
7. Ao fim da conversa (ou ao sair), senha, sessão, campos lidos e texto da conversa são descartados (NFR-10).

## Como os componentes são preparados (fora do ar, antes da demonstração)

- **Documentos:** a Lanna envia os PDFs públicos do UniCEUB; pdfplumber extrai o texto; o texto é quebrado em trechos; o modelo de embeddings gera os vetores; FAISS guarda o índice em arquivo local. Documentos públicos não são dados pessoais.
- **Ajuste dos embeddings:** o grupo escreve pares de pergunta e trecho (a Groq pode rascunhar, o grupo revisa), separa treino e teste e ajusta o modelo no Kaggle ou no Colab gratuitos. Mede-se quantas vezes o trecho certo aparece entre os primeiros resultados, antes e depois (T-004). Depois do ajuste, os vetores de todos os trechos são gerados de novo.
- **Classificador:** o grupo escreve perguntas de exemplo por tipo, sem dado real de aluno, separa treino e teste, compara uma linha de base simples com o modelo maior e mede acerto por tipo (T-005).
- Os arquivos dos modelos treinados e o índice ficam no contêiner do servidor.

## Que dados saem do computador do grupo

| Para onde | O que vai | O que nunca vai |
|---|---|---|
| Espaço Aluno (ea.uniceub.br) | Usuário e senha do próprio aluno, no login, e os pedidos de página | Nada além disso |
| Groq | A pergunta e, conforme o tipo, trechos de documentos públicos ou os campos extraídos do Espaço Aluno | Senha, cookie de sessão, páginas inteiras, motivo de abonos de falta, nome e matrícula |
| Kaggle ou Colab (treino) | Perguntas de exemplo escritas pelo grupo e trechos de documentos públicos | Qualquer dado real de aluno |

Na memória do servidor ficam, durante a conversa: a sessão do Espaço Aluno e os campos lidos. Nada é gravado em disco nem em log (NFR-05, NFR-10). Os registros do servidor não incluem texto de perguntas nem de respostas.

## Como cada requisito é atendido

| Requisito | Onde |
|---|---|
| FR-01, FR-12 | Tela e servidor; resposta com o documento de origem |
| FR-02 | Busca nos documentos (AI-03) |
| FR-03 a FR-09 | Leitor do Espaço Aluno, escolhido pelo classificador (AI-02); calendário depende de onde estiver (ponto aberto) |
| FR-10, FR-13 | Login no site (D-003) e aviso de sessão expirada |
| FR-11, NFR-08 | Classificador (fora do escopo) e limite de semelhança na busca |
| NFR-01 | Tudo gratuito: Groq gratuita, Kaggle e Colab para treino, computador do grupo para rodar |
| NFR-02, NFR-03 | Só a sessão de quem fez login; só as contas do grupo |
| NFR-04 | O leitor só faz pedidos de leitura de página |
| NFR-05, NFR-10 | Senha e sessão só na memória; nada em disco ou log |
| NFR-09 | Classificador e busca em CPU; a Groq responde rápido; T-001 e T-007 medem |
| NFR-11 | Servidor local, demonstração ao vivo |
| NFR-12 | Ajuste dos embeddings e classificador, com medição (T-004, T-005) |

## Riscos e o que ainda não se sabe

- **Login e leitura do Espaço Aluno (T-008):** sem API; o login pode ter captcha ou verificação em dois passos, e a leitura das páginas pode quebrar se o layout mudar. É o maior risco do projeto, e por isso o plano o testa logo no início. Se for inviável, o trabalho continua só com os documentos públicos.
- **Limites da Groq gratuita (T-001, T-002) e retenção de dados (T-003):** os limites só aparecem na conta, e a página oficial de dados não foi lida.
- **Treino (T-004, T-005, T-006):** quantos exemplos o grupo precisa escrever e se a cota gratuita de GPU basta.
- **Computador do grupo:** a demonstração depende do computador e da internet de um integrante (D-005).
- **TI do UniCEUB:** não se sabe se sabe e autoriza o acesso; fica mais urgente antes de abrir o chatbot para outros alunos.
- **Versões das bibliotecas:** não foram conferidas (D-006).

## O que fica para o plano

- Qual integrante hospeda o site na demonstração e se a turma acessa também pelo celular, com um túnel gratuito (ainda não pesquisado).
- Se o classificador final será BERTimbau ou o modelo simples; sai da comparação de T-005.
- De onde vem cada consulta, em especial o calendário acadêmico (documento público ou Espaço Aluno).

## Decisões desta etapa

D-001 (serviço de modelo de IA), D-002 e D-004 (documentos por busca e o treino), D-003 (entrada no Espaço Aluno), D-005 (hospedagem), D-006 (stack) e D-007 (dados pessoais) estão em `docs/decisions.md`, com a pesquisa em `docs/research.md` e as verificações em `docs/test-plan.md`.
