#!/bin/bash

# Verifica se foi fornecido um arquivo de entrada
if [ $# -eq 0 ]; then
  echo "Erro: Nenhum arquivo especificado."
  echo "Uso: $0 <arquivo.md>"
  exit 1
fi

# Caminho completo do arquivo de entrada
input_file="$1"

# Verifica se o arquivo existe
if [ ! -f "$input_file" ]; then
  echo "Erro: Arquivo '$input_file' não encontrado."
  exit 1
fi

# Extrai nome base (sem extensão)
base_name=$(basename "$input_file" .md)

# Verifica se os arquivos de suporte existem no diretório atual
if [ ! -f "template.tex" ] || [ ! -f "metadata.yaml" ]; then
  echo "Erro: Arquivos template.tex ou metadata.yaml não encontrados no diretório atual."
  exit 1
fi

# Diretório de destino para os PDFs
target_dir="../docs/assets/"

# Cria o diretório de destino se não existir
mkdir -p "$target_dir"

# Executa o pandoc no diretório atual
pandoc "$input_file" \
  --metadata-file="metadata.yaml" \
  --template="template.tex" \
  -o "$target_dir/$base_name.pdf"

echo "Arquivo $target_dir$base_name.pdf gerado com sucesso!"
