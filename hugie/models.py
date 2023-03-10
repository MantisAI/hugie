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


class EndpointImageCredentials(BaseModel):
    username: str = Field(..., alias="Username for private registry")
    password: str = Field(..., alias="Password for private registry")


class EndpointModelImageConfig(BaseModel):
    credentials: EndpointImageCredentials = EndpointImageCredentials()
    env: dict = Field({}, alias="Environment variables")
    health_route: str = Field("/health", alias="Health route")
    port: int = Field(80, alias="Port", description="Endpoint API port")
    url: str = Field(
        ..., alias="URL for the container", example="https://host/image:tag"
    )


class EndpointModelImage(BaseModel):
    image: str = Field(
        "huggingface",
        description="One of ['huggingface', 'custom']",
        regex="^(huggingface|custom)$",
    )
    config: dict = {}

    def __call__(self, **kwargs):
        return {self.image: self.config}


class EndpointModel(BaseModel):
    framework: str = Field(..., alias="Framework, one of [custom, pytorch, tensorflow]")
    image: dict = Field({"huggingface": {}})
    repository: str = Field(..., alias="Repository name, e.g. gpt2")
    revision: str = Field(
        ..., description="Model commit hash, if not set, the latest commit will be used"
    )
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
    model: EndpointModel = EndpointModel()
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

        model = EndpointModel(
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
