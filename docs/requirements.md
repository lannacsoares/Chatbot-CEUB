# Requisitos

**Projeto:** chatbot-uniceub · **Versão:** 0.1 · **Data:** 2026-11-09

> **Em resumo:** o aluno do UniCEUB conversa com um chatbot em um site e recebe respostas sobre as regras da faculdade e sobre a própria situação no Espaço Aluno (faltas, professores, notas, horários, calendário, caminho de processos). O chatbot só responde e orienta. Tudo precisa ser gratuito, e a entrega final é em dezembro. Itens marcados como "proposto" foram sugeridos pelo agente a pedido do grupo e podem ser ajustados.

## O que o sistema é

Um chatbot em um site para alunos do UniCEUB tirarem dúvidas em linguagem natural. Ele responde a partir de documentos públicos da instituição e, com o login do próprio aluno, de informações do Espaço Aluno. Existe um único tipo de usuário: o aluno.

## Requisitos funcionais

O que o aluno precisa conseguir fazer.

| Nº | Requisito | Prioridade | Origem |
|---|---|---|---|
| FR-01 | O aluno envia perguntas em linguagem natural, em um site, e recebe a resposta na mesma conversa | Primeira versão | Dito: entrega como site |
| FR-02 | O chatbot responde dúvidas gerais (regulamentos, regras, informativos) a partir de documentos públicos do UniCEUB | Primeira versão | Dito |
| FR-03 | O aluno informa quantas faltas tem em uma matéria e o chatbot responde com o valor mostrado no Espaço Aluno | Primeira versão | Dito |
| FR-04 | O aluno pergunta se há falta agendada e o chatbot responde com o que consta no Espaço Aluno | Primeira versão | Dito |
| FR-05 | O aluno pergunta quem é o professor de uma matéria e o chatbot responde com o nome que consta no Espaço Aluno | Primeira versão | Dito |
| FR-06 | O aluno pergunta como abrir um processo e o chatbot indica o caminho no Espaço Aluno, sem abrir o processo | Primeira versão | Dito |
| FR-07 | O aluno consulta as próprias notas pelo chatbot | Primeira versão | Dito |
| FR-08 | O aluno consulta os próprios horários pelo chatbot | Primeira versão | Dito |
| FR-09 | O aluno consulta o calendário acadêmico pelo chatbot | Primeira versão | Dito |
| FR-10 | Para consultas pessoais, o aluno entra com a própria conta do Espaço Aluno | Primeira versão | Dito: uso do login do aluno |
| FR-11 | Quando não souber responder ou não tiver acesso à informação, o chatbot diz isso e, quando possível, indica onde o aluno encontra, sem inventar a resposta | Primeira versão | Dito: o chatbot deve responder que não tem conteúdo suficiente, em vez de inventar |
| FR-12 | Nas respostas gerais, o chatbot indica de qual documento a informação veio | Primeira versão | Proposto |
| FR-13 | Se a sessão do Espaço Aluno expirar, o chatbot avisa e pede novo login | Primeira versão | Proposto, a partir do que o grupo viu: a sessão é um cookie que expira |

## Requisitos não funcionais

Como o sistema precisa se comportar.

