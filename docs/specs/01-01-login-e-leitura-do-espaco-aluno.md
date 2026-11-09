# Login e leitura do Espaço Aluno

**Fase:** 1 · Provas e base · **Frente:** A · Espaço Aluno · **Situação:** não iniciada

## O que faz

Um script em Python que entra no Espaço Aluno (ea.uniceub.br) com a conta de um integrante do grupo, chega ao `/Painel`, abre a página de uma disciplina e mostra os campos de faltas e professor extraídos da página. Também anota o que o login exige (captcha, verificação em dois passos) e por quanto tempo a sessão dura.

## O que não faz

- Não lê notas, horários, calendário nem falta agendada (02-04).
- Não guarda senha nem cookie em lugar nenhum: usuário e senha são digitados na hora ou vêm de variáveis de ambiente.
- Não faz nenhuma ação no Espaço Aluno, só abre páginas (NFR-04).
- Não faz parte do servidor ainda (01-04 e 03-01).

## Pronta quando

- [ ] Entra com a conta de um integrante sem usar nenhum cookie copiado do navegador.
- [ ] Anota se há captcha ou verificação em dois passos e quanto tempo a sessão dura.
- [ ] Mostra, de uma disciplina real, o número de faltas, o percentual e o professor.
- [ ] Navega a partir do `/Painel`, sem usar endereços copiados com parâmetros codificados.
- [ ] Nenhuma senha ou cookie aparece em arquivo, repositório, saída do terminal ou log.
- [ ] O resultado (deu certo, deu certo com ressalvas, não dá) está escrito para o grupo decidir o rumo da frente.

## Vem de

FR-03, FR-05, FR-10, NFR-04, NFR-05, D-003, D-007 e T-008.

## Como testar

A escrever na entrega.
