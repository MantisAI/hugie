# generated by datamodel-codegen:
#   filename:  https://api.endpoints.huggingface.cloud/api-doc/openapi.json
#   timestamp: 2023-09-03T20:33:30+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field, RootModel, conint


class Accelerator(Enum):
    cpu = 'cpu'
    gpu = 'gpu'


class ApiResponseError(BaseModel):
    error: str


class Decrypted(RootModel):
    root: str


class Empty(BaseModel):
    pass


class EndpointAccelerator(Enum):
    cpu = 'cpu'
    gpu = 'gpu'


class EndpointAccount(BaseModel):
    id: str = Field(..., description='Account id')
    name: str = Field(..., description='Account name')


class EndpointFramework(Enum):
    custom = 'custom'
    pytorch = 'pytorch'
    tensorflow = 'tensorflow'


class EndpointImageCredentials(BaseModel):
    password: Decrypted
    username: str = Field(..., description='Registry username')


class EndpointModelImageItem(BaseModel):
    huggingface: Dict[str, Any] = Field(
        ..., description='Model served by an Hugging Face container'
    )


class Custom(BaseModel):
    credentials: Optional[EndpointImageCredentials] = None
    env: Optional[Dict[str, str]] = Field(
        None, description='Container environment variables'
    )
    health_route: Optional[str] = Field(
        None, description='Container health route', example='/health'
    )
    port: Optional[conint(ge=0)] = Field(
        80, description='Endpoint API port', example=8000
    )
    url: str = Field(
        ..., description='URL fo the container', example='https://host/image:tag'
    )


class EndpointModelImageItem1(BaseModel):
    custom: Custom = Field(..., description='Model served by a custom container')


class EndpointModelImage(RootModel):
    root: Union[EndpointModelImageItem, EndpointModelImageItem1]


class EndpointModelImageUpdateItem(BaseModel):
    huggingface: Dict[str, Any] = Field(
        ..., description='Model served by an Hugging Face container'
    )


class Custom1(BaseModel):
    credentials: Optional[EndpointImageCredentials] = None
    env: Optional[Dict[str, str]] = Field(
        None, description='Container environment variables'
    )
    health_route: Optional[str] = Field(
        None, description='Container health route', example='/health'
    )
    port: Optional[conint(ge=0)] = Field(
        80, description='Endpoint API port', example=8000
    )
    url: Optional[str] = Field(
        None, description='URL fo the container', example='https://host/image:tag'
    )


class EndpointModelImageUpdateItem1(BaseModel):
    custom: Custom1 = Field(..., description='Model served by a custom container')


class EndpointModelImageUpdate(RootModel):
    root: Union[EndpointModelImageUpdateItem, EndpointModelImageUpdateItem1] = Field(
        ..., description='Update endpoint model image'
    )


class EndpointProvider(BaseModel):
    region: str = Field(..., description='Provider region', example='us-east-1')
    vendor: str = Field(..., description='Provider vendor', example='aws')


class EndpointScaling(BaseModel):
    maxReplica: conint(ge=0) = Field(
        ..., description='Maximum number of endpoint replica', example=8
    )
    minReplica: conint(ge=0) = Field(
        ..., description='Minimum number of endpoint replica', example=2
    )


class EndpointScalingUpdate(BaseModel):
    maxReplica: Optional[conint(ge=0)] = Field(
        None, description='Maximum number of endpoint replica', example=8
    )
    minReplica: Optional[conint(ge=0)] = Field(
        None, description='Minimum number of endpoint replica', example=2
    )


class EndpointState(Enum):
    pending = 'pending'
    initializing = 'initializing'
    updating = 'updating'
    updateFailed = 'updateFailed'
    running = 'running'
    paused = 'paused'
    failed = 'failed'
    scaledToZero = 'scaledToZero'


class EndpointStatusPrivate(BaseModel):
    serviceName: Optional[str] = Field(
        None, description='VPC service name used to add the private link'
    )


class EndpointTask(Enum):
    text_classification = 'text-classification'
    zero_shot_classification = 'zero-shot-classification'
    token_classification = 'token-classification'
    question_answering = 'question-answering'
    fill_mask = 'fill-mask'
    summarization = 'summarization'
    translation = 'translation'
    text2text_generation = 'text2text-generation'
    text_generation = 'text-generation'
    feature_extraction = 'feature-extraction'
    image_classification = 'image-classification'
    automatic_speech_recognition = 'automatic-speech-recognition'
    audio_classification = 'audio-classification'
    object_detection = 'object-detection'
    image_segmentation = 'image-segmentation'
    table_question_answering = 'table-question-answering'
    conversational = 'conversational'
    sentence_similarity = 'sentence-similarity'
    sentence_embeddings = 'sentence-embeddings'
    sentence_ranking = 'sentence-ranking'
    text_to_image = 'text-to-image'
    custom = 'custom'


class EndpointType(Enum):
    public = 'public'
    protected = 'protected'
    private = 'private'


class MetricName(Enum):
    request_count = 'request-count'
    median_latency = 'median-latency'
    p95_latency = 'p95-latency'
    success_throughput = 'success-throughput'
    bad_request_throughput = 'bad-request-throughput'
    server_error_throughput = 'server-error-throughput'
    cpu_usage = 'cpu-usage'
    memory_usage = 'memory-usage'
    gpu_usage = 'gpu-usage'
    gpu_memory_usage = 'gpu-memory-usage'
    average_latency = 'average-latency'
    success_rate = 'success-rate'
    bad_request_rate = 'bad-request-rate'
    server_error_rate = 'server-error-rate'


