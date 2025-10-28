from config import Config
from services.tmdb_service import TMDBService

service = TMDBService()
filmes = service.atualizar_catalogo(3)
print(filmes.keys())

print("🔍 Testando configurações...")
print(f"✅ API Key: {Config.TMDB_API_KEY[:10]}...{Config.TMDB_API_KEY[-5:]}")
print(f"✅ Base URL: {Config.TMDB_BASE_URL}")
print(f"✅ Debug: {Config.DEBUG}")
print(f"✅ Estoque padrão: {Config.ESTOQUE_PADRAO}")
print(f"✅ Preço padrão: R$ {Config.PRECO_PADRAO}")
print("\n🎉 Configuração carregada com sucesso!")