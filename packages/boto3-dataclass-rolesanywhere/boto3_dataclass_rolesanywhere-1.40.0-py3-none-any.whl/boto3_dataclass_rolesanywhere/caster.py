# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_rolesanywhere import type_defs as bs_td


class ROLESANYWHERECaster:

    def create_profile(
        self,
        res: "bs_td.ProfileDetailResponseTypeDef",
    ) -> "dc_td.ProfileDetailResponse":
        return dc_td.ProfileDetailResponse.make_one(res)

    def create_trust_anchor(
        self,
        res: "bs_td.TrustAnchorDetailResponseTypeDef",
    ) -> "dc_td.TrustAnchorDetailResponse":
        return dc_td.TrustAnchorDetailResponse.make_one(res)

    def delete_attribute_mapping(
        self,
        res: "bs_td.DeleteAttributeMappingResponseTypeDef",
    ) -> "dc_td.DeleteAttributeMappingResponse":
        return dc_td.DeleteAttributeMappingResponse.make_one(res)

    def delete_crl(
        self,
        res: "bs_td.CrlDetailResponseTypeDef",
    ) -> "dc_td.CrlDetailResponse":
        return dc_td.CrlDetailResponse.make_one(res)

    def delete_profile(
        self,
        res: "bs_td.ProfileDetailResponseTypeDef",
    ) -> "dc_td.ProfileDetailResponse":
        return dc_td.ProfileDetailResponse.make_one(res)

    def delete_trust_anchor(
        self,
        res: "bs_td.TrustAnchorDetailResponseTypeDef",
    ) -> "dc_td.TrustAnchorDetailResponse":
        return dc_td.TrustAnchorDetailResponse.make_one(res)

    def disable_crl(
        self,
        res: "bs_td.CrlDetailResponseTypeDef",
    ) -> "dc_td.CrlDetailResponse":
        return dc_td.CrlDetailResponse.make_one(res)

    def disable_profile(
        self,
        res: "bs_td.ProfileDetailResponseTypeDef",
    ) -> "dc_td.ProfileDetailResponse":
        return dc_td.ProfileDetailResponse.make_one(res)

    def disable_trust_anchor(
        self,
        res: "bs_td.TrustAnchorDetailResponseTypeDef",
    ) -> "dc_td.TrustAnchorDetailResponse":
        return dc_td.TrustAnchorDetailResponse.make_one(res)

    def enable_crl(
        self,
        res: "bs_td.CrlDetailResponseTypeDef",
    ) -> "dc_td.CrlDetailResponse":
        return dc_td.CrlDetailResponse.make_one(res)

    def enable_profile(
        self,
        res: "bs_td.ProfileDetailResponseTypeDef",
    ) -> "dc_td.ProfileDetailResponse":
        return dc_td.ProfileDetailResponse.make_one(res)

    def enable_trust_anchor(
        self,
        res: "bs_td.TrustAnchorDetailResponseTypeDef",
    ) -> "dc_td.TrustAnchorDetailResponse":
        return dc_td.TrustAnchorDetailResponse.make_one(res)

    def get_crl(
        self,
        res: "bs_td.CrlDetailResponseTypeDef",
    ) -> "dc_td.CrlDetailResponse":
        return dc_td.CrlDetailResponse.make_one(res)

    def get_profile(
        self,
        res: "bs_td.ProfileDetailResponseTypeDef",
    ) -> "dc_td.ProfileDetailResponse":
        return dc_td.ProfileDetailResponse.make_one(res)

    def get_subject(
        self,
        res: "bs_td.SubjectDetailResponseTypeDef",
    ) -> "dc_td.SubjectDetailResponse":
        return dc_td.SubjectDetailResponse.make_one(res)

    def get_trust_anchor(
        self,
        res: "bs_td.TrustAnchorDetailResponseTypeDef",
    ) -> "dc_td.TrustAnchorDetailResponse":
        return dc_td.TrustAnchorDetailResponse.make_one(res)

    def import_crl(
        self,
        res: "bs_td.CrlDetailResponseTypeDef",
    ) -> "dc_td.CrlDetailResponse":
        return dc_td.CrlDetailResponse.make_one(res)

    def list_crls(
        self,
        res: "bs_td.ListCrlsResponseTypeDef",
    ) -> "dc_td.ListCrlsResponse":
        return dc_td.ListCrlsResponse.make_one(res)

    def list_profiles(
        self,
        res: "bs_td.ListProfilesResponseTypeDef",
    ) -> "dc_td.ListProfilesResponse":
        return dc_td.ListProfilesResponse.make_one(res)

    def list_subjects(
        self,
        res: "bs_td.ListSubjectsResponseTypeDef",
    ) -> "dc_td.ListSubjectsResponse":
        return dc_td.ListSubjectsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_trust_anchors(
        self,
        res: "bs_td.ListTrustAnchorsResponseTypeDef",
    ) -> "dc_td.ListTrustAnchorsResponse":
        return dc_td.ListTrustAnchorsResponse.make_one(res)

    def put_attribute_mapping(
        self,
        res: "bs_td.PutAttributeMappingResponseTypeDef",
    ) -> "dc_td.PutAttributeMappingResponse":
        return dc_td.PutAttributeMappingResponse.make_one(res)

    def put_notification_settings(
        self,
        res: "bs_td.PutNotificationSettingsResponseTypeDef",
    ) -> "dc_td.PutNotificationSettingsResponse":
        return dc_td.PutNotificationSettingsResponse.make_one(res)

    def reset_notification_settings(
        self,
        res: "bs_td.ResetNotificationSettingsResponseTypeDef",
    ) -> "dc_td.ResetNotificationSettingsResponse":
        return dc_td.ResetNotificationSettingsResponse.make_one(res)

    def update_crl(
        self,
        res: "bs_td.CrlDetailResponseTypeDef",
    ) -> "dc_td.CrlDetailResponse":
        return dc_td.CrlDetailResponse.make_one(res)

    def update_profile(
        self,
        res: "bs_td.ProfileDetailResponseTypeDef",
    ) -> "dc_td.ProfileDetailResponse":
        return dc_td.ProfileDetailResponse.make_one(res)

    def update_trust_anchor(
        self,
        res: "bs_td.TrustAnchorDetailResponseTypeDef",
    ) -> "dc_td.TrustAnchorDetailResponse":
        return dc_td.TrustAnchorDetailResponse.make_one(res)


rolesanywhere_caster = ROLESANYWHERECaster()
