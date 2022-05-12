from contextvars import ContextVar

import peewee as pw

from app.core.config import get_app_settings


SETTINGS = get_app_settings()


db_state_default = {"closed": None, "conn": None, "ctx": None, "transactions": None}
db_state = ContextVar("db_state", default=db_state_default.copy())


class PeeweeConnectionState(pw._ConnectionState):  # noqa
    def __init__(self, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]


db = pw.PostgresqlDatabase(
    database=SETTINGS.db_name,
    user=SETTINGS.db_user,
    password=SETTINGS.db_password,
    host=SETTINGS.db_host,
    port=SETTINGS.db_port,
)

db._state = PeeweeConnectionState()
