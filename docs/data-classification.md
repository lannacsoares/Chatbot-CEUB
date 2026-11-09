# Classificação dos dados

**Projeto:** chatbot-uniceub · **Versão:** 0.1 · **Data:** 2026-11-09

> **Em resumo:** o chatbot lida com dados pessoais do aluno (login, faltas, notas, horários) só durante a conversa. Nada é guardado depois: os dados são usados na hora e descartados, e o histórico não é mantido. À Groq, que escreve a resposta, vão só a pergunta e os campos necessários, nunca senha, cookie, página inteira nem o motivo de abonos (D-007). O ponto de atenção que resta é o que a Groq faz com o texto recebido, que ainda não foi verificado (T-003).

## De quem são os dados

| De quem | O que passa pelo chatbot | Para que é preciso | Por quanto tempo fica |
|---|---|---|---|
| Aluno (na primeira versão, só as quatro pessoas do grupo) | Matrícula e senha digitadas no login | Entrar no Espaço Aluno | Só o necessário para entrar; não são guardadas (a confirmar na arquitetura) |
| Aluno | Sessão do Espaço Aluno (cookie) | Consultar o Espaço Aluno como aquele aluno | Só durante a conversa; descartada depois |
| Aluno | Faltas, falta agendada, professor, notas, horários lidos do Espaço Aluno | Responder as perguntas pessoais | Usados na hora e descartados depois |
| Aluno | Texto das perguntas e das respostas | Conduzir a conversa | Só durante a conversa; o histórico não é guardado |

## Quão sensível é cada um

| O que passa pelo chatbot | Sensibilidade | O que isso significa aqui |
|---|---|---|
| Matrícula e senha | Comum, mas de alto risco | Dão acesso à conta inteira. Não podem ir para arquivos do projeto, repositório nem logs (NFR-05) |
| Sessão (cookie) | Comum, mas de alto risco | Vale como a senha enquanto não expira. Mesmo cuidado acima |
| Faltas, notas, horários, professor | Dado pessoal comum | Só o próprio aluno vê. Nenhuma resposta traz dados de outra conta (NFR-02) |
| Abonos de falta | A verificar | Se o Espaço Aluno mostrar o motivo de um abono, ele pode revelar dado de saúde, que é sensível. O grupo ainda não conferiu |
| Texto das perguntas | Comum | Pode conter dados pessoais que o aluno digitar |

## Quem pode ver

| Quem | O que vê | Como entra |
|---|---|---|
| O próprio aluno | Os próprios dados, na conversa | Login com a conta do Espaço Aluno |
| Groq (serviço do modelo de IA, D-001) | A pergunta e os campos extraídos do Espaço Aluno que a pergunta precisa (D-007); nunca senha, cookie, página inteira, nome, matrícula nem o motivo de abonos | Chamada feita pelo servidor do grupo. Pelo resumo de terceiros, o plano gratuito não treina com o que se envia; a página oficial sobre retenção não foi lida (T-003) |
| O grupo, durante o desenvolvimento | Só os próprios dados de cada um, nos testes com as contas do grupo | Conta de cada pessoa |

## O que o projeto faz a respeito

- **Coleta:** no login e quando o aluno faz uma pergunta. O aluno é avisado pela tela de aviso de privacidade (ver `docs/wireframes.md`).
- **Apagamento:** nada é guardado depois da conversa; ao terminar ou ao expirar a sessão, os dados deixam de existir no chatbot. Os registros do servidor não guardam texto de perguntas nem de respostas, e nada vai para o disco (D-007, `docs/architecture.md`).
- **Pedido do titular:** como nada é guardado, não há o que entregar nem apagar (dedução, a confirmar quando a arquitetura estiver definida).
- **Vazamento:** ainda não definido.

## A lei

Dados de alunos no Brasil são dados pessoais e entram na Lei Geral de Proteção de Dados (LGPD). O que ela exige deste projeto não foi verificado em detalhe.

## Pontos em aberto

- O que a Groq faz com o texto recebido (retenção e uso). Depende de ler a página oficial dela (T-003).
- Se os abonos de falta mostram o motivo. Depende do grupo conferir no Espaço Aluno.
- O que fazer em caso de vazamento. Depende do grupo.
- O que a LGPD exige deste projeto. Depende do grupo e, se houver venda ao UniCEUB, da TI e do jurídico da faculdade.
