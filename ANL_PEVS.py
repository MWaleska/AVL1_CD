"""
Análise da Produção da Extração Vegetal e Silvicultura (PEVS)
Projeto: Transformação Digital na Educação - Questão 5
Ferramenta: VSCode + Python + Matplotlib

Este script realiza análise completa dos dados PEVS do IBGE,
gerando visualizações e insights para políticas públicas de bioeconomia.
"""

import pandas as pd          # Manipulação e análise de dados estruturados
import matplotlib.pyplot as plt  # Criação de gráficos e visualizações
import seaborn as sns        # Visualizações estatísticas avançadas
import numpy as np           # Operações matemáticas e arrays
import warnings              # Controle de avisos do sistema
warnings.filterwarnings('ignore')  # Suprime avisos desnecessários

def configurar_graficos():
    """
    Configura o estilo visual dos gráficos para apresentação profissional.
    
    Define:
    - Estilo padrão do matplotlib
    - Tamanho das figuras (12x8 polegadas)
    - Tamanho da fonte (10pt)
    - Paleta de cores harmoniosa
    """
    plt.style.use('default')                    # Estilo limpo e profissional
    plt.rcParams['figure.figsize'] = (12, 8)    # Tamanho otimizado para tela
    plt.rcParams['font.size'] = 10              # Fonte legível
    sns.set_palette("husl")                     # Paleta de cores vibrantes
    print("✅ Configurações de gráficos aplicadas")

def carregar_dados():
    """
    Carrega dados simulados baseados nos números reais da questão 1 da prova.
    
    Os dados incluem:
    - Série temporal 2019-2024 de produção de açaí, carvão vegetal e erva-mate
    - Distribuição da produção por estados brasileiros
    - PIB agropecuário regional para correlações
    
    Returns:
        tuple: (df_temporal, df_estados) - DataFrames com dados organizados
    """
    print("📊 Carregando dados PEVS...")
    
    # Valores em toneladas, refletindo crescimento real do setor
    dados_acai = {
        'Ano': [2019, 2020, 2021, 2022, 2023, 2024],
        'Producao_Acai': [222706, 225430, 230150, 235890, 242100, 247461],  # Crescimento de 11.1%
        'Carvao_Vegetal': [372355, 385200, 398750, 420300, 465800, 502512], # Crescimento de 35.0%
        'Erva_Mate': [185000, 190000, 188000, 192000, 195000, 198000]       # Estabilidade com flutuações
    }
    
    # Baseado na especialização regional por biomas
    dados_estados = {
        'Estado': ['Pará', 'Amazonas', 'Acre', 'Rondônia', 'Maranhão'],
        'Producao_Acai': [98500, 75200, 35600, 25800, 12361],              # Pará lidera com 39.8%
        'Percentual': [39.8, 30.4, 14.4, 10.4, 5.0],                      # Distribuição percentual
        'PIB_Agropecuario': [15.2, 8.5, 4.2, 6.8, 3.1]                    # PIB em bilhões para correlação
    }
    
    df_temporal = pd.DataFrame(dados_acai)
    df_estados = pd.DataFrame(dados_estados)
    
    print(f"✅ Dados carregados: {len(df_temporal)} anos, {len(df_estados)} estados")
    return df_temporal, df_estados

