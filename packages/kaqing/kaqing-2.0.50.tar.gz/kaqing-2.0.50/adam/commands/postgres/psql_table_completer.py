from adam.commands.postgres.postgres_utils import pg_table_names
from adam.sql.table_name_completer import NestedDict, TableNameCompleter

class PsqlTableNameCompleter(TableNameCompleter):
    def __init__(self, namespace: str, pg_path: str, nested_dict: NestedDict = {}, ignore_case: bool = True):
        self.namespace = namespace
        self.pg_path = pg_path
        self.ignore_case = ignore_case
        self.append_nested_dict(nested_dict)

    def __repr__(self) -> str:
        return "PsqlTableCompleter(%r, pg_path=%r)" % (self.namespace, self.pg_path)

    def nested(self, data: NestedDict) -> 'TableNameCompleter':
        return PsqlTableNameCompleter(self.namespace, self.pg_path).append_nested_dict(data)

    def tables(self) -> list[str]:
        return pg_table_names(self.namespace, self.pg_path)