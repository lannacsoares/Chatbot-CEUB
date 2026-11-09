# Pesquisa

**Projeto:** chatbot-uniceub · **Versão:** 0.1 · **Data:** 2026-11-09

> **Em resumo:** foram pesquisadas duas perguntas. (1) Qual serviço de modelo de IA gratuito usar: a Groq, decidida em D-001, porque, pelos termos publicados, o plano gratuito não treina com os dados enviados. (2) Como os documentos públicos entram no chatbot e o que o grupo treina, já que o professor exige treino: a recomendação é buscar nos documentos a cada pergunta e treinar dois componentes pequenos do próprio grupo (um classificador que decide o tipo de pergunta e um modelo de busca ajustado aos documentos do UniCEUB), em GPU gratuita, deixando a Groq só para escrever a resposta. A segunda foi decidida em D-002, na linha da recomendação.

## Qual serviço de modelo de IA gratuito o chatbot deve usar?

Critérios usados, vindos do projeto: custo zero (NFR-01), dados pessoais de alunos passam pelo modelo (NFR-02, NFR-10), o modelo precisa escolher entre ferramentas (AI-01), respostas em português, e o uso é pequeno (quatro contas do grupo, entrega em dezembro).

- **Decisão:** Groq (GroqCloud), com um modelo aberto que suporte chamada de ferramentas (D-001, decidida em 2026-11-09).
- **Motivo:** é a única das quatro opções pesquisadas cujo plano gratuito, pelos termos descritos, não usa o que se envia para treinar modelos, o que pesa porque faltas, notas e horários dos alunos vão no texto. Tem plano gratuito permanente, sem cartão, e modelos abertos com chamada de ferramentas.
- **Alternativas:**
  - **Google Gemini API (cota gratuita):** limites generosos, mas nos termos oficiais a cota gratuita é "serviço não pago": o Google usa o conteúdo enviado e as respostas para melhorar produtos, e revisores humanos podem ler. Não combina com dados pessoais de alunos. A exceção do Espaço Econômico Europeu, Suíça e Reino Unido não vale para o Brasil.
  - **Mistral (plano Experiment):** gratuito, mas a página oficial de ajuda diz que as requisições no plano Experiment podem ser usadas para treinar os modelos. Mesma objeção.
  - **OpenRouter (modelos `:free`):** apenas 50 requisições por dia na conta gratuita e 20 por minuto; relatos de falhas na chamada de ferramentas em modelos gratuitos e de provedores que treinam com os dados. Inviável para um chatbot que faz mais de uma chamada por resposta.
- **Limites da Groq:** a página oficial de limites mostra só os limites-base do plano pago Developer (por exemplo, 30 requisições por minuto, 1 mil por dia, 8 mil tokens por minuto, 200 mil por dia para `openai/gpt-oss-120b`, `openai/gpt-oss-20b` e `qwen/qwen3.8-27b`). Os valores do plano gratuito só aparecem na conta, em configurações. Fontes de terceiros indicam cerca de 30 requisições por minuto e 6 mil a 12 mil tokens por minuto no gratuito, o que pode estourar em respostas que usam várias ferramentas seguidas.
- **Fontes** (todas lidas em 2026-11-09):
  - https://console.groq.com/docs/rate-limits.md (oficial, lida inteira)
  - https://developersdigest.tech/models/free-api/groq (terceiros; resume o contrato de serviço da Groq sobre treino e retenção, verificado pelo site em 2026-10-18)
  - https://fast.io/resources/groq-rate-limit/ (terceiros; limites do plano gratuito)
  - https://ai.google.dev/terms (oficial, termos de março de 2026; lida em trechos de resultado de busca)
  - https://help.mistral.ai/en/articles/450104-how-can-i-try-the-api-for-free-with-the-experiment-plan (oficial; lida em trecho de resultado de busca)
  - https://openrouter.ai/pricing (oficial; lida em trecho de resultado de busca)
  - https://lilting.ch/en/articles/openrouter-free-models (terceiros; falhas de chamada de ferramentas)

## Como os documentos públicos entram no chatbot e o que o grupo treina?

Critérios usados, vindos do projeto: o professor exige treinar algo (sem treino, não há IA no trabalho); custo zero (NFR-01); o chatbot deve citar a fonte (FR-12) e dizer que não tem conteúdo suficiente quando não achar (FR-11, NFR-08); o treino precisa ser medível (conjunto de teste, métricas); os dados pessoais do aluno nunca entram no treino (NFR-10).

