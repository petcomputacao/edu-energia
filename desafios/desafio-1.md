# Desafio: análise do consumo de energia em domicílios brasileiros

## Problema

Você foi contratado como analista de dados para estudar o consumo de energia
elétrica em domicílios brasileiros. O objetivo é identificar padrões, calcular
estatísticas básicas e gerar visualizações que ajudem a entender o consumo médio
para cada região do país.

## Dados fornecidos

Foram fornecidos os seguintes dados:

- Norte: 120, 150, 90, 110, 130
- Nordeste: 140, 160, 100, 120, 180
- Sudeste: 200, 220, 180, 210, 240
- Sul: 160, 170, 150, 140, 190
- Centro-oeste: 130, 140, 120, 110, 160

Os valores estão em kWh/mês.

## Perguntas que você deve ser capaz de responder

1. Quais as médias de consumo das regiões?
2. Qual o menor e maior valor?
3. Os valores variam muito entre si?
4. O consumo segue algum padrão entre as regiões?

## Tarefas

### Parte 1: cálculo de estatísticas básicas

Para cada região, determine:

1. Média de consumo
2. Maior e menor valor
3. Se o consumo médio é acima de 150 kWh/mês

### Parte 2: função de classificação

Crie uma função que recebe uma região como parâmetro e retorna:

1. "ALTO" se a média for > 170 kWh
2. "MODERADO" se entre 130 e 170 kWh
3. "BAIXO" se < 130 kWh

### Parte 3: aplicação da função a todas as regiões

Aplique a função acima para todas as regiões e salve o resultado em um
dicionário.

### Parte 4: visualização

Gere um gráfico de barras mostrando:

1. Média de consumo por região
2. Barras coloridas conforme classificação (ALTO, MODERADO, BAIXO)
