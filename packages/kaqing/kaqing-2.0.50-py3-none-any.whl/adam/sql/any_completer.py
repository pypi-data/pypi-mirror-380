from typing import Any, Dict, Iterable, Mapping, Optional, Set, Union
from prompt_toolkit.completion import CompleteEvent, Completer, Completion, NestedCompleter, WordCompleter
from prompt_toolkit.document import Document

from adam.sql.sql_utils import safe_terms

NestedDict = Mapping[str, Union[Any, Set[str], None, Completer]]

class AnyCompleter(Completer):
    def __init__(self, default: str = None, nested_dict: NestedDict = {}, ignore_case: bool = True):
        self.default = default
        self.ignore_case = ignore_case
        self.append_nested_dict(nested_dict)

    def append_nested_dict(self, data: NestedDict) -> "AnyCompleter":
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

        terms, has_space = safe_terms(text)
        if has_space:
            second_term = None
            if len(terms) > 1:
                second_term = terms[1]

            yielded = False
            if second_term:
                completer = self.options.get(second_term)

                if completer is not None:
                    first_term = terms[0]
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
        elif words := self.words():
            for c in words.get_completions(document, complete_event):
                yield c

    def words(self):
        if not self.default:
            return None

        return WordCompleter(
            [self.default], ignore_case=self.ignore_case
        )

    def nested(self, data: NestedDict) -> 'AnyCompleter':
        return AnyCompleter(self.default).append_nested_dict(data)