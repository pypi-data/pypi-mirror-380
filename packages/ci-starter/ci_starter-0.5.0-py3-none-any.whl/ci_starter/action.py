from re import compile
from typing import Self

from .errors import ActionNotParsableError


class Action:
    PATTERN = compile(r"(?P<user>[\w_-]+)/(?P<repo>[\w_-]+)@(?P<commit>[\S]+)")

    def __init__(
        self,
        user: str,
        repo: str,
        commit: str,
    ) -> None:
        self.user = user
        self.repo = repo
        self.commit = commit

    def to_text(self):
        text = f"{self.user}/{self.repo}@{self.commit}"
        return text

    @classmethod
    def from_text(cls, text: str) -> Self:
        match = cls.PATTERN.search(text)
        if not match:
            raise ActionNotParsableError(text)

        return cls(**match.groupdict())
