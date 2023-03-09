"""
These models are based on the openapi specification of the Hugging Face
Inference Endpoints API: https://api.endpoints.huggingface.cloud/
"""

from pydantic import BaseModel, BaseSettings, Field

from hugie.utils import load_json


class ScalingModel(BaseModel):
    minReplica: int = 1
    maxReplica: int = 1


class ComputeModel(BaseModel):

    accelerator: str = None
    instanceSize: str = None
    instanceType: str = None
    scaling: ScalingModel = ScalingModel()


class ModelModel(BaseModel):

    framework: str = None
    image: dict = {"huggingface": {}}
    repository: str = None
    revision: str = None
    task: str = None


class ProviderModel(BaseModel):
    vendor: str = None
    region: str = None


class EndpointConfig(BaseSettings):
    """
    Config for the inference endpoint
    """

    accountId: str = None
    type: str = None
    compute: ComputeModel = ComputeModel()
    model: ModelModel = ModelModel()
    name: str = Field(
        ..., description="Name of the endpoint", max_length=32, regex="^[a-z0-9-]+$"
    )
    provider: ProviderModel = ProviderModel()

    @classmethod
    def from_json(self, path: str):
        """
        Load a config from a JSON file.
        """
        config = load_json(path)

        model = ModelModel(
            framework=config["model"]["framework"],
            image=config["model"]["image"],
            repository=config["model"]["repository"],
            revision=config["model"]["revision"],
            task=config["model"]["task"],
        )

        scaling = ScalingModel(
            minReplica=config["compute"]["scaling"]["minReplica"],
            maxReplica=config["compute"]["scaling"]["maxReplica"],
        )

        compute = ComputeModel(
            accelerator=config["compute"]["accelerator"],
            instanceSize=config["compute"]["instanceSize"],
            instanceType=config["compute"]["instanceType"],
            scaling=scaling,
        )

        provider = ProviderModel(
            vendor=config["provider"]["vendor"],
            region=config["provider"]["region"],
        )

        config = EndpointConfig(
            accountId=config["accountId"],
            type=config["type"],
            compute=compute,
            model=model,
            name=config["name"],
            provider=provider,
        )

        return config
