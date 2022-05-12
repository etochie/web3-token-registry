from contextvars import ContextVar

import peewee as pw

DATABASE_NAME = "postgres"
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


db = pw.PostgresqlDatabase(DATABASE_NAME, user='postgres', password='postgres',
                           host='db', port=5432)

db._state = PeeweeConnectionState()
