<!-- blueprint:start -->
## Blueprint

Chatbot do UniCEUB, feito em grupo para a matéria de Inteligência Artificial: em um site, o aluno tira dúvidas sobre as regras da faculdade (documentos públicos) e sobre a própria situação no Espaço Aluno (faltas, professores, notas, horários), e o chatbot só responde e orienta, sem executar ações.

| O quê | Onde |
|---|---|
| Os documentos | `docs/` |
| O plano e uma especificação por tarefa | `docs/plan.md`, `docs/specs/` |
| Onde o projeto está, para qualquer sessão | `.blueprint/state.md` |
| As decisões, cada uma com o motivo | `docs/decisions.md` |
| O que falta verificar | `docs/test-plan.md` |
| Um guia por função (as quatro frentes) | `docs/playbooks/` |
| O diário: um registro por sessão e os marcos | `.blueprint/journal/` |

### Como trabalhar aqui

1. **Leia `.blueprint/state.md` antes de responder.** Ele diz onde o projeto está. Nunca aja como se lembrasse de uma conversa: pode ter sido outra sessão, outro dia ou outro agente.
2. **Uma tarefa por vez, a partir do plano, em ordem.** A especificação da tarefa diz o que ela faz, o que não faz e quando está pronta. **Diga em qual tarefa está, pelo número e pelo nome, antes de começá-la**, para a pessoa saber qual você escolheu sem reler o plano.
3. **Toda entrega diz como testar:** o que rodar ou abrir, e o que deve aparecer. Isso vai em "Como testar" da especificação e no que você diz à pessoa.
4. **Registre o que aconteceu.** No fim da sessão, um registro em `.blueprint/journal/sessions/`. Uma decisão cara de desfazer vai para `docs/decisions.md`, com o motivo, quem decidiu e a data. Uma fase entregue vai para os marcos.
5. **Uma mudança que o plano não cobre.** Se for pequena, faça e diga em uma linha o que fez. Pequena é: mexe em uma parte do código, não traz decisão cara de desfazer, não traz fato novo sobre o projeto (a primeira tela, o primeiro dado guardado, o primeiro dado pessoal, o primeiro comando, a primeira chamada a um modelo) e cabe em uma tarefa. Se não for pequena, escreva a especificação com a pessoa antes de escrever código.
6. **Uma decisão cara de desfazer é da pessoa:** a stack, a hospedagem, o tratamento dos dados pessoais, qualquer coisa que gere custo. Traga opções e uma recomendação, e espere.
7. **Nunca escreva uma chave, um token ou uma senha** em arquivo deste projeto. Isso vale em especial para a senha e o cookie do Espaço Aluno e para a chave da Groq: nada disso vai para arquivo, repositório, log nem saída de teste.

### Regras deste projeto

- Tudo precisa ser gratuito (NFR-01).
- O chatbot só lê: nenhuma ação no Espaço Aluno (NFR-04).
- Só as contas do grupo (Lanna, Sofia, Geovanna e Erick) são usadas nos testes (NFR-03).
- Dados do Espaço Aluno vivem só na memória, durante a conversa, e só os campos necessários vão à Groq (NFR-10, D-007).
- Nenhum dado real de aluno entra no treino dos modelos (NFR-10).

### O método

Os documentos e o plano deste projeto foram escritos com o Blueprint, e as regras acima vêm dele. Este arquivo, os documentos e o plano bastam para continuar.
<!-- blueprint:end -->
