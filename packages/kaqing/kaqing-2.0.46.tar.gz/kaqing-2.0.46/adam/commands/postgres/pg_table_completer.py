from typing import Any, Dict, Iterable, Mapping, Optional, Set, Union
from prompt_toolkit.completion import CompleteEvent, Completer, Completion, NestedCompleter, WordCompleter
from prompt_toolkit.document import Document

from adam.commands.postgres.postgres_utils import pg_table_names

NestedDict = Mapping[str, Union[Any, Set[str], None, Completer]]

class PgTableCompleter(Completer):
    def __init__(self, namespace: str, pg_path: str, nested_dict: NestedDict = {}, ignore_case: bool = True):
        self.namespace = namespace
        self.pg_path = pg_path
        self.ignore_case = ignore_case
        self.append_nested_dict(nested_dict)

    def __repr__(self) -> str:
        return "PgTableCompleter(%r, pg_path=%r)" % (self.namespace, self.pg_path)

    def nested(self, data: NestedDict):
        return PgTableCompleter(self.namespace, self.pg_path).append_nested_dict(data)

    def append_nested_dict(self, data: NestedDict) -> "PgTableCompleter":
        options: Dict[str, Optional[Completer]] = {}
        for key, value in data.items():
            if isinstance(value, Completer):
                options[key] = value
            elif isinstance(value, dict):
                options[key] = NestedCompleter.from_nested_dict(value)
            elif isinstance(value, set):
                options[key] = NestedCompleter.from_nested_dict({item: None for item in value})
            else:
                assert value is None
                options[key] = None

        self.options = options

        return self

    def get_completions(
        self, document: Document, complete_event: CompleteEvent
    ) -> Iterable[Completion]:
        text = document.text_before_cursor.lstrip()
        stripped_len = len(document.text_before_cursor) - len(text)

        if " " in text:
            second_term = None
            tokens = text.split()
            if len(tokens) > 1:
                second_term = tokens[1]
            if second_term:
                completer = self.options.get(second_term)

                if completer is not None:
                    first_term = tokens[0]
                    remaining_text = text[len(first_term) :].lstrip()
                    move_cursor = len(text) - len(remaining_text) + stripped_len

                    remaining_text = remaining_text[len(second_term) :].lstrip()
                    move_cursor = len(text) - len(remaining_text) + stripped_len

                    new_document = Document(
                        remaining_text,
                        cursor_position=document.cursor_position - move_cursor,
                    )

                    for c in completer.get_completions(new_document, complete_event):
                        yield c
            else:
                completer = WordCompleter(
                    list(self.options.keys()), ignore_case=self.ignore_case
                )
                for c in completer.get_completions(document, complete_event):
                    yield c
        else:
            completer = WordCompleter(
                list(pg_table_names(self.namespace, self.pg_path)), ignore_case=self.ignore_case
            )
            for c in completer.get_completions(document, complete_event):
                yield c