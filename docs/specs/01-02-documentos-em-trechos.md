# Documentos em trechos

**Fase:** 1 · Provas e base · **Frente:** B · Documentos · **Situação:** não iniciada

## O que faz

Converte os PDFs públicos do UniCEUB (regulamentos, regras, informativos) em texto com pdfplumber e quebra o texto em trechos. Cada trecho guarda de qual documento e de qual página veio. O resultado fica em um arquivo local, pronto para a busca.

## O que não faz

- Não gera embeddings nem índice (02-01).
- Não inclui nenhum dado pessoal: só documentos públicos.
- Não baixa documentos sozinho da internet; os PDFs são os que a Lanna enviar.

## Pronta quando

- [ ] Todos os PDFs enviados foram convertidos em texto.
- [ ] Cada trecho tem o nome do documento e a página.
- [ ] O tamanho dos trechos foi escolhido e anotado com o motivo (trechos curtos demais perdem contexto, longos demais misturam assuntos).
- [ ] Uma amostra de trechos foi conferida à mão: o texto sai sem lixo (cabeçalhos repetidos, tabelas quebradas); o que não saiu bem está anotado.
- [ ] Os PDFs e o arquivo de trechos estão na pasta do projeto, sem nada pessoal.

## Vem de

FR-02, FR-12, D-002 e D-006.

## Como testar

A escrever na entrega.

Depende de: a Lanna enviar os PDFs.
