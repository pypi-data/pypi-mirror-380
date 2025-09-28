# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_schemas import type_defs as bs_td


class SCHEMASCaster:

    def create_discoverer(
        self,
        res: "bs_td.CreateDiscovererResponseTypeDef",
    ) -> "dc_td.CreateDiscovererResponse":
        return dc_td.CreateDiscovererResponse.make_one(res)

    def create_registry(
        self,
        res: "bs_td.CreateRegistryResponseTypeDef",
    ) -> "dc_td.CreateRegistryResponse":
        return dc_td.CreateRegistryResponse.make_one(res)

    def create_schema(
        self,
        res: "bs_td.CreateSchemaResponseTypeDef",
    ) -> "dc_td.CreateSchemaResponse":
        return dc_td.CreateSchemaResponse.make_one(res)

    def delete_discoverer(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_registry(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_resource_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_schema(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_schema_version(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_code_binding(
        self,
        res: "bs_td.DescribeCodeBindingResponseTypeDef",
    ) -> "dc_td.DescribeCodeBindingResponse":
        return dc_td.DescribeCodeBindingResponse.make_one(res)

    def describe_discoverer(
        self,
        res: "bs_td.DescribeDiscovererResponseTypeDef",
    ) -> "dc_td.DescribeDiscovererResponse":
        return dc_td.DescribeDiscovererResponse.make_one(res)

    def describe_registry(
        self,
        res: "bs_td.DescribeRegistryResponseTypeDef",
    ) -> "dc_td.DescribeRegistryResponse":
        return dc_td.DescribeRegistryResponse.make_one(res)

    def describe_schema(
        self,
        res: "bs_td.DescribeSchemaResponseTypeDef",
    ) -> "dc_td.DescribeSchemaResponse":
        return dc_td.DescribeSchemaResponse.make_one(res)

    def export_schema(
        self,
        res: "bs_td.ExportSchemaResponseTypeDef",
    ) -> "dc_td.ExportSchemaResponse":
        return dc_td.ExportSchemaResponse.make_one(res)

    def get_code_binding_source(
        self,
        res: "bs_td.GetCodeBindingSourceResponseTypeDef",
    ) -> "dc_td.GetCodeBindingSourceResponse":
        return dc_td.GetCodeBindingSourceResponse.make_one(res)

    def get_discovered_schema(
        self,
        res: "bs_td.GetDiscoveredSchemaResponseTypeDef",
    ) -> "dc_td.GetDiscoveredSchemaResponse":
        return dc_td.GetDiscoveredSchemaResponse.make_one(res)

    def get_resource_policy(
        self,
        res: "bs_td.GetResourcePolicyResponseTypeDef",
    ) -> "dc_td.GetResourcePolicyResponse":
        return dc_td.GetResourcePolicyResponse.make_one(res)

    def list_discoverers(
        self,
        res: "bs_td.ListDiscoverersResponseTypeDef",
    ) -> "dc_td.ListDiscoverersResponse":
        return dc_td.ListDiscoverersResponse.make_one(res)

    def list_registries(
        self,
        res: "bs_td.ListRegistriesResponseTypeDef",
    ) -> "dc_td.ListRegistriesResponse":
        return dc_td.ListRegistriesResponse.make_one(res)

    def list_schema_versions(
        self,
        res: "bs_td.ListSchemaVersionsResponseTypeDef",
    ) -> "dc_td.ListSchemaVersionsResponse":
        return dc_td.ListSchemaVersionsResponse.make_one(res)

    def list_schemas(
        self,
        res: "bs_td.ListSchemasResponseTypeDef",
    ) -> "dc_td.ListSchemasResponse":
        return dc_td.ListSchemasResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def put_code_binding(
        self,
        res: "bs_td.PutCodeBindingResponseTypeDef",
    ) -> "dc_td.PutCodeBindingResponse":
        return dc_td.PutCodeBindingResponse.make_one(res)

    def put_resource_policy(
        self,
        res: "bs_td.PutResourcePolicyResponseTypeDef",
    ) -> "dc_td.PutResourcePolicyResponse":
        return dc_td.PutResourcePolicyResponse.make_one(res)

    def search_schemas(
        self,
        res: "bs_td.SearchSchemasResponseTypeDef",
    ) -> "dc_td.SearchSchemasResponse":
        return dc_td.SearchSchemasResponse.make_one(res)

    def start_discoverer(
        self,
        res: "bs_td.StartDiscovererResponseTypeDef",
    ) -> "dc_td.StartDiscovererResponse":
        return dc_td.StartDiscovererResponse.make_one(res)

    def stop_discoverer(
        self,
        res: "bs_td.StopDiscovererResponseTypeDef",
    ) -> "dc_td.StopDiscovererResponse":
        return dc_td.StopDiscovererResponse.make_one(res)

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

    def update_discoverer(
        self,
        res: "bs_td.UpdateDiscovererResponseTypeDef",
    ) -> "dc_td.UpdateDiscovererResponse":
        return dc_td.UpdateDiscovererResponse.make_one(res)

    def update_registry(
        self,
        res: "bs_td.UpdateRegistryResponseTypeDef",
    ) -> "dc_td.UpdateRegistryResponse":
        return dc_td.UpdateRegistryResponse.make_one(res)

    def update_schema(
        self,
        res: "bs_td.UpdateSchemaResponseTypeDef",
    ) -> "dc_td.UpdateSchemaResponse":
        return dc_td.UpdateSchemaResponse.make_one(res)


schemas_caster = SCHEMASCaster()
