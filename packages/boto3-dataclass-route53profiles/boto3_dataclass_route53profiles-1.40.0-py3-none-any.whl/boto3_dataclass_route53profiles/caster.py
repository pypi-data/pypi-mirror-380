# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_route53profiles import type_defs as bs_td


class ROUTE53PROFILESCaster:

    def associate_profile(
        self,
        res: "bs_td.AssociateProfileResponseTypeDef",
    ) -> "dc_td.AssociateProfileResponse":
        return dc_td.AssociateProfileResponse.make_one(res)

    def associate_resource_to_profile(
        self,
        res: "bs_td.AssociateResourceToProfileResponseTypeDef",
    ) -> "dc_td.AssociateResourceToProfileResponse":
        return dc_td.AssociateResourceToProfileResponse.make_one(res)

    def create_profile(
        self,
        res: "bs_td.CreateProfileResponseTypeDef",
    ) -> "dc_td.CreateProfileResponse":
        return dc_td.CreateProfileResponse.make_one(res)

    def delete_profile(
        self,
        res: "bs_td.DeleteProfileResponseTypeDef",
    ) -> "dc_td.DeleteProfileResponse":
        return dc_td.DeleteProfileResponse.make_one(res)

    def disassociate_profile(
        self,
        res: "bs_td.DisassociateProfileResponseTypeDef",
    ) -> "dc_td.DisassociateProfileResponse":
        return dc_td.DisassociateProfileResponse.make_one(res)

    def disassociate_resource_from_profile(
        self,
        res: "bs_td.DisassociateResourceFromProfileResponseTypeDef",
    ) -> "dc_td.DisassociateResourceFromProfileResponse":
        return dc_td.DisassociateResourceFromProfileResponse.make_one(res)

    def get_profile(
        self,
        res: "bs_td.GetProfileResponseTypeDef",
    ) -> "dc_td.GetProfileResponse":
        return dc_td.GetProfileResponse.make_one(res)

    def get_profile_association(
        self,
        res: "bs_td.GetProfileAssociationResponseTypeDef",
    ) -> "dc_td.GetProfileAssociationResponse":
        return dc_td.GetProfileAssociationResponse.make_one(res)

    def get_profile_resource_association(
        self,
        res: "bs_td.GetProfileResourceAssociationResponseTypeDef",
    ) -> "dc_td.GetProfileResourceAssociationResponse":
        return dc_td.GetProfileResourceAssociationResponse.make_one(res)

    def list_profile_associations(
        self,
        res: "bs_td.ListProfileAssociationsResponseTypeDef",
    ) -> "dc_td.ListProfileAssociationsResponse":
        return dc_td.ListProfileAssociationsResponse.make_one(res)

    def list_profile_resource_associations(
        self,
        res: "bs_td.ListProfileResourceAssociationsResponseTypeDef",
    ) -> "dc_td.ListProfileResourceAssociationsResponse":
        return dc_td.ListProfileResourceAssociationsResponse.make_one(res)

    def list_profiles(
        self,
        res: "bs_td.ListProfilesResponseTypeDef",
    ) -> "dc_td.ListProfilesResponse":
        return dc_td.ListProfilesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def update_profile_resource_association(
        self,
        res: "bs_td.UpdateProfileResourceAssociationResponseTypeDef",
    ) -> "dc_td.UpdateProfileResourceAssociationResponse":
        return dc_td.UpdateProfileResourceAssociationResponse.make_one(res)


route53profiles_caster = ROUTE53PROFILESCaster()
