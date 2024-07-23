
from fastapi import APIRouter, Depends, Request, status

from api.v1.miztlisat.filters import FilterMiztlisatSchema
from api.v1.miztlisat.schemas import CreateMiztlisatSchema
from api.v1.miztlisat.services import CreateMiztliService, ListMiztliService
from core.settings import log
from core.settings.database import use_database_session
from core.utils.responses import (
    EnvelopeResponse,
    PaginationParams,
    default_pagination_params,
)

router = APIRouter(prefix="/data", tags=["CRUD data"])


@router.get(
    "",
    summary="Lista todos los codes",
    status_code=status.HTTP_200_OK,
    response_model=EnvelopeResponse,
)
async def get_all(
    request: Request,
    pagination_params: PaginationParams = Depends(default_pagination_params),
    query_params: FilterMiztlisatSchema = Depends(),
) -> ListMiztliService:
    with use_database_session() as session:
        log.info("Get List of Miztlisat")
        filters = query_params.model_dump(exclude_unset=True, exclude_defaults=True)
        return ListMiztliService(session=session).list(
            pagination_params=pagination_params, request=request, filters=filters
        )



@router.post(
    "",
    summary="Crear registro de usuario",
    status_code=status.HTTP_201_CREATED,
    response_model=EnvelopeResponse,
)
async def create(
    request: Request,
    payload: CreateMiztlisatSchema,
):
    log.info("Create User")
    with use_database_session() as session:
        log.info("Create a DisbursementPeriod")
        return CreateMiztliService(session=session).create(payload=payload)
