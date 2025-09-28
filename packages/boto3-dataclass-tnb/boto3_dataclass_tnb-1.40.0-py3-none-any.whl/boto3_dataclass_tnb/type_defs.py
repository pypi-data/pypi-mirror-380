# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_tnb import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class CancelSolNetworkOperationInput:
    boto3_raw_data: "type_defs.CancelSolNetworkOperationInputTypeDef" = (
        dataclasses.field()
    )

    nsLcmOpOccId = field("nsLcmOpOccId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CancelSolNetworkOperationInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelSolNetworkOperationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSolFunctionPackageInput:
    boto3_raw_data: "type_defs.CreateSolFunctionPackageInputTypeDef" = (
        dataclasses.field()
    )

    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateSolFunctionPackageInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSolFunctionPackageInputTypeDef"]
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
class CreateSolNetworkInstanceInput:
    boto3_raw_data: "type_defs.CreateSolNetworkInstanceInputTypeDef" = (
        dataclasses.field()
    )

    nsName = field("nsName")
    nsdInfoId = field("nsdInfoId")
    nsDescription = field("nsDescription")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateSolNetworkInstanceInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSolNetworkInstanceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSolNetworkPackageInput:
    boto3_raw_data: "type_defs.CreateSolNetworkPackageInputTypeDef" = (
        dataclasses.field()
    )

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSolNetworkPackageInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSolNetworkPackageInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSolFunctionPackageInput:
    boto3_raw_data: "type_defs.DeleteSolFunctionPackageInputTypeDef" = (
        dataclasses.field()
    )

    vnfPkgId = field("vnfPkgId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteSolFunctionPackageInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSolFunctionPackageInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSolNetworkInstanceInput:
    boto3_raw_data: "type_defs.DeleteSolNetworkInstanceInputTypeDef" = (
        dataclasses.field()
    )

    nsInstanceId = field("nsInstanceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteSolNetworkInstanceInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSolNetworkInstanceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSolNetworkPackageInput:
    boto3_raw_data: "type_defs.DeleteSolNetworkPackageInputTypeDef" = (
        dataclasses.field()
    )

    nsdInfoId = field("nsdInfoId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSolNetworkPackageInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSolNetworkPackageInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ErrorInfo:
    boto3_raw_data: "type_defs.ErrorInfoTypeDef" = dataclasses.field()

    cause = field("cause")
    details = field("details")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ErrorInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ErrorInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ToscaOverride:
    boto3_raw_data: "type_defs.ToscaOverrideTypeDef" = dataclasses.field()

    defaultValue = field("defaultValue")
    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ToscaOverrideTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ToscaOverrideTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSolFunctionInstanceInput:
    boto3_raw_data: "type_defs.GetSolFunctionInstanceInputTypeDef" = dataclasses.field()

    vnfInstanceId = field("vnfInstanceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSolFunctionInstanceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSolFunctionInstanceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSolFunctionInstanceMetadata:
    boto3_raw_data: "type_defs.GetSolFunctionInstanceMetadataTypeDef" = (
        dataclasses.field()
    )

    createdAt = field("createdAt")
    lastModified = field("lastModified")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetSolFunctionInstanceMetadataTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSolFunctionInstanceMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSolFunctionPackageContentInput:
    boto3_raw_data: "type_defs.GetSolFunctionPackageContentInputTypeDef" = (
        dataclasses.field()
    )

    accept = field("accept")
    vnfPkgId = field("vnfPkgId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSolFunctionPackageContentInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSolFunctionPackageContentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSolFunctionPackageDescriptorInput:
    boto3_raw_data: "type_defs.GetSolFunctionPackageDescriptorInputTypeDef" = (
        dataclasses.field()
    )

    accept = field("accept")
    vnfPkgId = field("vnfPkgId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSolFunctionPackageDescriptorInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSolFunctionPackageDescriptorInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSolFunctionPackageInput:
    boto3_raw_data: "type_defs.GetSolFunctionPackageInputTypeDef" = dataclasses.field()

    vnfPkgId = field("vnfPkgId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSolFunctionPackageInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSolFunctionPackageInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSolInstantiatedVnfInfo:
    boto3_raw_data: "type_defs.GetSolInstantiatedVnfInfoTypeDef" = dataclasses.field()

    vnfState = field("vnfState")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSolInstantiatedVnfInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSolInstantiatedVnfInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSolNetworkInstanceInput:
    boto3_raw_data: "type_defs.GetSolNetworkInstanceInputTypeDef" = dataclasses.field()

    nsInstanceId = field("nsInstanceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSolNetworkInstanceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSolNetworkInstanceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSolNetworkInstanceMetadata:
    boto3_raw_data: "type_defs.GetSolNetworkInstanceMetadataTypeDef" = (
        dataclasses.field()
    )

    createdAt = field("createdAt")
    lastModified = field("lastModified")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetSolNetworkInstanceMetadataTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSolNetworkInstanceMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LcmOperationInfo:
    boto3_raw_data: "type_defs.LcmOperationInfoTypeDef" = dataclasses.field()

    nsLcmOpOccId = field("nsLcmOpOccId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LcmOperationInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LcmOperationInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSolNetworkOperationInput:
    boto3_raw_data: "type_defs.GetSolNetworkOperationInputTypeDef" = dataclasses.field()

    nsLcmOpOccId = field("nsLcmOpOccId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSolNetworkOperationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSolNetworkOperationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstantiateMetadata:
    boto3_raw_data: "type_defs.InstantiateMetadataTypeDef" = dataclasses.field()

    nsdInfoId = field("nsdInfoId")
    additionalParamsForNs = field("additionalParamsForNs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstantiateMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstantiateMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyVnfInfoMetadata:
    boto3_raw_data: "type_defs.ModifyVnfInfoMetadataTypeDef" = dataclasses.field()

    vnfConfigurableProperties = field("vnfConfigurableProperties")
    vnfInstanceId = field("vnfInstanceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyVnfInfoMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyVnfInfoMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateNsMetadata:
    boto3_raw_data: "type_defs.UpdateNsMetadataTypeDef" = dataclasses.field()

    nsdInfoId = field("nsdInfoId")
    additionalParamsForNs = field("additionalParamsForNs")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateNsMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateNsMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProblemDetails:
    boto3_raw_data: "type_defs.ProblemDetailsTypeDef" = dataclasses.field()

    detail = field("detail")
    title = field("title")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProblemDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProblemDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSolNetworkPackageContentInput:
    boto3_raw_data: "type_defs.GetSolNetworkPackageContentInputTypeDef" = (
        dataclasses.field()
    )

    accept = field("accept")
    nsdInfoId = field("nsdInfoId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetSolNetworkPackageContentInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSolNetworkPackageContentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSolNetworkPackageDescriptorInput:
    boto3_raw_data: "type_defs.GetSolNetworkPackageDescriptorInputTypeDef" = (
        dataclasses.field()
    )

    nsdInfoId = field("nsdInfoId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSolNetworkPackageDescriptorInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSolNetworkPackageDescriptorInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSolNetworkPackageInput:
    boto3_raw_data: "type_defs.GetSolNetworkPackageInputTypeDef" = dataclasses.field()

    nsdInfoId = field("nsdInfoId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSolNetworkPackageInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSolNetworkPackageInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSolVnfcResourceInfoMetadata:
    boto3_raw_data: "type_defs.GetSolVnfcResourceInfoMetadataTypeDef" = (
        dataclasses.field()
    )

    cluster = field("cluster")
    helmChart = field("helmChart")
    nodeGroup = field("nodeGroup")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetSolVnfcResourceInfoMetadataTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSolVnfcResourceInfoMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstantiateSolNetworkInstanceInput:
    boto3_raw_data: "type_defs.InstantiateSolNetworkInstanceInputTypeDef" = (
        dataclasses.field()
    )

    nsInstanceId = field("nsInstanceId")
    additionalParamsForNs = field("additionalParamsForNs")
    dryRun = field("dryRun")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InstantiateSolNetworkInstanceInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstantiateSolNetworkInstanceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSolFunctionInstanceMetadata:
    boto3_raw_data: "type_defs.ListSolFunctionInstanceMetadataTypeDef" = (
        dataclasses.field()
    )

    createdAt = field("createdAt")
    lastModified = field("lastModified")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSolFunctionInstanceMetadataTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSolFunctionInstanceMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PaginatorConfig:
    boto3_raw_data: "type_defs.PaginatorConfigTypeDef" = dataclasses.field()

    MaxItems = field("MaxItems")
    PageSize = field("PageSize")
    StartingToken = field("StartingToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PaginatorConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PaginatorConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSolFunctionInstancesInput:
    boto3_raw_data: "type_defs.ListSolFunctionInstancesInputTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSolFunctionInstancesInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSolFunctionInstancesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSolFunctionPackageMetadata:
    boto3_raw_data: "type_defs.ListSolFunctionPackageMetadataTypeDef" = (
        dataclasses.field()
    )

    createdAt = field("createdAt")
    lastModified = field("lastModified")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSolFunctionPackageMetadataTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSolFunctionPackageMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSolFunctionPackagesInput:
    boto3_raw_data: "type_defs.ListSolFunctionPackagesInputTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSolFunctionPackagesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSolFunctionPackagesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSolNetworkInstanceMetadata:
    boto3_raw_data: "type_defs.ListSolNetworkInstanceMetadataTypeDef" = (
        dataclasses.field()
    )

    createdAt = field("createdAt")
    lastModified = field("lastModified")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSolNetworkInstanceMetadataTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSolNetworkInstanceMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSolNetworkInstancesInput:
    boto3_raw_data: "type_defs.ListSolNetworkInstancesInputTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSolNetworkInstancesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSolNetworkInstancesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSolNetworkOperationsMetadata:
    boto3_raw_data: "type_defs.ListSolNetworkOperationsMetadataTypeDef" = (
        dataclasses.field()
    )

    createdAt = field("createdAt")
    lastModified = field("lastModified")
    nsdInfoId = field("nsdInfoId")
    vnfInstanceId = field("vnfInstanceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSolNetworkOperationsMetadataTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSolNetworkOperationsMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSolNetworkOperationsInput:
    boto3_raw_data: "type_defs.ListSolNetworkOperationsInputTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    nsInstanceId = field("nsInstanceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSolNetworkOperationsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSolNetworkOperationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSolNetworkPackageMetadata:
    boto3_raw_data: "type_defs.ListSolNetworkPackageMetadataTypeDef" = (
        dataclasses.field()
    )

    createdAt = field("createdAt")
    lastModified = field("lastModified")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSolNetworkPackageMetadataTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSolNetworkPackageMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSolNetworkPackagesInput:
    boto3_raw_data: "type_defs.ListSolNetworkPackagesInputTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSolNetworkPackagesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSolNetworkPackagesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceInput:
    boto3_raw_data: "type_defs.ListTagsForResourceInputTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceInput:
    boto3_raw_data: "type_defs.TagResourceInputTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagResourceInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TerminateSolNetworkInstanceInput:
    boto3_raw_data: "type_defs.TerminateSolNetworkInstanceInputTypeDef" = (
        dataclasses.field()
    )

    nsInstanceId = field("nsInstanceId")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TerminateSolNetworkInstanceInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TerminateSolNetworkInstanceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceInput:
    boto3_raw_data: "type_defs.UntagResourceInputTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    tagKeys = field("tagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSolFunctionPackageInput:
    boto3_raw_data: "type_defs.UpdateSolFunctionPackageInputTypeDef" = (
        dataclasses.field()
    )

    operationalState = field("operationalState")
    vnfPkgId = field("vnfPkgId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateSolFunctionPackageInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSolFunctionPackageInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSolNetworkModify:
    boto3_raw_data: "type_defs.UpdateSolNetworkModifyTypeDef" = dataclasses.field()

    vnfConfigurableProperties = field("vnfConfigurableProperties")
    vnfInstanceId = field("vnfInstanceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSolNetworkModifyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSolNetworkModifyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSolNetworkServiceData:
    boto3_raw_data: "type_defs.UpdateSolNetworkServiceDataTypeDef" = dataclasses.field()

    nsdInfoId = field("nsdInfoId")
    additionalParamsForNs = field("additionalParamsForNs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSolNetworkServiceDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSolNetworkServiceDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSolNetworkPackageInput:
    boto3_raw_data: "type_defs.UpdateSolNetworkPackageInputTypeDef" = (
        dataclasses.field()
    )

    nsdInfoId = field("nsdInfoId")
    nsdOperationalState = field("nsdOperationalState")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSolNetworkPackageInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSolNetworkPackageInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutSolFunctionPackageContentInput:
    boto3_raw_data: "type_defs.PutSolFunctionPackageContentInputTypeDef" = (
        dataclasses.field()
    )

    file = field("file")
    vnfPkgId = field("vnfPkgId")
    contentType = field("contentType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutSolFunctionPackageContentInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutSolFunctionPackageContentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutSolNetworkPackageContentInput:
    boto3_raw_data: "type_defs.PutSolNetworkPackageContentInputTypeDef" = (
        dataclasses.field()
    )

    file = field("file")
    nsdInfoId = field("nsdInfoId")
    contentType = field("contentType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutSolNetworkPackageContentInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutSolNetworkPackageContentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidateSolFunctionPackageContentInput:
    boto3_raw_data: "type_defs.ValidateSolFunctionPackageContentInputTypeDef" = (
        dataclasses.field()
    )

    file = field("file")
    vnfPkgId = field("vnfPkgId")
    contentType = field("contentType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ValidateSolFunctionPackageContentInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidateSolFunctionPackageContentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidateSolNetworkPackageContentInput:
    boto3_raw_data: "type_defs.ValidateSolNetworkPackageContentInputTypeDef" = (
        dataclasses.field()
    )

    file = field("file")
    nsdInfoId = field("nsdInfoId")
    contentType = field("contentType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ValidateSolNetworkPackageContentInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidateSolNetworkPackageContentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSolFunctionPackageOutput:
    boto3_raw_data: "type_defs.CreateSolFunctionPackageOutputTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    id = field("id")
    onboardingState = field("onboardingState")
    operationalState = field("operationalState")
    tags = field("tags")
    usageState = field("usageState")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateSolFunctionPackageOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSolFunctionPackageOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSolNetworkInstanceOutput:
    boto3_raw_data: "type_defs.CreateSolNetworkInstanceOutputTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    id = field("id")
    nsInstanceName = field("nsInstanceName")
    nsdInfoId = field("nsdInfoId")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateSolNetworkInstanceOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSolNetworkInstanceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSolNetworkPackageOutput:
    boto3_raw_data: "type_defs.CreateSolNetworkPackageOutputTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    id = field("id")
    nsdOnboardingState = field("nsdOnboardingState")
    nsdOperationalState = field("nsdOperationalState")
    nsdUsageState = field("nsdUsageState")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateSolNetworkPackageOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSolNetworkPackageOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmptyResponseMetadata:
    boto3_raw_data: "type_defs.EmptyResponseMetadataTypeDef" = dataclasses.field()

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmptyResponseMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmptyResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSolFunctionPackageContentOutput:
    boto3_raw_data: "type_defs.GetSolFunctionPackageContentOutputTypeDef" = (
        dataclasses.field()
    )

    contentType = field("contentType")
    packageContent = field("packageContent")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSolFunctionPackageContentOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSolFunctionPackageContentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSolFunctionPackageDescriptorOutput:
    boto3_raw_data: "type_defs.GetSolFunctionPackageDescriptorOutputTypeDef" = (
        dataclasses.field()
    )

    contentType = field("contentType")
    vnfd = field("vnfd")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSolFunctionPackageDescriptorOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSolFunctionPackageDescriptorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSolNetworkPackageContentOutput:
    boto3_raw_data: "type_defs.GetSolNetworkPackageContentOutputTypeDef" = (
        dataclasses.field()
    )

    contentType = field("contentType")
    nsdContent = field("nsdContent")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSolNetworkPackageContentOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSolNetworkPackageContentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSolNetworkPackageDescriptorOutput:
    boto3_raw_data: "type_defs.GetSolNetworkPackageDescriptorOutputTypeDef" = (
        dataclasses.field()
    )

    contentType = field("contentType")
    nsd = field("nsd")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSolNetworkPackageDescriptorOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSolNetworkPackageDescriptorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstantiateSolNetworkInstanceOutput:
    boto3_raw_data: "type_defs.InstantiateSolNetworkInstanceOutputTypeDef" = (
        dataclasses.field()
    )

    nsLcmOpOccId = field("nsLcmOpOccId")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InstantiateSolNetworkInstanceOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstantiateSolNetworkInstanceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceOutput:
    boto3_raw_data: "type_defs.ListTagsForResourceOutputTypeDef" = dataclasses.field()

    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TerminateSolNetworkInstanceOutput:
    boto3_raw_data: "type_defs.TerminateSolNetworkInstanceOutputTypeDef" = (
        dataclasses.field()
    )

    nsLcmOpOccId = field("nsLcmOpOccId")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TerminateSolNetworkInstanceOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TerminateSolNetworkInstanceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSolFunctionPackageOutput:
    boto3_raw_data: "type_defs.UpdateSolFunctionPackageOutputTypeDef" = (
        dataclasses.field()
    )

    operationalState = field("operationalState")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateSolFunctionPackageOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSolFunctionPackageOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSolNetworkInstanceOutput:
    boto3_raw_data: "type_defs.UpdateSolNetworkInstanceOutputTypeDef" = (
        dataclasses.field()
    )

    nsLcmOpOccId = field("nsLcmOpOccId")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateSolNetworkInstanceOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSolNetworkInstanceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSolNetworkPackageOutput:
    boto3_raw_data: "type_defs.UpdateSolNetworkPackageOutputTypeDef" = (
        dataclasses.field()
    )

    nsdOperationalState = field("nsdOperationalState")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateSolNetworkPackageOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSolNetworkPackageOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSolNetworkOperationTaskDetails:
    boto3_raw_data: "type_defs.GetSolNetworkOperationTaskDetailsTypeDef" = (
        dataclasses.field()
    )

    taskContext = field("taskContext")
    taskEndTime = field("taskEndTime")

    @cached_property
    def taskErrorDetails(self):  # pragma: no cover
        return ErrorInfo.make_one(self.boto3_raw_data["taskErrorDetails"])

    taskName = field("taskName")
    taskStartTime = field("taskStartTime")
    taskStatus = field("taskStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSolNetworkOperationTaskDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSolNetworkOperationTaskDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionArtifactMeta:
    boto3_raw_data: "type_defs.FunctionArtifactMetaTypeDef" = dataclasses.field()

    @cached_property
    def overrides(self):  # pragma: no cover
        return ToscaOverride.make_many(self.boto3_raw_data["overrides"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FunctionArtifactMetaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FunctionArtifactMetaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkArtifactMeta:
    boto3_raw_data: "type_defs.NetworkArtifactMetaTypeDef" = dataclasses.field()

    @cached_property
    def overrides(self):  # pragma: no cover
        return ToscaOverride.make_many(self.boto3_raw_data["overrides"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkArtifactMetaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkArtifactMetaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSolNetworkInstanceOutput:
    boto3_raw_data: "type_defs.GetSolNetworkInstanceOutputTypeDef" = dataclasses.field()

    arn = field("arn")
    id = field("id")

    @cached_property
    def lcmOpInfo(self):  # pragma: no cover
        return LcmOperationInfo.make_one(self.boto3_raw_data["lcmOpInfo"])

    @cached_property
    def metadata(self):  # pragma: no cover
        return GetSolNetworkInstanceMetadata.make_one(self.boto3_raw_data["metadata"])

    nsInstanceDescription = field("nsInstanceDescription")
    nsInstanceName = field("nsInstanceName")
    nsState = field("nsState")
    nsdId = field("nsdId")
    nsdInfoId = field("nsdInfoId")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSolNetworkInstanceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSolNetworkInstanceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSolNetworkOperationMetadata:
    boto3_raw_data: "type_defs.GetSolNetworkOperationMetadataTypeDef" = (
        dataclasses.field()
    )

    createdAt = field("createdAt")
    lastModified = field("lastModified")

    @cached_property
    def instantiateMetadata(self):  # pragma: no cover
        return InstantiateMetadata.make_one(self.boto3_raw_data["instantiateMetadata"])

    @cached_property
    def modifyVnfInfoMetadata(self):  # pragma: no cover
        return ModifyVnfInfoMetadata.make_one(
            self.boto3_raw_data["modifyVnfInfoMetadata"]
        )

    @cached_property
    def updateNsMetadata(self):  # pragma: no cover
        return UpdateNsMetadata.make_one(self.boto3_raw_data["updateNsMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetSolNetworkOperationMetadataTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSolNetworkOperationMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSolVnfcResourceInfo:
    boto3_raw_data: "type_defs.GetSolVnfcResourceInfoTypeDef" = dataclasses.field()

    @cached_property
    def metadata(self):  # pragma: no cover
        return GetSolVnfcResourceInfoMetadata.make_one(self.boto3_raw_data["metadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSolVnfcResourceInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSolVnfcResourceInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSolFunctionInstanceInfo:
    boto3_raw_data: "type_defs.ListSolFunctionInstanceInfoTypeDef" = dataclasses.field()

    arn = field("arn")
    id = field("id")
    instantiationState = field("instantiationState")

    @cached_property
    def metadata(self):  # pragma: no cover
        return ListSolFunctionInstanceMetadata.make_one(self.boto3_raw_data["metadata"])

    nsInstanceId = field("nsInstanceId")
    vnfPkgId = field("vnfPkgId")

    @cached_property
    def instantiatedVnfInfo(self):  # pragma: no cover
        return GetSolInstantiatedVnfInfo.make_one(
            self.boto3_raw_data["instantiatedVnfInfo"]
        )

    vnfPkgName = field("vnfPkgName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSolFunctionInstanceInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSolFunctionInstanceInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSolFunctionInstancesInputPaginate:
    boto3_raw_data: "type_defs.ListSolFunctionInstancesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSolFunctionInstancesInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSolFunctionInstancesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSolFunctionPackagesInputPaginate:
    boto3_raw_data: "type_defs.ListSolFunctionPackagesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSolFunctionPackagesInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSolFunctionPackagesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSolNetworkInstancesInputPaginate:
    boto3_raw_data: "type_defs.ListSolNetworkInstancesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSolNetworkInstancesInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSolNetworkInstancesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSolNetworkOperationsInputPaginate:
    boto3_raw_data: "type_defs.ListSolNetworkOperationsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    nsInstanceId = field("nsInstanceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSolNetworkOperationsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSolNetworkOperationsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSolNetworkPackagesInputPaginate:
    boto3_raw_data: "type_defs.ListSolNetworkPackagesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSolNetworkPackagesInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSolNetworkPackagesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSolFunctionPackageInfo:
    boto3_raw_data: "type_defs.ListSolFunctionPackageInfoTypeDef" = dataclasses.field()

    arn = field("arn")
    id = field("id")
    onboardingState = field("onboardingState")
    operationalState = field("operationalState")
    usageState = field("usageState")

    @cached_property
    def metadata(self):  # pragma: no cover
        return ListSolFunctionPackageMetadata.make_one(self.boto3_raw_data["metadata"])

    vnfProductName = field("vnfProductName")
    vnfProvider = field("vnfProvider")
    vnfdId = field("vnfdId")
    vnfdVersion = field("vnfdVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSolFunctionPackageInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSolFunctionPackageInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSolNetworkInstanceInfo:
    boto3_raw_data: "type_defs.ListSolNetworkInstanceInfoTypeDef" = dataclasses.field()

    arn = field("arn")
    id = field("id")

    @cached_property
    def metadata(self):  # pragma: no cover
        return ListSolNetworkInstanceMetadata.make_one(self.boto3_raw_data["metadata"])

    nsInstanceDescription = field("nsInstanceDescription")
    nsInstanceName = field("nsInstanceName")
    nsState = field("nsState")
    nsdId = field("nsdId")
    nsdInfoId = field("nsdInfoId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSolNetworkInstanceInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSolNetworkInstanceInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSolNetworkOperationsInfo:
    boto3_raw_data: "type_defs.ListSolNetworkOperationsInfoTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    id = field("id")
    lcmOperationType = field("lcmOperationType")
    nsInstanceId = field("nsInstanceId")
    operationState = field("operationState")

    @cached_property
    def error(self):  # pragma: no cover
        return ProblemDetails.make_one(self.boto3_raw_data["error"])

    @cached_property
    def metadata(self):  # pragma: no cover
        return ListSolNetworkOperationsMetadata.make_one(
            self.boto3_raw_data["metadata"]
        )

    updateType = field("updateType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSolNetworkOperationsInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSolNetworkOperationsInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSolNetworkPackageInfo:
    boto3_raw_data: "type_defs.ListSolNetworkPackageInfoTypeDef" = dataclasses.field()

    arn = field("arn")
    id = field("id")

    @cached_property
    def metadata(self):  # pragma: no cover
        return ListSolNetworkPackageMetadata.make_one(self.boto3_raw_data["metadata"])

    nsdOnboardingState = field("nsdOnboardingState")
    nsdOperationalState = field("nsdOperationalState")
    nsdUsageState = field("nsdUsageState")
    nsdDesigner = field("nsdDesigner")
    nsdId = field("nsdId")
    nsdInvariantId = field("nsdInvariantId")
    nsdName = field("nsdName")
    nsdVersion = field("nsdVersion")
    vnfPkgIds = field("vnfPkgIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSolNetworkPackageInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSolNetworkPackageInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSolNetworkInstanceInput:
    boto3_raw_data: "type_defs.UpdateSolNetworkInstanceInputTypeDef" = (
        dataclasses.field()
    )

    nsInstanceId = field("nsInstanceId")
    updateType = field("updateType")

    @cached_property
    def modifyVnfInfoData(self):  # pragma: no cover
        return UpdateSolNetworkModify.make_one(self.boto3_raw_data["modifyVnfInfoData"])

    tags = field("tags")

    @cached_property
    def updateNs(self):  # pragma: no cover
        return UpdateSolNetworkServiceData.make_one(self.boto3_raw_data["updateNs"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateSolNetworkInstanceInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSolNetworkInstanceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSolFunctionPackageMetadata:
    boto3_raw_data: "type_defs.GetSolFunctionPackageMetadataTypeDef" = (
        dataclasses.field()
    )

    createdAt = field("createdAt")
    lastModified = field("lastModified")

    @cached_property
    def vnfd(self):  # pragma: no cover
        return FunctionArtifactMeta.make_one(self.boto3_raw_data["vnfd"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetSolFunctionPackageMetadataTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSolFunctionPackageMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutSolFunctionPackageContentMetadata:
    boto3_raw_data: "type_defs.PutSolFunctionPackageContentMetadataTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def vnfd(self):  # pragma: no cover
        return FunctionArtifactMeta.make_one(self.boto3_raw_data["vnfd"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutSolFunctionPackageContentMetadataTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutSolFunctionPackageContentMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidateSolFunctionPackageContentMetadata:
    boto3_raw_data: "type_defs.ValidateSolFunctionPackageContentMetadataTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def vnfd(self):  # pragma: no cover
        return FunctionArtifactMeta.make_one(self.boto3_raw_data["vnfd"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ValidateSolFunctionPackageContentMetadataTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidateSolFunctionPackageContentMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSolNetworkPackageMetadata:
    boto3_raw_data: "type_defs.GetSolNetworkPackageMetadataTypeDef" = (
        dataclasses.field()
    )

    createdAt = field("createdAt")
    lastModified = field("lastModified")

    @cached_property
    def nsd(self):  # pragma: no cover
        return NetworkArtifactMeta.make_one(self.boto3_raw_data["nsd"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSolNetworkPackageMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSolNetworkPackageMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutSolNetworkPackageContentMetadata:
    boto3_raw_data: "type_defs.PutSolNetworkPackageContentMetadataTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def nsd(self):  # pragma: no cover
        return NetworkArtifactMeta.make_one(self.boto3_raw_data["nsd"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutSolNetworkPackageContentMetadataTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutSolNetworkPackageContentMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidateSolNetworkPackageContentMetadata:
    boto3_raw_data: "type_defs.ValidateSolNetworkPackageContentMetadataTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def nsd(self):  # pragma: no cover
        return NetworkArtifactMeta.make_one(self.boto3_raw_data["nsd"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ValidateSolNetworkPackageContentMetadataTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidateSolNetworkPackageContentMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSolNetworkOperationOutput:
    boto3_raw_data: "type_defs.GetSolNetworkOperationOutputTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")

    @cached_property
    def error(self):  # pragma: no cover
        return ProblemDetails.make_one(self.boto3_raw_data["error"])

    id = field("id")
    lcmOperationType = field("lcmOperationType")

    @cached_property
    def metadata(self):  # pragma: no cover
        return GetSolNetworkOperationMetadata.make_one(self.boto3_raw_data["metadata"])

    nsInstanceId = field("nsInstanceId")
    operationState = field("operationState")
    tags = field("tags")

    @cached_property
    def tasks(self):  # pragma: no cover
        return GetSolNetworkOperationTaskDetails.make_many(self.boto3_raw_data["tasks"])

    updateType = field("updateType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSolNetworkOperationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSolNetworkOperationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSolVnfInfo:
    boto3_raw_data: "type_defs.GetSolVnfInfoTypeDef" = dataclasses.field()

    vnfState = field("vnfState")

    @cached_property
    def vnfcResourceInfo(self):  # pragma: no cover
        return GetSolVnfcResourceInfo.make_many(self.boto3_raw_data["vnfcResourceInfo"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetSolVnfInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetSolVnfInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSolFunctionInstancesOutput:
    boto3_raw_data: "type_defs.ListSolFunctionInstancesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def functionInstances(self):  # pragma: no cover
        return ListSolFunctionInstanceInfo.make_many(
            self.boto3_raw_data["functionInstances"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSolFunctionInstancesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSolFunctionInstancesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSolFunctionPackagesOutput:
    boto3_raw_data: "type_defs.ListSolFunctionPackagesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def functionPackages(self):  # pragma: no cover
        return ListSolFunctionPackageInfo.make_many(
            self.boto3_raw_data["functionPackages"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSolFunctionPackagesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSolFunctionPackagesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSolNetworkInstancesOutput:
    boto3_raw_data: "type_defs.ListSolNetworkInstancesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def networkInstances(self):  # pragma: no cover
        return ListSolNetworkInstanceInfo.make_many(
            self.boto3_raw_data["networkInstances"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSolNetworkInstancesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSolNetworkInstancesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSolNetworkOperationsOutput:
    boto3_raw_data: "type_defs.ListSolNetworkOperationsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def networkOperations(self):  # pragma: no cover
        return ListSolNetworkOperationsInfo.make_many(
            self.boto3_raw_data["networkOperations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSolNetworkOperationsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSolNetworkOperationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSolNetworkPackagesOutput:
    boto3_raw_data: "type_defs.ListSolNetworkPackagesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def networkPackages(self):  # pragma: no cover
        return ListSolNetworkPackageInfo.make_many(
            self.boto3_raw_data["networkPackages"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSolNetworkPackagesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSolNetworkPackagesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSolFunctionPackageOutput:
    boto3_raw_data: "type_defs.GetSolFunctionPackageOutputTypeDef" = dataclasses.field()

    arn = field("arn")
    id = field("id")

    @cached_property
    def metadata(self):  # pragma: no cover
        return GetSolFunctionPackageMetadata.make_one(self.boto3_raw_data["metadata"])

    onboardingState = field("onboardingState")
    operationalState = field("operationalState")
    tags = field("tags")
    usageState = field("usageState")
    vnfProductName = field("vnfProductName")
    vnfProvider = field("vnfProvider")
    vnfdId = field("vnfdId")
    vnfdVersion = field("vnfdVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSolFunctionPackageOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSolFunctionPackageOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutSolFunctionPackageContentOutput:
    boto3_raw_data: "type_defs.PutSolFunctionPackageContentOutputTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @cached_property
    def metadata(self):  # pragma: no cover
        return PutSolFunctionPackageContentMetadata.make_one(
            self.boto3_raw_data["metadata"]
        )

    vnfProductName = field("vnfProductName")
    vnfProvider = field("vnfProvider")
    vnfdId = field("vnfdId")
    vnfdVersion = field("vnfdVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutSolFunctionPackageContentOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutSolFunctionPackageContentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidateSolFunctionPackageContentOutput:
    boto3_raw_data: "type_defs.ValidateSolFunctionPackageContentOutputTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @cached_property
    def metadata(self):  # pragma: no cover
        return ValidateSolFunctionPackageContentMetadata.make_one(
            self.boto3_raw_data["metadata"]
        )

    vnfProductName = field("vnfProductName")
    vnfProvider = field("vnfProvider")
    vnfdId = field("vnfdId")
    vnfdVersion = field("vnfdVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ValidateSolFunctionPackageContentOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidateSolFunctionPackageContentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSolNetworkPackageOutput:
    boto3_raw_data: "type_defs.GetSolNetworkPackageOutputTypeDef" = dataclasses.field()

    arn = field("arn")
    id = field("id")

    @cached_property
    def metadata(self):  # pragma: no cover
        return GetSolNetworkPackageMetadata.make_one(self.boto3_raw_data["metadata"])

    nsdId = field("nsdId")
    nsdName = field("nsdName")
    nsdOnboardingState = field("nsdOnboardingState")
    nsdOperationalState = field("nsdOperationalState")
    nsdUsageState = field("nsdUsageState")
    nsdVersion = field("nsdVersion")
    tags = field("tags")
    vnfPkgIds = field("vnfPkgIds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSolNetworkPackageOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSolNetworkPackageOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutSolNetworkPackageContentOutput:
    boto3_raw_data: "type_defs.PutSolNetworkPackageContentOutputTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    id = field("id")

    @cached_property
    def metadata(self):  # pragma: no cover
        return PutSolNetworkPackageContentMetadata.make_one(
            self.boto3_raw_data["metadata"]
        )

    nsdId = field("nsdId")
    nsdName = field("nsdName")
    nsdVersion = field("nsdVersion")
    vnfPkgIds = field("vnfPkgIds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutSolNetworkPackageContentOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutSolNetworkPackageContentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidateSolNetworkPackageContentOutput:
    boto3_raw_data: "type_defs.ValidateSolNetworkPackageContentOutputTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    id = field("id")

    @cached_property
    def metadata(self):  # pragma: no cover
        return ValidateSolNetworkPackageContentMetadata.make_one(
            self.boto3_raw_data["metadata"]
        )

    nsdId = field("nsdId")
    nsdName = field("nsdName")
    nsdVersion = field("nsdVersion")
    vnfPkgIds = field("vnfPkgIds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ValidateSolNetworkPackageContentOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidateSolNetworkPackageContentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSolFunctionInstanceOutput:
    boto3_raw_data: "type_defs.GetSolFunctionInstanceOutputTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    id = field("id")

    @cached_property
    def instantiatedVnfInfo(self):  # pragma: no cover
        return GetSolVnfInfo.make_one(self.boto3_raw_data["instantiatedVnfInfo"])

    instantiationState = field("instantiationState")

    @cached_property
    def metadata(self):  # pragma: no cover
        return GetSolFunctionInstanceMetadata.make_one(self.boto3_raw_data["metadata"])

    nsInstanceId = field("nsInstanceId")
    tags = field("tags")
    vnfPkgId = field("vnfPkgId")
    vnfProductName = field("vnfProductName")
    vnfProvider = field("vnfProvider")
    vnfdId = field("vnfdId")
    vnfdVersion = field("vnfdVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSolFunctionInstanceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSolFunctionInstanceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
