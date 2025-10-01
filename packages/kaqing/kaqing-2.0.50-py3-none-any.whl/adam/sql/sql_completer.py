from typing import Dict, Iterable, Optional
from prompt_toolkit.completion import CompleteEvent, Completer, Completion, NestedCompleter, WordCompleter
from prompt_toolkit.document import Document

from adam.sql.any_completer import AnyCompleter as any
from adam.sql.sql_utils import safe_terms
from adam.sql.table_name_completer import TableNameCompleter

class SqlCompleter(NestedCompleter):
    def __init__(
        self, options: Dict[str, Optional[Completer]], ignore_case: bool = True
    ) -> None:
        super().__init__(options, ignore_case)

    def get_completions(
        self, document: Document, complete_event: CompleteEvent
    ) -> Iterable[Completion]:
        text = document.text_before_cursor.lstrip()
        stripped_len = len(document.text_before_cursor) - len(text)

        terms, has_space = safe_terms(text)
        if has_space:
            first_term = terms[0]
            completer = self.options.get(first_term)

            if completer is not None:
                remaining_text = text[len(first_term) :].lstrip()
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

    def completions(table: TableNameCompleter):
        return {
            'delete': {'from': table.nested({'where': any('id').nested({'=': any("'id'")})})},
            'insert': {'into': table.nested({'values(': None})},
            'select': any('*').nested({'from': table.nested({
                'limit': any('1'),
                'where': any('id').nested({'=': any("'id'").nested({'limit': any('1')})})
            })}),
            'update': table.nested({'set': {'column': {'=': None}}}),
        }