- **Decisão:** buscar nos documentos a cada pergunta (pipeline da Lanna: PDF, texto, trechos, embeddings, RAG) e treinar dois componentes pequenos do próprio grupo: (1) um classificador de tipo de pergunta (geral, pessoal ou fora do escopo, e qual consulta) e (2) um modelo de busca (embeddings) ajustado com perguntas e trechos dos documentos do UniCEUB. A Groq continua só escrevendo a resposta (D-002, decidida em 2026-11-09).
- **Motivo:** treinar o modelo de linguagem para "decorar" os documentos não é viável de graça: a Groq não oferece ajuste fino, e os adaptadores LoRA só rodam no plano Enterprise, então um modelo ajustado não poderia ser servido no plano gratuito. Além disso, um modelo que decorou os documentos não aponta a fonte e tende a inventar, o que vai contra FR-11 e FR-12. Os dois componentes propostos são pequenos, treinam em GPU gratuita em minutos ou horas, rodam em CPU, e dão trabalho de IA medível: criar o conjunto de dados, separar treino e teste, medir acerto.
- **Alternativas:**
  - **Só recuperação, sem treino:** é o mais simples e confiável, mas não atende à exigência do professor.
  - **Ajustar um modelo de linguagem (LoRA) e hospedar por conta própria:** é o "treino" mais literal, mas precisa de GPU para responder, que não há de graça de forma estável, e perde a chamada de ferramentas da Groq. Só vale se o professor exigir esse tipo de treino.
  - **Só o classificador (sem ajustar a busca):** mais fácil, e já é treino medível. É o mínimo aceitável se o tempo apertar.
- **Onde treinar (GPU gratuita):** Kaggle dá cerca de 30 horas de GPU por semana, com cota variável e sessões de 9 a 12 horas. O Google Colab gratuito não publica cota. Para modelos pequenos como os propostos, basta.
- **Modelos de partida:** `multilingual-e5-small` (licença MIT, 118 milhões de parâmetros, 384 dimensões) para a busca, ajustável com a biblioteca sentence-transformers; BERTimbau (licença MIT), um BERT em português, ou scikit-learn para o classificador. Um artigo de 2026 sobre avaliação de embeddings em português indica que o ajuste fino em português ajuda.
- **Onde rodar depois de treinado:** a documentação do Hugging Face Spaces lista o hardware CPU Basic (2 vCPU, 16 GB) como gratuito, mas mensagens em fóruns de 2026 relatam restrições em Spaces gratuitos de CPU, Docker e Gradio. Os dois relatos conflitam. A hospedagem continua uma decisão em aberto (parte da arquitetura).
- **Fontes** (pesquisadas em 2026-11-09):
  - https://console.groq.com/docs/lora (oficial; adaptadores LoRA só no plano Enterprise)
  - Páginas e resultados de busca sobre a cota gratuita de GPU do Kaggle e do Colab (terceiros e documentação; lidos em trechos de resultado de busca)
  - Documentação do Hugging Face Spaces sobre hardware gratuito e mensagens de fórum de 2026 sobre restrições (oficial e fórum; lidos em trechos de resultado de busca)
  - Cartões de modelo de `multilingual-e5-small` e BERTimbau (licenças MIT) e o artigo MTEB-PT 2026 (lidos em trechos de resultado de busca)

## Onde o site e os modelos treinados devem rodar de graça?

Critérios usados, vindos do projeto: custo zero (NFR-01); demonstração ao vivo em sala (NFR-11); resposta em até 15 segundos (NFR-09); nenhum dado de aluno gravado (NFR-10, NFR-05); o servidor precisa carregar o modelo de embeddings (cerca de 118 milhões de parâmetros, o que dá algo como 470 MB em precisão normal, conta minha) e o classificador, e falar com a Groq e com o Espaço Aluno.

