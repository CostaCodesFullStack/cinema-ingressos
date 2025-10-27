# 🎬 Sistema de Vendas de Ingressos de Cinema refatorado

# Autor: Cauã Costa
# Data: 26/10/2025
# Versão: 2.0.0

from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import os

# Importa configurações e serviços

try:
    from config import Config
    from services.tmdb_service import TMDBService
    from utils.helpers import carregar_json, salvar_json, mesclar_filmes, criar_diretorios
except ImportError:
    print("⚠️ Módulos não encontrados. Usando modo básico.")
    # Fallback para modo básico sem API
    Config = None
    TMDBService = None
    carregar_json = None
    salvar_json = None
    mesclar_filmes = None
    criar_diretorios = None

app = Flask(__name__)

# Configurações
if Config:
    app.config.from_object(Config)
    app.secret_key = Config.SECRET_KEY
else:
    app.secret_key = 'dev-secret-key'

# Inicializa serviço TMDB (se disponível)
tmdb_service = TMDBService() if TMDBService else None


# ================== FUNÇÕES DE PERSISTÊNCIA ==================

def carregar_filmes():
    """Carregar os filmes do arquivo JSON"""
    arquivo = 'dados/filmes.json'

    # Dados padrão caso não tenha arquivo
    dados_padrao = {
        "Titanic": {
            "estoque": 100,
            "preco": 20.0,
            "imagem": "https://image.tmdb.org/t/p/w500/9xjZS2rlVxm8SFx8kPC3aIGCOYQ.jpg",
            "ano": 1997,
            "genero": "Romance/Drama",
        },
        "O Poderoso Chefão": {
            "estoque": 80,
            "preco": 20.0,
            "imagem": "https://image.tmdb.org/t/p/w500/3bhkrj58Vtu7enYsRolD1fZdja1.jpg",
            "ano": 1972,
            "genero": "Crime/Drama",
        },
        "A Origem": {
            "estoque": 50,
            "preco": 20.0,
            "imagem": "https://image.tmdb.org/t/p/w500/edv5CZvWj09upOsy2Y6IwDhK8bt.jpg",
            "ano": 2010,
            "genero": "Ação/Ficção",
        },
        "Na sua pele": {
            "estoque": 60,
            "preco": 20.0,
            "imagem": "https://image.tmdb.org/t/p/w500/mwUUv7cEHvwz6re2rDbvLGN0qCo.jpg",
            "ano": 2020,
            "genero": "Terror/Suspense",
        },
    }

    if carregar_json:
        return carregar_json(arquivo, dados_padrao)
    else:
        # Fallback sem helper
        try:
            import json
            with open(arquivo, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return dados_padrao


def salvar_filmes(dados_filmes):
    """ Salvar os filmes no arquvio JSON """
    arquivo = 'dados/filmes.json'

    if salvar_json:
        salvar_json(arquivo, dados_filmes)
    else:
        # Fallback sem helper
        import json
        os.makedirs('dados', exist_ok=True)
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados_filmes, f, indent=2, ensure_ascii=False)


def carregar_historico():
    """Carrega o histórico do arquivo JSON"""
    arquivo = 'dados/historico.json'

    if carregar_json:
        return carregar_json(arquivo, [])
    else:
        # Fallback sem helper
        try:
            import json
            with open(arquivo, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

def salvar_historico(dados_historico):
    """Salva o histórico no arquivo JSON"""
    arquivo = 'dados/historico.json'

    if salvar_json:
        salvar_json(arquivo, dados_historico)
    else:
        # Fallback sem helper
        import json
        os.makedirs('dados', exist_ok=True)
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados_historico, f, indent=2, ensure_ascii=False)

def contar_vendas_por_filme(historico):
    """Conta vendas por filme"""
    vendas = {}
    for item in historico:
        filme = item.get("filme")
        qtd = item.get("quantidade", 0)
        vendas[filme] = vendas.get(filme, 0) + qtd
    return vendas

# ================== FUNÇÕES DA API TMDB ==================

