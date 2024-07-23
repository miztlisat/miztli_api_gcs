from collections.abc import Generator

from sqlalchemy import create_engine, select, text
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import NullPool

from core.settings import log, settings
from core.utils.exceptions import BaseAppException
from models import Miztlisat
from models.base_model import Base as BaseModel

engine = create_engine(
    settings.POSTGRESQL_URL.unicode_string(),
    poolclass=NullPool,
    connect_args={"application_name": "fee-api-service"},
)
Session = sessionmaker(bind=engine, autocommit=False)  # noqa: F811


def get_session() -> Generator:
    log.info("Getting db session")
    db = Session()
    log.info("DB session has been stablished")
    try:
        yield db
    except Exception as exc:  # noqa: BLE001
        db.rollback()
        log.info(exc)
    finally:
        db.close()


def create_schemas():
    schema_format = "CREATE SCHEMA IF NOT EXISTS {}"
    query_schema_public = text(schema_format.format("public"))

    with engine.connect() as conn:
        with conn.begin():
            conn.execute(query_schema_public)

        conn.close()


class DatabaseSessionMixin:
    """Database session mixin."""

    def __enter__(self) -> Session:  # type: ignore  # noqa: PGH003
        self.session = next(get_session())
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


def use_database_session():
    return DatabaseSessionMixin()


def validate_db_conections():
    try:
        session = next(get_session())
        session.execute(select(Miztlisat).select_from(Miztlisat).limit(1)).all()
        log.info("1) Table 'users'................. O.K")
    except Exception as e:  # noqa: BLE001
        session.close()
        message_error = f"Error on validate_db_conections, message error: {e}"
        raise BaseAppException(message_error)


def init_db():
    create_schemas()
    BaseModel.metadata.create_all(engine)
