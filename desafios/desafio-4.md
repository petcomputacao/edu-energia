# Desafio: consumo de energia em blocos da universidade

## Problema

O **SmartusCampus UFCG** está investigando disparidades no consumo mensal de
energia elétrica (em kWh) entre os blocos SPLAB e LSD. O objetivo é identificar
padrões de consumo e tomar medidas a respeito. Você foi contratado(a) como
analista de dados para realizar uma análise comparativa.

## Dados fornecidos

Foram fornecidas amostras de consumo de todos os blocos, com informações de
identificação do medidor, dia da medição e valor da potência ativa, dentre
outros dados irrelevantes para a análise.

Estes dados constam no arquivo `.csv` disponibilizado.

## Perguntas que você deve ser capaz de responder

1. Qual a média, mediana e moda de consumo dos blocos?
2. Qual a amplitude total, desvio padrão e coeficiente de variação dos
conjuntos?
3. Um consumo de 17017 kWh é atípico?
4. Qual dos blocos tem a maior dispersão? E a menor?

## Tarefa

### Parte 1: medidas de tendência central

Calcule, para cada bloco:

- Média aritmética do consumo (kW/h)
- Mediana do consumo (kW/h)
- Moda do consumo (se aplicável) (kW/h)

### Parte 2: medidas de variabilidade

Calcule, para cada conjunto:

- Amplitude total
- Desvio padrão
- Coeficiente de variação

### Parte 3: medidas de posição

Para o bloco LSD:

- Calcule os quadris 1 (25º percentil) e 3 (75º percentil)
- Determine o escore-z para uma hora em que foi consumido 17017 kWh
- Determine se este consumo de 17017 kWh é atípico no bloco

### Parte 4: Construção de boxplots

Crie boxplots comparativos que identifiquem outliers e determine qual bloco tem
a maior dispersão.

### Parte 5: análise gráfica complementar

Gere gráficos complementares para ambos os blocos e compare-os.
