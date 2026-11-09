# Busca com embeddings prontos

**Fase:** 2 · Busca, treino e consultas · **Frente:** B · Documentos · **Situação:** não iniciada

## O que faz

Gera os vetores dos trechos com um modelo de embeddings pronto (`multilingual-e5-small`), guarda os vetores em um índice FAISS em arquivo e, dada uma pergunta, devolve os trechos mais parecidos com o documento e a página de origem. Define um limite de semelhança abaixo do qual a busca diz que não achou nada. Esta é a linha de base: os números daqui serão comparados com os do modelo ajustado (02-02).

## O que não faz

- Não ajusta o modelo (02-02).
- Não escreve a resposta; só devolve os trechos.
- Não classifica o tipo da pergunta (02-03).

## Pronta quando

- [ ] O índice é gerado a partir dos trechos de 01-02 e salvo em arquivo.
- [ ] Uma pergunta devolve os 5 trechos mais parecidos, cada um com documento e página.
- [ ] O limite de semelhança foi escolhido olhando exemplos de perguntas com e sem resposta nos documentos, e o valor e o motivo estão anotados.
- [ ] Os resultados com o modelo pronto foram guardados como linha de base: quantas vezes o trecho certo aparece entre os 5 primeiros, em um conjunto de perguntas conferidas à mão.
- [ ] O tempo de busca por pergunta foi medido em CPU.

## Vem de

FR-02, FR-11, FR-12, NFR-09, D-002 e D-006.

## Como testar

A escrever na entrega.

Depende de: 01-02.
