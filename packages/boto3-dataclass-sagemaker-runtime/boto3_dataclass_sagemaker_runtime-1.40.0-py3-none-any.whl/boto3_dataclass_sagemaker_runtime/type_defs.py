# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_sagemaker_runtime import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class InternalStreamFailure:
    boto3_raw_data: "type_defs.InternalStreamFailureTypeDef" = dataclasses.field()

    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InternalStreamFailureTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InternalStreamFailureTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvokeEndpointAsyncInput:
    boto3_raw_data: "type_defs.InvokeEndpointAsyncInputTypeDef" = dataclasses.field()

    EndpointName = field("EndpointName")
    InputLocation = field("InputLocation")
    ContentType = field("ContentType")
    Accept = field("Accept")
    CustomAttributes = field("CustomAttributes")
    InferenceId = field("InferenceId")
    RequestTTLSeconds = field("RequestTTLSeconds")
    InvocationTimeoutSeconds = field("InvocationTimeoutSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvokeEndpointAsyncInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokeEndpointAsyncInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseMetadata:
    boto3_raw_data: "type_defs.ResponseMetadataTypeDef" = dataclasses.field()

    RequestId = field("RequestId")
    HTTPStatusCode = field("HTTPStatusCode")
    HTTPHeaders = field("HTTPHeaders")
    RetryAttempts = field("RetryAttempts")
    HostId = field("HostId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResponseMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModelStreamError:
    boto3_raw_data: "type_defs.ModelStreamErrorTypeDef" = dataclasses.field()

    Message = field("Message")
    ErrorCode = field("ErrorCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ModelStreamErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModelStreamErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PayloadPart:
    boto3_raw_data: "type_defs.PayloadPartTypeDef" = dataclasses.field()

    Bytes = field("Bytes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PayloadPartTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PayloadPartTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvokeEndpointInput:
    boto3_raw_data: "type_defs.InvokeEndpointInputTypeDef" = dataclasses.field()

    EndpointName = field("EndpointName")
    Body = field("Body")
    ContentType = field("ContentType")
    Accept = field("Accept")
    CustomAttributes = field("CustomAttributes")
    TargetModel = field("TargetModel")
    TargetVariant = field("TargetVariant")
    TargetContainerHostname = field("TargetContainerHostname")
    InferenceId = field("InferenceId")
    EnableExplanations = field("EnableExplanations")
    InferenceComponentName = field("InferenceComponentName")
    SessionId = field("SessionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvokeEndpointInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokeEndpointInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvokeEndpointWithResponseStreamInput:
    boto3_raw_data: "type_defs.InvokeEndpointWithResponseStreamInputTypeDef" = (
        dataclasses.field()
    )

    EndpointName = field("EndpointName")
    Body = field("Body")
    ContentType = field("ContentType")
    Accept = field("Accept")
    CustomAttributes = field("CustomAttributes")
    TargetVariant = field("TargetVariant")
    TargetContainerHostname = field("TargetContainerHostname")
    InferenceId = field("InferenceId")
    InferenceComponentName = field("InferenceComponentName")
    SessionId = field("SessionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InvokeEndpointWithResponseStreamInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokeEndpointWithResponseStreamInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvokeEndpointAsyncOutput:
    boto3_raw_data: "type_defs.InvokeEndpointAsyncOutputTypeDef" = dataclasses.field()

    InferenceId = field("InferenceId")
    OutputLocation = field("OutputLocation")
    FailureLocation = field("FailureLocation")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvokeEndpointAsyncOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokeEndpointAsyncOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvokeEndpointOutput:
    boto3_raw_data: "type_defs.InvokeEndpointOutputTypeDef" = dataclasses.field()

    Body = field("Body")
    ContentType = field("ContentType")
    InvokedProductionVariant = field("InvokedProductionVariant")
    CustomAttributes = field("CustomAttributes")
    NewSessionId = field("NewSessionId")
    ClosedSessionId = field("ClosedSessionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvokeEndpointOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokeEndpointOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseStream:
    boto3_raw_data: "type_defs.ResponseStreamTypeDef" = dataclasses.field()

    @cached_property
    def PayloadPart(self):  # pragma: no cover
        return PayloadPart.make_one(self.boto3_raw_data["PayloadPart"])

    @cached_property
    def ModelStreamError(self):  # pragma: no cover
        return ModelStreamError.make_one(self.boto3_raw_data["ModelStreamError"])

    @cached_property
    def InternalStreamFailure(self):  # pragma: no cover
        return InternalStreamFailure.make_one(
            self.boto3_raw_data["InternalStreamFailure"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResponseStreamTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResponseStreamTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvokeEndpointWithResponseStreamOutput:
    boto3_raw_data: "type_defs.InvokeEndpointWithResponseStreamOutputTypeDef" = (
        dataclasses.field()
    )

    Body = field("Body")
    ContentType = field("ContentType")
    InvokedProductionVariant = field("InvokedProductionVariant")
    CustomAttributes = field("CustomAttributes")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InvokeEndpointWithResponseStreamOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokeEndpointWithResponseStreamOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
