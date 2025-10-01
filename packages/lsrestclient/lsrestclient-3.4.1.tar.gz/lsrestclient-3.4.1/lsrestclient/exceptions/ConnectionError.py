from typing import Optional


class ConnectionError(Exception):
    """Exception class for connection errors.

    Args:
            url (Optional[str]): The URL that the connection could not be established to.

    Attributes:
            url (Optional[str]): The URL that the connection could not be established to.

    Raises:
            ConnectionError: If a connection could not be established to the given URL.

    """

    url: str

    def __init__(self, url: Optional[str] = None) -> None:
        self.url = url
        super().__init__(f"Connection could not be established to '{url}'")
