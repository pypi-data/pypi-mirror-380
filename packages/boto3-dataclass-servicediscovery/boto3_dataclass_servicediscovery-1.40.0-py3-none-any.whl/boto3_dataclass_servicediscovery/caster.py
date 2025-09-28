# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_servicediscovery import type_defs as bs_td


class SERVICEDISCOVERYCaster:

    def create_http_namespace(
        self,
        res: "bs_td.CreateHttpNamespaceResponseTypeDef",
    ) -> "dc_td.CreateHttpNamespaceResponse":
        return dc_td.CreateHttpNamespaceResponse.make_one(res)

    def create_private_dns_namespace(
        self,
        res: "bs_td.CreatePrivateDnsNamespaceResponseTypeDef",
    ) -> "dc_td.CreatePrivateDnsNamespaceResponse":
        return dc_td.CreatePrivateDnsNamespaceResponse.make_one(res)

    def create_public_dns_namespace(
        self,
        res: "bs_td.CreatePublicDnsNamespaceResponseTypeDef",
    ) -> "dc_td.CreatePublicDnsNamespaceResponse":
        return dc_td.CreatePublicDnsNamespaceResponse.make_one(res)

    def create_service(
        self,
        res: "bs_td.CreateServiceResponseTypeDef",
    ) -> "dc_td.CreateServiceResponse":
        return dc_td.CreateServiceResponse.make_one(res)

    def delete_namespace(
        self,
        res: "bs_td.DeleteNamespaceResponseTypeDef",
    ) -> "dc_td.DeleteNamespaceResponse":
        return dc_td.DeleteNamespaceResponse.make_one(res)

    def deregister_instance(
        self,
        res: "bs_td.DeregisterInstanceResponseTypeDef",
    ) -> "dc_td.DeregisterInstanceResponse":
        return dc_td.DeregisterInstanceResponse.make_one(res)

    def discover_instances(
        self,
        res: "bs_td.DiscoverInstancesResponseTypeDef",
    ) -> "dc_td.DiscoverInstancesResponse":
        return dc_td.DiscoverInstancesResponse.make_one(res)

    def discover_instances_revision(
        self,
        res: "bs_td.DiscoverInstancesRevisionResponseTypeDef",
    ) -> "dc_td.DiscoverInstancesRevisionResponse":
        return dc_td.DiscoverInstancesRevisionResponse.make_one(res)

    def get_instance(
        self,
        res: "bs_td.GetInstanceResponseTypeDef",
    ) -> "dc_td.GetInstanceResponse":
        return dc_td.GetInstanceResponse.make_one(res)

    def get_instances_health_status(
        self,
        res: "bs_td.GetInstancesHealthStatusResponseTypeDef",
    ) -> "dc_td.GetInstancesHealthStatusResponse":
        return dc_td.GetInstancesHealthStatusResponse.make_one(res)

    def get_namespace(
        self,
        res: "bs_td.GetNamespaceResponseTypeDef",
    ) -> "dc_td.GetNamespaceResponse":
        return dc_td.GetNamespaceResponse.make_one(res)

    def get_operation(
        self,
        res: "bs_td.GetOperationResponseTypeDef",
    ) -> "dc_td.GetOperationResponse":
        return dc_td.GetOperationResponse.make_one(res)

    def get_service(
        self,
        res: "bs_td.GetServiceResponseTypeDef",
    ) -> "dc_td.GetServiceResponse":
        return dc_td.GetServiceResponse.make_one(res)

    def get_service_attributes(
        self,
        res: "bs_td.GetServiceAttributesResponseTypeDef",
    ) -> "dc_td.GetServiceAttributesResponse":
        return dc_td.GetServiceAttributesResponse.make_one(res)

    def list_instances(
        self,
        res: "bs_td.ListInstancesResponseTypeDef",
    ) -> "dc_td.ListInstancesResponse":
        return dc_td.ListInstancesResponse.make_one(res)

    def list_namespaces(
        self,
        res: "bs_td.ListNamespacesResponseTypeDef",
    ) -> "dc_td.ListNamespacesResponse":
        return dc_td.ListNamespacesResponse.make_one(res)

    def list_operations(
        self,
        res: "bs_td.ListOperationsResponseTypeDef",
    ) -> "dc_td.ListOperationsResponse":
        return dc_td.ListOperationsResponse.make_one(res)

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

    def register_instance(
        self,
        res: "bs_td.RegisterInstanceResponseTypeDef",
    ) -> "dc_td.RegisterInstanceResponse":
        return dc_td.RegisterInstanceResponse.make_one(res)

    def update_http_namespace(
        self,
        res: "bs_td.UpdateHttpNamespaceResponseTypeDef",
    ) -> "dc_td.UpdateHttpNamespaceResponse":
        return dc_td.UpdateHttpNamespaceResponse.make_one(res)

    def update_instance_custom_health_status(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_private_dns_namespace(
        self,
        res: "bs_td.UpdatePrivateDnsNamespaceResponseTypeDef",
    ) -> "dc_td.UpdatePrivateDnsNamespaceResponse":
        return dc_td.UpdatePrivateDnsNamespaceResponse.make_one(res)

    def update_public_dns_namespace(
        self,
        res: "bs_td.UpdatePublicDnsNamespaceResponseTypeDef",
    ) -> "dc_td.UpdatePublicDnsNamespaceResponse":
        return dc_td.UpdatePublicDnsNamespaceResponse.make_one(res)

    def update_service(
        self,
        res: "bs_td.UpdateServiceResponseTypeDef",
    ) -> "dc_td.UpdateServiceResponse":
        return dc_td.UpdateServiceResponse.make_one(res)


servicediscovery_caster = SERVICEDISCOVERYCaster()
