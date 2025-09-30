from _typeshed import Incomplete
from gllm_core.constants import EventType as EventType
from gllm_core.event.handler.event_handler import BaseEventHandler as BaseEventHandler
from gllm_core.schema import Event as Event
from gllm_core.utils import LoggerManager as LoggerManager

DEFAULT_SEPARATOR_LENGTH: int
MIN_SEPARATOR_LENGTH: int

class PrintEventHandler(BaseEventHandler):
    """An event handler that prints the event with human readable format.

    Attributes:
        name (str): The name assigned to the event handler.
        padding_char (str): The character to use for padding.
        separator_length (int): The length of the separator. Must be at least 10.
    """
    padding_char: Incomplete
    separator_length: Incomplete
    def __init__(self, name: str | None = None, padding_char: str = '=', separator_length: int = ...) -> None:
        '''Initializes a new instance of the PrintEventHandler class.

        Args:
            name (str, optional): The name assigned to the event handler. Defaults to the class name.
            padding_char (str, optional): The character to use for padding. Defaults to "=".
            separator_length (int, optional): The length of the separator. Must be at least 10. Defaults to 120.

        Raises:
            ValueError: If the separator length is less than 10.
        '''
    async def emit(self, event: Event) -> None:
        """Emits the given event.

        Args:
            event (Event): The event to be emitted.
        """
