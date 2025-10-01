from ruamel.yaml import YAML as Yaml


def from_yaml(s: str) -> dict:
    yaml = Yaml()
    obj = yaml.load(s)
    return obj
