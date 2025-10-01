from adam.commands.postgres.psql_table_completer import PsqlTableNameCompleter
from adam.sql.sql_completer import SqlCompleter

def psql_completions(ns: str, pg_path: str):
    return {
        '\h': None,
        '\d': None,
        '\dt': None,
        '\du': None
    } | SqlCompleter.completions(PsqlTableNameCompleter(ns, pg_path))
    # } | PsqlTableCompleter(ns, pg_path).completions()