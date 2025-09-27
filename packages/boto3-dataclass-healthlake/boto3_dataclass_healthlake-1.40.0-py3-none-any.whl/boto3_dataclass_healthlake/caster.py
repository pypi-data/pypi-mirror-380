# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_healthlake import type_defs as bs_td


class HEALTHLAKECaster:

    def create_fhir_datastore(
        self,
        res: "bs_td.CreateFHIRDatastoreResponseTypeDef",
    ) -> "dc_td.CreateFHIRDatastoreResponse":
        return dc_td.CreateFHIRDatastoreResponse.make_one(res)

    def delete_fhir_datastore(
        self,
        res: "bs_td.DeleteFHIRDatastoreResponseTypeDef",
    ) -> "dc_td.DeleteFHIRDatastoreResponse":
        return dc_td.DeleteFHIRDatastoreResponse.make_one(res)

    def describe_fhir_datastore(
        self,
        res: "bs_td.DescribeFHIRDatastoreResponseTypeDef",
    ) -> "dc_td.DescribeFHIRDatastoreResponse":
        return dc_td.DescribeFHIRDatastoreResponse.make_one(res)

    def describe_fhir_export_job(
        self,
        res: "bs_td.DescribeFHIRExportJobResponseTypeDef",
    ) -> "dc_td.DescribeFHIRExportJobResponse":
        return dc_td.DescribeFHIRExportJobResponse.make_one(res)

    def describe_fhir_import_job(
        self,
        res: "bs_td.DescribeFHIRImportJobResponseTypeDef",
    ) -> "dc_td.DescribeFHIRImportJobResponse":
        return dc_td.DescribeFHIRImportJobResponse.make_one(res)

    def list_fhir_datastores(
        self,
        res: "bs_td.ListFHIRDatastoresResponseTypeDef",
    ) -> "dc_td.ListFHIRDatastoresResponse":
        return dc_td.ListFHIRDatastoresResponse.make_one(res)

    def list_fhir_export_jobs(
        self,
        res: "bs_td.ListFHIRExportJobsResponseTypeDef",
    ) -> "dc_td.ListFHIRExportJobsResponse":
        return dc_td.ListFHIRExportJobsResponse.make_one(res)

    def list_fhir_import_jobs(
        self,
        res: "bs_td.ListFHIRImportJobsResponseTypeDef",
    ) -> "dc_td.ListFHIRImportJobsResponse":
        return dc_td.ListFHIRImportJobsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def start_fhir_export_job(
        self,
        res: "bs_td.StartFHIRExportJobResponseTypeDef",
    ) -> "dc_td.StartFHIRExportJobResponse":
        return dc_td.StartFHIRExportJobResponse.make_one(res)

    def start_fhir_import_job(
        self,
        res: "bs_td.StartFHIRImportJobResponseTypeDef",
    ) -> "dc_td.StartFHIRImportJobResponse":
        return dc_td.StartFHIRImportJobResponse.make_one(res)


healthlake_caster = HEALTHLAKECaster()
