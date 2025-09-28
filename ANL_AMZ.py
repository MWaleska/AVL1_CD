"""
Análise de Desmatamento da Amazônia Legal
Projeto: Transformação Digital na Educação - Questão 5
Ferramenta: Google Colab + Python + Matplotlib

: Este código demonstra como usar Google Colab para análise de dados
ambientais, focando no desmatamento da Amazônia Legal baseado nos dados da questão 4.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings
warnings.filterwarnings('ignore')

def configurar_ambiente_colab():
    """
    : Primeiro, vou configurar o ambiente do Google Colab
    para garantir que todas as visualizações sejam exibidas corretamente
    e tenham qualidade profissional para nossa análise.
    """
    print("🌐 CONFIGURANDO AMBIENTE GOOGLE COLAB...")
    print("   → Aplicando configurações otimizadas para Colab")
    print("   → Definindo estilo seaborn para gráficos mais elegantes")
    print("   → Configurando paleta de cores para dados ambientais")
    
    # Configurações específicas para Google Colab
    plt.style.use('seaborn-v0_8')
    plt.rcParams['figure.figsize'] = (14, 10)
    plt.rcParams['font.size'] = 11
    sns.set_palette("RdYlGn_r")  # Paleta vermelha-verde para dados ambientais
    
    print("✅ Ambiente Colab configurado com sucesso!")

def carregar_dados_desmatamento():
    """
    : Agora vou carregar os dados de desmatamento da Amazônia
    que utilizei na questão 4. Estes dados mostram a evolução do desmatamento
    e das políticas de fiscalização de 2020 a 2024.
    """
    print("\n🌳 CARREGANDO DADOS DE DESMATAMENTO AMAZÔNIA LEGAL...")
    print("   → Dados temporais: 5 anos de monitoramento (2020-2024)")
    print("   → Métricas: Área desmatada, multas aplicadas, valores arrecadados")
    print("   → Fonte: TerraBrasilis/INPE e Portal Dados Abertos MMA")
    
    # : Dados baseados na minha análise da questão 4
    dados_temporais = {
        'Ano': [2020, 2021, 2022, 2023, 2024],
        'Area_Desmatada_km2': [10851, 11038, 11568, 9001, 6288],  # Redução de 45.6%
        'Multas_Aplicadas': [12500, 13200, 14800, 15847, 16200],  # Aumento de 29.6%
        'Valor_Multas_Bilhoes': [1.8, 1.9, 2.0, 2.1, 2.3],
        'Multas_Pagas_Percentual': [10, 11, 11.5, 12, 12]  # Apenas 12% são pagas
    }
    
    # : Distribuição por estados - Pará lidera com 41%
    dados_estados = {
        'Estado': ['Pará', 'Amazonas', 'Rondônia', 'Acre', 'Mato Grosso'],
        'Percentual_Desmatamento': [41, 25, 18, 8, 8],
        'Area_km2_2024': [2578, 1572, 1132, 503, 503],
        'Multas_2024': [6642, 4050, 2916, 1296, 1296]
    }
    
    # : Convertendo para DataFrames para facilitar análise
    df_temporal = pd.DataFrame(dados_temporais)
    df_estados = pd.DataFrame(dados_estados)
    
    print(f"✅ Dados carregados: {len(df_temporal)} anos, {len(df_estados)} estados")
    print(f"   → Período crítico: {df_temporal['Ano'].min()} a {df_temporal['Ano'].max()}")
    print(f"   → Redução total: {((11568-6288)/11568)*100:.1f}% no desmatamento")
    
    return df_temporal, df_estados

def criar_dashboard_ambiental(df_temporal, df_estados):
    """
    : Vou criar um dashboard ambiental completo com 6 visualizações
    que mostram a evolução do desmatamento, eficácia das políticas de fiscalização
    e distribuição regional dos problemas ambientais.
    """
    print("\n📊 CRIANDO DASHBOARD AMBIENTAL INTERATIVO...")
    print("   → Layout: 2x3 (6 gráficos especializados)")
    print("   → Foco: Impacto das políticas de fiscalização")
    print("   → Objetivo: Demonstrar correlação entre multas e redução")
    
    # : Criando figura com 6 subplots para análise completa
    fig, axes = plt.subplots(2, 3, figsize=(20, 12))
    fig.suptitle('DASHBOARD AMBIENTAL - DESMATAMENTO AMAZÔNIA LEGAL', 
                 fontsize=18, fontweight='bold', y=0.95)
    
    # GRÁFICO 1:  - Evolução do desmatamento com linha de tendência
    print("   🔥 Criando gráfico de evolução do desmatamento...")
    axes[0,0].plot(df_temporal['Ano'], df_temporal['Area_Desmatada_km2'], 
                   marker='o', linewidth=4, markersize=10, color='red', label='Área Desmatada')
    
    # Adicionando linha de tendência para mostrar a redução
    z = np.polyfit(df_temporal['Ano'], df_temporal['Area_Desmatada_km2'], 1)
    p = np.poly1d(z)
    axes[0,0].plot(df_temporal['Ano'], p(df_temporal['Ano']), "--", alpha=0.8, color='darkred', label='Tendência')
    
    axes[0,0].set_title('Evolução do Desmatamento (km²)', fontweight='bold', fontsize=12)
    axes[0,0].set_xlabel('Ano')
    axes[0,0].set_ylabel('Área Desmatada (km²)')
    axes[0,0].grid(True, alpha=0.3)
    axes[0,0].legend()
    
    # GRÁFICO 2:  - Ranking de estados por desmatamento
    print("   🏆 Criando ranking de estados...")
    colors_estados = ['#FF4444', '#FF6666', '#FF8888', '#FFAAAA', '#FFCCCC']
    bars = axes[0,1].bar(df_estados['Estado'], df_estados['Area_km2_2024'], 
                         color=colors_estados, alpha=0.8)
    axes[0,1].set_title('Desmatamento por Estado (2024)', fontweight='bold', fontsize=12)
    axes[0,1].set_xlabel('Estado')
    axes[0,1].set_ylabel('Área (km²)')
    axes[0,1].tick_params(axis='x', rotation=45)
    
    # Adicionando valores nas barras
    for bar in bars:
        height = bar.get_height()
        axes[0,1].annotate(f'{height:,}',
                          xy=(bar.get_x() + bar.get_width() / 2, height),
                          xytext=(0, 3), textcoords="offset points",
                          ha='center', va='bottom', fontsize=9)
    
    # GRÁFICO 3:  - Distribuição percentual por estado
    print("   🥧 Criando distribuição percentual...")
    axes[0,2].pie(df_estados['Percentual_Desmatamento'], labels=df_estados['Estado'], 
                  autopct='%1.1f%%', startangle=90, colors=colors_estados)
    axes[0,2].set_title('Distribuição do Desmatamento (%)', fontweight='bold', fontsize=12)
    
    # GRÁFICO 4:  - Evolução das multas aplicadas
    print("   💰 Criando gráfico de multas...")
    axes[1,0].bar(df_temporal['Ano'], df_temporal['Multas_Aplicadas'], 
                  color='orange', alpha=0.7, label='Multas Aplicadas')
    axes[1,0].set_title('Multas Aplicadas por Ano', fontweight='bold', fontsize=12)
    axes[1,0].set_xlabel('Ano')
    axes[1,0].set_ylabel('Número de Multas')
    axes[1,0].legend()
    
    # GRÁFICO 5:  - Valor das multas vs efetividade
    print("   📈 Analisando efetividade das multas...")
    ax2 = axes[1,1].twinx()  # Segundo eixo Y
    
    line1 = axes[1,1].plot(df_temporal['Ano'], df_temporal['Valor_Multas_Bilhoes'], 
                          marker='s', linewidth=3, color='green', label='Valor (R$ Bi)')
    line2 = ax2.plot(df_temporal['Ano'], df_temporal['Multas_Pagas_Percentual'], 
                     marker='^', linewidth=3, color='blue', label='% Pagas')
    
    axes[1,1].set_title('Valor vs Efetividade das Multas', fontweight='bold', fontsize=12)
    axes[1,1].set_xlabel('Ano')
    axes[1,1].set_ylabel('Valor (R$ Bilhões)', color='green')
    ax2.set_ylabel('Percentual Pago (%)', color='blue')
    
    # Combinando legendas
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    axes[1,1].legend(lines, labels, loc='upper left')
    
    # GRÁFICO 6:  - Correlação desmatamento vs multas
    print("   🔍 Analisando correlação desmatamento vs fiscalização...")
    scatter = axes[1,2].scatter(df_temporal['Area_Desmatada_km2'], df_temporal['Multas_Aplicadas'], 
                               s=150, c=df_temporal['Ano'], cmap='viridis', alpha=0.7)
    
    # Linha de tendência para mostrar correlação
    z = np.polyfit(df_temporal['Area_Desmatada_km2'], df_temporal['Multas_Aplicadas'], 1)
    p = np.poly1d(z)
    axes[1,2].plot(df_temporal['Area_Desmatada_km2'], p(df_temporal['Area_Desmatada_km2']), 
                   "r--", alpha=0.8, label='Tendência')
    
    axes[1,2].set_title('Desmatamento vs Multas', fontweight='bold', fontsize=12)
    axes[1,2].set_xlabel('Área Desmatada (km²)')
    axes[1,2].set_ylabel('Número de Multas')
    axes[1,2].legend()
    
    # Colorbar para mostrar evolução temporal
    plt.colorbar(scatter, ax=axes[1,2], label='Ano')
    
    plt.tight_layout()
    plt.show()
    print("✅ Dashboard ambiental criado com sucesso!")

def calcular_metricas_ambientais(df_temporal, df_estados):
    """
    : Agora vou calcular as métricas ambientais principais
    que demonstram o impacto das políticas de fiscalização e orientam
    futuras decisões de gestão ambiental.
    """
    print("\n📊 CALCULANDO MÉTRICAS AMBIENTAIS...")
    print("   → Analisando eficácia das políticas de fiscalização")
    print("   → Calculando projeções para 2025-2026")
    print("   → Identificando correlações entre variáveis")
    
    # : Calculando redução do desmatamento
    reducao_desmatamento = ((df_temporal['Area_Desmatada_km2'].iloc[2] - 
                            df_temporal['Area_Desmatada_km2'].iloc[-1]) / 
                           df_temporal['Area_Desmatada_km2'].iloc[2]) * 100
    
    # : Calculando aumento da fiscalização
    aumento_multas = ((df_temporal['Multas_Aplicadas'].iloc[-1] - 
                      df_temporal['Multas_Aplicadas'].iloc[0]) / 
                     df_temporal['Multas_Aplicadas'].iloc[0]) * 100
    
    # : Calculando efetividade financeira
    valor_total_2024 = df_temporal['Valor_Multas_Bilhoes'].iloc[-1]
    valor_arrecadado = valor_total_2024 * 0.12  # 12% são efetivamente pagas
    
    # : Projeção otimista para 2025
    area_2024 = df_temporal['Area_Desmatada_km2'].iloc[-1]
    projecao_2025 = area_2024 * 0.7  # 30% de redução adicional
    
    # : Exibindo resultados de forma organizada
    print("\n" + "="*70)
    print("🌍 RESULTADOS DAS ANÁLISES AMBIENTAIS")
    print("="*70)
    print(f"📉 Redução do desmatamento (2022-2024): {reducao_desmatamento:.1f}%")
    print(f"📈 Aumento das multas (2020-2024): {aumento_multas:.1f}%")
    print(f"🏆 Estado com maior desmatamento: {df_estados.loc[df_estados['Percentual_Desmatamento'].idxmax(), 'Estado']}")
    print(f"💰 Efetividade das multas: R$ {valor_arrecadado:.2f} bilhões arrecadados (12%)")
    print(f"🔮 Projeção 2025 (cenário otimista): {projecao_2025:.0f} km²")
    
    return {
        'reducao_desmatamento': reducao_desmatamento,
        'aumento_multas': aumento_multas,
        'valor_arrecadado': valor_arrecadado,
        'projecao_2025': projecao_2025
    }

def gerar_recomendacoes_ambientais(metricas):
    """
    : Para finalizar, vou apresentar recomendações baseadas
    em evidências científicas para otimizar as políticas ambientais
    e maximizar a proteção da Amazônia Legal.
    """
    print("\n" + "="*70)
    print("🎯 RECOMENDAÇÕES PARA POLÍTICAS AMBIENTAIS")
    print("="*70)
    
    print("BASEADO NAS ANÁLISES, RECOMENDO:")
    print(f"   🎯 PRIORIDADE ALTA:")
    print("   • 🚁 Intensificar fiscalização no Pará (41% do desmatamento)")
    print("   • 🛰️ Implementar monitoramento por satélite em tempo real")
    print("   • 💳 Criar sistema de bloqueio de crédito rural para infratores")
    
    print(f"\n   📊 PRIORIDADE MÉDIA:")
    print("   • 🤖 Automatizar detecção de desmatamento com IA")
    print("   • 🏛️ Melhorar cobrança das multas (apenas 12% são pagas)")
    print("   • 🌱 Criar incentivos para preservação florestal")
    
    print(f"\n   🔮 PROJEÇÕES:")
    print(f"   • Se mantidas as políticas atuais: {metricas['projecao_2025']:.0f} km² em 2025")
    print(f"   • Potencial de redução adicional: 30% com intensificação")
    print(f"   • Meta sugerida: Menos de 4.000 km² até 2026")

def main():
    """
    : Esta é a função principal que demonstra o uso do Google Colab
    para análise de dados ambientais. Vou executar todas as etapas para mostrar
    um workflow completo de ciência de dados aplicada à gestão ambiental.
    """
    print("🌐 INICIANDO DEMONSTRAÇÃO NO GOOGLE COLAB")
    print("="*70)
    print("FERRAMENTA: Google Colab + Python + Matplotlib")
    print("PROJETO: Transformação Digital na Educação - Questão 5")
    print("FOCO: Análise de Dados Ambientais - Desmatamento Amazônia")
    print("="*70)
    
    # : Executando workflow completo
    print("\n🔧 ETAPA 1: CONFIGURAÇÃO DO AMBIENTE COLAB")
    configurar_ambiente_colab()
    
    print("\n🌳 ETAPA 2: CARREGAMENTO DOS DADOS AMBIENTAIS")
    df_temporal, df_estados = carregar_dados_desmatamento()
    
    print("\n📊 ETAPA 3: CRIAÇÃO DO DASHBOARD AMBIENTAL")
    criar_dashboard_ambiental(df_temporal, df_estados)
    
    print("\n📈 ETAPA 4: CÁLCULO DAS MÉTRICAS AMBIENTAIS")
    metricas = calcular_metricas_ambientais(df_temporal, df_estados)
    
    print("\n🎯 ETAPA 5: GERAÇÃO DE RECOMENDAÇÕES")
    gerar_recomendacoes_ambientais(metricas)
    
    print("\n" + "="*70)
    print("✅ DEMONSTRAÇÃO GOOGLE COLAB CONCLUÍDA!")
    print("📹 CÓDIGO PRONTO PARA GRAVAÇÃO DO SEGUNDO VÍDEO")
    print("🎯 FERRAMENTA DEMONSTRADA: Google Colab + Python")
    print("="*70)

# : Executando o programa principal
if __name__ == "__main__":
    main()
