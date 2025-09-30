import logging
import humps  # noqa
import uuid

from collections.abc import AsyncGenerator
from datetime import date, datetime  # Entity field type

from importlib.metadata import version as _version, PackageNotFoundError
from fastapi import FastAPI, Depends, Response, status
from fastapi_pagination import add_pagination, Params
from fastapi_pagination.ext.sqlalchemy import paginate as sa_paginate
from fastapi_users import FastAPIUsers
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlmodel import Field, SQLModel, Session, create_engine, select

from .decorators import action
from .resource import RouterGenerator
from .utils import pluralize, make_optional_model


try:
    __version__ = _version("balify")
except PackageNotFoundError:
    # fallback for local editable installs or when package metadata not available
    __version__ = "0.0.0"


# Constats flags
auth = "auth"


# Read database config from `.env` or envirenment
class Settings(BaseSettings):  # type: ignore
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    database_url: str = "sqlite:///database.db"


settings = Settings()

print("--> Read database url: %s" % settings.database_url)
engine = create_engine(settings.database_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


class _OMeta(type):
    """Metaclass for `O` object

    Bind FastAPI instance to `O`

    TODO: Compare `Metaclass` and `__init_subclass__`, then choose one in for `_OMeta`
    """

    # TODO: FastAPI-Users liftspan in `auth.py`, just like `add_pagination`
    _app = FastAPI()

    def __new__(cls, *args, **kwargs):
        meta = super().__new__(cls, *args, **kwargs)

        print("--> _OMeta _app: %s" % id(cls._app))

        meta._app = add_pagination(cls._app)

        print("--> add_pagination meta._app: %s" % id(meta._app))

        # Register FastAPI-Users routers
        from .auth import add_users

        meta._app = add_users(meta._app)

        return meta

    @property
    def _endpoint(self):
        if self._o_endpoint:  # noqa
            endpoint = self._o_endpoint  # noqa
        else:
            # Generate endpoint from resource name
            name = self.__name__.replace("Resource", "")
            words = humps.decamelize(name).split("_")
            words[-1] = pluralize(words[-1])
            endpoint = "-".join(words)

        if not endpoint.startswith("/"):
            endpoint = f"/{endpoint}"
        return endpoint

    def as_router(self):
        print("--> Generate routers in App(%s)" % id(self._app))
        return RouterGenerator(self)()


GREETERS = [{"name": "Josh"}]


class O(metaclass=_OMeta):
    """O is a proxy for model, schema, resource

    model is SQLAlchemy/SQLModel model
    schema is Pydantic model
    resource is Restful resource
    """

    schema = None  # the schema is SQLModel instance
    dependencies = []  # router depends

    @classmethod
    def serve(cls, *entities) -> None:
        print("--> serve App(%s)" % id(cls._app))
        for entity in entities:
            print("--> Serve entity `%s` in App(%s)" % (str(entity), id(cls._app)))
            cls._app.include_router(
                entity.as_router(), prefix=f"/{pluralize(entity.__name__.lower())}"
            )

        # Generate all SQLModel schemas to database
        create_db_and_tables()

    @classmethod
    def depends(cls, *args, **kwargs):
        """Depends build-in depends"""

        from .auth import current_active_user

        if auth in args:
            cls.dependencies = [Depends(current_active_user)]

        return cls

    @action()
    def list(self):
        """Generic `list` method

        TODO: implement the pagination and filter expressions like `bali`

        User.query().filter(*get_filters_expr(User, **schema_in.filters))

        """
        with Session(engine) as session:
            statement = select(self.schema)
            # targets = session.exec(statement).all()
            return sa_paginate(session, statement, Params(page=1, size=10))

    @action()
    def get(self, pk=None):

        with Session(engine) as session:
            statement = select(self.schema).where(self.schema.id == pk)  # type: ignore
            target = session.exec(statement).first()

        return target

    @action()
    def create(self, schema_in):
        """Generic create method"""
        print("--> self if %s(type: %s)" % (self, type(self)))
        print("--> self.schema: %s" % self.schema)
        print("--> param schema_in: %s" % schema_in)
        # self.schema(**schema_in)  # type: ignore

        with Session(engine) as session:

            # # Option 1: Commit schema_in directly
            # # sqlalchemy.orm.exc.DetachedInstanceError:
            # # Instance <UserSQLModel at 0x7748e76918a0> is not bound to a Session;
            # # attribute refresh operation cannot proceed (Background on this error at: https://sqlalche.me/e/20/bhk3)
            # session.add(schema_in)

            # Option 2: Create New schema instance
            # Why use model_validate?
            # Because SQLModel not validate data when `table=True`
            # ref: https://github.com/fastapi/sqlmodel/issues/453
            target = self.schema.model_validate(schema_in.model_dump())  # type: ignore
            session.add(target)
            session.commit()
            session.refresh(target)

            print("--> target: %s (type: %s)" % (target, type(target)))
            print("--> target.id: %d" % target.id)

        return target

    @action()
    def update(self, schema_in=None, pk=None):

        with Session(engine) as session:
            statement = select(self.schema).where(self.schema.id == pk)  # type: ignore
            target = session.exec(statement).first()

            optional_model = make_optional_model(self.schema)  # type: ignore
            optional_schema = optional_model.model_validate(schema_in.model_dump())  # type: ignore
            for k, v in optional_schema.model_dump().items():  # type: ignore
                if v is not None:
                    setattr(target, k, v)

            session.add(target)
            session.commit()
            session.refresh(target)

        return target

    @action()
    def delete(self, pk=None):
        with Session(engine) as session:
            statement = select(self.schema).where(self.schema.id == pk)  # type: ignore
            target = session.exec(statement).first()
            if target:
                session.delete(target)
                session.commit()

        # In previou `bali-core`, it return {"result": True} to compatible with gRPC
        # It can be simpler with 204 status response
        # return {"result": True}
        return Response(status_code=status.HTTP_204_NO_CONTENT)


# I found that `O, o` in `from balify import O, o` look like an cute emontion.
# May be I can split the metaclass to uppercase `O` and lowercase `o`.
# Uppercase `O` for define entity, could be translate to model, schema and resource.
# Lowercase `o` for FastAPI instance, provide `serve` functionality.
#
# On the other hand, using both the uppercase O and the lowercase o helps developers
# form good coding style habits.
o = O
