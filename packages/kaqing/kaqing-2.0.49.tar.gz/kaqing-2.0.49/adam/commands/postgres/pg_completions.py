from adam.commands.postgres.pg_table_completer import PgTableCompleter

def pg_completions(ns: str, pg_path: str):
    return {
        '\h': None,
        '\d': None,
        '\dt': None,
        '\du': None
    } | PgTableCompleter(ns, pg_path).completions()