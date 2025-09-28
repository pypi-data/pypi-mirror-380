# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_serverlessrepo import type_defs as bs_td


class SERVERLESSREPOCaster:

    def create_application(
        self,
        res: "bs_td.CreateApplicationResponseTypeDef",
    ) -> "dc_td.CreateApplicationResponse":
        return dc_td.CreateApplicationResponse.make_one(res)

    def create_application_version(
        self,
        res: "bs_td.CreateApplicationVersionResponseTypeDef",
    ) -> "dc_td.CreateApplicationVersionResponse":
        return dc_td.CreateApplicationVersionResponse.make_one(res)

    def create_cloud_formation_change_set(
        self,
        res: "bs_td.CreateCloudFormationChangeSetResponseTypeDef",
    ) -> "dc_td.CreateCloudFormationChangeSetResponse":
        return dc_td.CreateCloudFormationChangeSetResponse.make_one(res)

    def create_cloud_formation_template(
        self,
        res: "bs_td.CreateCloudFormationTemplateResponseTypeDef",
    ) -> "dc_td.CreateCloudFormationTemplateResponse":
        return dc_td.CreateCloudFormationTemplateResponse.make_one(res)

    def delete_application(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_application(
        self,
        res: "bs_td.GetApplicationResponseTypeDef",
    ) -> "dc_td.GetApplicationResponse":
        return dc_td.GetApplicationResponse.make_one(res)

    def get_application_policy(
        self,
        res: "bs_td.GetApplicationPolicyResponseTypeDef",
    ) -> "dc_td.GetApplicationPolicyResponse":
        return dc_td.GetApplicationPolicyResponse.make_one(res)

    def get_cloud_formation_template(
        self,
        res: "bs_td.GetCloudFormationTemplateResponseTypeDef",
    ) -> "dc_td.GetCloudFormationTemplateResponse":
        return dc_td.GetCloudFormationTemplateResponse.make_one(res)

    def list_application_dependencies(
        self,
        res: "bs_td.ListApplicationDependenciesResponseTypeDef",
    ) -> "dc_td.ListApplicationDependenciesResponse":
        return dc_td.ListApplicationDependenciesResponse.make_one(res)

    def list_application_versions(
        self,
        res: "bs_td.ListApplicationVersionsResponseTypeDef",
    ) -> "dc_td.ListApplicationVersionsResponse":
        return dc_td.ListApplicationVersionsResponse.make_one(res)

    def list_applications(
        self,
        res: "bs_td.ListApplicationsResponseTypeDef",
    ) -> "dc_td.ListApplicationsResponse":
        return dc_td.ListApplicationsResponse.make_one(res)

    def put_application_policy(
        self,
        res: "bs_td.PutApplicationPolicyResponseTypeDef",
    ) -> "dc_td.PutApplicationPolicyResponse":
        return dc_td.PutApplicationPolicyResponse.make_one(res)

    def unshare_application(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_application(
        self,
        res: "bs_td.UpdateApplicationResponseTypeDef",
    ) -> "dc_td.UpdateApplicationResponse":
        return dc_td.UpdateApplicationResponse.make_one(res)


serverlessrepo_caster = SERVERLESSREPOCaster()
