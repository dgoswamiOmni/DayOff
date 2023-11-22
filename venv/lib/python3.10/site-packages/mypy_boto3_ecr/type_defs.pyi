"""
Type annotations for ecr service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecr/type_defs/)

Usage::

    ```python
    from mypy_boto3_ecr.type_defs import AttributeTypeDef

    data: AttributeTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    EncryptionTypeType,
    FindingSeverityType,
    ImageFailureCodeType,
    ImageTagMutabilityType,
    LayerAvailabilityType,
    LayerFailureCodeType,
    LifecyclePolicyPreviewStatusType,
    ReplicationStatusType,
    ScanFrequencyType,
    ScanStatusType,
    ScanTypeType,
    TagStatusType,
    UpstreamRegistryType,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AttributeTypeDef",
    "AuthorizationDataTypeDef",
    "AwsEcrContainerImageDetailsTypeDef",
    "BatchCheckLayerAvailabilityRequestRequestTypeDef",
    "LayerFailureTypeDef",
    "LayerTypeDef",
    "ResponseMetadataTypeDef",
    "ImageIdentifierTypeDef",
    "BatchGetRepositoryScanningConfigurationRequestRequestTypeDef",
    "RepositoryScanningConfigurationFailureTypeDef",
    "BlobTypeDef",
    "CompleteLayerUploadRequestRequestTypeDef",
    "CreatePullThroughCacheRuleRequestRequestTypeDef",
    "EncryptionConfigurationTypeDef",
    "ImageScanningConfigurationTypeDef",
    "TagTypeDef",
    "CvssScoreAdjustmentTypeDef",
    "CvssScoreTypeDef",
    "DeleteLifecyclePolicyRequestRequestTypeDef",
    "DeletePullThroughCacheRuleRequestRequestTypeDef",
    "DeleteRepositoryPolicyRequestRequestTypeDef",
    "DeleteRepositoryRequestRequestTypeDef",
    "ImageReplicationStatusTypeDef",
    "PaginatorConfigTypeDef",
    "WaiterConfigTypeDef",
    "ImageScanStatusTypeDef",
    "DescribeImagesFilterTypeDef",
    "DescribePullThroughCacheRulesRequestRequestTypeDef",
    "PullThroughCacheRuleTypeDef",
    "DescribeRepositoriesRequestRequestTypeDef",
    "GetAuthorizationTokenRequestRequestTypeDef",
    "GetDownloadUrlForLayerRequestRequestTypeDef",
    "LifecyclePolicyPreviewFilterTypeDef",
    "LifecyclePolicyPreviewSummaryTypeDef",
    "GetLifecyclePolicyRequestRequestTypeDef",
    "GetRepositoryPolicyRequestRequestTypeDef",
    "ImageScanFindingsSummaryTypeDef",
    "InitiateLayerUploadRequestRequestTypeDef",
    "LifecyclePolicyRuleActionTypeDef",
    "ListImagesFilterTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "VulnerablePackageTypeDef",
    "PutImageRequestRequestTypeDef",
    "PutImageTagMutabilityRequestRequestTypeDef",
    "PutLifecyclePolicyRequestRequestTypeDef",
    "PutRegistryPolicyRequestRequestTypeDef",
    "RecommendationTypeDef",
    "ScanningRepositoryFilterTypeDef",
    "ReplicationDestinationTypeDef",
    "RepositoryFilterTypeDef",
    "SetRepositoryPolicyRequestRequestTypeDef",
    "StartLifecyclePolicyPreviewRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdatePullThroughCacheRuleRequestRequestTypeDef",
    "ValidatePullThroughCacheRuleRequestRequestTypeDef",
    "ImageScanFindingTypeDef",
    "ResourceDetailsTypeDef",
    "BatchCheckLayerAvailabilityResponseTypeDef",
    "CompleteLayerUploadResponseTypeDef",
    "CreatePullThroughCacheRuleResponseTypeDef",
    "DeleteLifecyclePolicyResponseTypeDef",
    "DeletePullThroughCacheRuleResponseTypeDef",
    "DeleteRegistryPolicyResponseTypeDef",
    "DeleteRepositoryPolicyResponseTypeDef",
    "GetAuthorizationTokenResponseTypeDef",
    "GetDownloadUrlForLayerResponseTypeDef",
    "GetLifecyclePolicyResponseTypeDef",
    "GetRegistryPolicyResponseTypeDef",
    "GetRepositoryPolicyResponseTypeDef",
    "InitiateLayerUploadResponseTypeDef",
    "PutImageTagMutabilityResponseTypeDef",
    "PutLifecyclePolicyResponseTypeDef",
    "PutRegistryPolicyResponseTypeDef",
    "SetRepositoryPolicyResponseTypeDef",
    "StartLifecyclePolicyPreviewResponseTypeDef",
    "UpdatePullThroughCacheRuleResponseTypeDef",
    "UploadLayerPartResponseTypeDef",
    "ValidatePullThroughCacheRuleResponseTypeDef",
    "BatchDeleteImageRequestRequestTypeDef",
    "BatchGetImageRequestRequestTypeDef",
    "DescribeImageReplicationStatusRequestRequestTypeDef",
    "DescribeImageScanFindingsRequestRequestTypeDef",
    "ImageFailureTypeDef",
    "ImageTypeDef",
    "ListImagesResponseTypeDef",
    "StartImageScanRequestRequestTypeDef",
    "UploadLayerPartRequestRequestTypeDef",
    "PutImageScanningConfigurationRequestRequestTypeDef",
    "PutImageScanningConfigurationResponseTypeDef",
    "RepositoryTypeDef",
    "CreateRepositoryRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CvssScoreDetailsTypeDef",
    "DescribeImageReplicationStatusResponseTypeDef",
    "DescribeImageScanFindingsRequestDescribeImageScanFindingsPaginateTypeDef",
    "DescribePullThroughCacheRulesRequestDescribePullThroughCacheRulesPaginateTypeDef",
    "DescribeRepositoriesRequestDescribeRepositoriesPaginateTypeDef",
    "DescribeImageScanFindingsRequestImageScanCompleteWaitTypeDef",
    "StartImageScanResponseTypeDef",
    "DescribeImagesRequestDescribeImagesPaginateTypeDef",
    "DescribeImagesRequestRequestTypeDef",
    "DescribePullThroughCacheRulesResponseTypeDef",
    "GetLifecyclePolicyPreviewRequestGetLifecyclePolicyPreviewPaginateTypeDef",
    "GetLifecyclePolicyPreviewRequestLifecyclePolicyPreviewCompleteWaitTypeDef",
    "GetLifecyclePolicyPreviewRequestRequestTypeDef",
    "ImageDetailTypeDef",
    "LifecyclePolicyPreviewResultTypeDef",
    "ListImagesRequestListImagesPaginateTypeDef",
    "ListImagesRequestRequestTypeDef",
    "PackageVulnerabilityDetailsTypeDef",
    "RemediationTypeDef",
    "RegistryScanningRuleTypeDef",
    "RepositoryScanningConfigurationTypeDef",
    "ReplicationRuleTypeDef",
    "ResourceTypeDef",
    "BatchDeleteImageResponseTypeDef",
    "BatchGetImageResponseTypeDef",
    "PutImageResponseTypeDef",
    "CreateRepositoryResponseTypeDef",
    "DeleteRepositoryResponseTypeDef",
    "DescribeRepositoriesResponseTypeDef",
    "ScoreDetailsTypeDef",
    "DescribeImagesResponseTypeDef",
    "GetLifecyclePolicyPreviewResponseTypeDef",
    "PutRegistryScanningConfigurationRequestRequestTypeDef",
    "RegistryScanningConfigurationTypeDef",
    "BatchGetRepositoryScanningConfigurationResponseTypeDef",
    "ReplicationConfigurationTypeDef",
    "EnhancedImageScanFindingTypeDef",
    "GetRegistryScanningConfigurationResponseTypeDef",
    "PutRegistryScanningConfigurationResponseTypeDef",
    "DescribeRegistryResponseTypeDef",
    "PutReplicationConfigurationRequestRequestTypeDef",
    "PutReplicationConfigurationResponseTypeDef",
    "ImageScanFindingsTypeDef",
    "DescribeImageScanFindingsResponseTypeDef",
)

AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "key": str,
        "value": NotRequired[str],
    },
)
AuthorizationDataTypeDef = TypedDict(
    "AuthorizationDataTypeDef",
    {
        "authorizationToken": NotRequired[str],
        "expiresAt": NotRequired[datetime],
        "proxyEndpoint": NotRequired[str],
    },
)
AwsEcrContainerImageDetailsTypeDef = TypedDict(
    "AwsEcrContainerImageDetailsTypeDef",
    {
        "architecture": NotRequired[str],
        "author": NotRequired[str],
        "imageHash": NotRequired[str],
        "imageTags": NotRequired[List[str]],
        "platform": NotRequired[str],
        "pushedAt": NotRequired[datetime],
        "registry": NotRequired[str],
        "repositoryName": NotRequired[str],
    },
)
BatchCheckLayerAvailabilityRequestRequestTypeDef = TypedDict(
    "BatchCheckLayerAvailabilityRequestRequestTypeDef",
    {
        "repositoryName": str,
        "layerDigests": Sequence[str],
        "registryId": NotRequired[str],
    },
)
LayerFailureTypeDef = TypedDict(
    "LayerFailureTypeDef",
    {
        "layerDigest": NotRequired[str],
        "failureCode": NotRequired[LayerFailureCodeType],
        "failureReason": NotRequired[str],
    },
)
LayerTypeDef = TypedDict(
    "LayerTypeDef",
    {
        "layerDigest": NotRequired[str],
        "layerAvailability": NotRequired[LayerAvailabilityType],
        "layerSize": NotRequired[int],
        "mediaType": NotRequired[str],
    },
)
ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
    },
)
ImageIdentifierTypeDef = TypedDict(
    "ImageIdentifierTypeDef",
    {
        "imageDigest": NotRequired[str],
        "imageTag": NotRequired[str],
    },
)
BatchGetRepositoryScanningConfigurationRequestRequestTypeDef = TypedDict(
    "BatchGetRepositoryScanningConfigurationRequestRequestTypeDef",
    {
        "repositoryNames": Sequence[str],
    },
)
RepositoryScanningConfigurationFailureTypeDef = TypedDict(
    "RepositoryScanningConfigurationFailureTypeDef",
    {
        "repositoryName": NotRequired[str],
        "failureCode": NotRequired[Literal["REPOSITORY_NOT_FOUND"]],
        "failureReason": NotRequired[str],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
CompleteLayerUploadRequestRequestTypeDef = TypedDict(
    "CompleteLayerUploadRequestRequestTypeDef",
    {
        "repositoryName": str,
        "uploadId": str,
        "layerDigests": Sequence[str],
        "registryId": NotRequired[str],
    },
)
CreatePullThroughCacheRuleRequestRequestTypeDef = TypedDict(
    "CreatePullThroughCacheRuleRequestRequestTypeDef",
    {
        "ecrRepositoryPrefix": str,
        "upstreamRegistryUrl": str,
        "registryId": NotRequired[str],
        "upstreamRegistry": NotRequired[UpstreamRegistryType],
        "credentialArn": NotRequired[str],
    },
)
EncryptionConfigurationTypeDef = TypedDict(
    "EncryptionConfigurationTypeDef",
    {
        "encryptionType": EncryptionTypeType,
        "kmsKey": NotRequired[str],
    },
)
ImageScanningConfigurationTypeDef = TypedDict(
    "ImageScanningConfigurationTypeDef",
    {
        "scanOnPush": NotRequired[bool],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
CvssScoreAdjustmentTypeDef = TypedDict(
    "CvssScoreAdjustmentTypeDef",
    {
        "metric": NotRequired[str],
        "reason": NotRequired[str],
    },
)
CvssScoreTypeDef = TypedDict(
    "CvssScoreTypeDef",
    {
        "baseScore": NotRequired[float],
        "scoringVector": NotRequired[str],
        "source": NotRequired[str],
        "version": NotRequired[str],
    },
)
DeleteLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "DeleteLifecyclePolicyRequestRequestTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
    },
)
DeletePullThroughCacheRuleRequestRequestTypeDef = TypedDict(
    "DeletePullThroughCacheRuleRequestRequestTypeDef",
    {
        "ecrRepositoryPrefix": str,
        "registryId": NotRequired[str],
    },
)
DeleteRepositoryPolicyRequestRequestTypeDef = TypedDict(
    "DeleteRepositoryPolicyRequestRequestTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
    },
)
DeleteRepositoryRequestRequestTypeDef = TypedDict(
    "DeleteRepositoryRequestRequestTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
        "force": NotRequired[bool],
    },
)
ImageReplicationStatusTypeDef = TypedDict(
    "ImageReplicationStatusTypeDef",
    {
        "region": NotRequired[str],
        "registryId": NotRequired[str],
        "status": NotRequired[ReplicationStatusType],
        "failureCode": NotRequired[str],
    },
)
PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": NotRequired[int],
        "PageSize": NotRequired[int],
        "StartingToken": NotRequired[str],
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
ImageScanStatusTypeDef = TypedDict(
    "ImageScanStatusTypeDef",
    {
        "status": NotRequired[ScanStatusType],
        "description": NotRequired[str],
    },
)
DescribeImagesFilterTypeDef = TypedDict(
    "DescribeImagesFilterTypeDef",
    {
        "tagStatus": NotRequired[TagStatusType],
    },
)
DescribePullThroughCacheRulesRequestRequestTypeDef = TypedDict(
    "DescribePullThroughCacheRulesRequestRequestTypeDef",
    {
        "registryId": NotRequired[str],
        "ecrRepositoryPrefixes": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
PullThroughCacheRuleTypeDef = TypedDict(
    "PullThroughCacheRuleTypeDef",
    {
        "ecrRepositoryPrefix": NotRequired[str],
        "upstreamRegistryUrl": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "registryId": NotRequired[str],
        "credentialArn": NotRequired[str],
        "upstreamRegistry": NotRequired[UpstreamRegistryType],
        "updatedAt": NotRequired[datetime],
    },
)
DescribeRepositoriesRequestRequestTypeDef = TypedDict(
    "DescribeRepositoriesRequestRequestTypeDef",
    {
        "registryId": NotRequired[str],
        "repositoryNames": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
GetAuthorizationTokenRequestRequestTypeDef = TypedDict(
    "GetAuthorizationTokenRequestRequestTypeDef",
    {
        "registryIds": NotRequired[Sequence[str]],
    },
)
GetDownloadUrlForLayerRequestRequestTypeDef = TypedDict(
    "GetDownloadUrlForLayerRequestRequestTypeDef",
    {
        "repositoryName": str,
        "layerDigest": str,
        "registryId": NotRequired[str],
    },
)
LifecyclePolicyPreviewFilterTypeDef = TypedDict(
    "LifecyclePolicyPreviewFilterTypeDef",
    {
        "tagStatus": NotRequired[TagStatusType],
    },
)
LifecyclePolicyPreviewSummaryTypeDef = TypedDict(
    "LifecyclePolicyPreviewSummaryTypeDef",
    {
        "expiringImageTotalCount": NotRequired[int],
    },
)
GetLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "GetLifecyclePolicyRequestRequestTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
    },
)
GetRepositoryPolicyRequestRequestTypeDef = TypedDict(
    "GetRepositoryPolicyRequestRequestTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
    },
)
ImageScanFindingsSummaryTypeDef = TypedDict(
    "ImageScanFindingsSummaryTypeDef",
    {
        "imageScanCompletedAt": NotRequired[datetime],
        "vulnerabilitySourceUpdatedAt": NotRequired[datetime],
        "findingSeverityCounts": NotRequired[Dict[FindingSeverityType, int]],
    },
)
InitiateLayerUploadRequestRequestTypeDef = TypedDict(
    "InitiateLayerUploadRequestRequestTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
    },
)
LifecyclePolicyRuleActionTypeDef = TypedDict(
    "LifecyclePolicyRuleActionTypeDef",
    {
        "type": NotRequired[Literal["EXPIRE"]],
    },
)
ListImagesFilterTypeDef = TypedDict(
    "ListImagesFilterTypeDef",
    {
        "tagStatus": NotRequired[TagStatusType],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
VulnerablePackageTypeDef = TypedDict(
    "VulnerablePackageTypeDef",
    {
        "arch": NotRequired[str],
        "epoch": NotRequired[int],
        "filePath": NotRequired[str],
        "name": NotRequired[str],
        "packageManager": NotRequired[str],
        "release": NotRequired[str],
        "sourceLayerHash": NotRequired[str],
        "version": NotRequired[str],
    },
)
PutImageRequestRequestTypeDef = TypedDict(
    "PutImageRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageManifest": str,
        "registryId": NotRequired[str],
        "imageManifestMediaType": NotRequired[str],
        "imageTag": NotRequired[str],
        "imageDigest": NotRequired[str],
    },
)
PutImageTagMutabilityRequestRequestTypeDef = TypedDict(
    "PutImageTagMutabilityRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageTagMutability": ImageTagMutabilityType,
        "registryId": NotRequired[str],
    },
)
PutLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "PutLifecyclePolicyRequestRequestTypeDef",
    {
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "registryId": NotRequired[str],
    },
)
PutRegistryPolicyRequestRequestTypeDef = TypedDict(
    "PutRegistryPolicyRequestRequestTypeDef",
    {
        "policyText": str,
    },
)
RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "url": NotRequired[str],
        "text": NotRequired[str],
    },
)
ScanningRepositoryFilterTypeDef = TypedDict(
    "ScanningRepositoryFilterTypeDef",
    {
        "filter": str,
        "filterType": Literal["WILDCARD"],
    },
)
ReplicationDestinationTypeDef = TypedDict(
    "ReplicationDestinationTypeDef",
    {
        "region": str,
        "registryId": str,
    },
)
RepositoryFilterTypeDef = TypedDict(
    "RepositoryFilterTypeDef",
    {
        "filter": str,
        "filterType": Literal["PREFIX_MATCH"],
    },
)
SetRepositoryPolicyRequestRequestTypeDef = TypedDict(
    "SetRepositoryPolicyRequestRequestTypeDef",
    {
        "repositoryName": str,
        "policyText": str,
        "registryId": NotRequired[str],
        "force": NotRequired[bool],
    },
)
StartLifecyclePolicyPreviewRequestRequestTypeDef = TypedDict(
    "StartLifecyclePolicyPreviewRequestRequestTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
        "lifecyclePolicyText": NotRequired[str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
UpdatePullThroughCacheRuleRequestRequestTypeDef = TypedDict(
    "UpdatePullThroughCacheRuleRequestRequestTypeDef",
    {
        "ecrRepositoryPrefix": str,
        "credentialArn": str,
        "registryId": NotRequired[str],
    },
)
ValidatePullThroughCacheRuleRequestRequestTypeDef = TypedDict(
    "ValidatePullThroughCacheRuleRequestRequestTypeDef",
    {
        "ecrRepositoryPrefix": str,
        "registryId": NotRequired[str],
    },
)
ImageScanFindingTypeDef = TypedDict(
    "ImageScanFindingTypeDef",
    {
        "name": NotRequired[str],
        "description": NotRequired[str],
        "uri": NotRequired[str],
        "severity": NotRequired[FindingSeverityType],
        "attributes": NotRequired[List[AttributeTypeDef]],
    },
)
ResourceDetailsTypeDef = TypedDict(
    "ResourceDetailsTypeDef",
    {
        "awsEcrContainerImage": NotRequired[AwsEcrContainerImageDetailsTypeDef],
    },
)
BatchCheckLayerAvailabilityResponseTypeDef = TypedDict(
    "BatchCheckLayerAvailabilityResponseTypeDef",
    {
        "layers": List[LayerTypeDef],
        "failures": List[LayerFailureTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CompleteLayerUploadResponseTypeDef = TypedDict(
    "CompleteLayerUploadResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "uploadId": str,
        "layerDigest": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePullThroughCacheRuleResponseTypeDef = TypedDict(
    "CreatePullThroughCacheRuleResponseTypeDef",
    {
        "ecrRepositoryPrefix": str,
        "upstreamRegistryUrl": str,
        "createdAt": datetime,
        "registryId": str,
        "upstreamRegistry": UpstreamRegistryType,
        "credentialArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteLifecyclePolicyResponseTypeDef = TypedDict(
    "DeleteLifecyclePolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "lastEvaluatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeletePullThroughCacheRuleResponseTypeDef = TypedDict(
    "DeletePullThroughCacheRuleResponseTypeDef",
    {
        "ecrRepositoryPrefix": str,
        "upstreamRegistryUrl": str,
        "createdAt": datetime,
        "registryId": str,
        "credentialArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteRegistryPolicyResponseTypeDef = TypedDict(
    "DeleteRegistryPolicyResponseTypeDef",
    {
        "registryId": str,
        "policyText": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteRepositoryPolicyResponseTypeDef = TypedDict(
    "DeleteRepositoryPolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "policyText": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAuthorizationTokenResponseTypeDef = TypedDict(
    "GetAuthorizationTokenResponseTypeDef",
    {
        "authorizationData": List[AuthorizationDataTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDownloadUrlForLayerResponseTypeDef = TypedDict(
    "GetDownloadUrlForLayerResponseTypeDef",
    {
        "downloadUrl": str,
        "layerDigest": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLifecyclePolicyResponseTypeDef = TypedDict(
    "GetLifecyclePolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "lastEvaluatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRegistryPolicyResponseTypeDef = TypedDict(
    "GetRegistryPolicyResponseTypeDef",
    {
        "registryId": str,
        "policyText": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRepositoryPolicyResponseTypeDef = TypedDict(
    "GetRepositoryPolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "policyText": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InitiateLayerUploadResponseTypeDef = TypedDict(
    "InitiateLayerUploadResponseTypeDef",
    {
        "uploadId": str,
        "partSize": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutImageTagMutabilityResponseTypeDef = TypedDict(
    "PutImageTagMutabilityResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageTagMutability": ImageTagMutabilityType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutLifecyclePolicyResponseTypeDef = TypedDict(
    "PutLifecyclePolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutRegistryPolicyResponseTypeDef = TypedDict(
    "PutRegistryPolicyResponseTypeDef",
    {
        "registryId": str,
        "policyText": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SetRepositoryPolicyResponseTypeDef = TypedDict(
    "SetRepositoryPolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "policyText": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartLifecyclePolicyPreviewResponseTypeDef = TypedDict(
    "StartLifecyclePolicyPreviewResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "status": LifecyclePolicyPreviewStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePullThroughCacheRuleResponseTypeDef = TypedDict(
    "UpdatePullThroughCacheRuleResponseTypeDef",
    {
        "ecrRepositoryPrefix": str,
        "registryId": str,
        "updatedAt": datetime,
        "credentialArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UploadLayerPartResponseTypeDef = TypedDict(
    "UploadLayerPartResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "uploadId": str,
        "lastByteReceived": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ValidatePullThroughCacheRuleResponseTypeDef = TypedDict(
    "ValidatePullThroughCacheRuleResponseTypeDef",
    {
        "ecrRepositoryPrefix": str,
        "registryId": str,
        "upstreamRegistryUrl": str,
        "credentialArn": str,
        "isValid": bool,
        "failure": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDeleteImageRequestRequestTypeDef = TypedDict(
    "BatchDeleteImageRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageIds": Sequence[ImageIdentifierTypeDef],
        "registryId": NotRequired[str],
    },
)
BatchGetImageRequestRequestTypeDef = TypedDict(
    "BatchGetImageRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageIds": Sequence[ImageIdentifierTypeDef],
        "registryId": NotRequired[str],
        "acceptedMediaTypes": NotRequired[Sequence[str]],
    },
)
DescribeImageReplicationStatusRequestRequestTypeDef = TypedDict(
    "DescribeImageReplicationStatusRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageId": ImageIdentifierTypeDef,
        "registryId": NotRequired[str],
    },
)
DescribeImageScanFindingsRequestRequestTypeDef = TypedDict(
    "DescribeImageScanFindingsRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageId": ImageIdentifierTypeDef,
        "registryId": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ImageFailureTypeDef = TypedDict(
    "ImageFailureTypeDef",
    {
        "imageId": NotRequired[ImageIdentifierTypeDef],
        "failureCode": NotRequired[ImageFailureCodeType],
        "failureReason": NotRequired[str],
    },
)
ImageTypeDef = TypedDict(
    "ImageTypeDef",
    {
        "registryId": NotRequired[str],
        "repositoryName": NotRequired[str],
        "imageId": NotRequired[ImageIdentifierTypeDef],
        "imageManifest": NotRequired[str],
        "imageManifestMediaType": NotRequired[str],
    },
)
ListImagesResponseTypeDef = TypedDict(
    "ListImagesResponseTypeDef",
    {
        "imageIds": List[ImageIdentifierTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartImageScanRequestRequestTypeDef = TypedDict(
    "StartImageScanRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageId": ImageIdentifierTypeDef,
        "registryId": NotRequired[str],
    },
)
UploadLayerPartRequestRequestTypeDef = TypedDict(
    "UploadLayerPartRequestRequestTypeDef",
    {
        "repositoryName": str,
        "uploadId": str,
        "partFirstByte": int,
        "partLastByte": int,
        "layerPartBlob": BlobTypeDef,
        "registryId": NotRequired[str],
    },
)
PutImageScanningConfigurationRequestRequestTypeDef = TypedDict(
    "PutImageScanningConfigurationRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageScanningConfiguration": ImageScanningConfigurationTypeDef,
        "registryId": NotRequired[str],
    },
)
PutImageScanningConfigurationResponseTypeDef = TypedDict(
    "PutImageScanningConfigurationResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageScanningConfiguration": ImageScanningConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RepositoryTypeDef = TypedDict(
    "RepositoryTypeDef",
    {
        "repositoryArn": NotRequired[str],
        "registryId": NotRequired[str],
        "repositoryName": NotRequired[str],
        "repositoryUri": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "imageTagMutability": NotRequired[ImageTagMutabilityType],
        "imageScanningConfiguration": NotRequired[ImageScanningConfigurationTypeDef],
        "encryptionConfiguration": NotRequired[EncryptionConfigurationTypeDef],
    },
)
CreateRepositoryRequestRequestTypeDef = TypedDict(
    "CreateRepositoryRequestRequestTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "imageTagMutability": NotRequired[ImageTagMutabilityType],
        "imageScanningConfiguration": NotRequired[ImageScanningConfigurationTypeDef],
        "encryptionConfiguration": NotRequired[EncryptionConfigurationTypeDef],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence[TagTypeDef],
    },
)
CvssScoreDetailsTypeDef = TypedDict(
    "CvssScoreDetailsTypeDef",
    {
        "adjustments": NotRequired[List[CvssScoreAdjustmentTypeDef]],
        "score": NotRequired[float],
        "scoreSource": NotRequired[str],
        "scoringVector": NotRequired[str],
        "version": NotRequired[str],
    },
)
DescribeImageReplicationStatusResponseTypeDef = TypedDict(
    "DescribeImageReplicationStatusResponseTypeDef",
    {
        "repositoryName": str,
        "imageId": ImageIdentifierTypeDef,
        "replicationStatuses": List[ImageReplicationStatusTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeImageScanFindingsRequestDescribeImageScanFindingsPaginateTypeDef = TypedDict(
    "DescribeImageScanFindingsRequestDescribeImageScanFindingsPaginateTypeDef",
    {
        "repositoryName": str,
        "imageId": ImageIdentifierTypeDef,
        "registryId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribePullThroughCacheRulesRequestDescribePullThroughCacheRulesPaginateTypeDef = TypedDict(
    "DescribePullThroughCacheRulesRequestDescribePullThroughCacheRulesPaginateTypeDef",
    {
        "registryId": NotRequired[str],
        "ecrRepositoryPrefixes": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeRepositoriesRequestDescribeRepositoriesPaginateTypeDef = TypedDict(
    "DescribeRepositoriesRequestDescribeRepositoriesPaginateTypeDef",
    {
        "registryId": NotRequired[str],
        "repositoryNames": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeImageScanFindingsRequestImageScanCompleteWaitTypeDef = TypedDict(
    "DescribeImageScanFindingsRequestImageScanCompleteWaitTypeDef",
    {
        "repositoryName": str,
        "imageId": ImageIdentifierTypeDef,
        "registryId": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
StartImageScanResponseTypeDef = TypedDict(
    "StartImageScanResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageId": ImageIdentifierTypeDef,
        "imageScanStatus": ImageScanStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeImagesRequestDescribeImagesPaginateTypeDef = TypedDict(
    "DescribeImagesRequestDescribeImagesPaginateTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
        "imageIds": NotRequired[Sequence[ImageIdentifierTypeDef]],
        "filter": NotRequired[DescribeImagesFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeImagesRequestRequestTypeDef = TypedDict(
    "DescribeImagesRequestRequestTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
        "imageIds": NotRequired[Sequence[ImageIdentifierTypeDef]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filter": NotRequired[DescribeImagesFilterTypeDef],
    },
)
DescribePullThroughCacheRulesResponseTypeDef = TypedDict(
    "DescribePullThroughCacheRulesResponseTypeDef",
    {
        "pullThroughCacheRules": List[PullThroughCacheRuleTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLifecyclePolicyPreviewRequestGetLifecyclePolicyPreviewPaginateTypeDef = TypedDict(
    "GetLifecyclePolicyPreviewRequestGetLifecyclePolicyPreviewPaginateTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
        "imageIds": NotRequired[Sequence[ImageIdentifierTypeDef]],
        "filter": NotRequired[LifecyclePolicyPreviewFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetLifecyclePolicyPreviewRequestLifecyclePolicyPreviewCompleteWaitTypeDef = TypedDict(
    "GetLifecyclePolicyPreviewRequestLifecyclePolicyPreviewCompleteWaitTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
        "imageIds": NotRequired[Sequence[ImageIdentifierTypeDef]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filter": NotRequired[LifecyclePolicyPreviewFilterTypeDef],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetLifecyclePolicyPreviewRequestRequestTypeDef = TypedDict(
    "GetLifecyclePolicyPreviewRequestRequestTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
        "imageIds": NotRequired[Sequence[ImageIdentifierTypeDef]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filter": NotRequired[LifecyclePolicyPreviewFilterTypeDef],
    },
)
ImageDetailTypeDef = TypedDict(
    "ImageDetailTypeDef",
    {
        "registryId": NotRequired[str],
        "repositoryName": NotRequired[str],
        "imageDigest": NotRequired[str],
        "imageTags": NotRequired[List[str]],
        "imageSizeInBytes": NotRequired[int],
        "imagePushedAt": NotRequired[datetime],
        "imageScanStatus": NotRequired[ImageScanStatusTypeDef],
        "imageScanFindingsSummary": NotRequired[ImageScanFindingsSummaryTypeDef],
        "imageManifestMediaType": NotRequired[str],
        "artifactMediaType": NotRequired[str],
        "lastRecordedPullTime": NotRequired[datetime],
    },
)
LifecyclePolicyPreviewResultTypeDef = TypedDict(
    "LifecyclePolicyPreviewResultTypeDef",
    {
        "imageTags": NotRequired[List[str]],
        "imageDigest": NotRequired[str],
        "imagePushedAt": NotRequired[datetime],
        "action": NotRequired[LifecyclePolicyRuleActionTypeDef],
        "appliedRulePriority": NotRequired[int],
    },
)
ListImagesRequestListImagesPaginateTypeDef = TypedDict(
    "ListImagesRequestListImagesPaginateTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
        "filter": NotRequired[ListImagesFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListImagesRequestRequestTypeDef = TypedDict(
    "ListImagesRequestRequestTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filter": NotRequired[ListImagesFilterTypeDef],
    },
)
PackageVulnerabilityDetailsTypeDef = TypedDict(
    "PackageVulnerabilityDetailsTypeDef",
    {
        "cvss": NotRequired[List[CvssScoreTypeDef]],
        "referenceUrls": NotRequired[List[str]],
        "relatedVulnerabilities": NotRequired[List[str]],
        "source": NotRequired[str],
        "sourceUrl": NotRequired[str],
        "vendorCreatedAt": NotRequired[datetime],
        "vendorSeverity": NotRequired[str],
        "vendorUpdatedAt": NotRequired[datetime],
        "vulnerabilityId": NotRequired[str],
        "vulnerablePackages": NotRequired[List[VulnerablePackageTypeDef]],
    },
)
RemediationTypeDef = TypedDict(
    "RemediationTypeDef",
    {
        "recommendation": NotRequired[RecommendationTypeDef],
    },
)
RegistryScanningRuleTypeDef = TypedDict(
    "RegistryScanningRuleTypeDef",
    {
        "scanFrequency": ScanFrequencyType,
        "repositoryFilters": List[ScanningRepositoryFilterTypeDef],
    },
)
RepositoryScanningConfigurationTypeDef = TypedDict(
    "RepositoryScanningConfigurationTypeDef",
    {
        "repositoryArn": NotRequired[str],
        "repositoryName": NotRequired[str],
        "scanOnPush": NotRequired[bool],
        "scanFrequency": NotRequired[ScanFrequencyType],
        "appliedScanFilters": NotRequired[List[ScanningRepositoryFilterTypeDef]],
    },
)
ReplicationRuleTypeDef = TypedDict(
    "ReplicationRuleTypeDef",
    {
        "destinations": List[ReplicationDestinationTypeDef],
        "repositoryFilters": NotRequired[List[RepositoryFilterTypeDef]],
    },
)
ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "details": NotRequired[ResourceDetailsTypeDef],
        "id": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "type": NotRequired[str],
    },
)
BatchDeleteImageResponseTypeDef = TypedDict(
    "BatchDeleteImageResponseTypeDef",
    {
        "imageIds": List[ImageIdentifierTypeDef],
        "failures": List[ImageFailureTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchGetImageResponseTypeDef = TypedDict(
    "BatchGetImageResponseTypeDef",
    {
        "images": List[ImageTypeDef],
        "failures": List[ImageFailureTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutImageResponseTypeDef = TypedDict(
    "PutImageResponseTypeDef",
    {
        "image": ImageTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRepositoryResponseTypeDef = TypedDict(
    "CreateRepositoryResponseTypeDef",
    {
        "repository": RepositoryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteRepositoryResponseTypeDef = TypedDict(
    "DeleteRepositoryResponseTypeDef",
    {
        "repository": RepositoryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeRepositoriesResponseTypeDef = TypedDict(
    "DescribeRepositoriesResponseTypeDef",
    {
        "repositories": List[RepositoryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ScoreDetailsTypeDef = TypedDict(
    "ScoreDetailsTypeDef",
    {
        "cvss": NotRequired[CvssScoreDetailsTypeDef],
    },
)
DescribeImagesResponseTypeDef = TypedDict(
    "DescribeImagesResponseTypeDef",
    {
        "imageDetails": List[ImageDetailTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLifecyclePolicyPreviewResponseTypeDef = TypedDict(
    "GetLifecyclePolicyPreviewResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "status": LifecyclePolicyPreviewStatusType,
        "nextToken": str,
        "previewResults": List[LifecyclePolicyPreviewResultTypeDef],
        "summary": LifecyclePolicyPreviewSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutRegistryScanningConfigurationRequestRequestTypeDef = TypedDict(
    "PutRegistryScanningConfigurationRequestRequestTypeDef",
    {
        "scanType": NotRequired[ScanTypeType],
        "rules": NotRequired[Sequence[RegistryScanningRuleTypeDef]],
    },
)
RegistryScanningConfigurationTypeDef = TypedDict(
    "RegistryScanningConfigurationTypeDef",
    {
        "scanType": NotRequired[ScanTypeType],
        "rules": NotRequired[List[RegistryScanningRuleTypeDef]],
    },
)
BatchGetRepositoryScanningConfigurationResponseTypeDef = TypedDict(
    "BatchGetRepositoryScanningConfigurationResponseTypeDef",
    {
        "scanningConfigurations": List[RepositoryScanningConfigurationTypeDef],
        "failures": List[RepositoryScanningConfigurationFailureTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReplicationConfigurationTypeDef = TypedDict(
    "ReplicationConfigurationTypeDef",
    {
        "rules": List[ReplicationRuleTypeDef],
    },
)
EnhancedImageScanFindingTypeDef = TypedDict(
    "EnhancedImageScanFindingTypeDef",
    {
        "awsAccountId": NotRequired[str],
        "description": NotRequired[str],
        "findingArn": NotRequired[str],
        "firstObservedAt": NotRequired[datetime],
        "lastObservedAt": NotRequired[datetime],
        "packageVulnerabilityDetails": NotRequired[PackageVulnerabilityDetailsTypeDef],
        "remediation": NotRequired[RemediationTypeDef],
        "resources": NotRequired[List[ResourceTypeDef]],
        "score": NotRequired[float],
        "scoreDetails": NotRequired[ScoreDetailsTypeDef],
        "severity": NotRequired[str],
        "status": NotRequired[str],
        "title": NotRequired[str],
        "type": NotRequired[str],
        "updatedAt": NotRequired[datetime],
    },
)
GetRegistryScanningConfigurationResponseTypeDef = TypedDict(
    "GetRegistryScanningConfigurationResponseTypeDef",
    {
        "registryId": str,
        "scanningConfiguration": RegistryScanningConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutRegistryScanningConfigurationResponseTypeDef = TypedDict(
    "PutRegistryScanningConfigurationResponseTypeDef",
    {
        "registryScanningConfiguration": RegistryScanningConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeRegistryResponseTypeDef = TypedDict(
    "DescribeRegistryResponseTypeDef",
    {
        "registryId": str,
        "replicationConfiguration": ReplicationConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutReplicationConfigurationRequestRequestTypeDef = TypedDict(
    "PutReplicationConfigurationRequestRequestTypeDef",
    {
        "replicationConfiguration": ReplicationConfigurationTypeDef,
    },
)
PutReplicationConfigurationResponseTypeDef = TypedDict(
    "PutReplicationConfigurationResponseTypeDef",
    {
        "replicationConfiguration": ReplicationConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImageScanFindingsTypeDef = TypedDict(
    "ImageScanFindingsTypeDef",
    {
        "imageScanCompletedAt": NotRequired[datetime],
        "vulnerabilitySourceUpdatedAt": NotRequired[datetime],
        "findingSeverityCounts": NotRequired[Dict[FindingSeverityType, int]],
        "findings": NotRequired[List[ImageScanFindingTypeDef]],
        "enhancedFindings": NotRequired[List[EnhancedImageScanFindingTypeDef]],
    },
)
DescribeImageScanFindingsResponseTypeDef = TypedDict(
    "DescribeImageScanFindingsResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageId": ImageIdentifierTypeDef,
        "imageScanStatus": ImageScanStatusTypeDef,
        "imageScanFindings": ImageScanFindingsTypeDef,
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