| Nº | Requisito | Prioridade | Origem |
|---|---|---|---|
| NFR-01 | Custo zero: o modelo de IA, a hospedagem e qualquer outro serviço usado têm plano gratuito | Primeira versão | Dito |
| NFR-02 | O chatbot só acessa informações da conta de quem fez login. Nenhuma resposta traz dados de outra conta | Primeira versão | Dito (cada aluno vê só os próprios dados) e dado pessoal sujeito à LGPD |
| NFR-03 | Na primeira versão, só as contas do grupo (Lanna, Sofia, Geovanna e Erick) são usadas | Primeira versão | Dito |
| NFR-04 | O chatbot é somente leitura: não executa nenhuma ação no Espaço Aluno | Primeira versão | Dito |
| NFR-05 | Senha, cookie de sessão e token não são gravados em arquivos do projeto, no repositório nem em logs | Primeira versão | Dito (não vão para os arquivos do projeto) |
| NFR-06 | O chatbot responde em português do Brasil | Primeira versão | Proposto |
| NFR-07 | Precisão: o chatbot acerta pelo menos 80% de um conjunto de 40 perguntas de teste (5 por tipo de consulta, nas 8 consultas), conferindo cada resposta com a fonte | Primeira versão | Proposto |
| NFR-08 | Honestidade: em um conjunto de 10 perguntas fora do escopo, o chatbot admite não saber ou orienta, sem inventar, em pelo menos 90% | Primeira versão | Proposto |
| NFR-09 | Desempenho: a resposta chega em até 15 segundos em pelo menos 90% das perguntas do conjunto de teste | Primeira versão | Proposto |
| NFR-10 | Os dados lidos do Espaço Aluno para responder são usados só na hora e descartados; o chatbot não os guarda depois da conversa | Primeira versão | Dito |
| NFR-11 | O protótipo pode ser demonstrado ao vivo, em sala e sem slides, mostrando exemplos de uso, resultados e limitações | Primeira versão | Proposto, a partir da descrição do trabalho feita pelo professor |
| NFR-12 | O grupo treina o modelo de embeddings e o classificador de tipo de pergunta, separa dados de treino e de teste e mostra o resultado medido (busca antes e depois do ajuste; acerto do classificador) | Primeira versão | Dito (D-004) |

## Limites

- Projeto da matéria de Inteligência Artificial, feito por um grupo de quatro pessoas.
- Entrega final em dezembro, com entregas semanais. A desta semana é a descrição formal do projeto e os requisitos funcionais e não funcionais.
- Sem verba: tudo gratuito, incluindo o modelo de IA e a hospedagem.
- Todo o grupo tem algum conhecimento de Python, JavaScript, serviço de IA e Git; o nível de cada um não foi dito.
- O professor concordou com o uso do login do aluno para consultar o Espaço Aluno.
- Descrição do trabalho feita pelo professor: o grupo (até 6 pessoas) apresenta em aula, sem slides, três pontos: intuição (o problema, onde a IA entra e a lógica do modelo, sem aprofundar a matemática), código (os trechos mais relevantes, a estrutura, as bibliotecas e como as partes se conectam) e funcionamento (demonstração, resultados e limitações). Python é fortemente recomendado. Ele pede um protótipo funcional e bem explicado, em vez de um sistema complexo e inacabado, e diz que a profundidade da explicação importa mais que a complexidade.
- Dados do Espaço Aluno são dados pessoais, sujeitos à LGPD.

## Fora da primeira versão

- Executar ações no Espaço Aluno, como abrir um processo.
- Uso por alunos de fora do grupo.
- Aplicativo e WhatsApp.

## Como saberemos que deu certo

O grupo pediu que o agente propusesse os números. Proposta: os números dos requisitos NFR-07, NFR-08 e NFR-09, medidos com um conjunto de perguntas de teste que o grupo monta, e a entrega final aceita pelo professor.

## Pontos em aberto

| Nº | Ponto | Depende de |
|---|---|---|
| 1 | Os números de NFR-07, NFR-08 e NFR-09 foram propostos pelo agente e precisam da concordância do grupo | O grupo |
| 2 | A descrição do trabalho dá três pontos de apresentação (intuição, código, funcionamento), mas não diz os pesos nem se há rubrica de nota. Os requisitos refletem os três pontos (NFR-11) | O grupo, com o professor |
| 3 | De onde vem cada consulta (Espaço Aluno ou documento público), principalmente o calendário acadêmico | Etapa de modelagem |
| 4 | Como o login do aluno é feito no site e como a sessão é guardada | Decisão da etapa de arquitetura |
