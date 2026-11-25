# Sessão 2026-11-25 · claude-code

- **Início:** 2026-11-25
- **Ramo:** escopo-mvp-v1

## Pedido

Qual o próximo passo para começar o desenvolvimento. Erick escolheu a frente C (Classificador).

## Feito

- Constatado: nenhuma tarefa começada e as metas do plano (17/11, 22/11, 25/11) já passaram.
- Tarefa 01-03 iniciada: tipos em `classificador/tipos.py`, rascunho de 50 perguntas (10 por tipo, autor `agente`) em `classificador/dados/perguntas.csv`, `verificar.py` (contagens e erros) e `separar.py` (separa ~20% para teste uma única vez, com semente fixa, e congela o teste). A separação foi testada só numa cópia.
- "Como testar" e situação da especificação 01-03 atualizados.

- Tarefa 02-03 adiantada: `treinar.py` (validação cruzada só no treino, medida única no teste, matriz de confusão, salva o modelo), `classificar.py` (entrega para a frente D, limite de confiança de 50% proposto), `README.md` e `requirements.txt`. Testado numa cópia descartável: 60% com o rascunho, sem valor de resultado.
- `docs/perguntas-para-o-grupo.md`: 12 perguntas pendentes, com proposta do agente, para Erick responder com a líder.

- Respostas do grupo registradas (`docs/perguntas-para-o-grupo.md`): frentes no plano, D-008 confirmado, D-009 ("falta agendada" sai; classificador com 4 tipos), 27/11 é entrega parcial. Erick escreve todas as perguntas de exemplo.
- 8 PDFs oficiais baixados do InfoCentral para `documentos/` (com permissão de Erick). 4 têm texto; 4 são imagens escaneadas e precisam de OCR (`documentos/README.md`). O Espaço Aluno não abriu no navegador (página de erro), então nada foi buscado lá.

- Tarefa 01-04 feita no ramo `frente-d-servidor`: servidor FastAPI, tela e cliente da Groq em `servidor/`; T-001, T-002 (escolhido openai/gpt-oss-120b; llama-3.3-70b não existe mais na Groq) e T-003 (em `docs/research.md`). A chave fica na variável de ambiente do usuário, nunca em arquivo.

- PR #3 aberto (servidor). Correções no servidor: chave lida também das variáveis de usuário do Windows; recusa de assuntos fora do UniCEUB; negrito na tela.
- Tarefa 03-02 adiantada: `avaliacao/perguntas_teste.csv` (14 gerais com artigo, 6 pessoais, 10 fora do escopo) e `avaliacao/medir.py`. Medição de "antes": precisão 0/20, honestidade 9/10, tempo 100% (mediana 3,2 s); o modelo inventou em 6 das 14 gerais.
- Aviso para a frente B: o PDF de Normas de TCC sai com as palavras grudadas no pdfplumber.

- Classificador: 60 perguntas novas do agente (100 no total); teste separado e congelado. TF-IDF deu 75%. A pedido de Erick, o BERTimbau entrou (D-010): BERTimbau + regressão foi escolhido por validação cruzada e deu 90% no teste (fora do escopo reconhecido: 80%, meta 90%).
- A comparação foi encerrada pelo Claude Code por falta de memória, mas depois de salvar o modelo.

## Em aberto

- Ligar a retenção zero na conta da Groq antes de dados reais (recomendado; Erick confirma).

- Faltam 10 perguntas por tipo, escritas pelas quatro pessoas, antes de separar o teste.
- Data da apresentação final; refazer as metas do plano.
- OCR dos 4 PDFs escaneados ou deixá-los fora da v1 (frente B).
- Quem leva as frentes A, B e D, a data da apresentação e o novo cronograma.
