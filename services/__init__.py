"""
Pacote de serviços do Sistema de Cinema Flask
"""

from .tmdb_service import TMDBService
from .auth_service import AuthService, User

__all__ = ['TMDBService', 'AuthService', 'User']