class MetricsParams(BaseModel):
    dnsPrefix: str
    from_: conint(ge=0) = Field(..., alias='from')
    step: Optional[str] = None
    to: conint(ge=0)


class Status(Enum):
    available = 'available'
    notAvailable = 'notAvailable'


class Compute(BaseModel):
    accelerator: Accelerator
    architecture: str = Field(
        ..., description='Compute accelerator architecture', example='Nvidia Tesla T4'
    )
    gpuMemoryGb: Optional[conint(ge=0)] = Field(
        None, description='Amount of memory per GPU in GB', example='24'
    )
    instanceSize: str = Field(
        ..., description='Compute accelerator instance size', example='medium'
    )
    instanceType: str = Field(
        ..., description='Compute accelerator instance type', example='g4dn.xlarge'
    )
    memoryGb: conint(ge=0) = Field(
        ...,
        description='Amount of RAM which can be requested per endpoint replica',
        example='14',
    )
    numAccelerators: conint(ge=0) = Field(
        ...,
        description='Number of accelerator units which can be requested per endpoint replica',
        example='1',
    )
    numCpus: Optional[conint(ge=0)] = Field(
        None,
        description='Number of CPUs which can be requested per endpoint replica',
        example='3',
    )
    pricePerHour: float = Field(
        ...,
        description='Price per hour in dollar of an endpoint replica',
        example='0.6',
    )
    status: Status


class ComputeList(BaseModel):
    items: List[Compute] = Field(
        ..., description='Vendor region compute resources list'
    )


class EndpointCompute(BaseModel):
    accelerator: EndpointAccelerator
    instanceSize: str = Field(..., example='large')
    instanceType: str = Field(..., description='Compute instance type', example='c6i')
    scaling: EndpointScaling


class EndpointComputeUpdate(BaseModel):
    accelerator: Optional[EndpointAccelerator] = None
    instanceSize: Optional[str] = Field(None, example='large')
    instanceType: Optional[str] = Field(
        None, description='Compute instance type', example='c6i'
    )
    scaling: Optional[EndpointScalingUpdate] = None


class EndpointModel(BaseModel):
    framework: EndpointFramework
    image: EndpointModelImage
    repository: str = Field(..., description='HuggingFace repository', example='gpt2')
    revision: Optional[str] = Field(
        None,
        description='Model commit hash, if not set the latest commit will be used',
        example='6c0e6080953db56375760c0471a8c5f2929baf11',
    )
    task: Optional[EndpointTask] = None


class EndpointModelUpdate(BaseModel):
    framework: Optional[EndpointFramework] = None
    image: Optional[EndpointModelImageUpdate] = None
    repository: Optional[str] = Field(
        None, description='HuggingFace repository', example='gpt2'
    )
    revision: Optional[str] = Field(
        None,
        description='Model commit hash, if not set the latest commit will be used',
        example='6c0e6080953db56375760c0471a8c5f2929baf11',
    )
    task: Optional[EndpointTask] = None


class EndpointStatus(BaseModel):
    createdAt: datetime = Field(..., description='Date of creation')
    createdBy: EndpointAccount
    message: str = Field(
        ...,
        description='Information about the state of the endpoint',
        example='Endpoint is ready',
    )
    private: Optional[EndpointStatusPrivate] = None
    readyReplica: conint(ge=0) = Field(
        ..., description='Number of replica ready to handle requests', example=2
    )
    state: EndpointState
    targetReplica: conint(ge=0) = Field(
        ..., description='Target number of replica to handle requests', example=4
    )
    updatedAt: datetime = Field(..., description='Date of last update')
    updatedBy: EndpointAccount
    url: Optional[str] = Field(
        None,
        description='URL the endpoint is reachable at',
        example='https://endpoint-id.region.vendor.endpoints.huggingface.cloud',
    )


class EndpointUpdate(BaseModel):
    compute: Optional[EndpointComputeUpdate] = None
    model: Optional[EndpointModelUpdate] = None


class EndpointWithStatus(BaseModel):
    accountId: Optional[str] = Field(
        None, description='Account ID used to link a VPC to a private endpoint'
    )
    compute: EndpointCompute
    model: EndpointModel
    name: str = Field(
        ...,
        description="Endpoint name. Must only contains lowercase alphanumeric characters or '-' and have a length of 32 characters maximum",
        example='my-endpoint',
    )
    provider: EndpointProvider
    status: EndpointStatus
    type: EndpointType


class EndpointWithStatusList(BaseModel):
    items: List[EndpointWithStatus]


class Region(BaseModel):
    computes: List[Compute] = Field(
        ..., description='Vendor region compute resources list'
    )
    label: str = Field(..., example='N. Virginia')
    name: str = Field(..., description='Region name', example='us-east-1')
    status: Status


class RegionList(BaseModel):
    items: List[Region] = Field(..., description='Vendor regions list')


class Vendor(BaseModel):
    name: str = Field(..., example='aws')
    regions: List[Region] = Field(..., description='Vendor regions list')
    status: Status


class VendorList(BaseModel):
    items: List[Vendor] = Field(..., description='Vendors list')


class Vendors(BaseModel):
    vendors: List[Vendor] = Field(..., description='Vendors list')


class Endpoint(BaseModel):
    accountId: Optional[str] = Field(
        None, description='Account ID used to link a VPC to a private endpoint'
    )
    compute: EndpointCompute
    model: EndpointModel
    name: str = Field(
        ...,
        description="Endpoint name. Must only contains lowercase alphanumeric characters or '-' and have a length of 32 characters maximum",
        example='my-endpoint',
    )
    provider: EndpointProvider
    type: EndpointType
