"""
Configurações do Sistema de Cinema Flask
Autor: Cauã Costa
Data: 26/10/2025
"""

import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env (se existir)
load_dotenv()

class Config:
    """
    Classe de configuração central do sistema
    Todas as configurações ficam aqui para facilitar manutenção
    """
    
    # ==================== CONFIGURAÇÕES FLASK ====================
    
    # Chave secreta para sessões, cookies e segurança
    # IMPORTANTE: Mude isso em produção!
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')

    # Modo debug (True = mostra erros detalhados, False = produção)
    DEBUG = os.getenv('DEBUG', 'True') == 'True'


    # ==================== CONFIGURAÇÕES TMDB API ====================
    
    # Sua chave de API do TMDB
    # Obtenha em: https://www.themoviedb.org/settings/api

    TMDB_API_KEY = os.getenv('TMDB_API_KEY', 'c06e7ccd90466973a29b5de97bb41c83')
    
    # URL base da API do TMDB (versão 3)
    TMDB_BASE_URL = 'https://api.themoviedb.org/3'
    
    # URL base para imagens do TMDB
    # w500 = largura de 500 pixels (existem outros tamanhos: w200, w300, original)
    TMDB_IMAGE_BASE_URL = 'https://image.tmdb.org/t/p/w500'
    
    
    # ==================== CONFIGURAÇÕES DO SISTEMA ====================
    
    # Estoque padrão ao adicionar novo filme
    ESTOQUE_PADRAO = 100
    
    # Preço padrão dos ingressos (em reais)
    PRECO_PADRAO = 20.0
    
    # Quantidade de filmes a buscar ao atualizar catálogo
    QUANTIDADE_FILMES_CATALOGO = 8
    
    
    # ==================== CAMINHOS DE ARQUIVOS ====================
    
    # Arquivo JSON com dados dos filmes
    ARQUIVO_FILMES = 'dados/filmes.json'
    
    # Arquivo JSON com histórico de vendas
    ARQUIVO_HISTORICO = 'dados/historico.json'
    
    
    # ==================== OUTRAS CONFIGURAÇÕES ====================
    
    # Idioma para buscar filmes na API
    TMDB_LANGUAGE = 'pt-BR'
    
    # Região para filmes em cartaz
    TMDB_REGION = 'BR'

# ==================== CONFIGURAÇÃO DE DESENVOLVIMENTO ====================
class DevelopmentConfig(Config):
    """Configurações específicas para ambiente de desenvolvimento"""
    DEBUG = True
    TESTING = False

# ==================== CONFIGURAÇÃO DE PRODUÇÃO ====================
class ProductionConfig(Config):
    """Configurações específicas para ambiente de produção"""
    DEBUG = False
    TESTING = False

    # Em produção, EXIGE que SECRET_KEY esteja no .env
    SECRET_KEY = os.getenv('SECRET_KEY')
    if not SECRET_KEY:
        raise ValueError("SECRET_KEY não configurada no ambiente de produção!")

# ==================== CONFIGURAÇÃO DE TESTE ====================
class TestingConfig(Config):
    """Configurações específicas para testes"""
    TESTING = True
    DEBUG = True

# ==================== SELETOR DE CONFIGURAÇÃO ====================
# Escolhe qual configuração usar baseado na variável de ambiente FLASK_ENV

config_por_ambiente = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

def obter_config():
    """
    Retorna a configuração apropriada baseado no ambiente
    
    Returns:
        Classe de configuração adequada
    """  
    ambiente = os.getenv('FLASK_ENV', 'default')
    return config_por_ambiente.get(ambiente, DevelopmentConfig)