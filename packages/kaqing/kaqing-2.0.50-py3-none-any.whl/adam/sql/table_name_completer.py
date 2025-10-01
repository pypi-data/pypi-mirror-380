from abc import abstractmethod
from prompt_toolkit.completion import  WordCompleter

from .any_completer import AnyCompleter, NestedDict

class TableNameCompleter(AnyCompleter):
    def __init__(self, nested_dict: NestedDict = {}, ignore_case: bool = True):
        super().__init__(nested_dict=nested_dict, ignore_case=ignore_case)

    def words(self):
        return WordCompleter(
            self.tables(), ignore_case=self.ignore_case
        )

    @abstractmethod
    def tables(self) -> list[str]:
        pass