# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_servicecatalog_appregistry import type_defs as bs_td


class SERVICECATALOG_APPREGISTRYCaster:

    def associate_attribute_group(
        self,
        res: "bs_td.AssociateAttributeGroupResponseTypeDef",
    ) -> "dc_td.AssociateAttributeGroupResponse":
        return dc_td.AssociateAttributeGroupResponse.make_one(res)

    def associate_resource(
        self,
        res: "bs_td.AssociateResourceResponseTypeDef",
    ) -> "dc_td.AssociateResourceResponse":
        return dc_td.AssociateResourceResponse.make_one(res)

    def create_application(
        self,
        res: "bs_td.CreateApplicationResponseTypeDef",
    ) -> "dc_td.CreateApplicationResponse":
        return dc_td.CreateApplicationResponse.make_one(res)

    def create_attribute_group(
        self,
        res: "bs_td.CreateAttributeGroupResponseTypeDef",
    ) -> "dc_td.CreateAttributeGroupResponse":
        return dc_td.CreateAttributeGroupResponse.make_one(res)

    def delete_application(
        self,
        res: "bs_td.DeleteApplicationResponseTypeDef",
    ) -> "dc_td.DeleteApplicationResponse":
        return dc_td.DeleteApplicationResponse.make_one(res)

    def delete_attribute_group(
        self,
        res: "bs_td.DeleteAttributeGroupResponseTypeDef",
    ) -> "dc_td.DeleteAttributeGroupResponse":
        return dc_td.DeleteAttributeGroupResponse.make_one(res)

    def disassociate_attribute_group(
        self,
        res: "bs_td.DisassociateAttributeGroupResponseTypeDef",
    ) -> "dc_td.DisassociateAttributeGroupResponse":
        return dc_td.DisassociateAttributeGroupResponse.make_one(res)

    def disassociate_resource(
        self,
        res: "bs_td.DisassociateResourceResponseTypeDef",
    ) -> "dc_td.DisassociateResourceResponse":
        return dc_td.DisassociateResourceResponse.make_one(res)

    def get_application(
        self,
        res: "bs_td.GetApplicationResponseTypeDef",
    ) -> "dc_td.GetApplicationResponse":
        return dc_td.GetApplicationResponse.make_one(res)

    def get_associated_resource(
        self,
        res: "bs_td.GetAssociatedResourceResponseTypeDef",
    ) -> "dc_td.GetAssociatedResourceResponse":
        return dc_td.GetAssociatedResourceResponse.make_one(res)

    def get_attribute_group(
        self,
        res: "bs_td.GetAttributeGroupResponseTypeDef",
    ) -> "dc_td.GetAttributeGroupResponse":
        return dc_td.GetAttributeGroupResponse.make_one(res)

    def get_configuration(
        self,
        res: "bs_td.GetConfigurationResponseTypeDef",
    ) -> "dc_td.GetConfigurationResponse":
        return dc_td.GetConfigurationResponse.make_one(res)

    def list_applications(
        self,
        res: "bs_td.ListApplicationsResponseTypeDef",
    ) -> "dc_td.ListApplicationsResponse":
        return dc_td.ListApplicationsResponse.make_one(res)

    def list_associated_attribute_groups(
        self,
        res: "bs_td.ListAssociatedAttributeGroupsResponseTypeDef",
    ) -> "dc_td.ListAssociatedAttributeGroupsResponse":
        return dc_td.ListAssociatedAttributeGroupsResponse.make_one(res)

    def list_associated_resources(
        self,
        res: "bs_td.ListAssociatedResourcesResponseTypeDef",
    ) -> "dc_td.ListAssociatedResourcesResponse":
        return dc_td.ListAssociatedResourcesResponse.make_one(res)

    def list_attribute_groups(
        self,
        res: "bs_td.ListAttributeGroupsResponseTypeDef",
    ) -> "dc_td.ListAttributeGroupsResponse":
        return dc_td.ListAttributeGroupsResponse.make_one(res)

    def list_attribute_groups_for_application(
        self,
        res: "bs_td.ListAttributeGroupsForApplicationResponseTypeDef",
    ) -> "dc_td.ListAttributeGroupsForApplicationResponse":
        return dc_td.ListAttributeGroupsForApplicationResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def put_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def sync_resource(
        self,
        res: "bs_td.SyncResourceResponseTypeDef",
    ) -> "dc_td.SyncResourceResponse":
        return dc_td.SyncResourceResponse.make_one(res)

    def update_application(
        self,
        res: "bs_td.UpdateApplicationResponseTypeDef",
    ) -> "dc_td.UpdateApplicationResponse":
        return dc_td.UpdateApplicationResponse.make_one(res)

    def update_attribute_group(
        self,
        res: "bs_td.UpdateAttributeGroupResponseTypeDef",
    ) -> "dc_td.UpdateAttributeGroupResponse":
        return dc_td.UpdateAttributeGroupResponse.make_one(res)


servicecatalog_appregistry_caster = SERVICECATALOG_APPREGISTRYCaster()
