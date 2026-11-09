# Decisões

Todas as decisões do projeto, em um só lugar, a mais nova por último. Uma decisão nunca é reescrita: quando ela muda, uma nova entrada a substitui e diz qual.

## D-001 · Serviço de modelo de IA

- **Decisão:** usar a Groq (GroqCloud), no plano gratuito, com um modelo aberto que suporte chamada de ferramentas. O modelo exato será escolhido nos testes.
- **Motivo:** custo zero (NFR-01) e, pelos termos descritos, o plano gratuito não usa o que se envia para treinar modelos, o que pesa porque dados pessoais de alunos passam pelo modelo.
- **Alternativas:** Google Gemini (a cota gratuita permite uso do conteúdo pelo Google e leitura por revisores humanos), Mistral (plano gratuito pode ser usado para treino) e OpenRouter (só 50 requisições por dia e chamada de ferramentas instável em modelos gratuitos). Detalhes em `docs/research.md`.
- **Decidido por:** Lanna, aceitando a recomendação · **Data:** 2026-11-09
- **Fontes:** `docs/research.md`, lidas em 2026-11-09.
- **Situação:** decided
- **Para testar:** T-001, T-002 e T-003, em `docs/test-plan.md`.

## D-002 · Como os documentos públicos entram no chatbot e o que o grupo treina

- **Decisão:** os documentos públicos do UniCEUB entram por busca a cada pergunta, no pipeline proposto pela Lanna: salvar em PDF, converter para texto, quebrar em trechos, gerar embeddings e fazer RAG (buscar os trechos mais parecidos com a pergunta e entregá-los ao modelo da Groq, que escreve a resposta citando a fonte). Sobre essa base, o grupo treina dois componentes pequenos em GPU gratuita (Kaggle ou Colab): (1) o ajuste do modelo de embeddings com pares de pergunta e trecho dos documentos do UniCEUB; (2) um classificador do tipo de pergunta (geral, pessoal ou fora do escopo, e qual consulta pessoal). A consulta ao Espaço Aluno de cada integrante do grupo continua parte do produto: o classificador é o que decide quando a pergunta vai para a busca nos documentos e quando vai para a consulta pessoal.
- **Motivo:** o professor exige treinar algo, e a Groq não serve modelo ajustado no plano gratuito (adaptadores LoRA só no plano Enterprise). Dois componentes pequenos treinam de graça, rodam em CPU e dão trabalho de IA medível (conjunto de dados, separação treino e teste, métricas). A busca mantém a fonte citável (FR-12) e permite dizer "não tenho conteúdo suficiente" (FR-11).
- **Alternativas:** só ajustar os embeddings; só o classificador; ajustar um modelo de linguagem (LoRA) e hospedar por conta própria; só busca, sem treino. Detalhes em `docs/research.md`.
- **Decidido por:** Lanna, que escolheu manter o pipeline dela como base e treinar embeddings e classificador (primeira opção), com a condição de não abrir mão das consultas ao Espaço Aluno · **Data:** 2026-11-09
- **Fontes:** `docs/research.md`, pesquisadas em 2026-11-09.
- **Situação:** decided
- **Efeito em D-001:** a Groq continua só para escrever as respostas; não é treinada nem ajustada.
- **Para testar:** T-004 a T-007, em `docs/test-plan.md`.

## D-003 · Como o chatbot entra no Espaço Aluno

- **Decisão:** o aluno digita usuário e senha da conta do Espaço Aluno no site do chatbot. O servidor do chatbot entra no Espaço Aluno por ele, lê só as páginas necessárias para a pergunta e descarta tudo ao fim da conversa: senha, cookie de sessão e dados lidos. Nada é gravado (NFR-10). Na primeira versão vale só para as contas do grupo (NFR-03).
- **Motivo:** é o caminho mais simples para entregar como site, sem instalar nada no computador do aluno, e é compatível com o que se viu do Espaço Aluno: login por cookie de sessão e páginas HTML, sem token nem API.
- **Alternativas:** extensão de navegador que lê as páginas na sessão já aberta do aluno (a senha não passa pelo servidor do grupo, mas dá mais trabalho e exige instalar a extensão); o aluno colar os dados na conversa (mais simples e seguro, mas não é o acesso ao Espaço Aluno que o grupo descreveu).
- **Riscos aceitos:** a senha passa pelo servidor do grupo; a leitura das páginas pode quebrar se o layout do Espaço Aluno mudar; a área de TI do UniCEUB pode não saber desse acesso (ponto aberto no estado do projeto).
- **Decidido por:** Lanna, aceitando a recomendação · **Data:** 2026-11-09
- **Fontes:** o que foi visto no Espaço Aluno com a conta da Lanna (DevTools), registrado em `.blueprint/state.md`. Sem pesquisa externa.
- **Situação:** decided
- **Para testar:** T-008, em `docs/test-plan.md`.

## D-004 · O treino faz parte fixa do projeto

