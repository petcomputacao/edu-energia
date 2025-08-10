# Desafio: trabalhando com a classificação dos dados

## Problema

Uma empresa a privada está pensando em analisar a eficiência energética de um
determinado setor da UFCG para ver a viabilidade de colocar placas solares,
então eles escolheram o laboratório do LSD. Porém, para avaliar se o
investimento irá compensar, eles querem toda a classificação dos gastos
energéticos desse laboratório, bem como ver insights de gráficos que demonstram
visualmente como está o uso da energia dentro desse laboratório. Sua missão será
trabalhar com os dados e criar gráficos que ajudem essa empresa a validar seu
investimento.

## Dados fornecidos

| Data e hora      | Medidor     | Tensão (V) | Corrente (A) | Consumo (kWh) | Fator de potência |
|------------------|-------------|------------|--------------|---------------|-------------------|
| 24/06/2024 00:00 | Medidor LSD | 127.98     | 43.88        | 16578.33      | 0.917             |
| 24/06/2024 01:00 | Medidor LSD | 127.70     | 44.04        | 16685.77      | 0.921             |
| 24/06/2024 02:00 | Medidor LSD | 127.79     | 44.23        | 16844.66      | 0.922             |
| 24/06/2024 03:00 | Medidor LSD | 127.93     | 44.36        | 16739.53      | 0.920             |
| 24/06/2024 04:00 | Medidor LSD | 127.93     | 43.91        | 16700.73      | 0.922             |

## Perguntas que você deve ser capaz de responder

1. Quais os tipos de variáveis das colunas?
2. Os valores de consumo são, em sua maioria, baixos, médios ou altos?
3. Como o consumo evoluiu entre os horários?
4. Existe tendência visível entre a corrente o consumo?

## Tarefas

### Parte 1: classificação de variáveis

Classifique cada coluna da tabela como: qualitativa nominal, ordinal,
quantitativa contínua, discreta ou temporal.

### Parte 2: gráfico de variável qualitativa nominal

Construa um gráfico de barras com a quantidade de registros por medidor usando
os dados da tabela. Qual seria a aparência desse gráfico? O que você esperaria
visualizar?

### Parte 3: distribuição de frequência do Consumo

Separe os valores de Consumo (kWh) em 3 faixas (ex: baixa, média, alta) e conte
quantos valores caem em cada grupo.

### Parte 4: série temporal

Usando os dados de Consumo e Data, desenhe um gráfico de linha que mostra a
evolução do consumo ao longo dos horários de 00:00 até 04:00 do dia 24/06/2024.

### Parte 5: diagrama de dispersão (corrente x consumo)

Com os dados da tabela, crie um gráfico de dispersão mostrando a relação entre
Corrente (A) e Consumo (kWh). Existe uma tendência visível? Quando a corrente
aumenta, o consumo também aumenta?
