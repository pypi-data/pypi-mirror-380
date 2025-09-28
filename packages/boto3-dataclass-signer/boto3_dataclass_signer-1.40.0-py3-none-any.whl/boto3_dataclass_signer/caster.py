# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_signer import type_defs as bs_td


class SIGNERCaster:

    def add_profile_permission(
        self,
        res: "bs_td.AddProfilePermissionResponseTypeDef",
    ) -> "dc_td.AddProfilePermissionResponse":
        return dc_td.AddProfilePermissionResponse.make_one(res)

    def cancel_signing_profile(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_signing_job(
        self,
        res: "bs_td.DescribeSigningJobResponseTypeDef",
    ) -> "dc_td.DescribeSigningJobResponse":
        return dc_td.DescribeSigningJobResponse.make_one(res)

    def get_revocation_status(
        self,
        res: "bs_td.GetRevocationStatusResponseTypeDef",
    ) -> "dc_td.GetRevocationStatusResponse":
        return dc_td.GetRevocationStatusResponse.make_one(res)

    def get_signing_platform(
        self,
        res: "bs_td.GetSigningPlatformResponseTypeDef",
    ) -> "dc_td.GetSigningPlatformResponse":
        return dc_td.GetSigningPlatformResponse.make_one(res)

    def get_signing_profile(
        self,
        res: "bs_td.GetSigningProfileResponseTypeDef",
    ) -> "dc_td.GetSigningProfileResponse":
        return dc_td.GetSigningProfileResponse.make_one(res)

    def list_profile_permissions(
        self,
        res: "bs_td.ListProfilePermissionsResponseTypeDef",
    ) -> "dc_td.ListProfilePermissionsResponse":
        return dc_td.ListProfilePermissionsResponse.make_one(res)

    def list_signing_jobs(
        self,
        res: "bs_td.ListSigningJobsResponseTypeDef",
    ) -> "dc_td.ListSigningJobsResponse":
        return dc_td.ListSigningJobsResponse.make_one(res)

    def list_signing_platforms(
        self,
        res: "bs_td.ListSigningPlatformsResponseTypeDef",
    ) -> "dc_td.ListSigningPlatformsResponse":
        return dc_td.ListSigningPlatformsResponse.make_one(res)

    def list_signing_profiles(
        self,
        res: "bs_td.ListSigningProfilesResponseTypeDef",
    ) -> "dc_td.ListSigningProfilesResponse":
        return dc_td.ListSigningProfilesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def put_signing_profile(
        self,
        res: "bs_td.PutSigningProfileResponseTypeDef",
    ) -> "dc_td.PutSigningProfileResponse":
        return dc_td.PutSigningProfileResponse.make_one(res)

    def remove_profile_permission(
        self,
        res: "bs_td.RemoveProfilePermissionResponseTypeDef",
    ) -> "dc_td.RemoveProfilePermissionResponse":
        return dc_td.RemoveProfilePermissionResponse.make_one(res)

    def revoke_signature(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def revoke_signing_profile(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def sign_payload(
        self,
        res: "bs_td.SignPayloadResponseTypeDef",
    ) -> "dc_td.SignPayloadResponse":
        return dc_td.SignPayloadResponse.make_one(res)

    def start_signing_job(
        self,
        res: "bs_td.StartSigningJobResponseTypeDef",
    ) -> "dc_td.StartSigningJobResponse":
        return dc_td.StartSigningJobResponse.make_one(res)


signer_caster = SIGNERCaster()
