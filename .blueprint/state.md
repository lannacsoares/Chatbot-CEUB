---
blueprint_state: 1
project: chatbot-uniceub
starting_point: start
document_language: pt-BR
developers: 4
documents_at: docs/
tasks_at: docs/plan.md
memory: journal
observability: journal
updated: 2026-11-09T19:42:00Z
updated_by: Claude Code
---

# Project state

## Project kind

| Fact | Value | Known how |
|---|---|---|
| has-screens | yes | deduced |
| stores-data | no | deduced |
| holds-personal-data | yes | deduced |
| used-by-command-or-code | unknown | - |
| calls-a-model | yes | deduced |

Deduced: chatbot com interface de conversa que responde dúvidas de alunos do UniCEUB, usando documentos públicos e dados pessoais do Espaço Aluno.

## Criteria the person declared

- Projeto da matéria de Inteligência Artificial; desenvolvido por um grupo de quatro pessoas.
- O professor da matéria concordou que o chatbot use o token do login da página do UniCEUB para consultar o Espaço Aluno do próprio aluno.
- As respostas gerais vêm de documentos públicos da instituição (regulamentos, regras, informativos).
- No início, o chatbot usa apenas os logins do próprio grupo (Lanna, Sofia, Geovanna e Erick), sem alunos de fora.
- O objetivo por enquanto é a entrega do trabalho; futuramente, se der certo, vender ao UniCEUB.
- O chatbot só responde e orienta, sem executar ações no Espaço Aluno.
- Entrega como site.
- Tudo precisa ser gratuito: o modelo de IA e a hospedagem do site incluídos. Sem verba.
- Entrega final do trabalho em dezembro, com entregas semanais; a desta semana é a descrição formal do projeto e os requisitos funcionais e não funcionais.
- Todos do grupo têm algum conhecimento das ferramentas listadas (Python, JavaScript, serviço de IA, Git); o nível de cada um não foi dito.
- Cada conversa começa do zero: o histórico das conversas não é guardado.
- Se o chatbot não tiver conteúdo suficiente, ele deve dizer isso em vez de inventar uma resposta.
- Os dados lidos do Espaço Aluno são usados só na hora e descartados depois.
- O chatbot deve buscar sozinho a informação, ser "treinado" com os documentos abertos do UniCEUB e ter acesso ao Espaço Aluno do próprio aluno.
- Quando o modelo errar, o aluno vê a fonte e um lembrete para conferir no Espaço Aluno ou na secretaria.
- Descrição do trabalho feita pelo professor (colada pela Lanna): apresentação em aula, sem slides, com três pontos (intuição, código e funcionamento com demonstração); grupos de até 6 pessoas; Python fortemente recomendado; protótipo funcional e bem explicado vale mais que sistema complexo e inacabado. "Busca semântica" está entre as aplicações sugeridas. O texto não diz que é preciso treinar um modelo; a Lanna disse que o professor exige treino, então isso pode ter sido dito em aula.

## Steps

| Step | Situation | Main questions |
|---|---|---|
| system-description | closed | 4 of 4 |
| requirements | closed | 3 of 3 |
| modeling | closed | 4 of 4 |
| architecture | closed | 4 of 4 |
| plan | closed | 2 of 2 |

## Documents

| Document | Situation | Where |
|---|---|---|
| system-description | ready | docs/system-description.md |
| requirements | ready | docs/requirements.md |
| research | ready | docs/research.md |
| architecture | ready | docs/architecture.md |
| decisions | ready | docs/decisions.md |
| plan | ready | docs/plan.md |
| test-plan | ready | docs/test-plan.md |
| use-cases | ready | docs/use-cases.md |
| data-classification | ready | docs/data-classification.md |
| wireframes | ready | docs/wireframes.md |
| ai-features | ready | docs/ai-features.md |
| playbooks | ready | docs/playbooks/ |

## Main questions

### system-description

- [x] Que problema o sistema resolve, e para quem
- [x] O que o grupo quer conseguir com ele
- [x] Como ele chega a quem usa
- [x] O que fica fora da primeira versão

### requirements

- [x] O que cada tipo de usuário precisa conseguir fazer
- [x] O que limita o projeto: verba, prazo, lei, o que o grupo já usa
- [x] Como saber que deu certo

