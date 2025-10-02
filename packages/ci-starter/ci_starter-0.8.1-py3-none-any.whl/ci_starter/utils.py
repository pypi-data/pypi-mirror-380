from ruamel.yaml import YAML as Yaml

from ci_starter.step import Step


def from_yaml(s: str) -> dict:
    yaml = Yaml()
    yaml.register_class(Step)
    obj = yaml.load(s)
    return obj
