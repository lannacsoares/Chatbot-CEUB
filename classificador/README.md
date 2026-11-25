# Classificador (frente C)

Decide o tipo de cada pergunta antes de o chatbot responder. Tarefas 01-03 e 02-03.

## Como escrever as suas perguntas (cada integrante)

Abra `dados/perguntas.csv` e acrescente linhas no fim, no formato:

```
"a pergunta, do jeito que você escreveria",tipo,seu-nome
```

- Escreva perguntas de cada um dos 4 tipos.
- Escreva como você falaria de verdade: formal, gíria, abreviado, sem acento, com erro de digitação, frase curta. Variar é o que faz o modelo aprender.
- **Nunca** coloque nome de pessoa, matrícula ou dado real. Nome de disciplina pode.
- Deixe a pergunta entre aspas.

| Tipo | Quando usar | Exemplo |
|---|---|---|
| `geral` | Regra da faculdade que está nos documentos públicos | qual o limite de faltas? |
| `faltas` | Quantas faltas **você** tem, ou sua frequência | quantas faltas tenho em redes |
| `professor` | Quem é o professor de uma disciplina **sua** | quem dá aula de cálculo pra mim |
| `fora_do_escopo` | Notas, horários, calendário, abrir processo, pedir ação, pergunta sobre outra pessoa, assunto fora da faculdade | qual minha nota em IA? |

Depois rode `python classificador/verificar.py`. Deve terminar com "Sem erros.".

## Passo a passo do treino (frente C)

```
pip install -r classificador/requirements.txt
python classificador/verificar.py   # todos os tipos com "ok"
python classificador/separar.py     # UMA vez; commit de dados/teste.csv
python classificador/treinar.py     # mede no teste e salva models/classificador.joblib
python classificador/classificar.py "quantas faltas eu tenho em cálculo?"
```

## Para a frente D

```python
from classificador.classificar import classificar
tipo, confianca = classificar(pergunta)   # tipo de tipos.py, confiança de 0 a 1
```

Se a confiança fica abaixo de 50%, o tipo devolvido é `fora_do_escopo`, e o chatbot diz que não tem conteúdo suficiente.
