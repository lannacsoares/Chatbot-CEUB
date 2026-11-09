# Funcionalidades de IA

**Projeto:** chatbot-uniceub · **Versão:** 0.1 · **Data:** 2026-11-09

> **Em resumo:** três componentes de IA. Um classificador, treinado pelo grupo, decide o tipo de pergunta: geral (busca nos documentos públicos do UniCEUB), pessoal (consulta ao Espaço Aluno de quem fez login) ou fora do escopo. Um modelo de embeddings, ajustado pelo grupo com os documentos do UniCEUB, acha os trechos certos. O modelo de linguagem da Groq (D-001) escreve a resposta. Só lê, nunca age. Quando não há conteúdo suficiente, deve dizer isso em vez de inventar. Decisões em D-001 e D-002.

## O que o modelo faz aqui

| Nº | O que faz | Para quem | Quanto custa por uso |
|---|---|---|---|
| AI-01 | Recebe a pergunta, com os trechos ou dados que as ferramentas trouxeram, e escreve a resposta em português | Aluno | Ainda não medido. Precisa caber em plano gratuito (NFR-01) |
| AI-02 | Classifica o tipo da pergunta (treinado pelo grupo) | Aluno, sem ver | Roda em CPU, sem custo por uso |
| AI-03 | Encontra os trechos dos documentos mais parecidos com a pergunta (embeddings ajustados pelo grupo) | Aluno, sem ver | Roda em CPU, sem custo por uso |

## AI-01 · Responder a pergunta do aluno

**O que ele recebe:**
- a pergunta do aluno;
- trechos dos documentos públicos do UniCEUB, quando a pergunta é geral (não são dados pessoais);
- dados lidos do Espaço Aluno do aluno que fez login (faltas, falta agendada, professor, notas, horários), quando a pergunta é pessoal. Estes são dados pessoais (ver `docs/data-classification.md`).

**Onde buscar:** cada tipo de consulta é uma ferramenta que o grupo constrói: buscar nos documentos públicos, consultar faltas, falta agendada, professor, notas, horários, calendário acadêmico e caminho para abrir um processo. Quem decide o caminho é o classificador (AI-02), que roda antes do modelo de linguagem; o modelo só escreve a resposta com o que a ferramenta trouxe. Todas as ferramentas só leem (NFR-04). Ele não navega livremente pelo Espaço Aluno. Uma pergunta que mistura os dois tipos ("quantas faltas posso ter em X e quantas eu tenho?") usa as duas ferramentas.

**O que se espera de volta:** uma resposta em português, na conversa. Nas respostas gerais, com o documento de origem (FR-12). Se não houver conteúdo suficiente, a resposta diz isso (FR-11, UC-02).

**Qual modelo:** Groq no plano gratuito (D-001), com um modelo aberto que suporte chamada de ferramentas. O modelo exato sai dos testes T-001 e T-002.

**Documentos públicos (D-002).** Os documentos entram por busca a cada pergunta: PDF, texto, trechos, embeddings, busca dos trechos mais parecidos (RAG) e resposta com a fonte (FR-12). O modelo de linguagem não é treinado com os documentos; o treino do grupo está nos dois componentes abaixo.

## AI-02 · Classificar o tipo da pergunta

- **Função:** decidir, antes de qualquer consulta, para onde a pergunta vai: documentos públicos (geral), Espaço Aluno (pessoal, e qual consulta: faltas, falta agendada, professor, notas, horários, calendário, caminho de processo) ou fora do escopo. Pergunta fora do escopo recebe a resposta "não tenho conteúdo suficiente" sem gastar uma chamada da Groq, o que ajuda no limite do plano gratuito, no tempo de resposta (NFR-09) e em NFR-08.
- **Como é treinado:** com perguntas de exemplo escritas pelo grupo para cada tipo, separadas em treino e teste. Modelo de partida: BERTimbau ou scikit-learn, treinado no Kaggle ou no Colab gratuitos. Nenhum dado real de aluno entra no treino (NFR-10); as perguntas de exemplo só têm o jeito de perguntar.
- **Como se mede:** acerto geral e por tipo no conjunto de teste (T-005). A meta de acerto ainda precisa ser combinada pelo grupo.
- **Quando erra:** pergunta pessoal classificada como geral recebe resposta dos documentos e o lembrete de conferir no Espaço Aluno; pergunta fora do escopo classificada como outro tipo tende a ser pega pela falta de trecho suficiente na busca (FR-11). Caso de baixa confiança do classificador: decisão a tomar na implementação, proposta de usar o caminho que admite não saber.

## AI-03 · Encontrar os trechos dos documentos

- **Função:** transformar a pergunta e os trechos dos documentos em vetores e devolver os trechos mais parecidos, com o documento de origem.
- **Como é treinado:** ajuste fino de um modelo de embeddings pronto (`multilingual-e5-small`, licença MIT) com pares de pergunta e trecho escritos a partir dos PDFs do UniCEUB, treino e teste separados, em GPU gratuita.
- **Como se mede:** quantas vezes o trecho certo aparece entre os primeiros resultados, antes e depois do ajuste (T-004).

**O que o aluno vê:** um aviso de que quem responde é uma inteligência artificial, a fonte da resposta quando houver, e um lembrete para conferir no Espaço Aluno ou na secretaria. O grupo aceitou o lembrete e a fonte.

## Quando o modelo erra

| O que acontece | O que o produto faz |
|---|---|
| Não há conteúdo suficiente para responder | Diz que não tem conteúdo suficiente e, quando possível, indica onde procurar (UC-02) |
| O modelo erra uma informação, por exemplo um número | O aluno vê a fonte e o lembrete para conferir no Espaço Aluno ou na secretaria |
| A resposta demora mais que o limite (NFR-09) | Proposto: mostra que está consultando e, se passar muito do limite, avisa que não conseguiu responder agora |
| O serviço do modelo está fora do ar, ou o limite do plano gratuito acabou | Proposto: avisa que não conseguiu responder agora e que o aluno pode tentar mais tarde |

O produto nunca trata a resposta do modelo como certa. Como ele só lê e não executa ações, não há nada difícil de desfazer que precise de confirmação.

## Limites e custo

- **Por uso:** ainda não medido.
- **O que limita:** o plano gratuito da Groq, em chamadas, tamanho e velocidade, a cota de GPU gratuita para treinar e o hardware gratuito onde AI-02 e AI-03 rodam (T-006 e T-007). Ninguém paga.
- **O que fica registrado:** nenhum dado pessoal nem texto de conversa (NFR-10 e `docs/data-classification.md`).

## O que ficou de fora

- O modelo não executa ações no Espaço Aluno.
- O modelo não guarda histórico de conversas.
- O modelo não acessa nada fora das ferramentas que o grupo construir.
