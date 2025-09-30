from adam.commands.cql.cql_table_completer import CqlTableCompleter
from adam.commands.cql.cql_utils import table_names
from adam.repl_state import ReplState

def cql_completions(state: ReplState) -> dict[str, any]:
    completer = CqlTableCompleter(table_names(state))
    return {
        'describe': {
            'keyspaces': None,
            'table': completer.completions(),
            'tables': None},
    } | completer.completions()