from abc import abstractmethod
from typing import Any, Dict, Iterable, Mapping, Optional, Set, Union
from prompt_toolkit.completion import CompleteEvent, Completer, Completion, NestedCompleter, WordCompleter
from prompt_toolkit.document import Document

NestedDict = Mapping[str, Union[Any, Set[str], None, Completer]]

class TableCompleter(Completer):
    def __init__(self, nested_dict: NestedDict = {}, ignore_case: bool = True):
        self.ignore_case = ignore_case
        self.append_nested_dict(nested_dict)

    def append_nested_dict(self, data: NestedDict) -> "TableCompleter":
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

            yielded = False
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
                    yielded = True

            if not yielded:
                completer = WordCompleter(
                    list(self.options.keys()), ignore_case=self.ignore_case
                )
                for c in completer.get_completions(document, complete_event):
                    yield c
        else:
            completer = WordCompleter(
                self.tables(), ignore_case=self.ignore_case
            )
            for c in completer.get_completions(document, complete_event):
                yield c

    @abstractmethod
    def nested(self, data: NestedDict) -> 'TableCompleter':
        pass

    @abstractmethod
    def tables(self) -> list[str]:
        pass

    def completions(self):
        return {
            'delete': {'from': self.nested({'where': {'id': {'=': {"'id'": None}}}})},
            'insert': {'into': self.nested({'values(': None})},
            'select': {'*': {'from': self.nested({
                'limit': {'1': {'where': {'id': {'=': {"'id'": None}}}}},
                'where': {'id': {'=': {"'id'": {'limit': {'1': None}}}}}
            })}},
            'update': self.nested({'set': {'column': {'=': None}}}),
        }