from adam.commands.postgres.postgres_utils import pg_table_names
from adam.table_completer import NestedDict, TableCompleter

class PgTableCompleter(TableCompleter):
    def __init__(self, namespace: str, pg_path: str, nested_dict: NestedDict = {}, ignore_case: bool = True):
        self.namespace = namespace
        self.pg_path = pg_path
        self.ignore_case = ignore_case
        self.append_nested_dict(nested_dict)

    def __repr__(self) -> str:
        return "PgTableCompleter(%r, pg_path=%r)" % (self.namespace, self.pg_path)

    def nested(self, data: NestedDict) -> 'TableCompleter':
        return PgTableCompleter(self.namespace, self.pg_path).append_nested_dict(data)

    def tables(self) -> list[str]:
        return pg_table_names(self.namespace, self.pg_path)