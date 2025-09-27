# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_iotdeviceadvisor import type_defs as bs_td


class IOTDEVICEADVISORCaster:

    def create_suite_definition(
        self,
        res: "bs_td.CreateSuiteDefinitionResponseTypeDef",
    ) -> "dc_td.CreateSuiteDefinitionResponse":
        return dc_td.CreateSuiteDefinitionResponse.make_one(res)

    def get_endpoint(
        self,
        res: "bs_td.GetEndpointResponseTypeDef",
    ) -> "dc_td.GetEndpointResponse":
        return dc_td.GetEndpointResponse.make_one(res)

    def get_suite_definition(
        self,
        res: "bs_td.GetSuiteDefinitionResponseTypeDef",
    ) -> "dc_td.GetSuiteDefinitionResponse":
        return dc_td.GetSuiteDefinitionResponse.make_one(res)

    def get_suite_run(
        self,
        res: "bs_td.GetSuiteRunResponseTypeDef",
    ) -> "dc_td.GetSuiteRunResponse":
        return dc_td.GetSuiteRunResponse.make_one(res)

    def get_suite_run_report(
        self,
        res: "bs_td.GetSuiteRunReportResponseTypeDef",
    ) -> "dc_td.GetSuiteRunReportResponse":
        return dc_td.GetSuiteRunReportResponse.make_one(res)

    def list_suite_definitions(
        self,
        res: "bs_td.ListSuiteDefinitionsResponseTypeDef",
    ) -> "dc_td.ListSuiteDefinitionsResponse":
        return dc_td.ListSuiteDefinitionsResponse.make_one(res)

    def list_suite_runs(
        self,
        res: "bs_td.ListSuiteRunsResponseTypeDef",
    ) -> "dc_td.ListSuiteRunsResponse":
        return dc_td.ListSuiteRunsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def start_suite_run(
        self,
        res: "bs_td.StartSuiteRunResponseTypeDef",
    ) -> "dc_td.StartSuiteRunResponse":
        return dc_td.StartSuiteRunResponse.make_one(res)

    def update_suite_definition(
        self,
        res: "bs_td.UpdateSuiteDefinitionResponseTypeDef",
    ) -> "dc_td.UpdateSuiteDefinitionResponse":
        return dc_td.UpdateSuiteDefinitionResponse.make_one(res)


iotdeviceadvisor_caster = IOTDEVICEADVISORCaster()
