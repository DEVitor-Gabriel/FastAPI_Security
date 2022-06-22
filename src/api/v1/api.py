from fastapi import APIRouter

from src.api.v1.controllers import artigo
from src.api.v1.controllers import usuario


api_router = APIRouter()

api_router.include_router(artigo.router, prefix='/artigos', tags=['artigos'])
api_router.include_router(
    usuario.router, prefix='/usuarios', tags=['usuarios'])
