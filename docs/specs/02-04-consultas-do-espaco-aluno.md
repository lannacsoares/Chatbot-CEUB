# Consultas do Espaço Aluno

**Fase:** 2 · Busca, treino e consultas · **Frente:** A · Espaço Aluno · **Situação:** não iniciada

## O que faz

Transforma o script de 01-01 em um módulo com uma função por consulta, cada uma devolvendo só os campos que a pergunta precisa. Ordem: faltas por matéria, falta agendada e professor da matéria; depois notas, horários e calendário acadêmico (se ele estiver no Espaço Aluno) e o caminho para abrir um processo (um texto de orientação, sem abrir o processo). Detecta quando a sessão expirou.

## O que não faz

- Não faz nenhuma ação no Espaço Aluno, só abre páginas (NFR-04).
- Não lê nem envia o motivo de abonos de falta, nome nem matrícula (D-007).
- Não guarda dados: os campos vivem só na memória durante a conversa (NFR-10).
- Não é usado por alunos de fora do grupo (NFR-03).

## Pronta quando

- [ ] Cada consulta da lista devolve só os campos necessários, e uma consulta que não funcionar está anotada com o motivo.
- [ ] Uma conta do grupo vê só os próprios dados: testado com as quatro contas (NFR-02).
- [ ] Quando a sessão expira, o módulo avisa de um jeito que o servidor pode mostrar ao aluno (FR-13).
- [ ] Quando o layout muda ou um campo não aparece, a consulta diz que não conseguiu ler em vez de inventar um valor.
- [ ] Nada é gravado em disco, em log nem em arquivo do projeto (NFR-05, NFR-10).
- [ ] Está anotado de onde vem o calendário acadêmico (Espaço Aluno ou documento público).

## Vem de

FR-03 a FR-10, FR-13, NFR-02, NFR-04, NFR-05, NFR-10, D-003 e D-007.

## Como testar

A escrever na entrega.

Depende de: 01-01. Se 01-01 mostrar que não dá para entrar no Espaço Aluno, o grupo decide o que fazer com esta tarefa antes de começá-la.
