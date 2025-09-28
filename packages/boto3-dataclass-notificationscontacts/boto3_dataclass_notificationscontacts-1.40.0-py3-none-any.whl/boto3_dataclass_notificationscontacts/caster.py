# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_notificationscontacts import type_defs as bs_td


class NOTIFICATIONSCONTACTSCaster:

    def create_email_contact(
        self,
        res: "bs_td.CreateEmailContactResponseTypeDef",
    ) -> "dc_td.CreateEmailContactResponse":
        return dc_td.CreateEmailContactResponse.make_one(res)

    def get_email_contact(
        self,
        res: "bs_td.GetEmailContactResponseTypeDef",
    ) -> "dc_td.GetEmailContactResponse":
        return dc_td.GetEmailContactResponse.make_one(res)

    def list_email_contacts(
        self,
        res: "bs_td.ListEmailContactsResponseTypeDef",
    ) -> "dc_td.ListEmailContactsResponse":
        return dc_td.ListEmailContactsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)


notificationscontacts_caster = NOTIFICATIONSCONTACTSCaster()
