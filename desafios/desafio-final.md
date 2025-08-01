# Desafio final: consumo de energia em bairros residenciais

## Contexto

Você é analista de dados da universidade, responsável por monitorar e otimizar
o consumo de energia nos diferentes blocos do campus. Recentemente, a reitoria
solicitou um relatório detalhado sobre os padrões de consumo para identificar
possíveis desperdícios, horários de pico e oportunidades de economia.

Seu desafio é analisar os dados de consumo de energia dos últimos meses e
responder às perguntas que se seguem.

## Dados fornecidos

Colunas:

- `Medidor` (identificação do bloco)
- `Data_hora` (data e hora da medição, em intervalos de 1 hora)
- `Potencia_ativa` (em kW)
- `Potencia_reativa` (em kVAR)
- `Fator_potencia` (adimensional)
- `Corrente_fase_a` (em A)
- `Corrente_fase_b` (em A)
- `Corrente_fase_c` (em A)

Estes dados constam no arquivo `dados.csv` disponibilizado no site do minicurso.

## Tarefas

### Parte 1: carregamento e limpeza dos dados

- Importe os dados usando `pandas`
- Verifique e trate valores ausentes ou inconsistentes
- Converta a coluna `hora` para o tipo `datetime`
- Converta as colunas numéricas para o tipo `float`

### Parte 2: análise exploratória básica

- Calcule estatísticas descritivas (média, mediana, desvio padrão) para cada
variável numérica
- Compare o consumo médio de energia (potência ativa) entre os diferentes blocos

### Parte 3: identificação de padrões temporais

- Crie um gráfico de linha (usando `matplotlib`) mostrando a variação da
potência ativa ao longo do tempo para um bloco específico
- Identifique os horários de pico de consumo em um dia típico (agregue os dados
por hora)

### Parte 4: análise de fator de potência

- O fator de potência indica e eficiência do uso de energia. Valores abaixo de
0,92 podem indicar desperdício
- Plote um histograma do fator de potência e identifique se há blocos com baixa
eficiência

### Parte 5: correlação entre variáveis

- Verifique se há correlação entre a potência ativa e a corrente (calcular para
cada fase) usando um gráfico de dispersão

### Parte 6: relatório final

Sintetize suas descobertas, destacando:

- Qual bloco tem o maior consumo médio?
- Em quais horários ocorrem picos de demanda?
- Há blocos com fator de potência preocupante?
