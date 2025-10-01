from adam.commands.cql.cql_table_completer import CqlTableNameCompleter
from adam.commands.cql.cql_utils import table_names
from adam.repl_state import ReplState
from adam.sql.sql_completer import SqlCompleter

def cql_completions(state: ReplState) -> dict[str, any]:
    table_name_completer = CqlTableNameCompleter(table_names(state))
    return {
        'describe': {
            'keyspaces': None,
            'table': table_name_completer,
            'tables': None},
    } | SqlCompleter.completions(table_name_completer)