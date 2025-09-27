# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_iotsecuretunneling import type_defs as bs_td


class IOTSECURETUNNELINGCaster:

    def describe_tunnel(
        self,
        res: "bs_td.DescribeTunnelResponseTypeDef",
    ) -> "dc_td.DescribeTunnelResponse":
        return dc_td.DescribeTunnelResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_tunnels(
        self,
        res: "bs_td.ListTunnelsResponseTypeDef",
    ) -> "dc_td.ListTunnelsResponse":
        return dc_td.ListTunnelsResponse.make_one(res)

    def open_tunnel(
        self,
        res: "bs_td.OpenTunnelResponseTypeDef",
    ) -> "dc_td.OpenTunnelResponse":
        return dc_td.OpenTunnelResponse.make_one(res)

    def rotate_tunnel_access_token(
        self,
        res: "bs_td.RotateTunnelAccessTokenResponseTypeDef",
    ) -> "dc_td.RotateTunnelAccessTokenResponse":
        return dc_td.RotateTunnelAccessTokenResponse.make_one(res)


iotsecuretunneling_caster = IOTSECURETUNNELINGCaster()
