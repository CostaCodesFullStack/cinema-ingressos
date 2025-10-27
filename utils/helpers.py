""" Funções auxiliares do sistema """
import json
import os
from config import Config

def criar_diretorios():
    """Cria diretórios necessários se não existirem"""
    os.makedirs('dados', exist_ok=True)
    os.makedirs('static', exist_ok=True)
    os.makedirs('templates', exist_ok=True)
    os.makedirs('services', exist_ok=True)
    os.makedirs('utils', exist_ok=True)

def carregar_json(arquivo, padrao=None):
    """
    Carrega dados de um arquivo JSON
    
    Args:
        arquivo: Caminho do arquivo
        padrao: Valor padrão se arquivo não existir
        
    Returns:
        Dados do arquivo ou valor padrão
    """
    if padrao is None:
        padrao = {}
    
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return padrao
    except json.JSONDecodeError:
        print(f"Erro ao decodificar {arquivo}. Usando valor padrão.")
        return padrao
    
def salvar_json(arquivo, dados):
    """
    Salva dados em um arquivo JSON
    
    Args:
        arquivo: Caminho do arquivo
        dados: Dados a serem salvos
    """
    # Garante que o diretório existe
    os.makedirs(os.path.dirname(arquivo), exist_ok=True)

    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)

def mesclar_filmes(filmes_atuais, filmes_novos, manter_estoque=True):
    """
    Mescla filmes atuais com novos filmes da API
    
    Args:
        filmes_atuais: Dicionário com filmes atuais
        filmes_novos: Dicionário com filmes novos da API
        manter_estoque: Se True, mantém estoque dos filmes existentes
        
    Returns:
        Dicionário com filmes mesclados
    """
    filmes_mesclados = filmes_novos.copy()

    if manter_estoque:
        for titulo, dados in filmes_mesclados.items():
            if titulo in filmes_atuais:
                # Mantém o estoque do filme atual
                dados['estoque'] = filmes_atuais[titulo]['estoque']
                
    return filmes_mesclados