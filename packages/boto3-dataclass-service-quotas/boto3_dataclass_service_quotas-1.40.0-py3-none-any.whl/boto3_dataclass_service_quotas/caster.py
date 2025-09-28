# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_service_quotas import type_defs as bs_td


class SERVICE_QUOTASCaster:

    def get_aws_default_service_quota(
        self,
        res: "bs_td.GetAWSDefaultServiceQuotaResponseTypeDef",
    ) -> "dc_td.GetAWSDefaultServiceQuotaResponse":
        return dc_td.GetAWSDefaultServiceQuotaResponse.make_one(res)

    def get_association_for_service_quota_template(
        self,
        res: "bs_td.GetAssociationForServiceQuotaTemplateResponseTypeDef",
    ) -> "dc_td.GetAssociationForServiceQuotaTemplateResponse":
        return dc_td.GetAssociationForServiceQuotaTemplateResponse.make_one(res)

    def get_requested_service_quota_change(
        self,
        res: "bs_td.GetRequestedServiceQuotaChangeResponseTypeDef",
    ) -> "dc_td.GetRequestedServiceQuotaChangeResponse":
        return dc_td.GetRequestedServiceQuotaChangeResponse.make_one(res)

    def get_service_quota(
        self,
        res: "bs_td.GetServiceQuotaResponseTypeDef",
    ) -> "dc_td.GetServiceQuotaResponse":
        return dc_td.GetServiceQuotaResponse.make_one(res)

    def get_service_quota_increase_request_from_template(
        self,
        res: "bs_td.GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef",
    ) -> "dc_td.GetServiceQuotaIncreaseRequestFromTemplateResponse":
        return dc_td.GetServiceQuotaIncreaseRequestFromTemplateResponse.make_one(res)

    def list_aws_default_service_quotas(
        self,
        res: "bs_td.ListAWSDefaultServiceQuotasResponseTypeDef",
    ) -> "dc_td.ListAWSDefaultServiceQuotasResponse":
        return dc_td.ListAWSDefaultServiceQuotasResponse.make_one(res)

    def list_requested_service_quota_change_history(
        self,
        res: "bs_td.ListRequestedServiceQuotaChangeHistoryResponseTypeDef",
    ) -> "dc_td.ListRequestedServiceQuotaChangeHistoryResponse":
        return dc_td.ListRequestedServiceQuotaChangeHistoryResponse.make_one(res)

    def list_requested_service_quota_change_history_by_quota(
        self,
        res: "bs_td.ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef",
    ) -> "dc_td.ListRequestedServiceQuotaChangeHistoryByQuotaResponse":
        return dc_td.ListRequestedServiceQuotaChangeHistoryByQuotaResponse.make_one(res)

    def list_service_quota_increase_requests_in_template(
        self,
        res: "bs_td.ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef",
    ) -> "dc_td.ListServiceQuotaIncreaseRequestsInTemplateResponse":
        return dc_td.ListServiceQuotaIncreaseRequestsInTemplateResponse.make_one(res)

    def list_service_quotas(
        self,
        res: "bs_td.ListServiceQuotasResponseTypeDef",
    ) -> "dc_td.ListServiceQuotasResponse":
        return dc_td.ListServiceQuotasResponse.make_one(res)

    def list_services(
        self,
        res: "bs_td.ListServicesResponseTypeDef",
    ) -> "dc_td.ListServicesResponse":
        return dc_td.ListServicesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def put_service_quota_increase_request_into_template(
        self,
        res: "bs_td.PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef",
    ) -> "dc_td.PutServiceQuotaIncreaseRequestIntoTemplateResponse":
        return dc_td.PutServiceQuotaIncreaseRequestIntoTemplateResponse.make_one(res)

    def request_service_quota_increase(
        self,
        res: "bs_td.RequestServiceQuotaIncreaseResponseTypeDef",
    ) -> "dc_td.RequestServiceQuotaIncreaseResponse":
        return dc_td.RequestServiceQuotaIncreaseResponse.make_one(res)


service_quotas_caster = SERVICE_QUOTASCaster()
