from adam.sql.table_name_completer import NestedDict, TableNameCompleter

class CqlTableNameCompleter(TableNameCompleter):
    def __init__(self, tables: list[str], nested_dict: NestedDict = {}, ignore_case: bool = True):
        self._tables = tables
        self.ignore_case = ignore_case
        self.append_nested_dict(nested_dict)

    def __repr__(self) -> str:
        return "CqlTableCompleter(%r)" % (len(self._tables))

    def nested(self, data: NestedDict) -> 'TableNameCompleter':
        return CqlTableNameCompleter(self._tables).append_nested_dict(data)

    def tables(self) -> list[str]:
        return self._tables