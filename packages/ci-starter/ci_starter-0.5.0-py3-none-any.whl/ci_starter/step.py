from copy import deepcopy
from typing import ClassVar, Self

from ruamel.yaml.comments import Comment, CommentedMap, comment_attrib
from ruamel.yaml.constructor import Constructor
from ruamel.yaml.nodes import MappingNode
from ruamel.yaml.representer import Representer
from ruamel.yaml.tokens import CommentToken

from ci_starter.action import Action


class Step:
    yaml_tag: ClassVar[str] = "!step"

    def __init__(self, **kwargs) -> None:
        self._kwargs = kwargs
        normal_kwargs = {k: v for k, v in self._kwargs.items() if k not in {"comment", "uses"}}

        for k, v in normal_kwargs.items():
            setattr(self, k, v)

        self.uses = Action.from_text(kwargs.get("uses"))
        setattr(self, comment_attrib, kwargs.get("comment"))

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