def atualizar_filmes_tmdb(manter_estoque=True):
    """
    Atualiza catálogo de filmes usando a API do TMDB
    
    Args:
        manter_estoque: Se True, mantém o estoque dos filmes existentes
        
    Returns:
        True se sucesso, False caso contrário
    """
    if not tmdb_service:
        print("⚠️ Serviço TMDB não disponível")
        return False
    
    try:
        # Carrega filmes atuais
        filmes_atuais = carregar_filmes()

        # Busca filmes novos da API
        filmes_novos = tmdb_service.atualizar_catalogo()

        if not filmes_novos:
            print("❌ Nenhum filme retornado da API")
            return False

        # Mescla filmes (mantendo estoque se necessário)
        if manter_estoque and mesclar_filmes:
            filmes_final = mesclar_filmes(filmes_atuais, filmes_novos, manter_estoque=True)
        else:
            filmes_final = filmes_novos

        # Salva filmes atualizados
        salvar_filmes(filmes_final)

        print(f"✅ Catálogo atualizado com {len(filmes_final)} filmes")
        return True
    except Exception as e:
        print(f"❌ Erro ao atualizar filmes: {e}")
        return False

def adicionar_filme_especifico(titulo):
    """
    Adiciona um filme específico ao catálogo
    
    Args:
        titulo: Título do filme a buscar
        
    Returns:
        True se sucesso, False caso contrário
    """
    if not tmdb_service:
        return False

    try:
        # Busca o filme
        resultado = tmdb_service.buscar_filme(titulo)

        if not resultado or not resultado.get('results'):
            print(f"❌ Filme '{titulo}' não encontrado")
            return False

        # Pega o primeiro resultado
        filme_tmdb = resultado['results'][0]
        filme_formatado = tmdb_service.formatar_para_sistema(filme_tmdb)

        if not filme_formatado:
            return False

        # Carrega filmes atuais e adiciona o novo
        filmes = carregar_filmes()
        filmes[filme_tmdb['title']] = filme_formatado

        # Salva
        salvar_filmes(filmes)

        print(f"✅ Filme '{filme_tmdb['title']}' adicionado com sucesso")
        return True

    except Exception as e:
        print(f"❌ Erro ao adicionar filme: {e}")
        return False



# ================== INICIALIZAÇÃO ==================

# Cria diretórios necessários
try:
    if criar_diretorios:
        criar_diretorios()
except Exception:
    os.makedirs('dados', exist_ok=True)

# Carrega dados
filmes= carregar_filmes()
historico = carregar_historico()

# ================== ROTAS ==================

@app.route("/")
def index():
    termo = request.args.get('busca', '').lower()
    if termo:
        filtrados = {nome: dados for nome, dados in filmes.items() if termo in nome.lower()}
    else:
        filtrados = filmes
    
    vendas_por_filme = contar_vendas_por_filme(historico)
    
    return render_template("index.html", filmes=filtrados, vendas_por_filme=vendas_por_filme)


@app.route("/comprar/<filme>", methods=["GET", "POST"])
def comprar(filme):
    if filme not in filmes:
        flash("Filme não encontrado!", "error")
        return redirect(url_for("index"))

    if request.method == "POST":
        # Pega os valores
        idade_raw = request.form.get("idade")
        estudante = request.form.get("estudante")
        qtd_raw = request.form.get("quantidade")

        # Validações básicas
        if not idade_raw or not estudante or not qtd_raw:
            erro_msg = "⚠️ Por favor, preencha todos os campos."
            return render_template(
                "compra.html",
                filme=filme,
                erro=erro_msg,
                estoque=filmes[filme]["estoque"],
                filmes=filmes,
            )

        try:
            idade = int(idade_raw)
            qtd = int(qtd_raw)
        except ValueError:
            return render_template(
                "compra.html",
                filme=filme,
                erro="⚠️ Idade e quantidade devem ser números válidos.",
                estoque=filmes[filme]["estoque"],
                filmes=filmes,
            )

        if qtd <= 0:
            return render_template(
                "compra.html",
                filme=filme,
                erro="⚠️ A quantidade deve ser maior que zero.",
                estoque=filmes[filme]["estoque"],
                filmes=filmes,
            )

        if idade < 0 or idade > 120:
            return render_template(
                "compra.html",
                filme=filme,
                erro="⚠️ Idade inválida. Digite um valor entre 0 e 120.",
                estoque=filmes[filme]["estoque"],
                filmes=filmes,
            )

        # Preços
        preco_inteira = filmes[filme]["preco"]
        preco_meia = preco_inteira / 2

        if idade < 18 or estudante == "sim":
            tipo = "Meia"
            preco = preco_meia
        else:
            tipo = "Inteira"
            preco = preco_inteira

        # Checar estoque
        if filmes[filme]["estoque"] >= qtd:
            filmes[filme]["estoque"] -= qtd
            total = preco * qtd
            historico.append({
                "filme": filme,
                "tipo": tipo,
                "quantidade": qtd,
                "total": total,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M")
            })
            salvar_filmes(filmes)
            salvar_historico(historico)
            
            return redirect(
                url_for("sucesso", filme=filme, total=f"{total:.2f}", tipo=tipo)
            )
        else:
            return render_template(
                "compra.html",
                filme=filme,
                erro=f"⚠️ Ingressos insuficientes. Disponível: {filmes[filme]['estoque']}, Solicitado: {qtd}",
                estoque=filmes[filme]["estoque"],
                filmes=filmes,
            )

    # GET -> mostrar formulário
    return render_template(
        "compra.html",
        filme=filme,
        erro=None,
        estoque=filmes[filme]["estoque"],
        filmes=filmes,
    )


