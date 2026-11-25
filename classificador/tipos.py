"""Tipos de pergunta da v1 (tarefa 01-03, D-008, D-009).

Este é o único lugar onde os tipos são definidos. O classificador (02-03),
o servidor (03-01) e os scripts de dados leem daqui.
"""

TIPOS = {
    "geral": (
        "Regras e informações da faculdade que estão nos documentos públicos "
        "do UniCEUB (regulamentos, normas, informativos). Ex.: 'qual o limite "
        "de faltas por disciplina?'"
    ),
    "faltas": (
        "Quantas faltas o próprio aluno tem, ou o percentual de frequência, "
        "em uma disciplina ou no geral. Lido do Espaço Aluno."
    ),
    "professor": (
        "Quem é o professor de uma disciplina do próprio aluno. "
        "Lido do Espaço Aluno."
    ),
    "fora_do_escopo": (
        "Tudo o que a v1 não responde: assuntos fora da faculdade; notas, "
        "horários, calendário, caminho de processo e 'falta agendada' (ficaram para depois da "
        "v1, D-008, D-009); pedidos de ação no Espaço Aluno (NFR-04); e perguntas "
        "sobre a situação de outra pessoa."
    ),
}

NOMES = list(TIPOS)
