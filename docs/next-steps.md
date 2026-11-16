# Próximos passos (depois da v1)

**Projeto:** chatbot-uniceub · **Versão:** 0.1 · **Data:** 2026-11-11

> **Em resumo:** a v1 é um MVP simples, só para a entrega da disciplina (D-008). Tudo o que já estava mapeado e não cabe nela fica aqui, registrado e fora do plano de entrega. Nada desta lista é prometido para a apresentação.

## O que a v1 entrega

- Site com tela de conversa, rodando direto no computador de um integrante.
- Respostas sobre as regras da faculdade, a partir de documentos públicos, com a fonte.
- Consultas pessoais de faltas por matéria, falta agendada e professor, com o login do próprio aluno.
- Classificador de tipo de pergunta (TF-IDF e regressão logística) e ajuste pequeno dos embeddings, com os números de antes e depois.
- Teste com 20 perguntas e 10 fora do escopo.

## O que fica para depois

| Tema | O que é | Vem de |
|---|---|---|
| Docker | Empacotar o servidor e os modelos em contêiner | D-005, D-006 |
| Servidor e nuvem | Hospedagem de verdade, sempre no ar, para vender ao UniCEUB. Exige comparar custo, limites e o tratamento de dados pessoais de novo | D-005, `docs/research.md` |
| Acesso pelo celular | Túnel gratuito ou hospedagem, e tela pensada para o celular | D-005, `docs/wireframes.md` |
| BERTimbau | Classificador maior, comparado com o simples | D-002, D-006, T-005 |
| Notas, horários, calendário | Consultas FR-07, FR-08 e FR-09. O calendário pode vir de documento público em vez do Espaço Aluno | FR-07 a FR-09 |
| Caminho de processo | Orientação de como abrir um processo, sem abrir (FR-06) | FR-06 |
| Pergunta mista | Uma pergunta que usa documentos e Espaço Aluno ao mesmo tempo | `docs/ai-features.md` |
| Teste maior | 40 perguntas nas 8 consultas (NFR-07 completo) | NFR-07 |
| Mais treino | Mais pares de pergunta e trecho, mais documentos, mais exemplos do classificador | NFR-12 |
| Alunos de fora do grupo | Antes disso: autorização da área de TI do UniCEUB, LGPD, e provavelmente outro jeito de entrar que não passe a senha pelo servidor do grupo (extensão de navegador ou API oficial) | NFR-03, D-003 |
| Outros canais | Aplicativo e WhatsApp | `docs/requirements.md` |

## Ordem sugerida quando a v1 estiver entregue

1. Consultas que faltam (notas, horários), por serem as mais pedidas.
2. Docker e hospedagem de teste.
3. BERTimbau e teste de 40 perguntas.
4. Conversa com a TI do UniCEUB, antes de qualquer aluno de fora.
