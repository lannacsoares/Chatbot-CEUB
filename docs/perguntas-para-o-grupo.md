# Perguntas para o grupo

**Data:** 2026-11-25 · **Para:** Erick e a líder responderem juntos

> **Em resumo:** 12 perguntas que estão travando ou vão travar o projeto, da mais urgente para a menos urgente. Cada uma traz uma proposta do agente: se concordarem, marquem "ok"; se não, escrevam a resposta. As respostas voltam para o plano, os requisitos e as decisões.

## Bloco 1 · Destrava o trabalho hoje

**1. Quem leva cada frente?** Erick já leva a C (Classificador).

| Frente             | O que faz                                                 | Quem           |
| ------------------ | --------------------------------------------------------- | -------------- |
| A · Espaço Aluno | Login e leitura das faltas e do professor (o maior risco) | Lanna          |
| B · Documentos    | PDFs, trechos, busca e ajuste dos embeddings              | Sophia/Lanna   |
| C · Classificador | Perguntas de exemplo e treino do classificador            | Erick          |
| D · Servidor      | Servidor, tela, Groq e juntar tudo                        | Geovanna/Erick |

**2. Qual a data da apresentação, e quais entregas semanais ainda faltam?**
As metas do plano (17/11, 22/11 e 25/11) já passaram e nenhuma tarefa estava começada. Com a data, o plano é refeito.
Resposta: 27/11

**3. O escopo menor da v1 (D-008) está confirmado?**
Na v1 entram três consultas pessoais (faltas, falta agendada e professor) e o classificador simples (TF-IDF). Ficam de fora Docker, nuvem, BERTimbau, notas, horários, calendário e caminho de processo. Proposta: confirmar e juntar o ramo `escopo-mvp-v1` à `main`.
Resposta: (X ) ok ( ) muda:

**4. Quais documentos públicos entram, e quando chegam os PDFs?**
Proposta: 3 a 5 documentos que respondam às perguntas mais comuns (regulamento acadêmico, regras de frequência e abono, manual do aluno). A frente B não começa sem eles.
Resposta: usa o claude in chrome e busca esses docs no meu espaço aluno e na web

**5. Até quando cada pessoa escreve as suas perguntas de exemplo?**
Cada pessoa escreve cerca de 3 perguntas por tipo, 15 no total, do jeito que fala de verdade, sem nome nem dado real. As instruções estão em `classificador/README.md`. Proposta: até 27/11. Só depois disso dá para separar o teste e treinar.
Resposta: eu escrevo todas

## Bloco 2 · Metas e regras do chatbot

**6. Meta de acerto do classificador.** Precisa ser combinada antes do treino (02-03).
Proposta: pelo menos 80% de acerto geral no conjunto de teste e pelo menos 90% das perguntas fora do escopo reconhecidas como tal.
Resposta: (X ) ok ( ) muda:

**7. Metas do chatbot completo (NFR-07 a NFR-09).**
Proposta: acerta pelo menos 80% de 20 perguntas de teste; admite não saber em pelo menos 90% de 10 perguntas fora do escopo; responde em até 15 segundos em pelo menos 90% dos casos.
Resposta: (X ) ok ( ) muda:

**8. O que fazer quando o classificador está em dúvida?**
Proposta: se a confiança no tipo escolhido for menor que 50%, tratar como fora do escopo, ou seja, o chatbot diz que não tem conteúdo suficiente. Ele erra para o lado de não inventar.
Resposta: (X ) ok ( ) muda:

**9. O que é "falta agendada" no Espaço Aluno?**
Hoje as perguntas de exemplo supõem que é uma falta já lançada para uma data futura. Se for outra coisa, as perguntas desse tipo mudam.
Resposta: não sabemos do que se refere, acho que não existe isso

## Bloco 3 · Pode esperar alguns dias

**10. Os abonos de falta mostram o motivo, por exemplo um atestado médico?**
Se mostrarem, isso é dado de saúde e o chatbot não deve ler nem enviar à Groq. Alguém confere na própria conta.
Resposta: não

**11. Na demonstração, em qual computador o chatbot roda?**
Na v1 a turma vê só a tela desse computador.
Resposta: no meu

**12. Perguntas para o professor** (a líder leva):

- O que ele aceita como "treino": um classificador treinado pelo grupo e o ajuste dos embeddings bastam? Resposta: sim
- O que ele quis dizer com "tokens do login"? O Espaço Aluno usa sessão por cookie, não token.

Resposta:
