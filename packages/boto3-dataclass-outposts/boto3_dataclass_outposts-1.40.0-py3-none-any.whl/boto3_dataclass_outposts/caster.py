# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_outposts import type_defs as bs_td


class OUTPOSTSCaster:

    def create_order(
        self,
        res: "bs_td.CreateOrderOutputTypeDef",
    ) -> "dc_td.CreateOrderOutput":
        return dc_td.CreateOrderOutput.make_one(res)

    def create_outpost(
        self,
        res: "bs_td.CreateOutpostOutputTypeDef",
    ) -> "dc_td.CreateOutpostOutput":
        return dc_td.CreateOutpostOutput.make_one(res)

    def create_site(
        self,
        res: "bs_td.CreateSiteOutputTypeDef",
    ) -> "dc_td.CreateSiteOutput":
        return dc_td.CreateSiteOutput.make_one(res)

    def get_capacity_task(
        self,
        res: "bs_td.GetCapacityTaskOutputTypeDef",
    ) -> "dc_td.GetCapacityTaskOutput":
        return dc_td.GetCapacityTaskOutput.make_one(res)

    def get_catalog_item(
        self,
        res: "bs_td.GetCatalogItemOutputTypeDef",
    ) -> "dc_td.GetCatalogItemOutput":
        return dc_td.GetCatalogItemOutput.make_one(res)

    def get_connection(
        self,
        res: "bs_td.GetConnectionResponseTypeDef",
    ) -> "dc_td.GetConnectionResponse":
        return dc_td.GetConnectionResponse.make_one(res)

    def get_order(
        self,
        res: "bs_td.GetOrderOutputTypeDef",
    ) -> "dc_td.GetOrderOutput":
        return dc_td.GetOrderOutput.make_one(res)

    def get_outpost(
        self,
        res: "bs_td.GetOutpostOutputTypeDef",
    ) -> "dc_td.GetOutpostOutput":
        return dc_td.GetOutpostOutput.make_one(res)

    def get_outpost_billing_information(
        self,
        res: "bs_td.GetOutpostBillingInformationOutputTypeDef",
    ) -> "dc_td.GetOutpostBillingInformationOutput":
        return dc_td.GetOutpostBillingInformationOutput.make_one(res)

    def get_outpost_instance_types(
        self,
        res: "bs_td.GetOutpostInstanceTypesOutputTypeDef",
    ) -> "dc_td.GetOutpostInstanceTypesOutput":
        return dc_td.GetOutpostInstanceTypesOutput.make_one(res)

    def get_outpost_supported_instance_types(
        self,
        res: "bs_td.GetOutpostSupportedInstanceTypesOutputTypeDef",
    ) -> "dc_td.GetOutpostSupportedInstanceTypesOutput":
        return dc_td.GetOutpostSupportedInstanceTypesOutput.make_one(res)

    def get_site(
        self,
        res: "bs_td.GetSiteOutputTypeDef",
    ) -> "dc_td.GetSiteOutput":
        return dc_td.GetSiteOutput.make_one(res)

    def get_site_address(
        self,
        res: "bs_td.GetSiteAddressOutputTypeDef",
    ) -> "dc_td.GetSiteAddressOutput":
        return dc_td.GetSiteAddressOutput.make_one(res)

    def list_asset_instances(
        self,
        res: "bs_td.ListAssetInstancesOutputTypeDef",
    ) -> "dc_td.ListAssetInstancesOutput":
        return dc_td.ListAssetInstancesOutput.make_one(res)

    def list_assets(
        self,
        res: "bs_td.ListAssetsOutputTypeDef",
    ) -> "dc_td.ListAssetsOutput":
        return dc_td.ListAssetsOutput.make_one(res)

    def list_blocking_instances_for_capacity_task(
        self,
        res: "bs_td.ListBlockingInstancesForCapacityTaskOutputTypeDef",
    ) -> "dc_td.ListBlockingInstancesForCapacityTaskOutput":
        return dc_td.ListBlockingInstancesForCapacityTaskOutput.make_one(res)

    def list_capacity_tasks(
        self,
        res: "bs_td.ListCapacityTasksOutputTypeDef",
    ) -> "dc_td.ListCapacityTasksOutput":
        return dc_td.ListCapacityTasksOutput.make_one(res)

    def list_catalog_items(
        self,
        res: "bs_td.ListCatalogItemsOutputTypeDef",
    ) -> "dc_td.ListCatalogItemsOutput":
        return dc_td.ListCatalogItemsOutput.make_one(res)

    def list_orders(
        self,
        res: "bs_td.ListOrdersOutputTypeDef",
    ) -> "dc_td.ListOrdersOutput":
        return dc_td.ListOrdersOutput.make_one(res)

    def list_outposts(
        self,
        res: "bs_td.ListOutpostsOutputTypeDef",
    ) -> "dc_td.ListOutpostsOutput":
        return dc_td.ListOutpostsOutput.make_one(res)

    def list_sites(
        self,
        res: "bs_td.ListSitesOutputTypeDef",
    ) -> "dc_td.ListSitesOutput":
        return dc_td.ListSitesOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def start_capacity_task(
        self,
        res: "bs_td.StartCapacityTaskOutputTypeDef",
    ) -> "dc_td.StartCapacityTaskOutput":
        return dc_td.StartCapacityTaskOutput.make_one(res)

    def start_connection(
        self,
        res: "bs_td.StartConnectionResponseTypeDef",
    ) -> "dc_td.StartConnectionResponse":
        return dc_td.StartConnectionResponse.make_one(res)

    def update_outpost(
        self,
        res: "bs_td.UpdateOutpostOutputTypeDef",
    ) -> "dc_td.UpdateOutpostOutput":
        return dc_td.UpdateOutpostOutput.make_one(res)

    def update_site(
        self,
        res: "bs_td.UpdateSiteOutputTypeDef",
    ) -> "dc_td.UpdateSiteOutput":
        return dc_td.UpdateSiteOutput.make_one(res)

    def update_site_address(
        self,
        res: "bs_td.UpdateSiteAddressOutputTypeDef",
    ) -> "dc_td.UpdateSiteAddressOutput":
        return dc_td.UpdateSiteAddressOutput.make_one(res)

    def update_site_rack_physical_properties(
        self,
        res: "bs_td.UpdateSiteRackPhysicalPropertiesOutputTypeDef",
    ) -> "dc_td.UpdateSiteRackPhysicalPropertiesOutput":
        return dc_td.UpdateSiteRackPhysicalPropertiesOutput.make_one(res)


outposts_caster = OUTPOSTSCaster()