### modeling

- [x] As jornadas que não podem dar errado
- [x] O que o sistema guarda, e se há dado pessoal
- [x] Quais são as telas principais
- [x] O que o modelo faz no produto, e o que o produto faz quando ele erra

### architecture

- [x] Stack
- [x] Hospedagem
- [x] Tratamento dos dados pessoais
- [x] Outras decisões que geram custo

### plan

- [x] O que vem primeiro
- [x] Quem faz o quê

## Refinement questions left for later

- [x] requirements: o professor avalia por alguma rubrica? Resposta parcial: a descrição do trabalho dá os três pontos da apresentação (intuição, código, funcionamento), sem pesos. Refletido em NFR-11.
- [x] architecture: "treinar" é exigência da matéria? Resposta: sim, o professor exige treinar algo. Resolvida em D-002.
- [x] architecture: o texto do trabalho não exige treino, mas o grupo quer fazer o treino e o tornou parte fixa do projeto (D-004). Perguntar ao professor o que ele aceita como treino continua útil, mas não bloqueia nada.
- [ ] modeling: em que aparelhos o site será aberto (computador, celular ou os dois)? Necessário para desenhar as telas.
- [ ] modeling: a aparência do site segue as cores do UniCEUB ou é livre? Necessário para decidir se o projeto precisa do documento de design.

## Answers

### system-description · O problema e quem usa

Idioma dos documentos: português do Brasil. Desenvolvem em grupo: Lanna, Sofia, Geovanna e Erick.
O chatbot tira dúvidas dos alunos sobre o UniCEUB. Ideia central: (1) responder a partir de documentos públicos da instituição (regulamentações, regras, informativos), extraídos para alimentar o chat; (2) consultar a página pessoal do aluno no Espaço Aluno, usando o token do login do site do UniCEUB, com a concordância do professor da matéria. Exemplos de perguntas pessoais: se há falta agendada, quem é o professor de uma matéria, quantas faltas tem em uma matéria, qual o caminho para abrir um processo no Espaço Aluno.

### system-description · Dúvida sobre o token

Foi explicado como o token funciona (crachá temporário do login; o chatbot age como o aluno que logou). A ideia inicial é usar somente os logins do grupo.

### system-description · Checagem do Espaço Aluno

Com a conta da Lanna, pelo F12 (aba Rede), na página de uma disciplina: o Espaço Aluno (ea.uniceub.br) roda em ASP.NET MVC (servidor IIS). A página com as faltas e o professor chega como HTML pronto (tipo document), não como JSON. Em Fetch/XHR só apareceram scripts e estilos, sem API de dados. Os cabeçalhos de pedido saíram "provisórios" (service worker), então ainda não se viu se há cookie de sessão ou cabeçalho Authorization. Os endereços das páginas levam parâmetros codificados.

Depois, na aba Application: não há token no Local Storage nem no Session Storage. Entre os cookies (só os nomes foram vistos) há `ASP.NET_SessionId` e `__RequestVerificationToken` (proteção contra falsificação de formulário, não é token de login); os demais são de análise e marketing. Não apareceu `.ASPXAUTH`. Leitura: o login parece ser guardado como sessão no servidor, identificada pelo cookie `ASP.NET_SessionId`.

### system-description · Objetivo, entrega e escopo

Objetivo por enquanto: entregar o trabalho da matéria; futuramente, se der certo, vender ao UniCEUB. Entrega: um site. Fora da primeira versão (tirado de "só responda minhas dúvidas e me oriente, não faça nada por mim"): o chatbot não executa ações no Espaço Aluno, só responde e orienta.

### requirements · Usuários e consultas

Só existe um tipo de usuário: o aluno. Todas as consultas citadas são importantes para a primeira versão: regras gerais (documentos públicos), faltas por matéria, falta agendada, professor da matéria, caminho para abrir um processo, notas, horários e calendário acadêmico (lido como "todas essas que você citou"). A descrição do sistema foi atualizada com notas, horários e calendário.

### requirements · Limites do projeto

