class DownStreamError(Exception):
    status_code: int
    url: str
    content: str

    def __init__(self, url: str, status_code: int, content: str) -> None:
        self.url = url
        self.status_code = status_code
        self.content = content
        super().__init__(
            f"Downstream error calling {self.url}. {self.status_code} {self.content}"
        )
