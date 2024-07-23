


from fastapi import status

from api.v1.miztlisat.schemas import CreateMiztlisatSchema, ListMiztliSchema
from core.utils.generic_views import (
    BaseService,
    ListBaseService,
)
from core.utils.responses import create_simple_envelope_response
from models import (
    Miztlisat,
)


class ListMiztliService(ListBaseService):
    model = Miztlisat
    schema = ListMiztliSchema


class CreateMiztliService(BaseService):
    model = Miztlisat
    schema = ListMiztliSchema

    def create(self, payload: CreateMiztlisatSchema):

        instance = self.model(**payload.model_dump())
        self.session.add(instance)
        self.session.commit()

        return create_simple_envelope_response(
            data=instance.dict(),
            message="Code Created successfully",
            status_code=status.HTTP_201_CREATED,
            successful=True,
        )
