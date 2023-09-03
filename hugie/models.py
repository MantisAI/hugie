from hugie.models_v2 import Endpoint
from hugie.utils import load_json


class EndpointV2(Endpoint):
    """
    Config for the inference endpoint

    Based on the default class created by datamodel_code_generator, but
    incoporates classmethod to allow loading the config from a json file.
    """

    @classmethod
    def from_json(cls, path: str):
        data = load_json(path)

        return cls(**data)