- **Decisão:** rodar o site e os modelos no computador de um integrante do grupo durante a demonstração, empacotado em contêiner Docker para poder migrar depois (D-005, decidida em 2026-11-09).
- **Motivo:** custo zero sem cartão, sem sono nem partida lenta no dia da apresentação, e a senha e os dados do aluno passam só por um computador do grupo, não por uma nuvem. Para quatro contas de teste e uma demonstração em sala, não é preciso estar no ar o tempo todo.
- **Alternativas:**
  - **Google Cloud Run:** o plano "sempre grátis" inclui 2 milhões de requisições, 180 mil vCPU-segundos e 360 mil GiB-segundos por mês, o que cobre com folga o uso do grupo (estimativa minha). Mas todo projeto precisa de uma conta de cobrança ligada, e um orçamento com alerta avisa, não corta o gasto. Existe um limite de gasto (spend cap) em prévia pública desde julho de 2026, que também não para o serviço na hora. Serve se o grupo aceitar cadastrar um cartão e vigiar o uso.
  - **Render (plano gratuito):** sem cartão, mas só 512 MB de memória e 0,1 CPU, o serviço dorme após 15 minutos parado e leva cerca de um minuto para acordar. Provavelmente não comporta o modelo de embeddings com folga nem responde em 15 segundos (conclusão minha, a testar). Uma fonte de meados de 2026 cita ainda um plano gratuito de 256 MB limitado a 30 dias, o que conflita com as demais.
  - **Hugging Face Spaces:** a documentação oficial diz que criar um Space com computação (Gradio ou Docker) exige plano pago; só os Static Spaces são grátis, e esses só servem a tela, não rodam os modelos. Mensagens de fórum de 2026 relatam que o CPU Basic gratuito foi restringido por volta de julho. Fora para este uso.
  - **Outras:** Fly.io não tem plano gratuito para contas novas, a Koyeb pede plano pago desde fevereiro de 2026 e o Railway dá só um crédito mensal de US$ 5, não um plano gratuito (segundo uma fonte de outubro de 2026).
- **Fontes** (pesquisadas em 2026-11-09):
  - https://huggingface.co/docs/hub/en/spaces-overview (oficial)
  - https://huggingface.co/docs/hub/main/spaces-gpus (oficial; CPU Basic 2 vCPU e 16 GB)
  - https://discuss.huggingface.co/t/cpu-basic-quota-limit-with-only-one-space/180646 (fórum; restrição de julho de 2026)
  - https://render.com/docs/llms-full.txt (oficial; 512 MB, 0,1 CPU e dorme após 15 minutos)
  - https://jwatte.com/blog/render-com-platform-review/ (terceiros; mudança de plano em 1 de agosto de 2026)
  - https://cloud.google.com/run/pricing (oficial; cota gratuita)
  - https://tech-insider.org/how-to-set-up-google-cloud-run-2026/ (terceiros; conta de cobrança obrigatória)
  - https://cloud.google.com/run/docs/tips/services-cost-optimization (oficial; alerta de orçamento não é limite)
  - https://blog.g-gen.co.jp/entry/spend-cap-budgets-to-prevent-unintended-charges (terceiros; spend cap em prévia pública desde 2026-07-27)
  - https://dev.to/lightcloud/free-rest-api-hosting-mh3 (terceiros; Fly.io, Koyeb e Railway, verificado em 2026-10-13)

## Não verificado

- Se o Cloud Run, depois do crédito inicial de teste, mantém o uso gratuito sem cobrar nada para este caso. Pelas fontes sim, mas é preciso cartão e a conta confirma só no console do Google.
- Se o Espaço Aluno aceita login vindo do IP de um servidor em nuvem; rodar no computador do grupo evita a dúvida. Entra em T-008.
- O tempo de partida do Cloud Run com os modelos carregados. Entra em T-007.
- Oracle Cloud Always Free e outras opções não foram pesquisadas.
- Se a cota de GPU gratuita do Kaggle e do Colab hoje basta para o tempo de treino real do grupo. A cota é variável.
- O que o professor chama de "treinar" e qual tipo de treino conta na nota (ajuste fino de um modelo, classificador, busca ajustada). Só ele pode dizer.
- Quantos exemplos de pergunta o grupo precisa escrever para o classificador e para a busca ter acerto razoável. Depende dos documentos que a Lanna enviar.
- A página oficial da Groq sobre uso e retenção de dados (`console.groq.com/docs/your-data`) não pôde ser aberta nesta sessão. O que se sabe sobre treino e retenção vem de um resumo de terceiros. Convém ler a página antes de usar dados reais.
- Os limites exatos do plano gratuito da Groq, que só aparecem na conta. Se bastam para respostas com várias chamadas de ferramenta, vai para o plano de testes.
- Se há modelo gratuito na Groq com boa chamada de ferramentas e bom português. Vai para o plano de testes.
- Os limites atuais da cota gratuita do Gemini, que também só aparecem dentro do AI Studio.
