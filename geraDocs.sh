#!/bin/bash

# Gerando arquivos PDF para os desafios
pandoc desafios/desafio-1.md -o docs/assets/desafio-1.pdf
pandoc desafios/desafio-2.md -o docs/assets/desafio-2.pdf
pandoc desafios/desafio-3.md -o docs/assets/desafio-3.pdf
pandoc desafios/desafio-4.md -o docs/assets/desafio-4.pdf
pandoc desafios/desafio-final.md -o docs/assets/desafio-final.pdf

# Gerando arquivo PDF para o plano de curso
cd plano-de-curso
pdflatex main.tex
cp main.pdf ../docs/assets/plano-de-curso.pdf