def criar_dashboard_principal(df_temporal, df_estados):
    """
    Cria dashboard principal com 4 visualizações complementares.
    
    Visualizações incluídas:
    1. Evolução temporal do açaí (linha)
    2. Comparação açaí vs carvão vegetal (barras agrupadas)
    3. Produção por estado (barras horizontais)
    4. Distribuição percentual (pizza)
    
    Args:
        df_temporal (DataFrame): Dados de série temporal
        df_estados (DataFrame): Dados por estados
    """
    print("🎨 Criando dashboard principal...")
    
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('DASHBOARD PEVS - PRODUÇÃO EXTRATIVISTA VEGETAL', 
                 fontsize=16, fontweight='bold', y=0.95)
    
    # Mostra tendência de crescimento sustentável
    axes[0,0].plot(df_temporal['Ano'], df_temporal['Producao_Acai'], 
                   marker='o', linewidth=3, markersize=8, color='purple', label='Açaí')
    axes[0,0].set_title('Evolução da Produção de Açaí (2019-2024)', fontweight='bold')
    axes[0,0].set_xlabel('Ano')
    axes[0,0].set_ylabel('Produção (toneladas)')
    axes[0,0].grid(True, alpha=0.3)  # Grid sutil para facilitar leitura
    axes[0,0].legend()
    
    for i, v in enumerate(df_temporal['Producao_Acai']):
        axes[0,0].annotate(f'{v:,}', (df_temporal['Ano'][i], v), 
                          textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    
    # Barras agrupadas para comparar crescimento dos dois produtos
    x = np.arange(len(df_temporal['Ano']))
    width = 0.35  # Largura das barras
    
    bars1 = axes[0,1].bar(x - width/2, df_temporal['Producao_Acai']/1000, 
                         width, label='Açaí (mil ton)', color='purple', alpha=0.7)
    bars2 = axes[0,1].bar(x + width/2, df_temporal['Carvao_Vegetal']/1000, 
                         width, label='Carvão Vegetal (mil ton)', color='orange', alpha=0.7)
    
    axes[0,1].set_title('Comparação: Açaí vs Carvão Vegetal', fontweight='bold')
    axes[0,1].set_xlabel('Ano')
    axes[0,1].set_ylabel('Produção (mil toneladas)')
    axes[0,1].set_xticks(x)
    axes[0,1].set_xticklabels(df_temporal['Ano'])
    axes[0,1].legend()
    axes[0,1].grid(True, alpha=0.3)
    
    # Facilita comparação entre estados com nomes longos
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']  # Cores distintas
    bars = axes[1,0].barh(df_estados['Estado'], df_estados['Producao_Acai'], color=colors)
    axes[1,0].set_title('Produção de Açaí por Estado (2024)', fontweight='bold')
    axes[1,0].set_xlabel('Produção (toneladas)')
    
    for i, bar in enumerate(bars):
        width = bar.get_width()
        axes[1,0].annotate(f'{width:,}',
                          xy=(width, bar.get_y() + bar.get_height() / 2),
                          xytext=(3, 0),
                          textcoords="offset points",
                          ha='left', va='center', fontsize=9)
    
    # Visualização clara da concentração regional
    axes[1,1].pie(df_estados['Producao_Acai'], labels=df_estados['Estado'], 
                  autopct='%1.1f%%', startangle=90, colors=colors)
    axes[1,1].set_title('Distribuição da Produção por Estado', fontweight='bold')
    
    plt.tight_layout()  # Ajusta espaçamento automaticamente
    plt.show()
    print("✅ Dashboard principal criado")

def analise_correlacao(df_temporal):
    """
    Realiza análise de correlação entre os produtos extrativistas.
    
    Calcula correlações de Pearson entre:
    - Produção de açaí
    - Produção de carvão vegetal  
    - Produção de erva-mate
    
    Args:
        df_temporal (DataFrame): Dados temporais dos produtos
        
    Returns:
        DataFrame: Matriz de correlação
    """
    print("🔍 Analisando correlações...")
    
    # Renomear colunas para melhor apresentação
    dados_corr = df_temporal[['Producao_Acai', 'Carvao_Vegetal', 'Erva_Mate']].copy()
    dados_corr.columns = ['Açaí', 'Carvão Vegetal', 'Erva-Mate']
    
    plt.figure(figsize=(10, 8))
    correlacao = dados_corr.corr()  # Correlação de Pearson
    
    sns.heatmap(correlacao, annot=True,           # Mostrar valores
                cmap='RdYlBu_r',                  # Paleta divergente
                center=0,                         # Centro em zero
                square=True,                      # Células quadradas
                fmt='.3f',                        # 3 casas decimais
                cbar_kws={"shrink": .8})          # Barra de cores menor
    
    plt.title('Matriz de Correlação - Produtos Extrativistas', 
              fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.show()
    
    print("✅ Análise de correlação concluída")
    return correlacao

def calcular_estatisticas(df_temporal, df_estados):
    """
    Calcula estatísticas descritivas e indicadores de crescimento.
    
    Métricas calculadas:
    - Taxa de crescimento percentual (2019-2024)
    - Estado líder em produção
    - Produção total nacional
    - Média anual de produção
    
    Args:
        df_temporal (DataFrame): Dados temporais
        df_estados (DataFrame): Dados por estados
        
    Returns:
        dict: Dicionário com estatísticas calculadas
    """
    print("📈 Calculando estatísticas...")
    
    # Fórmula: ((valor_final - valor_inicial) / valor_inicial) * 100
    crescimento_acai = ((df_temporal['Producao_Acai'].iloc[-1] - 
                        df_temporal['Producao_Acai'].iloc[0]) / 
                       df_temporal['Producao_Acai'].iloc[0]) * 100
    
    crescimento_carvao = ((df_temporal['Carvao_Vegetal'].iloc[-1] - 
                          df_temporal['Carvao_Vegetal'].iloc[0]) / 
                         df_temporal['Carvao_Vegetal'].iloc[0]) * 100
    
    estado_lider = df_estados.loc[df_estados['Producao_Acai'].idxmax(), 'Estado']
    producao_total = df_estados['Producao_Acai'].sum()
    
    print("\n" + "="*50)
    print("📊 ANÁLISES ESTATÍSTICAS")
    print("="*50)
    print(f"Crescimento do Açaí (2019-2024): {crescimento_acai:.1f}%")
    print(f"Crescimento do Carvão Vegetal (2019-2024): {crescimento_carvao:.1f}%")
    print(f"Estado líder: {estado_lider}")
    print(f"Produção total 2024: {producao_total:,} toneladas")
    print(f"Média anual açaí: {df_temporal['Producao_Acai'].mean():,.0f} toneladas")
    
    return {
        'crescimento_acai': crescimento_acai,
        'crescimento_carvao': crescimento_carvao,
        'estado_lider': estado_lider,
        'producao_total': producao_total
    }

def gerar_insights(estatisticas):
    """
    Gera insights estratégicos baseados nas análises realizadas.
    
    Produz:
    - Insights principais sobre tendências
    - Recomendações para políticas públicas
    - Alertas sobre sustentabilidade ambiental
    
    Args:
        estatisticas (dict): Dicionário com estatísticas calculadas
    """
    print("\n" + "="*50)
    print("💡 INSIGHTS PRINCIPAIS")
    print("="*50)
    
    insights = [
        f"1. Açaí apresenta crescimento sustentável de {estatisticas['crescimento_acai']:.1f}%",
        f"2. {estatisticas['estado_lider']} domina a produção nacional",
        f"3. Carvão vegetal cresceu {estatisticas['crescimento_carvao']:.1f}% - atenção ambiental necessária",
        "4. Diversificação regional indica potencial de bioeconomia",
        "5. Correlação alta entre produtos sugere sinergia produtiva"
    ]
    
    for insight in insights:
        print(insight)
    
    print("\n" + "="*50)
    print("🎯 RECOMENDAÇÕES ESTRATÉGICAS")
    print("="*50)
    print("• Investir em certificação sustentável do açaí")
    print("• Monitorar impacto ambiental do carvão vegetal")
    print("• Desenvolver cadeias produtivas regionais")
    print("• Implementar tecnologias de rastreabilidade")
    print("• Criar incentivos para práticas sustentáveis")

def main():
    """
    Função principal que orquestra toda a análise.
    
    Fluxo de execução:
    1. Configurar ambiente gráfico
    2. Carregar dados simulados
    3. Criar visualizações principais
    4. Realizar análise de correlação
    5. Calcular estatísticas descritivas
    6. Gerar insights e recomendações
    """
    print("🚀 INICIANDO ANÁLISE PEVS")
    print("="*50)
    
    configurar_graficos()                                    # Configurar ambiente
    df_temporal, df_estados = carregar_dados()              # Carregar dados
    criar_dashboard_principal(df_temporal, df_estados)      # Criar visualizações
    correlacao = analise_correlacao(df_temporal)            # Análise de correlação
    estatisticas = calcular_estatisticas(df_temporal, df_estados)  # Calcular estatísticas
    gerar_insights(estatisticas)                            # Gerar insights
    
    print("\n✅ ANÁLISE CONCLUÍDA COM SUCESSO!")
    print("📹 Pronto para gravação do vídeo da Questão 5")

# Executa apenas quando o arquivo é rodado diretamente
if __name__ == "__main__":
    main()
