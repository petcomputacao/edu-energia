# Educação em dados de energia

## Sobre o minicurso

O objetivo deste minicurso é capacitar os participantes a coletar, classificar,
visualizar e analisar dados de consumo de energia elétrica do SmartCampus UFCG,
permitindo um ferramental base para intervir sobre a realidade. Para cumprir
esse objetivo, fornecemos um ambiente de teoria e prática em conceitos de,
especialmente, computação, eletricidade e estatística. Nesse sentido, utilizamos
a metodologia do ensino baseado em problemas (PBL, na sigla em inglês) para
criar um ambiente imersivo e o mais próximo possível de situações reais.

Para acessar a página do curso, acesse [este link](https://petcomputacao.github.io/edu-energia/).

## Como manter

O repositório deste minicurso está dividido em:

- `docs`, diretório onde ficam os arquivos do Github Pages;
- `documentos`, diretório onde ficam os arquivos Markdown geradores dos
documentos do minicurso e o script Bash que os gera;
- `resolucoes`, diretório onde ficam as soluções-modelo dos desafios do
minicurso;
- `bibliografia.md`, arquivo onde estão as referências de materiais usados para
estudo e elaboração do minicurso.

Portanto, para atualizar os documentos do minicurso (plano de curso, roadmap,
dicionário de dados e desafios), é necessário:

1. Editar os arquivos Markdown do diretório `documentos`;
2. Executar o script bash `geraDocs.sh <nome_do_arquivo.md>`, para que o arquivo
seja convertido em formato PDF e movido para `docs/assets/`.

Para executar esses passos, você deve ter as seguintes ferramentas no seu
ambiente:

- LaTeX;
- Pandoc.