Prazo: entrega final em dezembro, com entregas semanais; a desta semana é a descrição mais formal do projeto e os requisitos funcionais e não funcionais. Verba: nenhuma, tudo gratuito, incluindo o modelo de IA e onde o site roda. Ferramentas: todo o grupo tem algum conhecimento nas que foram listadas (Python, JavaScript, serviço de IA, Git). Chegou também um "7" solto no fim da resposta, que não foi interpretado.

### requirements · Como saber que deu certo

A pergunta sobre a rubrica do professor não foi entendida e ficou como pergunta de refinamento. Sobre os números de sucesso, o grupo pediu que o agente propusesse. Proposta, escrita em `docs/requirements.md`: acertar ao menos 80% de 40 perguntas de teste (NFR-07), admitir não saber em ao menos 90% de 10 perguntas fora do escopo (NFR-08) e responder em até 15 segundos em ao menos 90% dos casos (NFR-09). Os números são do agente e ainda precisam da concordância do grupo.

### modeling · Jornadas e histórico

Jornadas que não podem dar errado: A (entrar com a conta e fazer uma pergunta pessoal), por ser a função principal, e D (pergunta fora do escopo), porque o risco do sistema é o chatbot inventar uma resposta; o ideal é que ele diga que não tem conteúdo suficiente para responder. Histórico: cada conversa começa do zero. Escritas em `docs/use-cases.md`. O requisito FR-11 passou a vir do que a pessoa disse.

### modeling · O que o sistema guarda e as telas

Dados do Espaço Aluno: usados só na hora e descartados depois. Somado a "cada conversa começa do zero", o chatbot não guarda dados de usuário; por isso `stores-data` ficou `no` (dedução do agente), embora ele precise dos documentos públicos como conteúdo. Há dado pessoal, então `docs/data-classification.md` foi escrito. Telas: as três propostas (login com a conta do Espaço Aluno, conversa e aviso de privacidade), "por enquanto somente essas". Escritas em `docs/wireframes.md`. O requisito NFR-10 foi acrescentado.

### modeling · O que o modelo faz

O grupo corrigiu a proposta do agente: o modelo precisa buscar sozinho a informação, ser "treinado" com os documentos abertos do UniCEUB e ter acesso ao Espaço Aluno de cada um para responder as consultas já listadas. Isso foi escrito como um modelo que escolhe entre ferramentas de leitura que o grupo constrói (buscar nos documentos e consultar cada informação do Espaço Aluno). A palavra "treinado" ficou como decisão de arquitetura: a proposta do agente é buscar nos documentos a cada pergunta em vez de treinar o modelo. Quando o modelo errar: "pode ser assim mesmo", ou seja, mostrar a fonte e o lembrete para conferir. Escrito em `docs/ai-features.md`.

### architecture · Serviço de modelo de IA

O grupo aceitou a recomendação da Groq. Perguntou também como funciona o "treinamento": se envia os dados pessoais ou se o login dá acesso. Foi explicado que os dados pessoais não são enviados antes nem usados para treinar; são lidos na hora, com o login, e descartados. Os documentos públicos (PDF) podem ser enviados normalmente, e entram por busca a cada pergunta. A pergunta sobre o professor exigir treino de modelo continua sem resposta.

### architecture · Treino e documentos públicos

O grupo confirmou que o professor exige treinar algo ("se não, não tem sentido a aplicação de IA no trabalho"). A Lanna descreveu o pipeline dos documentos: salvar em PDF, converter para texto, gerar embeddings e fazer RAG. O agente explicou que embeddings de um modelo pronto não contam como treino do grupo e propôs ajustar os embeddings e treinar um classificador de tipo de pergunta. Ela perguntou qual seria a função do classificador (explicado: decidir se a pergunta vai para os documentos, para o Espaço Aluno ou fora do escopo) e disse para seguir assim, sem abrir mão das consultas ao Espaço Aluno de cada integrante. Registrado como D-002 (decidida pela Lanna, a partir da primeira opção). O que o professor aceita como treino segue como pergunta aberta.

### architecture · Entrada no Espaço Aluno

O grupo aceitou a recomendação: o aluno digita usuário e senha no site do chatbot, o servidor entra por ele, lê as páginas na hora e descarta tudo (D-003). Não foi possível verificar se o login tem captcha ou verificação em dois passos; vai para T-008.

### architecture · Hospedagem

