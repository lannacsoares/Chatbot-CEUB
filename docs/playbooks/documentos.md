# Guia da frente B · Documentos

> **Em resumo:** esta frente transforma os PDFs públicos do UniCEUB em uma busca que acha o trecho certo, e ajusta o modelo de embeddings para isso. Entrega o índice e o modelo ajustado para a frente D usar no servidor.

## O que esta função faz

- Converte os PDFs em texto e em trechos com documento e página de origem (01-02).
- Gera os vetores e o índice FAISS, com um limite de semelhança para "sem conteúdo suficiente" (02-01).
- Ajusta o modelo de embeddings com pares de pergunta e trecho e mede antes e depois (02-02, T-004, T-006).

## As tarefas desta função

| Tarefa | Especificação |
|---|---|
| 01-02 Documentos em trechos | `specs/01-02-documentos-em-trechos.md` |
| 02-01 Busca com embeddings prontos | `specs/02-01-busca-com-embeddings-prontos.md` |
| 02-02 Ajuste dos embeddings | `specs/02-02-ajuste-dos-embeddings.md` |

## Antes de começar uma tarefa

1. Leia `.blueprint/state.md` e a especificação da tarefa.
2. Os PDFs são os que a Lanna enviar; use só documentos públicos, sem dado pessoal.
3. Separe os pares de teste antes de treinar e nunca os use para ajustar o modelo.
4. Nenhum dado real de aluno entra no treino (NFR-10). Se usar a Groq para rascunhar perguntas, mande só trechos públicos e revise tudo.

## Quando a tarefa termina

1. Escreva o resultado em "Como testar" da especificação, com os números medidos, e diga ao grupo.
2. Registre a sessão em `.blueprint/journal/sessions/`.
3. Entregue à frente D o arquivo do índice e do modelo e como carregá-los. Avise a frente C se o jeito de medir for útil para o classificador.

## O que esta função não decide

- Trocar o modelo de embeddings de partida, o serviço de treino ou qualquer coisa que gere custo: é da pessoa.
- Cortar o treino: ele é parte fixa do projeto (D-004).
- A meta de acerto da busca, que o grupo combina.