- **Decisão:** o grupo vai treinar os dois componentes de D-002 (ajuste dos embeddings e classificador de tipo de pergunta). O treino deixa de ser um reforço opcional e passa a ser parte fixa do escopo, mesmo que o texto do trabalho do professor não o exija. Se o tempo apertar, o que se corta é outra coisa (por exemplo, consultas do Espaço Aluno além das primeiras), não o treino.
- **Motivo:** o grupo quer fazer o treino. Ele dá o que explicar em "intuição" e "código" na apresentação e o que medir em "funcionamento" (acerto antes e depois do ajuste; acerto do classificador).
- **Alternativas:** manter o treino como opcional, decidido só se sobrar tempo; ou só busca com embeddings prontos. O grupo descartou as duas.
- **Decidido por:** Lanna, em nome do grupo · **Data:** 2026-11-09
- **Fontes:** descrição do trabalho feita pelo professor, colada pela Lanna em 2026-11-09 (não exige treino, mas não o impede).
- **Situação:** decided
- **Efeito em D-002:** confirma o que D-002 já dizia e torna fixo o treino de T-004, T-005 e T-006.

## D-005 · Onde o site e os modelos treinados rodam

- **Decisão:** o site e os modelos treinados rodam no computador de um integrante do grupo, durante a demonstração e os testes, empacotados em contêiner Docker para poder migrar para uma nuvem depois. Quem hospeda e como a turma acessa (só na tela da demonstração ou também pelo celular, com um túnel gratuito) fica para o plano.
- **Motivo:** custo zero sem cartão (NFR-01), sem sono nem partida lenta no dia da apresentação (NFR-11), e a senha e os dados dos alunos passam só por um computador do grupo (NFR-05, NFR-10).
- **Alternativas:** Google Cloud Run (cota gratuita boa, mas exige conta de cobrança com cartão e o alerta de orçamento não corta o gasto); Render gratuito (512 MB, 0,1 CPU e dorme após 15 minutos, provavelmente pouco para o modelo de busca); Hugging Face Spaces (a documentação oficial exige plano pago para rodar modelos). Detalhes em `docs/research.md`.
- **Riscos aceitos:** o site não fica no ar o tempo todo; a demonstração depende do computador e da internet do integrante; para vender ao UniCEUB depois será preciso uma hospedagem de verdade.
- **Decidido por:** Lanna, aceitando a recomendação · **Data:** 2026-11-09
- **Fontes:** `docs/research.md`, pesquisadas em 2026-11-09.
- **Situação:** decided
- **Para testar:** T-007 (tempo de resposta no computador escolhido), em `docs/test-plan.md`.

## D-006 · Stack

- **Decisão:** só Python. FastAPI para o servidor, com uma tela simples em HTML e JavaScript servida pelo próprio servidor; sentence-transformers para ajustar os embeddings; scikit-learn e, se couber, BERTimbau para o classificador; FAISS para guardar e buscar os vetores dos documentos; pdfplumber para ler os PDFs; requests e BeautifulSoup para ler as páginas do Espaço Aluno; Docker para empacotar (D-005). Tudo de código aberto e gratuito.
- **Motivo:** o professor recomenda Python, todo o grupo conhece (informado pelo grupo), há uma só base de código e poucas peças para explicar na apresentação.
- **Alternativas:** Python na IA com o site em React (mais bonito, mas duas bases de código); tudo em Streamlit ou Gradio (rápido, mas a tela e o login do Espaço Aluno ficam menos controláveis).
- **Decidido por:** Lanna, aceitando a recomendação · **Data:** 2026-11-09
- **Fontes:** nenhuma pesquisa; escolhas padrão para este tipo de trabalho, propostas pelo agente. Versões das bibliotecas não foram conferidas.
- **Situação:** decided
- **Para testar:** que as bibliotecas escolhidas funcionam juntas no computador do grupo, o que aparece nos primeiros passos do plano.

## D-007 · O que dos dados do Espaço Aluno vai para a Groq

- **Decisão:** o servidor lê a página do Espaço Aluno, extrai só os campos que a pergunta precisa (por exemplo, "Cálculo: 15 faltas, 25%") e manda à Groq apenas esses campos mais a pergunta. Senha e cookie de sessão nunca saem do servidor; páginas inteiras, nome, matrícula e o motivo de abonos de falta (que pode ser dado de saúde) não são enviados. Nada é gravado em disco nem em log, e os registros do servidor não guardam texto de perguntas nem de respostas.
- **Motivo:** sai menos dado pessoal do computador do grupo (NFR-02, NFR-10, NFR-05), e dá para mostrar na apresentação exatamente o que foi enviado. Reduz também o risco de a Groq se confundir lendo uma página inteira.
- **Alternativas:** mandar a página inteira como texto (mais simples de programar, mas sai muito mais dado pessoal); extrair só os campos e pedir confirmação do aluno na tela a cada pergunta pessoal (mais transparência, conversa mais lenta).
- **Decidido por:** Lanna, aceitando a recomendação · **Data:** 2026-11-09
- **Fontes:** nenhuma pesquisa; a página oficial da Groq sobre retenção de dados não foi lida (T-003).
- **Situação:** decided
- **Para testar:** T-003, antes de usar dados reais de alunos, em `docs/test-plan.md`.
