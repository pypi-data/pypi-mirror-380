# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_s3control import type_defs as bs_td


class S3CONTROLCaster:

    def associate_access_grants_identity_center(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_access_grant(
        self,
        res: "bs_td.CreateAccessGrantResultTypeDef",
    ) -> "dc_td.CreateAccessGrantResult":
        return dc_td.CreateAccessGrantResult.make_one(res)

    def create_access_grants_instance(
        self,
        res: "bs_td.CreateAccessGrantsInstanceResultTypeDef",
    ) -> "dc_td.CreateAccessGrantsInstanceResult":
        return dc_td.CreateAccessGrantsInstanceResult.make_one(res)

    def create_access_grants_location(
        self,
        res: "bs_td.CreateAccessGrantsLocationResultTypeDef",
    ) -> "dc_td.CreateAccessGrantsLocationResult":
        return dc_td.CreateAccessGrantsLocationResult.make_one(res)

    def create_access_point(
        self,
        res: "bs_td.CreateAccessPointResultTypeDef",
    ) -> "dc_td.CreateAccessPointResult":
        return dc_td.CreateAccessPointResult.make_one(res)

    def create_access_point_for_object_lambda(
        self,
        res: "bs_td.CreateAccessPointForObjectLambdaResultTypeDef",
    ) -> "dc_td.CreateAccessPointForObjectLambdaResult":
        return dc_td.CreateAccessPointForObjectLambdaResult.make_one(res)

    def create_bucket(
        self,
        res: "bs_td.CreateBucketResultTypeDef",
    ) -> "dc_td.CreateBucketResult":
        return dc_td.CreateBucketResult.make_one(res)

    def create_job(
        self,
        res: "bs_td.CreateJobResultTypeDef",
    ) -> "dc_td.CreateJobResult":
        return dc_td.CreateJobResult.make_one(res)

    def create_multi_region_access_point(
        self,
        res: "bs_td.CreateMultiRegionAccessPointResultTypeDef",
    ) -> "dc_td.CreateMultiRegionAccessPointResult":
        return dc_td.CreateMultiRegionAccessPointResult.make_one(res)

    def create_storage_lens_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_access_grant(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_access_grants_instance(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_access_grants_instance_resource_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_access_grants_location(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_access_point(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_access_point_for_object_lambda(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_access_point_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_access_point_policy_for_object_lambda(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_access_point_scope(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_bucket(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_bucket_lifecycle_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_bucket_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_bucket_replication(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_bucket_tagging(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_multi_region_access_point(
        self,
        res: "bs_td.DeleteMultiRegionAccessPointResultTypeDef",
    ) -> "dc_td.DeleteMultiRegionAccessPointResult":
        return dc_td.DeleteMultiRegionAccessPointResult.make_one(res)

    def delete_public_access_block(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_storage_lens_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_storage_lens_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_job(
        self,
        res: "bs_td.DescribeJobResultTypeDef",
    ) -> "dc_td.DescribeJobResult":
        return dc_td.DescribeJobResult.make_one(res)

    def describe_multi_region_access_point_operation(
        self,
        res: "bs_td.DescribeMultiRegionAccessPointOperationResultTypeDef",
    ) -> "dc_td.DescribeMultiRegionAccessPointOperationResult":
        return dc_td.DescribeMultiRegionAccessPointOperationResult.make_one(res)

    def dissociate_access_grants_identity_center(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_access_grant(
        self,
        res: "bs_td.GetAccessGrantResultTypeDef",
    ) -> "dc_td.GetAccessGrantResult":
        return dc_td.GetAccessGrantResult.make_one(res)

    def get_access_grants_instance(
        self,
        res: "bs_td.GetAccessGrantsInstanceResultTypeDef",
    ) -> "dc_td.GetAccessGrantsInstanceResult":
        return dc_td.GetAccessGrantsInstanceResult.make_one(res)

    def get_access_grants_instance_for_prefix(
        self,
        res: "bs_td.GetAccessGrantsInstanceForPrefixResultTypeDef",
    ) -> "dc_td.GetAccessGrantsInstanceForPrefixResult":
        return dc_td.GetAccessGrantsInstanceForPrefixResult.make_one(res)

    def get_access_grants_instance_resource_policy(
        self,
        res: "bs_td.GetAccessGrantsInstanceResourcePolicyResultTypeDef",
    ) -> "dc_td.GetAccessGrantsInstanceResourcePolicyResult":
        return dc_td.GetAccessGrantsInstanceResourcePolicyResult.make_one(res)

    def get_access_grants_location(
        self,
        res: "bs_td.GetAccessGrantsLocationResultTypeDef",
    ) -> "dc_td.GetAccessGrantsLocationResult":
        return dc_td.GetAccessGrantsLocationResult.make_one(res)

    def get_access_point(
        self,
        res: "bs_td.GetAccessPointResultTypeDef",
    ) -> "dc_td.GetAccessPointResult":
        return dc_td.GetAccessPointResult.make_one(res)

    def get_access_point_configuration_for_object_lambda(
        self,
        res: "bs_td.GetAccessPointConfigurationForObjectLambdaResultTypeDef",
    ) -> "dc_td.GetAccessPointConfigurationForObjectLambdaResult":
        return dc_td.GetAccessPointConfigurationForObjectLambdaResult.make_one(res)

    def get_access_point_for_object_lambda(
        self,
        res: "bs_td.GetAccessPointForObjectLambdaResultTypeDef",
    ) -> "dc_td.GetAccessPointForObjectLambdaResult":
        return dc_td.GetAccessPointForObjectLambdaResult.make_one(res)

    def get_access_point_policy(
        self,
        res: "bs_td.GetAccessPointPolicyResultTypeDef",
    ) -> "dc_td.GetAccessPointPolicyResult":
        return dc_td.GetAccessPointPolicyResult.make_one(res)

    def get_access_point_policy_for_object_lambda(
        self,
        res: "bs_td.GetAccessPointPolicyForObjectLambdaResultTypeDef",
    ) -> "dc_td.GetAccessPointPolicyForObjectLambdaResult":
        return dc_td.GetAccessPointPolicyForObjectLambdaResult.make_one(res)

    def get_access_point_policy_status(
        self,
        res: "bs_td.GetAccessPointPolicyStatusResultTypeDef",
    ) -> "dc_td.GetAccessPointPolicyStatusResult":
        return dc_td.GetAccessPointPolicyStatusResult.make_one(res)

    def get_access_point_policy_status_for_object_lambda(
        self,
        res: "bs_td.GetAccessPointPolicyStatusForObjectLambdaResultTypeDef",
    ) -> "dc_td.GetAccessPointPolicyStatusForObjectLambdaResult":
        return dc_td.GetAccessPointPolicyStatusForObjectLambdaResult.make_one(res)

    def get_access_point_scope(
        self,
        res: "bs_td.GetAccessPointScopeResultTypeDef",
    ) -> "dc_td.GetAccessPointScopeResult":
        return dc_td.GetAccessPointScopeResult.make_one(res)

    def get_bucket(
        self,
        res: "bs_td.GetBucketResultTypeDef",
    ) -> "dc_td.GetBucketResult":
        return dc_td.GetBucketResult.make_one(res)

    def get_bucket_lifecycle_configuration(
        self,
        res: "bs_td.GetBucketLifecycleConfigurationResultTypeDef",
    ) -> "dc_td.GetBucketLifecycleConfigurationResult":
        return dc_td.GetBucketLifecycleConfigurationResult.make_one(res)

    def get_bucket_policy(
        self,
        res: "bs_td.GetBucketPolicyResultTypeDef",
    ) -> "dc_td.GetBucketPolicyResult":
        return dc_td.GetBucketPolicyResult.make_one(res)

    def get_bucket_replication(
        self,
        res: "bs_td.GetBucketReplicationResultTypeDef",
    ) -> "dc_td.GetBucketReplicationResult":
        return dc_td.GetBucketReplicationResult.make_one(res)

    def get_bucket_tagging(
        self,
        res: "bs_td.GetBucketTaggingResultTypeDef",
    ) -> "dc_td.GetBucketTaggingResult":
        return dc_td.GetBucketTaggingResult.make_one(res)

    def get_bucket_versioning(
        self,
        res: "bs_td.GetBucketVersioningResultTypeDef",
    ) -> "dc_td.GetBucketVersioningResult":
        return dc_td.GetBucketVersioningResult.make_one(res)

    def get_data_access(
        self,
        res: "bs_td.GetDataAccessResultTypeDef",
    ) -> "dc_td.GetDataAccessResult":
        return dc_td.GetDataAccessResult.make_one(res)

    def get_job_tagging(
        self,
        res: "bs_td.GetJobTaggingResultTypeDef",
    ) -> "dc_td.GetJobTaggingResult":
        return dc_td.GetJobTaggingResult.make_one(res)

    def get_multi_region_access_point(
        self,
        res: "bs_td.GetMultiRegionAccessPointResultTypeDef",
    ) -> "dc_td.GetMultiRegionAccessPointResult":
        return dc_td.GetMultiRegionAccessPointResult.make_one(res)

    def get_multi_region_access_point_policy(
        self,
        res: "bs_td.GetMultiRegionAccessPointPolicyResultTypeDef",
    ) -> "dc_td.GetMultiRegionAccessPointPolicyResult":
        return dc_td.GetMultiRegionAccessPointPolicyResult.make_one(res)

    def get_multi_region_access_point_policy_status(
        self,
        res: "bs_td.GetMultiRegionAccessPointPolicyStatusResultTypeDef",
    ) -> "dc_td.GetMultiRegionAccessPointPolicyStatusResult":
        return dc_td.GetMultiRegionAccessPointPolicyStatusResult.make_one(res)

    def get_multi_region_access_point_routes(
        self,
        res: "bs_td.GetMultiRegionAccessPointRoutesResultTypeDef",
    ) -> "dc_td.GetMultiRegionAccessPointRoutesResult":
        return dc_td.GetMultiRegionAccessPointRoutesResult.make_one(res)

    def get_public_access_block(
        self,
        res: "bs_td.GetPublicAccessBlockOutputTypeDef",
    ) -> "dc_td.GetPublicAccessBlockOutput":
        return dc_td.GetPublicAccessBlockOutput.make_one(res)

    def get_storage_lens_configuration(
        self,
        res: "bs_td.GetStorageLensConfigurationResultTypeDef",
    ) -> "dc_td.GetStorageLensConfigurationResult":
        return dc_td.GetStorageLensConfigurationResult.make_one(res)

    def get_storage_lens_configuration_tagging(
        self,
        res: "bs_td.GetStorageLensConfigurationTaggingResultTypeDef",
    ) -> "dc_td.GetStorageLensConfigurationTaggingResult":
        return dc_td.GetStorageLensConfigurationTaggingResult.make_one(res)

    def get_storage_lens_group(
        self,
        res: "bs_td.GetStorageLensGroupResultTypeDef",
    ) -> "dc_td.GetStorageLensGroupResult":
        return dc_td.GetStorageLensGroupResult.make_one(res)

    def list_access_grants(
        self,
        res: "bs_td.ListAccessGrantsResultTypeDef",
    ) -> "dc_td.ListAccessGrantsResult":
        return dc_td.ListAccessGrantsResult.make_one(res)

    def list_access_grants_instances(
        self,
        res: "bs_td.ListAccessGrantsInstancesResultTypeDef",
    ) -> "dc_td.ListAccessGrantsInstancesResult":
        return dc_td.ListAccessGrantsInstancesResult.make_one(res)

    def list_access_grants_locations(
        self,
        res: "bs_td.ListAccessGrantsLocationsResultTypeDef",
    ) -> "dc_td.ListAccessGrantsLocationsResult":
        return dc_td.ListAccessGrantsLocationsResult.make_one(res)

    def list_access_points(
        self,
        res: "bs_td.ListAccessPointsResultTypeDef",
    ) -> "dc_td.ListAccessPointsResult":
        return dc_td.ListAccessPointsResult.make_one(res)

    def list_access_points_for_directory_buckets(
        self,
        res: "bs_td.ListAccessPointsForDirectoryBucketsResultTypeDef",
    ) -> "dc_td.ListAccessPointsForDirectoryBucketsResult":
        return dc_td.ListAccessPointsForDirectoryBucketsResult.make_one(res)

    def list_access_points_for_object_lambda(
        self,
        res: "bs_td.ListAccessPointsForObjectLambdaResultTypeDef",
    ) -> "dc_td.ListAccessPointsForObjectLambdaResult":
        return dc_td.ListAccessPointsForObjectLambdaResult.make_one(res)

    def list_caller_access_grants(
        self,
        res: "bs_td.ListCallerAccessGrantsResultTypeDef",
    ) -> "dc_td.ListCallerAccessGrantsResult":
        return dc_td.ListCallerAccessGrantsResult.make_one(res)

    def list_jobs(
        self,
        res: "bs_td.ListJobsResultTypeDef",
    ) -> "dc_td.ListJobsResult":
        return dc_td.ListJobsResult.make_one(res)

    def list_multi_region_access_points(
        self,
        res: "bs_td.ListMultiRegionAccessPointsResultTypeDef",
    ) -> "dc_td.ListMultiRegionAccessPointsResult":
        return dc_td.ListMultiRegionAccessPointsResult.make_one(res)

    def list_regional_buckets(
        self,
        res: "bs_td.ListRegionalBucketsResultTypeDef",
    ) -> "dc_td.ListRegionalBucketsResult":
        return dc_td.ListRegionalBucketsResult.make_one(res)

    def list_storage_lens_configurations(
        self,
        res: "bs_td.ListStorageLensConfigurationsResultTypeDef",
    ) -> "dc_td.ListStorageLensConfigurationsResult":
        return dc_td.ListStorageLensConfigurationsResult.make_one(res)

    def list_storage_lens_groups(
        self,
        res: "bs_td.ListStorageLensGroupsResultTypeDef",
    ) -> "dc_td.ListStorageLensGroupsResult":
        return dc_td.ListStorageLensGroupsResult.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResultTypeDef",
    ) -> "dc_td.ListTagsForResourceResult":
        return dc_td.ListTagsForResourceResult.make_one(res)

    def put_access_grants_instance_resource_policy(
        self,
        res: "bs_td.PutAccessGrantsInstanceResourcePolicyResultTypeDef",
    ) -> "dc_td.PutAccessGrantsInstanceResourcePolicyResult":
        return dc_td.PutAccessGrantsInstanceResourcePolicyResult.make_one(res)

    def put_access_point_configuration_for_object_lambda(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_access_point_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_access_point_policy_for_object_lambda(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_access_point_scope(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_bucket_lifecycle_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_bucket_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_bucket_replication(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_bucket_tagging(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_bucket_versioning(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_multi_region_access_point_policy(
        self,
        res: "bs_td.PutMultiRegionAccessPointPolicyResultTypeDef",
    ) -> "dc_td.PutMultiRegionAccessPointPolicyResult":
        return dc_td.PutMultiRegionAccessPointPolicyResult.make_one(res)

    def put_public_access_block(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_storage_lens_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_access_grants_location(
        self,
        res: "bs_td.UpdateAccessGrantsLocationResultTypeDef",
    ) -> "dc_td.UpdateAccessGrantsLocationResult":
        return dc_td.UpdateAccessGrantsLocationResult.make_one(res)

    def update_job_priority(
        self,
        res: "bs_td.UpdateJobPriorityResultTypeDef",
    ) -> "dc_td.UpdateJobPriorityResult":
        return dc_td.UpdateJobPriorityResult.make_one(res)

    def update_job_status(
        self,
        res: "bs_td.UpdateJobStatusResultTypeDef",
    ) -> "dc_td.UpdateJobStatusResult":
        return dc_td.UpdateJobStatusResult.make_one(res)

    def update_storage_lens_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


s3control_caster = S3CONTROLCaster()
