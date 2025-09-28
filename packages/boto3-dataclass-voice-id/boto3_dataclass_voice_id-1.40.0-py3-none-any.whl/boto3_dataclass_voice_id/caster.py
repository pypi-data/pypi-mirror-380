# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_voice_id import type_defs as bs_td


class VOICE_IDCaster:

    def associate_fraudster(
        self,
        res: "bs_td.AssociateFraudsterResponseTypeDef",
    ) -> "dc_td.AssociateFraudsterResponse":
        return dc_td.AssociateFraudsterResponse.make_one(res)

    def create_domain(
        self,
        res: "bs_td.CreateDomainResponseTypeDef",
    ) -> "dc_td.CreateDomainResponse":
        return dc_td.CreateDomainResponse.make_one(res)

    def create_watchlist(
        self,
        res: "bs_td.CreateWatchlistResponseTypeDef",
    ) -> "dc_td.CreateWatchlistResponse":
        return dc_td.CreateWatchlistResponse.make_one(res)

    def delete_domain(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_fraudster(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_speaker(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_watchlist(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_domain(
        self,
        res: "bs_td.DescribeDomainResponseTypeDef",
    ) -> "dc_td.DescribeDomainResponse":
        return dc_td.DescribeDomainResponse.make_one(res)

    def describe_fraudster(
        self,
        res: "bs_td.DescribeFraudsterResponseTypeDef",
    ) -> "dc_td.DescribeFraudsterResponse":
        return dc_td.DescribeFraudsterResponse.make_one(res)

    def describe_fraudster_registration_job(
        self,
        res: "bs_td.DescribeFraudsterRegistrationJobResponseTypeDef",
    ) -> "dc_td.DescribeFraudsterRegistrationJobResponse":
        return dc_td.DescribeFraudsterRegistrationJobResponse.make_one(res)

    def describe_speaker(
        self,
        res: "bs_td.DescribeSpeakerResponseTypeDef",
    ) -> "dc_td.DescribeSpeakerResponse":
        return dc_td.DescribeSpeakerResponse.make_one(res)

    def describe_speaker_enrollment_job(
        self,
        res: "bs_td.DescribeSpeakerEnrollmentJobResponseTypeDef",
    ) -> "dc_td.DescribeSpeakerEnrollmentJobResponse":
        return dc_td.DescribeSpeakerEnrollmentJobResponse.make_one(res)

    def describe_watchlist(
        self,
        res: "bs_td.DescribeWatchlistResponseTypeDef",
    ) -> "dc_td.DescribeWatchlistResponse":
        return dc_td.DescribeWatchlistResponse.make_one(res)

    def disassociate_fraudster(
        self,
        res: "bs_td.DisassociateFraudsterResponseTypeDef",
    ) -> "dc_td.DisassociateFraudsterResponse":
        return dc_td.DisassociateFraudsterResponse.make_one(res)

    def evaluate_session(
        self,
        res: "bs_td.EvaluateSessionResponseTypeDef",
    ) -> "dc_td.EvaluateSessionResponse":
        return dc_td.EvaluateSessionResponse.make_one(res)

    def list_domains(
        self,
        res: "bs_td.ListDomainsResponseTypeDef",
    ) -> "dc_td.ListDomainsResponse":
        return dc_td.ListDomainsResponse.make_one(res)

    def list_fraudster_registration_jobs(
        self,
        res: "bs_td.ListFraudsterRegistrationJobsResponseTypeDef",
    ) -> "dc_td.ListFraudsterRegistrationJobsResponse":
        return dc_td.ListFraudsterRegistrationJobsResponse.make_one(res)

    def list_fraudsters(
        self,
        res: "bs_td.ListFraudstersResponseTypeDef",
    ) -> "dc_td.ListFraudstersResponse":
        return dc_td.ListFraudstersResponse.make_one(res)

    def list_speaker_enrollment_jobs(
        self,
        res: "bs_td.ListSpeakerEnrollmentJobsResponseTypeDef",
    ) -> "dc_td.ListSpeakerEnrollmentJobsResponse":
        return dc_td.ListSpeakerEnrollmentJobsResponse.make_one(res)

    def list_speakers(
        self,
        res: "bs_td.ListSpeakersResponseTypeDef",
    ) -> "dc_td.ListSpeakersResponse":
        return dc_td.ListSpeakersResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_watchlists(
        self,
        res: "bs_td.ListWatchlistsResponseTypeDef",
    ) -> "dc_td.ListWatchlistsResponse":
        return dc_td.ListWatchlistsResponse.make_one(res)

    def opt_out_speaker(
        self,
        res: "bs_td.OptOutSpeakerResponseTypeDef",
    ) -> "dc_td.OptOutSpeakerResponse":
        return dc_td.OptOutSpeakerResponse.make_one(res)

    def start_fraudster_registration_job(
        self,
        res: "bs_td.StartFraudsterRegistrationJobResponseTypeDef",
    ) -> "dc_td.StartFraudsterRegistrationJobResponse":
        return dc_td.StartFraudsterRegistrationJobResponse.make_one(res)

    def start_speaker_enrollment_job(
        self,
        res: "bs_td.StartSpeakerEnrollmentJobResponseTypeDef",
    ) -> "dc_td.StartSpeakerEnrollmentJobResponse":
        return dc_td.StartSpeakerEnrollmentJobResponse.make_one(res)

    def update_domain(
        self,
        res: "bs_td.UpdateDomainResponseTypeDef",
    ) -> "dc_td.UpdateDomainResponse":
        return dc_td.UpdateDomainResponse.make_one(res)

    def update_watchlist(
        self,
        res: "bs_td.UpdateWatchlistResponseTypeDef",
    ) -> "dc_td.UpdateWatchlistResponse":
        return dc_td.UpdateWatchlistResponse.make_one(res)


voice_id_caster = VOICE_IDCaster()
