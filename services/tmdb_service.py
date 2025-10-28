"""Serviço para integração com a API do TMDB"""

import requests
from config import Config


class TMDBService:
    """Classe para gerenciar requisições à API do TMDB"""

    def __init__(self):
        self.api_key = Config.TMDB_API_KEY
        self.base_url = Config.TMDB_BASE_URL
        self.image_base_url = Config.TMDB_IMAGE_BASE_URL

    def _fazer_requisicao(self, endpoint, params=None):
        """Método privado para fazer requisições à API"""
        if params is None:
            params = {}

        params["api_key"] = self.api_key
        params["language"] = "pt-BR"

         # Garante que endpoint comece com /
        if not endpoint.startswith("/"):
            endpoint = "/" + endpoint

        url = self.base_url + endpoint

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição à API TMDB: {e}")
            return None

    def filmes_em_cartaz(self, pagina=1):
        """Busca filmes em cartaz no Brasil"""
        params = {"page": pagina, "region": "BR"}
        return self._fazer_requisicao("movie/now_playing", params)

    def filmes_populares(self, pagina=1):
        """Busca filmes populares"""
        params = {"page": pagina}
        return self._fazer_requisicao("movie/popular", params)

    def buscar_filme(self, titulo):
        """Busca um filme pelo título"""
        params = {"query": titulo}
        return self._fazer_requisicao("search/movie", params)

    def detalhes_filme(self, filme_id):
        """Busca detalhes de um filme pelo ID"""
        return self._fazer_requisicao(f"movie/{filme_id}")

    def formatar_para_sistema(self, filme_tmdb):
        """
        Converte dados da API TMDB para o formato do sistema

        Args:
            filme_tmdb: Dicionário com dados do filme da API

        Returns:
            Dicionário formatado para o sistema ou None se erro
        """
        try:
            # Busca detalhes completos se necessario
            if "genres" not in filme_tmdb:
                filme_id = filme_tmdb.get("id")
                if filme_id:
                    filme_tmdb = self.detalhes_filme(filme_id)

            if not filme_tmdb:
                return None

            # Extrai gêneros
            generos = [g["name"] for g in filme_tmdb.get("genres", [])]
            genero_texto = "/".join(generos) if generos else "N/A"

            # Ano de lançamento
            ano = 0
            if filme_tmdb.get("release_date"):
                try:
                    ano = int(filme_tmdb["release_date"][:4])
                except (ValueError, IndexError):
                    ano = 0

            # Monta o objeto formatado
            filme_formatado = {
                "estoque": Config.ESTOQUE_PADRAO,
                "preco": Config.PRECO_PADRAO,
                "imagem": f"{self.image_base_url}{filme_tmdb.get('poster_path', '')}",
                "ano": ano,
                "genero": genero_texto,
                "sinopse": filme_tmdb.get("overview", "Sem sinopse disponível"),
                "nota": round(filme_tmdb.get("vote_average", 0), 1),
                "tmdb_id": filme_tmdb.get("id"),
            }

            return filme_formatado

        except Exception as e:
            print(f"Erro ao formatar filme: {e}")
            return None

    def atualizar_catalogo(self, quantidade=None):
        """
        Busca filmes da API e retorna formatados para o sistema

        Args:
            quantidade: Número de filmes a buscar (padrão: Config.QUANTIDADE_FILMES_CATALOGO)

        Returns:
            Dicionário com filmes formatados {titulo: dados}
        """
        if quantidade is None:
            quantidade = Config.QUANTIDADE_FILMES_CATALOGO

        # Tenta buscar filmes em cartaz primeiro
        resultado = self.filmes_em_cartaz()

        # Se não conseguir, busca populares
        if not resultado or not resultado.get("results"):
            resultado = self.filmes_populares()

        if not resultado or not resultado.get("results"):
            print("Não foi possivel buscar filmes da API")
            return {}

        # Processa os filmes
        filmes_formatado = {}

        for filme_tmdb in resultado["results"][:quantidade]:
            titulo = filme_tmdb["title"]
            filme_formatado = self.formatar_para_sistema(filme_tmdb)

            if filme_formatado:
                filmes_formatado[titulo] = filme_formatado

        return filmes_formatado
