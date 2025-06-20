#!/bin/bash
pdflatex main.tex
mv main.pdf plano-de-curso.pdf
rm main.aux main.log main.out
