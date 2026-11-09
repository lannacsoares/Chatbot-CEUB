# Descrição do sistema

**Projeto:** chatbot-uniceub · **Versão:** 0.1 · **Data:** 2026-11-06

> **Em resumo:** chatbot em site que responde dúvidas de alunos do UniCEUB a partir de documentos públicos da instituição e, com o login do aluno, de dados do Espaço Aluno (faltas, professores, caminho de processos). Só responde e orienta, não executa ações. Trabalho da matéria de Inteligência Artificial, feito por um grupo de quatro pessoas. Na primeira versão, só os logins do próprio grupo são usados.

## O que é

Um chatbot para alunos do UniCEUB tirarem dúvidas em linguagem natural. Ele responde de duas fontes: documentos públicos da instituição (regulamentações, regras, informativos) e as informações pessoais do aluno no Espaço Aluno, consultadas com o login do próprio aluno.

O chatbot apenas responde e orienta. Quem faz qualquer ação no Espaço Aluno, como abrir um processo, é o aluno.

## Problema e valor

- **O problema:** o aluno tem dúvidas sobre as regras da faculdade e sobre a própria situação no Espaço Aluno, como faltas, professor de cada matéria e o caminho para abrir um processo.
- **Quem tem:** alunos do UniCEUB.
- **Como é resolvido hoje:** ainda não informado.
- **O que muda com o produto:** o aluno pergunta em linguagem natural e recebe a resposta, ou o caminho a seguir no Espaço Aluno.

## Quem usa

| Quem | O que precisa |
|---|---|
| Aluno do UniCEUB | Tirar dúvidas sobre regras da faculdade e sobre as próprias informações no Espaço Aluno |

Na primeira versão, os alunos que usam são apenas as quatro pessoas do grupo (Lanna, Sofia, Geovanna e Erick).

## Objetivos e sucesso

1. Entregar o trabalho da matéria de Inteligência Artificial.
2. Futuramente, se der certo, vender o chatbot ao UniCEUB.

**Como saberemos que deu certo:** ainda não definido. É uma pergunta da etapa de requisitos.

## Como chega às pessoas

Um site. Onde ele roda ainda não foi decidido; isso entra na etapa de arquitetura.

## Escopo

- **Na primeira versão:**
  - responder dúvidas gerais a partir de documentos públicos da instituição;
  - responder dúvidas pessoais lendo o Espaço Aluno do aluno que fez login: se há falta agendada, quem é o professor de uma matéria, quantas faltas há em uma matéria, qual o caminho para abrir um processo, notas, horários e calendário acadêmico (de onde vem cada informação ainda será definido).
- **Fora da primeira versão:**
  - executar ações no Espaço Aluno (o chatbot só responde e orienta);
  - uso por alunos de fora do grupo;
  - aplicativo ou WhatsApp.
- **Depois:** vender ao UniCEUB, se o trabalho der certo.

## Limites e contexto

- **Limites declarados:**
  - projeto da matéria de Inteligência Artificial, feito em grupo de quatro pessoas;
  - o professor concordou com o uso do login do aluno no site do UniCEUB para consultar o Espaço Aluno;
  - no início, só os logins do grupo;
  - verba e prazo ainda não informados (perguntas da etapa de requisitos).
- **Sistemas a conectar:** Espaço Aluno (`ea.uniceub.br`) e os documentos públicos do UniCEUB. Pelo que o grupo viu, o Espaço Aluno é feito em ASP.NET MVC, entrega as páginas como HTML pronto e guarda o login como sessão por cookie (`ASP.NET_SessionId`), sem token no armazenamento do navegador.
- **Decidido pelo agente:** nada.

## Pontos em aberto

| Nº | Ponto | Depende de |
|---|---|---|
| 1 | O professor falou em "tokens", mas o Espaço Aluno parece usar sessão por cookie. Confirmar o que ele tinha em mente | O grupo, com o professor |
| 2 | A TI do UniCEUB sabe e autoriza o uso do login para consultar o Espaço Aluno? Fica mais urgente antes de abrir para outros alunos e, se houver venda, é provável que a leitura de páginas dê lugar a uma integração oficial (dedução) | O grupo, com a TI do UniCEUB |
| 3 | Existe API oficial do UniCEUB? | O grupo, com a TI do UniCEUB |
| 4 | Como obter e guardar a sessão do aluno, que expira | Decisão da etapa de arquitetura |
