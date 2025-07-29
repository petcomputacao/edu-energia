#!/bin/bash
pdflatex main.tex
mv main.pdf ../docs/assets/plano-de-curso.pdf
rm main.aux main.log main.out