@app.route("/sucesso")
def sucesso():
    filme = request.args.get("filme")
    total = request.args.get("total")
    tipo = request.args.get("tipo")
    return render_template("sucesso.html", filme=filme, total=total, tipo=tipo)


@app.route("/historico")
def ver_historico():
    total_vendido = sum(item["total"] for item in historico)
    return render_template(
        "historico.html", historico=historico, total_vendido=total_vendido
    )


@app.route("/admin")
def admin():
    # Calcula estatísticas
    total_vendas = len(historico)
    total_arrecadado = sum(item["total"] for item in historico)
    vendas_por_filme = contar_vendas_por_filme(historico)

    return render_template(
        "admin.html",
        filmes=filmes,
        total_vendas=total_vendas,
        total_arrecadado=total_arrecadado,
        vendas_por_filme=vendas_por_filme,
        tmdb_disponivel=tmdb_service is not None
    )


@app.route("/buscar")
def buscar():
    termo = request.args.get("q", "").lower()
    filmes_filtrados = {
        nome: dados for nome, dados in filmes.items() if termo in nome.lower()
    }

    vendas_por_filme = contar_vendas_por_filme(historico)

    return render_template("index.html", filmes=filmes_filtrados, vendas_por_filme=vendas_por_filme)


@app.route("/admin/atualizar-catalogo", methods=["POST"])
def atualizar_catalogo():
    """Rota para atualizar catálogo via TMDB API"""
    if not tmdb_service:
        flash("API do TMDB não está configurada!", "error")
        return redirect(url_for("admin"))
    
    sucesso = atualizar_filmes_tmdb(manter_estoque=True)
    
    if sucesso:
        # Recarrega filmes globais
        global filmes
        filmes = carregar_filmes()
        flash("✅ Catálogo atualizado com sucesso!", "success")
    else:
        flash("❌ Erro ao atualizar catálogo", "error")
    
    return redirect(url_for("admin"))


@app.route("/admin/adicionar-filme", methods=["POST"])
def adicionar_filme():
    """Rota para adicionar filme específico"""
    if not tmdb_service:
        flash("API do TMDB não está configurada!", "error")
        return redirect(url_for("admin"))
    
    titulo = request.form.get("titulo", "").strip()
    
    if not titulo:
        flash("⚠️ Digite o título do filme", "warning")
        return redirect(url_for("admin"))
    
    sucesso = adicionar_filme_especifico(titulo)
    
    if sucesso:
        # Recarrega filmes globais
        global filmes
        filmes = carregar_filmes()
        flash(f"✅ Filme adicionado com sucesso!", "success")
    else:
        flash(f"❌ Filme '{titulo}' não encontrado", "error")
    
    return redirect(url_for("admin"))

# ================== EXECUÇÃO ==================
if __name__ == "__main__":
    print("\n" + "="*60)
    print("🎬 SISTEMA DE CINEMA FLASK - v2.0.0")
    print("="*60)
    
    if tmdb_service:
        print("✅ API TMDB: Ativa")
        print(f"📂 Filmes no catálogo: {len(filmes)}")
    else:
        print("⚠️  API TMDB: Desativada (modo básico)")
    
    print("="*60 + "\n")

    app.run(debug=True)
