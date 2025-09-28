# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_service_quotas import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class CreateSupportCaseRequest:
    boto3_raw_data: "type_defs.CreateSupportCaseRequestTypeDef" = dataclasses.field()

    RequestId = field("RequestId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSupportCaseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSupportCaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServiceQuotaIncreaseRequestFromTemplateRequest:
    boto3_raw_data: (
        "type_defs.DeleteServiceQuotaIncreaseRequestFromTemplateRequestTypeDef"
    ) = dataclasses.field()

    ServiceCode = field("ServiceCode")
    QuotaCode = field("QuotaCode")
    AwsRegion = field("AwsRegion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteServiceQuotaIncreaseRequestFromTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DeleteServiceQuotaIncreaseRequestFromTemplateRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ErrorReason:
    boto3_raw_data: "type_defs.ErrorReasonTypeDef" = dataclasses.field()

    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ErrorReasonTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ErrorReasonTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAWSDefaultServiceQuotaRequest:
    boto3_raw_data: "type_defs.GetAWSDefaultServiceQuotaRequestTypeDef" = (
        dataclasses.field()
    )

    ServiceCode = field("ServiceCode")
    QuotaCode = field("QuotaCode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAWSDefaultServiceQuotaRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAWSDefaultServiceQuotaRequestTypeDef"]
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
class GetRequestedServiceQuotaChangeRequest:
    boto3_raw_data: "type_defs.GetRequestedServiceQuotaChangeRequestTypeDef" = (
        dataclasses.field()
    )

    RequestId = field("RequestId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRequestedServiceQuotaChangeRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRequestedServiceQuotaChangeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceQuotaIncreaseRequestFromTemplateRequest:
    boto3_raw_data: (
        "type_defs.GetServiceQuotaIncreaseRequestFromTemplateRequestTypeDef"
    ) = dataclasses.field()

    ServiceCode = field("ServiceCode")
    QuotaCode = field("QuotaCode")
    AwsRegion = field("AwsRegion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetServiceQuotaIncreaseRequestFromTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.GetServiceQuotaIncreaseRequestFromTemplateRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceQuotaIncreaseRequestInTemplate:
    boto3_raw_data: "type_defs.ServiceQuotaIncreaseRequestInTemplateTypeDef" = (
        dataclasses.field()
    )

    ServiceCode = field("ServiceCode")
    ServiceName = field("ServiceName")
    QuotaCode = field("QuotaCode")
    QuotaName = field("QuotaName")
    DesiredValue = field("DesiredValue")
    AwsRegion = field("AwsRegion")
    Unit = field("Unit")
    GlobalQuota = field("GlobalQuota")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServiceQuotaIncreaseRequestInTemplateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceQuotaIncreaseRequestInTemplateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceQuotaRequest:
    boto3_raw_data: "type_defs.GetServiceQuotaRequestTypeDef" = dataclasses.field()

    ServiceCode = field("ServiceCode")
    QuotaCode = field("QuotaCode")
    ContextId = field("ContextId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetServiceQuotaRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceQuotaRequestTypeDef"]
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
class ListAWSDefaultServiceQuotasRequest:
    boto3_raw_data: "type_defs.ListAWSDefaultServiceQuotasRequestTypeDef" = (
        dataclasses.field()
    )

    ServiceCode = field("ServiceCode")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAWSDefaultServiceQuotasRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAWSDefaultServiceQuotasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRequestedServiceQuotaChangeHistoryByQuotaRequest:
    boto3_raw_data: (
        "type_defs.ListRequestedServiceQuotaChangeHistoryByQuotaRequestTypeDef"
    ) = dataclasses.field()

    ServiceCode = field("ServiceCode")
    QuotaCode = field("QuotaCode")
    Status = field("Status")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    QuotaRequestedAtLevel = field("QuotaRequestedAtLevel")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRequestedServiceQuotaChangeHistoryByQuotaRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListRequestedServiceQuotaChangeHistoryByQuotaRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRequestedServiceQuotaChangeHistoryRequest:
    boto3_raw_data: "type_defs.ListRequestedServiceQuotaChangeHistoryRequestTypeDef" = (
        dataclasses.field()
    )

    ServiceCode = field("ServiceCode")
    Status = field("Status")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    QuotaRequestedAtLevel = field("QuotaRequestedAtLevel")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRequestedServiceQuotaChangeHistoryRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRequestedServiceQuotaChangeHistoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceQuotaIncreaseRequestsInTemplateRequest:
    boto3_raw_data: (
        "type_defs.ListServiceQuotaIncreaseRequestsInTemplateRequestTypeDef"
    ) = dataclasses.field()

    ServiceCode = field("ServiceCode")
    AwsRegion = field("AwsRegion")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServiceQuotaIncreaseRequestsInTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListServiceQuotaIncreaseRequestsInTemplateRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceQuotasRequest:
    boto3_raw_data: "type_defs.ListServiceQuotasRequestTypeDef" = dataclasses.field()

    ServiceCode = field("ServiceCode")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    QuotaCode = field("QuotaCode")
    QuotaAppliedAtLevel = field("QuotaAppliedAtLevel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServiceQuotasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceQuotasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServicesRequest:
    boto3_raw_data: "type_defs.ListServicesRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServicesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServicesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceInfo:
    boto3_raw_data: "type_defs.ServiceInfoTypeDef" = dataclasses.field()

    ServiceCode = field("ServiceCode")
    ServiceName = field("ServiceName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServiceInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Tag:
    boto3_raw_data: "type_defs.TagTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricInfo:
    boto3_raw_data: "type_defs.MetricInfoTypeDef" = dataclasses.field()

    MetricNamespace = field("MetricNamespace")
    MetricName = field("MetricName")
    MetricDimensions = field("MetricDimensions")
    MetricStatisticRecommendation = field("MetricStatisticRecommendation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutServiceQuotaIncreaseRequestIntoTemplateRequest:
    boto3_raw_data: (
        "type_defs.PutServiceQuotaIncreaseRequestIntoTemplateRequestTypeDef"
    ) = dataclasses.field()

    QuotaCode = field("QuotaCode")
    ServiceCode = field("ServiceCode")
    AwsRegion = field("AwsRegion")
    DesiredValue = field("DesiredValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutServiceQuotaIncreaseRequestIntoTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.PutServiceQuotaIncreaseRequestIntoTemplateRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QuotaContextInfo:
    boto3_raw_data: "type_defs.QuotaContextInfoTypeDef" = dataclasses.field()

    ContextScope = field("ContextScope")
    ContextScopeType = field("ContextScopeType")
    ContextId = field("ContextId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QuotaContextInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QuotaContextInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QuotaPeriod:
    boto3_raw_data: "type_defs.QuotaPeriodTypeDef" = dataclasses.field()

    PeriodValue = field("PeriodValue")
    PeriodUnit = field("PeriodUnit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QuotaPeriodTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QuotaPeriodTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestServiceQuotaIncreaseRequest:
    boto3_raw_data: "type_defs.RequestServiceQuotaIncreaseRequestTypeDef" = (
        dataclasses.field()
    )

    ServiceCode = field("ServiceCode")
    QuotaCode = field("QuotaCode")
    DesiredValue = field("DesiredValue")
    ContextId = field("ContextId")
    SupportCaseAllowed = field("SupportCaseAllowed")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RequestServiceQuotaIncreaseRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequestServiceQuotaIncreaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAssociationForServiceQuotaTemplateResponse:
    boto3_raw_data: "type_defs.GetAssociationForServiceQuotaTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    ServiceQuotaTemplateAssociationStatus = field(
        "ServiceQuotaTemplateAssociationStatus"
    )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAssociationForServiceQuotaTemplateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAssociationForServiceQuotaTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceQuotaIncreaseRequestFromTemplateResponse:
    boto3_raw_data: (
        "type_defs.GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def ServiceQuotaIncreaseRequestInTemplate(self):  # pragma: no cover
        return ServiceQuotaIncreaseRequestInTemplate.make_one(
            self.boto3_raw_data["ServiceQuotaIncreaseRequestInTemplate"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceQuotaIncreaseRequestsInTemplateResponse:
    boto3_raw_data: (
        "type_defs.ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def ServiceQuotaIncreaseRequestInTemplateList(self):  # pragma: no cover
        return ServiceQuotaIncreaseRequestInTemplate.make_many(
            self.boto3_raw_data["ServiceQuotaIncreaseRequestInTemplateList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutServiceQuotaIncreaseRequestIntoTemplateResponse:
    boto3_raw_data: (
        "type_defs.PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def ServiceQuotaIncreaseRequestInTemplate(self):  # pragma: no cover
        return ServiceQuotaIncreaseRequestInTemplate.make_one(
            self.boto3_raw_data["ServiceQuotaIncreaseRequestInTemplate"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAWSDefaultServiceQuotasRequestPaginate:
    boto3_raw_data: "type_defs.ListAWSDefaultServiceQuotasRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ServiceCode = field("ServiceCode")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAWSDefaultServiceQuotasRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAWSDefaultServiceQuotasRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRequestedServiceQuotaChangeHistoryByQuotaRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListRequestedServiceQuotaChangeHistoryByQuotaRequestPaginateTypeDef"
    ) = dataclasses.field()

    ServiceCode = field("ServiceCode")
    QuotaCode = field("QuotaCode")
    Status = field("Status")
    QuotaRequestedAtLevel = field("QuotaRequestedAtLevel")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRequestedServiceQuotaChangeHistoryByQuotaRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListRequestedServiceQuotaChangeHistoryByQuotaRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRequestedServiceQuotaChangeHistoryRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListRequestedServiceQuotaChangeHistoryRequestPaginateTypeDef"
    ) = dataclasses.field()

    ServiceCode = field("ServiceCode")
    Status = field("Status")
    QuotaRequestedAtLevel = field("QuotaRequestedAtLevel")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRequestedServiceQuotaChangeHistoryRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListRequestedServiceQuotaChangeHistoryRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceQuotaIncreaseRequestsInTemplateRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListServiceQuotaIncreaseRequestsInTemplateRequestPaginateTypeDef"
    ) = dataclasses.field()

    ServiceCode = field("ServiceCode")
    AwsRegion = field("AwsRegion")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServiceQuotaIncreaseRequestsInTemplateRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListServiceQuotaIncreaseRequestsInTemplateRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceQuotasRequestPaginate:
    boto3_raw_data: "type_defs.ListServiceQuotasRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ServiceCode = field("ServiceCode")
    QuotaCode = field("QuotaCode")
    QuotaAppliedAtLevel = field("QuotaAppliedAtLevel")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListServiceQuotasRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceQuotasRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServicesRequestPaginate:
    boto3_raw_data: "type_defs.ListServicesRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServicesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServicesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServicesResponse:
    boto3_raw_data: "type_defs.ListServicesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Services(self):  # pragma: no cover
        return ServiceInfo.make_many(self.boto3_raw_data["Services"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServicesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServicesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceResponse:
    boto3_raw_data: "type_defs.ListTagsForResourceResponseTypeDef" = dataclasses.field()

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestedServiceQuotaChange:
    boto3_raw_data: "type_defs.RequestedServiceQuotaChangeTypeDef" = dataclasses.field()

    Id = field("Id")
    CaseId = field("CaseId")
    ServiceCode = field("ServiceCode")
    ServiceName = field("ServiceName")
    QuotaCode = field("QuotaCode")
    QuotaName = field("QuotaName")
    DesiredValue = field("DesiredValue")
    Status = field("Status")
    Created = field("Created")
    LastUpdated = field("LastUpdated")
    Requester = field("Requester")
    QuotaArn = field("QuotaArn")
    GlobalQuota = field("GlobalQuota")
    Unit = field("Unit")
    QuotaRequestedAtLevel = field("QuotaRequestedAtLevel")

    @cached_property
    def QuotaContext(self):  # pragma: no cover
        return QuotaContextInfo.make_one(self.boto3_raw_data["QuotaContext"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RequestedServiceQuotaChangeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequestedServiceQuotaChangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceQuota:
    boto3_raw_data: "type_defs.ServiceQuotaTypeDef" = dataclasses.field()

    ServiceCode = field("ServiceCode")
    ServiceName = field("ServiceName")
    QuotaArn = field("QuotaArn")
    QuotaCode = field("QuotaCode")
    QuotaName = field("QuotaName")
    Value = field("Value")
    Unit = field("Unit")
    Adjustable = field("Adjustable")
    GlobalQuota = field("GlobalQuota")

    @cached_property
    def UsageMetric(self):  # pragma: no cover
        return MetricInfo.make_one(self.boto3_raw_data["UsageMetric"])

    @cached_property
    def Period(self):  # pragma: no cover
        return QuotaPeriod.make_one(self.boto3_raw_data["Period"])

    @cached_property
    def ErrorReason(self):  # pragma: no cover
        return ErrorReason.make_one(self.boto3_raw_data["ErrorReason"])

    QuotaAppliedAtLevel = field("QuotaAppliedAtLevel")

    @cached_property
    def QuotaContext(self):  # pragma: no cover
        return QuotaContextInfo.make_one(self.boto3_raw_data["QuotaContext"])

    Description = field("Description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceQuotaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServiceQuotaTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRequestedServiceQuotaChangeResponse:
    boto3_raw_data: "type_defs.GetRequestedServiceQuotaChangeResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RequestedQuota(self):  # pragma: no cover
        return RequestedServiceQuotaChange.make_one(
            self.boto3_raw_data["RequestedQuota"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRequestedServiceQuotaChangeResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRequestedServiceQuotaChangeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRequestedServiceQuotaChangeHistoryByQuotaResponse:
    boto3_raw_data: (
        "type_defs.ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def RequestedQuotas(self):  # pragma: no cover
        return RequestedServiceQuotaChange.make_many(
            self.boto3_raw_data["RequestedQuotas"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRequestedServiceQuotaChangeHistoryResponse:
    boto3_raw_data: (
        "type_defs.ListRequestedServiceQuotaChangeHistoryResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def RequestedQuotas(self):  # pragma: no cover
        return RequestedServiceQuotaChange.make_many(
            self.boto3_raw_data["RequestedQuotas"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRequestedServiceQuotaChangeHistoryResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListRequestedServiceQuotaChangeHistoryResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestServiceQuotaIncreaseResponse:
    boto3_raw_data: "type_defs.RequestServiceQuotaIncreaseResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RequestedQuota(self):  # pragma: no cover
        return RequestedServiceQuotaChange.make_one(
            self.boto3_raw_data["RequestedQuota"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RequestServiceQuotaIncreaseResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequestServiceQuotaIncreaseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAWSDefaultServiceQuotaResponse:
    boto3_raw_data: "type_defs.GetAWSDefaultServiceQuotaResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Quota(self):  # pragma: no cover
        return ServiceQuota.make_one(self.boto3_raw_data["Quota"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAWSDefaultServiceQuotaResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAWSDefaultServiceQuotaResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceQuotaResponse:
    boto3_raw_data: "type_defs.GetServiceQuotaResponseTypeDef" = dataclasses.field()

    @cached_property
    def Quota(self):  # pragma: no cover
        return ServiceQuota.make_one(self.boto3_raw_data["Quota"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetServiceQuotaResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceQuotaResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAWSDefaultServiceQuotasResponse:
    boto3_raw_data: "type_defs.ListAWSDefaultServiceQuotasResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Quotas(self):  # pragma: no cover
        return ServiceQuota.make_many(self.boto3_raw_data["Quotas"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAWSDefaultServiceQuotasResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAWSDefaultServiceQuotasResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceQuotasResponse:
    boto3_raw_data: "type_defs.ListServiceQuotasResponseTypeDef" = dataclasses.field()

    @cached_property
    def Quotas(self):  # pragma: no cover
        return ServiceQuota.make_many(self.boto3_raw_data["Quotas"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServiceQuotasResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceQuotasResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
