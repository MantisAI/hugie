"""
These models are based on the openapi specification of the Hugging Face
Inference Endpoints API: https://api.endpoints.huggingface.cloud/
"""

from pydantic import BaseModel, BaseSettings, Field

from hugie.utils import load_json


class EndpointScaling(BaseModel):
    minReplica: int = Field(..., alias="Minimum number of endpoint replicas")
    maxReplica: int = Field(..., alias="Maximum number of endpoint replicas")


class EndpointCompute(BaseModel):

    accelerator: str = Field(
        ..., alias="Accelerator type, one of [cpu, gpu]", regex="^(cpu|gpu)$"
    )
    instanceSize: str = Field(..., alias="Instance size, e.g. large")
    instanceType: str = Field(..., alias="Instance type, e.g. c6i")
    scaling: EndpointScaling = EndpointScaling()


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
    type: str = Field(
        ...,
        description="Type of the endpoint, must be one of ['public', 'protected', 'private']",
        regex="^(public|protected|private)$",
    )
    compute: EndpointCompute = EndpointCompute()
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

        scaling = EndpointScaling(
            minReplica=config["compute"]["scaling"]["minReplica"],
            maxReplica=config["compute"]["scaling"]["maxReplica"],
        )

        compute = EndpointCompute(
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
