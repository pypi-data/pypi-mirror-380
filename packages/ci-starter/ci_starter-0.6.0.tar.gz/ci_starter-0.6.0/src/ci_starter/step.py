from copy import deepcopy
from typing import ClassVar, Self

from ruamel.yaml.comments import Comment, CommentedMap, comment_attrib
from ruamel.yaml.constructor import Constructor
from ruamel.yaml.nodes import MappingNode
from ruamel.yaml.representer import Representer
from ruamel.yaml.tokens import CommentToken
from semver import VersionInfo

from ci_starter.action import Action


class Step:
    yaml_tag: ClassVar[str] = "!step"
    version_comment_start = "# v"
    mysterious_comment_offset = 2

    def __init__(self, **kwargs) -> None:
        self._kwargs = kwargs
        normal_kwargs = {k: v for k, v in self._kwargs.items() if k not in {"comment", "uses"}}

        for k, v in normal_kwargs.items():
            setattr(self, k, v)

        comment: Comment = deepcopy(kwargs.get("comment"))
        setattr(self, comment_attrib, comment)

        version_string = self.comment_string
        version = VersionInfo.parse(version_string)
        self.uses = Action.from_text(kwargs.get("uses"), version=version)

    @property
    def comment_string(self) -> str:
        string = self.comment_token.value.strip().removeprefix(self.version_comment_start)
        return string

    @comment_string.setter
    def comment_string(self, value: VersionInfo) -> None:
        comment = getattr(self, comment_attrib)
        comment._items["uses"][2].value = f"{self.version_comment_start}{value}\n"
        comment._items["uses"][2].column = self.original_comment_column - self.mysterious_comment_offset

    @property
    def original_comment_column(self) -> int:
        original_comment = self._kwargs.get("comment")
        column = original_comment._items["uses"][2].column
        return column

    @property
    def comment_token(self) -> CommentToken:
        comment = getattr(self, comment_attrib)
        token: CommentToken = comment.items["uses"][2]
        return token

    @property
    def uses(self) -> Action:
        return self._uses

    @uses.setter
    def uses(self, action: Action) -> None:
        assert isinstance(action, Action), "uses must be set with an Action instance"
        self._uses = action
        if not action.is_from_text:
            self.comment_string = action.version
        self.items = self.value.items

    @property
    def value(self) -> dict:
        result = deepcopy(self._kwargs)
        result["uses"] = self.uses.to_text()
        del result["comment"]
        return result

    @classmethod
    def from_yaml(cls, constructor: Constructor, node: MappingNode) -> Self:
        comment = cls.get_action_comment(node)
        commented_map = CommentedMap()
        constructor.construct_mapping(node, maptyp=commented_map, deep=False)
        return cls(**commented_map, comment=comment)

    @classmethod
    def get_action_comment(cls, node: MappingNode) -> list[CommentToken | None]:
        f = filter(lambda tupl: tupl[0].value == "uses", node.value)
        _, scalar_node = next(f)
        comments: list[CommentToken | None] = scalar_node.comment
        comment = Comment()
        comment._items = {"uses": [None, None, *comments]}
        return comment

    @classmethod
    def to_yaml(cls, representer: Representer, node: Self) -> MappingNode:
        tag = cls.yaml_tag
        result = representer.represent_mapping(tag, node)
        return result

    def __repr__(self) -> str:
        attrs = ", ".join((f"{k}={v}" for k, v in self.value.items()))
        result = f"{self.__class__.__name__}({attrs})"
        return result
