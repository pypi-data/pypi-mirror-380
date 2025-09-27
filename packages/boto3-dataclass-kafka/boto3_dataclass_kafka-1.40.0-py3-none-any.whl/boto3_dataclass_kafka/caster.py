# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_kafka import type_defs as bs_td


class KAFKACaster:

    def batch_associate_scram_secret(
        self,
        res: "bs_td.BatchAssociateScramSecretResponseTypeDef",
    ) -> "dc_td.BatchAssociateScramSecretResponse":
        return dc_td.BatchAssociateScramSecretResponse.make_one(res)

    def create_cluster(
        self,
        res: "bs_td.CreateClusterResponseTypeDef",
    ) -> "dc_td.CreateClusterResponse":
        return dc_td.CreateClusterResponse.make_one(res)

    def create_cluster_v2(
        self,
        res: "bs_td.CreateClusterV2ResponseTypeDef",
    ) -> "dc_td.CreateClusterV2Response":
        return dc_td.CreateClusterV2Response.make_one(res)

    def create_configuration(
        self,
        res: "bs_td.CreateConfigurationResponseTypeDef",
    ) -> "dc_td.CreateConfigurationResponse":
        return dc_td.CreateConfigurationResponse.make_one(res)

    def create_replicator(
        self,
        res: "bs_td.CreateReplicatorResponseTypeDef",
    ) -> "dc_td.CreateReplicatorResponse":
        return dc_td.CreateReplicatorResponse.make_one(res)

    def create_vpc_connection(
        self,
        res: "bs_td.CreateVpcConnectionResponseTypeDef",
    ) -> "dc_td.CreateVpcConnectionResponse":
        return dc_td.CreateVpcConnectionResponse.make_one(res)

    def delete_cluster(
        self,
        res: "bs_td.DeleteClusterResponseTypeDef",
    ) -> "dc_td.DeleteClusterResponse":
        return dc_td.DeleteClusterResponse.make_one(res)

    def delete_configuration(
        self,
        res: "bs_td.DeleteConfigurationResponseTypeDef",
    ) -> "dc_td.DeleteConfigurationResponse":
        return dc_td.DeleteConfigurationResponse.make_one(res)

    def delete_replicator(
        self,
        res: "bs_td.DeleteReplicatorResponseTypeDef",
    ) -> "dc_td.DeleteReplicatorResponse":
        return dc_td.DeleteReplicatorResponse.make_one(res)

    def delete_vpc_connection(
        self,
        res: "bs_td.DeleteVpcConnectionResponseTypeDef",
    ) -> "dc_td.DeleteVpcConnectionResponse":
        return dc_td.DeleteVpcConnectionResponse.make_one(res)

    def describe_cluster(
        self,
        res: "bs_td.DescribeClusterResponseTypeDef",
    ) -> "dc_td.DescribeClusterResponse":
        return dc_td.DescribeClusterResponse.make_one(res)

    def describe_cluster_v2(
        self,
        res: "bs_td.DescribeClusterV2ResponseTypeDef",
    ) -> "dc_td.DescribeClusterV2Response":
        return dc_td.DescribeClusterV2Response.make_one(res)

    def describe_cluster_operation(
        self,
        res: "bs_td.DescribeClusterOperationResponseTypeDef",
    ) -> "dc_td.DescribeClusterOperationResponse":
        return dc_td.DescribeClusterOperationResponse.make_one(res)

    def describe_cluster_operation_v2(
        self,
        res: "bs_td.DescribeClusterOperationV2ResponseTypeDef",
    ) -> "dc_td.DescribeClusterOperationV2Response":
        return dc_td.DescribeClusterOperationV2Response.make_one(res)

    def describe_configuration(
        self,
        res: "bs_td.DescribeConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeConfigurationResponse":
        return dc_td.DescribeConfigurationResponse.make_one(res)

    def describe_configuration_revision(
        self,
        res: "bs_td.DescribeConfigurationRevisionResponseTypeDef",
    ) -> "dc_td.DescribeConfigurationRevisionResponse":
        return dc_td.DescribeConfigurationRevisionResponse.make_one(res)

    def describe_replicator(
        self,
        res: "bs_td.DescribeReplicatorResponseTypeDef",
    ) -> "dc_td.DescribeReplicatorResponse":
        return dc_td.DescribeReplicatorResponse.make_one(res)

    def describe_vpc_connection(
        self,
        res: "bs_td.DescribeVpcConnectionResponseTypeDef",
    ) -> "dc_td.DescribeVpcConnectionResponse":
        return dc_td.DescribeVpcConnectionResponse.make_one(res)

    def batch_disassociate_scram_secret(
        self,
        res: "bs_td.BatchDisassociateScramSecretResponseTypeDef",
    ) -> "dc_td.BatchDisassociateScramSecretResponse":
        return dc_td.BatchDisassociateScramSecretResponse.make_one(res)

    def get_bootstrap_brokers(
        self,
        res: "bs_td.GetBootstrapBrokersResponseTypeDef",
    ) -> "dc_td.GetBootstrapBrokersResponse":
        return dc_td.GetBootstrapBrokersResponse.make_one(res)

    def get_compatible_kafka_versions(
        self,
        res: "bs_td.GetCompatibleKafkaVersionsResponseTypeDef",
    ) -> "dc_td.GetCompatibleKafkaVersionsResponse":
        return dc_td.GetCompatibleKafkaVersionsResponse.make_one(res)

    def get_cluster_policy(
        self,
        res: "bs_td.GetClusterPolicyResponseTypeDef",
    ) -> "dc_td.GetClusterPolicyResponse":
        return dc_td.GetClusterPolicyResponse.make_one(res)

    def list_cluster_operations(
        self,
        res: "bs_td.ListClusterOperationsResponseTypeDef",
    ) -> "dc_td.ListClusterOperationsResponse":
        return dc_td.ListClusterOperationsResponse.make_one(res)

    def list_cluster_operations_v2(
        self,
        res: "bs_td.ListClusterOperationsV2ResponseTypeDef",
    ) -> "dc_td.ListClusterOperationsV2Response":
        return dc_td.ListClusterOperationsV2Response.make_one(res)

    def list_clusters(
        self,
        res: "bs_td.ListClustersResponseTypeDef",
    ) -> "dc_td.ListClustersResponse":
        return dc_td.ListClustersResponse.make_one(res)

    def list_clusters_v2(
        self,
        res: "bs_td.ListClustersV2ResponseTypeDef",
    ) -> "dc_td.ListClustersV2Response":
        return dc_td.ListClustersV2Response.make_one(res)

    def list_configuration_revisions(
        self,
        res: "bs_td.ListConfigurationRevisionsResponseTypeDef",
    ) -> "dc_td.ListConfigurationRevisionsResponse":
        return dc_td.ListConfigurationRevisionsResponse.make_one(res)

    def list_configurations(
        self,
        res: "bs_td.ListConfigurationsResponseTypeDef",
    ) -> "dc_td.ListConfigurationsResponse":
        return dc_td.ListConfigurationsResponse.make_one(res)

    def list_kafka_versions(
        self,
        res: "bs_td.ListKafkaVersionsResponseTypeDef",
    ) -> "dc_td.ListKafkaVersionsResponse":
        return dc_td.ListKafkaVersionsResponse.make_one(res)

    def list_nodes(
        self,
        res: "bs_td.ListNodesResponseTypeDef",
    ) -> "dc_td.ListNodesResponse":
        return dc_td.ListNodesResponse.make_one(res)

    def list_replicators(
        self,
        res: "bs_td.ListReplicatorsResponseTypeDef",
    ) -> "dc_td.ListReplicatorsResponse":
        return dc_td.ListReplicatorsResponse.make_one(res)

    def list_scram_secrets(
        self,
        res: "bs_td.ListScramSecretsResponseTypeDef",
    ) -> "dc_td.ListScramSecretsResponse":
        return dc_td.ListScramSecretsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_client_vpc_connections(
        self,
        res: "bs_td.ListClientVpcConnectionsResponseTypeDef",
    ) -> "dc_td.ListClientVpcConnectionsResponse":
        return dc_td.ListClientVpcConnectionsResponse.make_one(res)

    def list_vpc_connections(
        self,
        res: "bs_td.ListVpcConnectionsResponseTypeDef",
    ) -> "dc_td.ListVpcConnectionsResponse":
        return dc_td.ListVpcConnectionsResponse.make_one(res)

    def put_cluster_policy(
        self,
        res: "bs_td.PutClusterPolicyResponseTypeDef",
    ) -> "dc_td.PutClusterPolicyResponse":
        return dc_td.PutClusterPolicyResponse.make_one(res)

    def reboot_broker(
        self,
        res: "bs_td.RebootBrokerResponseTypeDef",
    ) -> "dc_td.RebootBrokerResponse":
        return dc_td.RebootBrokerResponse.make_one(res)

    def tag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_broker_count(
        self,
        res: "bs_td.UpdateBrokerCountResponseTypeDef",
    ) -> "dc_td.UpdateBrokerCountResponse":
        return dc_td.UpdateBrokerCountResponse.make_one(res)

    def update_broker_type(
        self,
        res: "bs_td.UpdateBrokerTypeResponseTypeDef",
    ) -> "dc_td.UpdateBrokerTypeResponse":
        return dc_td.UpdateBrokerTypeResponse.make_one(res)

    def update_broker_storage(
        self,
        res: "bs_td.UpdateBrokerStorageResponseTypeDef",
    ) -> "dc_td.UpdateBrokerStorageResponse":
        return dc_td.UpdateBrokerStorageResponse.make_one(res)

    def update_configuration(
        self,
        res: "bs_td.UpdateConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateConfigurationResponse":
        return dc_td.UpdateConfigurationResponse.make_one(res)

    def update_connectivity(
        self,
        res: "bs_td.UpdateConnectivityResponseTypeDef",
    ) -> "dc_td.UpdateConnectivityResponse":
        return dc_td.UpdateConnectivityResponse.make_one(res)

    def update_cluster_configuration(
        self,
        res: "bs_td.UpdateClusterConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateClusterConfigurationResponse":
        return dc_td.UpdateClusterConfigurationResponse.make_one(res)

    def update_cluster_kafka_version(
        self,
        res: "bs_td.UpdateClusterKafkaVersionResponseTypeDef",
    ) -> "dc_td.UpdateClusterKafkaVersionResponse":
        return dc_td.UpdateClusterKafkaVersionResponse.make_one(res)

    def update_monitoring(
        self,
        res: "bs_td.UpdateMonitoringResponseTypeDef",
    ) -> "dc_td.UpdateMonitoringResponse":
        return dc_td.UpdateMonitoringResponse.make_one(res)

    def update_replication_info(
        self,
        res: "bs_td.UpdateReplicationInfoResponseTypeDef",
    ) -> "dc_td.UpdateReplicationInfoResponse":
        return dc_td.UpdateReplicationInfoResponse.make_one(res)

    def update_security(
        self,
        res: "bs_td.UpdateSecurityResponseTypeDef",
    ) -> "dc_td.UpdateSecurityResponse":
        return dc_td.UpdateSecurityResponse.make_one(res)

    def update_storage(
        self,
        res: "bs_td.UpdateStorageResponseTypeDef",
    ) -> "dc_td.UpdateStorageResponse":
        return dc_td.UpdateStorageResponse.make_one(res)


kafka_caster = KAFKACaster()
