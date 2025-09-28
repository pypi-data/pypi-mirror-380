# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_workspaces_thin_client import type_defs as bs_td


class WORKSPACES_THIN_CLIENTCaster:

    def create_environment(
        self,
        res: "bs_td.CreateEnvironmentResponseTypeDef",
    ) -> "dc_td.CreateEnvironmentResponse":
        return dc_td.CreateEnvironmentResponse.make_one(res)

    def get_device(
        self,
        res: "bs_td.GetDeviceResponseTypeDef",
    ) -> "dc_td.GetDeviceResponse":
        return dc_td.GetDeviceResponse.make_one(res)

    def get_environment(
        self,
        res: "bs_td.GetEnvironmentResponseTypeDef",
    ) -> "dc_td.GetEnvironmentResponse":
        return dc_td.GetEnvironmentResponse.make_one(res)

    def get_software_set(
        self,
        res: "bs_td.GetSoftwareSetResponseTypeDef",
    ) -> "dc_td.GetSoftwareSetResponse":
        return dc_td.GetSoftwareSetResponse.make_one(res)

    def list_devices(
        self,
        res: "bs_td.ListDevicesResponseTypeDef",
    ) -> "dc_td.ListDevicesResponse":
        return dc_td.ListDevicesResponse.make_one(res)

    def list_environments(
        self,
        res: "bs_td.ListEnvironmentsResponseTypeDef",
    ) -> "dc_td.ListEnvironmentsResponse":
        return dc_td.ListEnvironmentsResponse.make_one(res)

    def list_software_sets(
        self,
        res: "bs_td.ListSoftwareSetsResponseTypeDef",
    ) -> "dc_td.ListSoftwareSetsResponse":
        return dc_td.ListSoftwareSetsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def update_device(
        self,
        res: "bs_td.UpdateDeviceResponseTypeDef",
    ) -> "dc_td.UpdateDeviceResponse":
        return dc_td.UpdateDeviceResponse.make_one(res)

    def update_environment(
        self,
        res: "bs_td.UpdateEnvironmentResponseTypeDef",
    ) -> "dc_td.UpdateEnvironmentResponse":
        return dc_td.UpdateEnvironmentResponse.make_one(res)


workspaces_thin_client_caster = WORKSPACES_THIN_CLIENTCaster()