O grupo aceitou a recomendação: o site e os modelos rodam no computador de um integrante, em contêiner Docker (D-005). O grupo também confirmou que quer fazer o treino e o tornou parte fixa do projeto (D-004).

### architecture · Stack, dados pessoais e fechamento

O grupo aceitou a stack só em Python (D-006) e o envio à Groq só dos campos necessários, sem gravar nada em disco nem em log (D-007). Não restaram outras decisões que gerem custo: tudo é gratuito e o treino usa Kaggle ou Colab (D-002, D-004). A arquitetura foi escrita em `docs/architecture.md` e a etapa foi fechada.

### plan · O que vem primeiro e quem faz o quê

Apresentação em aula na primeira quinzena de dezembro (data exata ainda não definida). O grupo aceitou uma frente por pessoa: (A) Espaço Aluno, (B) documentos, (C) classificador, (D) servidor, tela e Groq. Quem leva cada frente ainda será escolhido pelo grupo. O plano começa pelo teste de entrar no Espaço Aluno (o maior risco), em paralelo com os documentos, as perguntas de treino e o servidor. Escrito em `docs/plan.md`, com 11 tarefas em 3 fases e uma especificação por tarefa em `docs/specs/`. As metas de data (17/11, 29/11 e 6/12) foram propostas pelo agente.

## Decisions

- D-001 · Serviço de modelo de IA: Groq no plano gratuito · decided
- D-002 · Documentos públicos por busca (RAG) e treino de embeddings e classificador de pergunta · decided
- D-003 · Entrada no Espaço Aluno: login com usuário e senha no site do chatbot, sessão e dados descartados · decided
- D-004 · O treino (embeddings e classificador) faz parte fixa do projeto · decided
- D-005 · Hospedagem: no computador de um integrante, em contêiner Docker · decided
- D-006 · Stack: só Python (FastAPI, sentence-transformers, scikit-learn, FAISS, pdfplumber, requests e BeautifulSoup) · decided
- D-007 · Dados pessoais: só os campos necessários vão à Groq; nada em disco nem em log · decided

## Open points

- O que a Groq faz com o texto recebido (retenção e uso). À Groq vão só a pergunta e os campos necessários (D-007). Depende de ler a página oficial dela (T-003), antes de usar dados reais.
- Se os abonos de falta mostram o motivo, o que pode ser dado de saúde. Depende do grupo conferir no Espaço Aluno.
- Os números de NFR-07, NFR-08 e NFR-09 foram propostos pelo agente e precisam da concordância do grupo.
- A confirmar: o professor concordou com o uso do token de login, mas não sabemos se a área de TI do UniCEUB também sabe e autoriza. Fica mais urgente antes de abrir o chatbot para outros alunos. Depende do grupo.
- A conversar com o professor: ele sugeriu usar "tokens do login", mas o Espaço Aluno não parece usar token e sim sessão por cookie. Vale confirmar o que ele tinha em mente. Depende do grupo.
- A verificar: se existe API oficial do UniCEUB. Hoje os dados chegam como páginas HTML, e a sessão (cookie) expira, então o chatbot precisaria ler páginas e renovar o login. Como obter e guardar a sessão entra como decisão na etapa de arquitetura. Nenhum cookie, token ou senha vai para o chat nem para os arquivos do projeto.

- Os dados de treino do classificador e dos embeddings (perguntas de exemplo e pares pergunta-trecho) precisam ser escritos pelo grupo; quantos exemplos bastam depende dos documentos que a Lanna enviar.
- Qual integrante hospeda o site na demonstração, e se a turma acessa só pela tela da demonstração ou também pelo celular (túnel gratuito, ainda não pesquisado). Vai para o plano.

## Next question

O repositório está preparado (`AGENTS.md` com o bloco do Blueprint, `CLAUDE.md` e `GEMINI.md`, um guia por frente em `docs/playbooks/` e o diário em `.blueprint/journal/`). A primeira tarefa é a 01-01, Login e leitura do Espaço Aluno (`docs/specs/01-01-login-e-leitura-do-espaco-aluno.md`). O grupo escolhe quem leva cada frente (A, B, C, D), e a Lanna envia os PDFs para a 01-02 e informa a data da apresentação. Em paralelo, a Lanna pode enviar os PDFs dos documentos públicos.
