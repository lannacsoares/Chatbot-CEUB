# Guia da frente A · Espaço Aluno

> **Em resumo:** esta frente cuida de entrar no Espaço Aluno com a conta do aluno e ler as páginas, devolvendo só os campos que a pergunta precisa. Entrega o módulo de consultas para a frente D juntar ao servidor. É a frente do maior risco do projeto: se não der para entrar, o grupo decide o rumo.

## O que esta função faz

- Faz o login no Espaço Aluno e mantém a sessão só na memória (D-003).
- Lê as páginas a partir do `/Painel` e extrai só os campos necessários (D-007).
- Detecta sessão expirada e leitura que falhou, sem inventar valor (FR-13).
- Descobre e anota o que bloqueia o login (captcha, verificação em dois passos) e quanto dura a sessão (T-008).

## As tarefas desta função

| Tarefa | Especificação |
|---|---|
| 01-01 Login e leitura do Espaço Aluno | `specs/01-01-login-e-leitura-do-espaco-aluno.md` |
| 02-04 Consultas do Espaço Aluno | `specs/02-04-consultas-do-espaco-aluno.md` |

## Antes de começar uma tarefa

1. Leia `.blueprint/state.md` e a especificação da tarefa.
2. Leia `docs/data-classification.md` e `docs/architecture.md` (quais dados saem do computador e para onde).
3. Use só a conta de um integrante do grupo, e só com a pessoa presente. Senha e cookie ficam em variável de ambiente ou digitados na hora, nunca em arquivo, repositório, log nem saída de teste (NFR-05).
4. O código só abre páginas: nada de enviar formulário que mude algo no Espaço Aluno (NFR-04).

## Quando a tarefa termina

1. Escreva o resultado em "Como testar" da especificação e diga ao grupo.
2. Registre a sessão em `.blueprint/journal/sessions/`.
3. Entregue o módulo à frente D (servidor), que o liga ao fluxo em 03-01, e avise o que cada consulta devolve e quando falha.
4. Se 01-01 mostrar que não dá para entrar no Espaço Aluno, diga ao grupo logo: o plano precisa de uma decisão antes de 02-04.

## O que esta função não decide

- O que fazer se o login for inviável: é do grupo.
- O que vai para a Groq: está em D-007; mudar isso é decisão da pessoa.
- Acesso de alunos de fora do grupo, ou falar com a TI do UniCEUB.
