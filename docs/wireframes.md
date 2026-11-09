# Telas

**Projeto:** chatbot-uniceub · **Versão:** 0.1 · **Data:** 2026-11-09

> **Em resumo:** a primeira versão tem três telas, abertas por alunos em um site: login com a conta do Espaço Aluno, conversa e aviso de privacidade. Os esboços dizem o que há em cada tela e em que ordem, não como ela fica visualmente.

## As telas

| Tela | Quem vê | O que faz ali | Jornada |
|---|---|---|---|
| Login | Aluno | Entra com a conta do Espaço Aluno | UC-01 |
| Conversa | Aluno | Faz perguntas e lê as respostas | UC-01, UC-02 |
| Aviso de privacidade | Aluno | Lê como os dados são tratados | UC-01 |

**Aberto em:** ainda não informado. Proposta do agente: computador e celular.

## Login

A forma exata desta tela depende da decisão de arquitetura sobre como o chatbot obtém a sessão do aluno.

```
+------------------------------------------+
|  Chatbot UniCEUB                         |
|                                          |
|  Entre com a sua conta do Espaço Aluno   |
|                                          |
|  Matrícula  [______________________]     |
|  Senha      [______________________]     |
|                                          |
|  [ Entrar ]                              |
|                                          |
|  Como seus dados são tratados  (link)    |
+------------------------------------------+
```

| O que há nela | O que faz |
|---|---|
| Matrícula e senha | Campos de digitação |
| Entrar | Tenta o login; se aceito, vai para a Conversa |
| Como seus dados são tratados | Abre o Aviso de privacidade |

**Quando não há nada para mostrar:** não se aplica.
**Quando algo dá errado:** se o login não for aceito, mostra "Não foi possível entrar. Confira a matrícula e a senha e tente de novo", sem apagar a matrícula digitada.

## Conversa

```
+--------------------------------------------+
|  Chatbot UniCEUB          [Nova conversa] [Sair] |
|--------------------------------------------|
|  Chatbot: Olá! Pergunte sobre as regras    |
|  da faculdade ou sobre as suas faltas,     |
|  notas e horários.                         |
|                                            |
|  Você: Quantas faltas tenho em IA?         |
|                                            |
|  Chatbot: Você tem ... faltas em ...       |
|                                            |
|--------------------------------------------|
|  [ Digite sua pergunta...        ] [Enviar]|
+--------------------------------------------+
```

| O que há nela | O que faz |
|---|---|
| Mensagens | Mostram a conversa, de cima para baixo. Nas respostas gerais, aparece o documento de origem (FR-12) |
| Campo de pergunta e Enviar | Envia a pergunta e mostra a resposta na conversa |
| Nova conversa | Limpa a conversa e começa do zero |
| Sair | Encerra a sessão e volta para o Login |

**Quando não há nada para mostrar:** a conversa vazia mostra a saudação, com exemplos de perguntas.
**Quando algo dá errado:** se o chatbot não tiver conteúdo suficiente, ele diz isso na conversa (UC-02). Se a sessão expirar, avisa e leva ao Login (FR-13). Se o Espaço Aluno não responder, diz que não conseguiu consultar agora.

## Aviso de privacidade

O texto abaixo é uma proposta do agente e vale só se a arquitetura confirmar o que ele diz.

```
+------------------------------------------+
|  Como seus dados são tratados            |
|                                          |
|  - O chatbot consulta o Espaço Aluno     |
|    só com a sua conta e só para          |
|    responder às suas perguntas.          |
|  - Sua senha não é guardada.             |
|  - As conversas não são guardadas.       |
|  - O chatbot só lê, não faz nada no      |
|    Espaço Aluno por você.                |
|                                          |
|  [ Voltar ]                              |
+------------------------------------------+
```

| O que há nela | O que faz |
|---|---|
| Texto | Informa o que é lido e o que não é guardado |
| Voltar | Volta para a tela de onde o aluno veio |

**Quando não há nada para mostrar:** não se aplica.
**Quando algo dá errado:** não se aplica.

## Como o aluno passa de uma tela para outra

```
Login --[entrou]--> Conversa
Login --[abriu o aviso]--> Aviso de privacidade --[voltou]--> Login
Conversa --[Sair, ou sessão expirou]--> Login
Conversa --[Nova conversa]--> Conversa vazia
```

## O que ficou de fora

- Tela de histórico de conversas: o histórico não é guardado.
- Tela de administração: não há outro tipo de usuário.
- Tela de configurações: não foi pedida.
- Os botões Nova conversa e Sair foram sugeridos pelo agente.
