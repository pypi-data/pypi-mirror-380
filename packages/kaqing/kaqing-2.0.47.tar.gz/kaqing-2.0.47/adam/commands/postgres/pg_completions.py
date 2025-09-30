from adam.commands.postgres.pg_table_completer import PgTableCompleter

def pg_completions(ns: str, pg_path: str):
    table = PgTableCompleter(ns, pg_path)
    return {
        '\h': None,
        '\d': None,
        '\dt': None,
        '\du': None,
        'delete': {'from': table.nested({'where': {'id': {'=': None}}})},
        'insert': {'into': table.nested({'values': None})},
        'select': {'*': {'from': table.nested({
            'limit': {'1': {'where': {'id': {'=': {"'id'": None}}}}},
            'where': {'id': {'=': {"'id'": {'limit': {'1': None}}}}}
        })}},
        'update': table.nested({'set': None}),
    }