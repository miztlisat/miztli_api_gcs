from fastapi import APIRouter

from api.health.endpoints import router as healthcheck_endpoints
from api.v1.miztlisat.endpoints import router as miztlisat_endpoints
from core.settings import settings

api_healthcheck_router = APIRouter()
api_healthcheck_router.include_router(healthcheck_endpoints)

api_v1_router = APIRouter(prefix=f"/api/{settings.API_V1}")
api_v1_router.include_router(miztlisat_endpoints)
