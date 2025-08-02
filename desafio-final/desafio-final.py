import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    """Carrega os dados do arquivo CSV"""
    return pd.read_csv('dados.csv', delimiter=';', quotechar='"')

def clean_data(df):
    """Limpa os dados"""
    df['Data_hora'] = pd.to_datetime(df['Data_hora'], dayfirst=True, format='%d/%m/%Y, %H:%M:%S')
    # Converte colunas numéricas que podem ter vírgula como separador decimal
    numeric_cols = ['Potencia_ativa', 'Potencia_reativa', 'Fator_potencia', 
                   'Corrente_fase_a', 'Corrente_fase_b', 'Corrente_fase_c']
    for col in numeric_cols:
        df[col] = df[col].astype(str).str.replace(',', '.').astype(float)
    df = df.dropna()
    return df

def save_to_file(filename, content, mode='a'):
    """Salva conteúdo em um arquivo"""
    with open(filename, mode, encoding='utf-8') as f:
        f.write(content + '\n')

def calculate_basic_stats(df, filename):
    """Calcula estatísticas descritivas básicas"""
    numeric_cols = df.select_dtypes(include=['float64'])
    stats = numeric_cols.agg(['mean', 'median', 'std'])
    save_to_file(filename, "\nEstatísticas descritivas básicas:\n" + stats.to_string())

def calculate_group_mean(df, filename):
    """Calcula a média de consumo por medidor"""
    group_mean = df.groupby('Medidor')['Potencia_ativa'].mean()
    save_to_file(filename, "\nConsumo médio de energia por medidor:\n" + 
               group_mean.sort_values(ascending=False).to_string())

def get_temporal_patterns(df, medidor):
    """Calcula e gera gráfico de consumo temporal para um medidor"""
    bloco = df[df['Medidor'] == medidor]
    plt.figure(figsize=(12, 6))
    plt.plot(bloco['Data_hora'], bloco['Potencia_ativa'])
    plt.title(f'Variação da potência ativa para o medidor {medidor}')
    plt.xlabel('Data/Hora')
    plt.ylabel('Potência Ativa (kW)')
    plt.grid(True)
    plt.savefig('consumo-temporal.png')
    plt.close()

def calculate_peak_times(df, filename):
    """Calcula horários de pico agregados por hora"""
    df['Hora_do_dia'] = df['Data_hora'].dt.hour
    consumo_por_hora = df.groupby('Hora_do_dia')['Potencia_ativa'].mean()
    plt.figure(figsize=(12, 6))
    consumo_por_hora.plot(kind='bar')
    plt.title('Consumo médio por hora do dia')
    plt.xlabel('Hora do dia')
    plt.ylabel('Potência ativa média (kW)')
    plt.savefig('horarios-de-pico.png')
    plt.close()
    
    peak_hour = consumo_por_hora.idxmax()
    save_to_file(filename, f"\nHorário de pico de consumo: {peak_hour}:00")

def analyze_power_factor(df, filename):
    """Analisa o fator de potência"""
    plt.figure(figsize=(12, 6))
    df['Fator_potencia'].hist(bins=30)
    plt.title('Distribuição do fator de potência')
    plt.xlabel('Fator de potência')
    plt.ylabel('Frequência')
    plt.axvline(x=0.92, color='r', linestyle='--', label='Limite recomendado')
    plt.legend()
    plt.savefig('fator-potencia.png')
    plt.close()
    
    # Identificar blocos com baixo fator de potência
    low_pf = df.groupby('Medidor')['Fator_potencia'].mean()
    low_pf = low_pf[low_pf < 0.92]
    
    if not low_pf.empty:
        save_to_file(filename, "\nBlocos com fator de potência abaixo de 0.92:\n" + low_pf.to_string())
    else:
        save_to_file(filename, "\nNenhum bloco com fator de potência preocupante (abaixo de 0.92)")
    return low_pf

def plot_correlations(df):
    """Plota correlação entre potência ativa e corrente"""
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    phases = ['a', 'b', 'c']
    for i, phase in enumerate(phases):
        df.plot.scatter(x=f'Corrente_fase_{phase}', y='Potencia_ativa', ax=axes[i])
        axes[i].set_title(f'Correlação Potência Ativa vs Corrente Fase {phase.upper()}')
        axes[i].set_xlabel(f'Corrente Fase {phase.upper()} (A)')
        axes[i].set_ylabel('Potência Ativa (kW)')
    plt.tight_layout()
    plt.savefig('correlacao-corrente-potencia.png')
    plt.close()

if __name__ == "__main__":
    # Cria e limpa o arquivo de relatório não-gráfico
    report_filename = 'relatorio.txt'
    with open(report_filename, 'w', encoding='utf-8') as f:
        f.write("Relatório de Análise de Dados de Energia\n")

    # Parte 1: carregamento e limpeza dos dados
    df = load_data()
    df = clean_data(df)
    
    # Parte 2: análise exploratória básica
    calculate_basic_stats(df, report_filename)
    calculate_group_mean(df, report_filename)
    
    # Parte 3: identificação de padrões temporais
    get_temporal_patterns(df, 'MedCEEI')
    calculate_peak_times(df, report_filename)
    
    # Parte 4: análise de fator de potência
    analyze_power_factor(df, report_filename)
    
    # Parte 5: correlação entre variáveis
    plot_correlations(df)
