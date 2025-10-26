# 🎬 Sistema de Vendas de Ingressos de Cinema refatorado

# Autor: Cauã Costa
# Data: 25/10/2025
# Versão: 1.1.0

from flask import Flask, render_template, request, redirect, url_for
import json
import os
from datetime import datetime

app = Flask(__name__)


# ================== FUNÇÕES DE PERSISTÊNCIA ==================
def carregar_filme():
    """Carregar os filmes do arquivo JSON"""
    try:
        with open("dados/filmes.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        # Se o arquivo não existir, retorna os dados padrão
        return {
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


def salvar_filmes(dados_filmes):
    """ Salvar os filmes no arquvio JSON """
    with open('dados/filmes.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados_filmes, arquivo, indent=2, ensure_ascii=False)

def carregar_historico():
    """Carrega o histórico do arquivo JSON"""
    try:
        with open('dados/historico.json', 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_historico(dados_historico):
    """Salva o histórico no arquivo JSON"""
    with open('dados/historico.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados_historico, arquivo, indent=2, ensure_ascii=False)

def contar_vendas_por_filme(historico):
    vendas = {}
    for item in historico:
        filme = item.get("filme")
        qtd = item.get("quantidade", 0)
        vendas[filme] = vendas.get(filme, 0) + qtd
    return vendas


# ================== DADOS DO SISTEMA ==================

filmes= carregar_filme()
historico = carregar_historico()

# ================== ROTAS ==================


@app.route("/")
def index():
    termo = request.args.get('busca', '').lower()
    if termo:
        filtrados = {nome: dados for nome, dados in filmes.items() if termo in nome.lower()}
    else:
        filtrados = filmes
    vendas_por_filmes = contar_vendas_por_filme(historico)
    return render_template("index.html", filmes=filtrados, vendas_por_filme=vendas_por_filme)


@app.route("/comprar/<filme>", methods=["GET", "POST"])
def comprar(filme):

    if filme not in filmes:
        return redirect(url_for("index"))

    if request.method == "POST":
        # pega os valores com get() para evitar KeyError
        idade_raw = request.form.get("idade")
        estudante = request.form.get("estudante")
        qtd_raw = request.form.get("quantidade")

        # validações básicas
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

        # preços
        preco_inteira = filmes[filme]["preco"]
        preco_meia = preco_inteira / 2

        if idade < 18 or estudante == "sim":
            tipo = "Meia"
            preco = preco_meia
        else:
            tipo = "Inteira"
            preco = preco_inteira

        # checar estoque
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
            # redireciona para sucesso (passando params simples)
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
    # Calcular estatísticas
    total_vendas = len(historico)
    total_arrecadado = sum(item["total"] for item in historico)
    vendas_por_filme = contar_vendas_por_filme(historico)

    return render_template(
        "admin.html",
        filmes=filmes,
        total_vendas=total_vendas,
        total_arrecadado=total_arrecadado,
        vendas_por_filme=vendas_por_filme,
    )


@app.route("/buscar")
def buscar():
    termo = request.args.get("q", "").lower()
    filmes_filtrados = {
        nome: dados for nome, dados in filmes.items() if termo in nome.lower()
    }

    vendas_por_filme = contar_vendas_por_filme(historico)

    return render_template("index.html", filmes=filmes_filtrados, vendas_por_filme=vendas_por_filme)



# ================== EXECUÇÃO ==================
if __name__ == "__main__":
    app.run(debug=True)
