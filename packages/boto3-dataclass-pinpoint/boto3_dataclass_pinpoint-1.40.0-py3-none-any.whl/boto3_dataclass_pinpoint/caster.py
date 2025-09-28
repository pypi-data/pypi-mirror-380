# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_pinpoint import type_defs as bs_td


class PINPOINTCaster:

    def create_app(
        self,
        res: "bs_td.CreateAppResponseTypeDef",
    ) -> "dc_td.CreateAppResponse":
        return dc_td.CreateAppResponse.make_one(res)

    def create_campaign(
        self,
        res: "bs_td.CreateCampaignResponseTypeDef",
    ) -> "dc_td.CreateCampaignResponse":
        return dc_td.CreateCampaignResponse.make_one(res)

    def create_email_template(
        self,
        res: "bs_td.CreateEmailTemplateResponseTypeDef",
    ) -> "dc_td.CreateEmailTemplateResponse":
        return dc_td.CreateEmailTemplateResponse.make_one(res)

    def create_export_job(
        self,
        res: "bs_td.CreateExportJobResponseTypeDef",
    ) -> "dc_td.CreateExportJobResponse":
        return dc_td.CreateExportJobResponse.make_one(res)

    def create_import_job(
        self,
        res: "bs_td.CreateImportJobResponseTypeDef",
    ) -> "dc_td.CreateImportJobResponse":
        return dc_td.CreateImportJobResponse.make_one(res)

    def create_in_app_template(
        self,
        res: "bs_td.CreateInAppTemplateResponseTypeDef",
    ) -> "dc_td.CreateInAppTemplateResponse":
        return dc_td.CreateInAppTemplateResponse.make_one(res)

    def create_journey(
        self,
        res: "bs_td.CreateJourneyResponseTypeDef",
    ) -> "dc_td.CreateJourneyResponse":
        return dc_td.CreateJourneyResponse.make_one(res)

    def create_push_template(
        self,
        res: "bs_td.CreatePushTemplateResponseTypeDef",
    ) -> "dc_td.CreatePushTemplateResponse":
        return dc_td.CreatePushTemplateResponse.make_one(res)

    def create_recommender_configuration(
        self,
        res: "bs_td.CreateRecommenderConfigurationResponseTypeDef",
    ) -> "dc_td.CreateRecommenderConfigurationResponse":
        return dc_td.CreateRecommenderConfigurationResponse.make_one(res)

    def create_segment(
        self,
        res: "bs_td.CreateSegmentResponseTypeDef",
    ) -> "dc_td.CreateSegmentResponse":
        return dc_td.CreateSegmentResponse.make_one(res)

    def create_sms_template(
        self,
        res: "bs_td.CreateSmsTemplateResponseTypeDef",
    ) -> "dc_td.CreateSmsTemplateResponse":
        return dc_td.CreateSmsTemplateResponse.make_one(res)

    def create_voice_template(
        self,
        res: "bs_td.CreateVoiceTemplateResponseTypeDef",
    ) -> "dc_td.CreateVoiceTemplateResponse":
        return dc_td.CreateVoiceTemplateResponse.make_one(res)

    def delete_adm_channel(
        self,
        res: "bs_td.DeleteAdmChannelResponseTypeDef",
    ) -> "dc_td.DeleteAdmChannelResponse":
        return dc_td.DeleteAdmChannelResponse.make_one(res)

    def delete_apns_channel(
        self,
        res: "bs_td.DeleteApnsChannelResponseTypeDef",
    ) -> "dc_td.DeleteApnsChannelResponse":
        return dc_td.DeleteApnsChannelResponse.make_one(res)

    def delete_apns_sandbox_channel(
        self,
        res: "bs_td.DeleteApnsSandboxChannelResponseTypeDef",
    ) -> "dc_td.DeleteApnsSandboxChannelResponse":
        return dc_td.DeleteApnsSandboxChannelResponse.make_one(res)

    def delete_apns_voip_channel(
        self,
        res: "bs_td.DeleteApnsVoipChannelResponseTypeDef",
    ) -> "dc_td.DeleteApnsVoipChannelResponse":
        return dc_td.DeleteApnsVoipChannelResponse.make_one(res)

    def delete_apns_voip_sandbox_channel(
        self,
        res: "bs_td.DeleteApnsVoipSandboxChannelResponseTypeDef",
    ) -> "dc_td.DeleteApnsVoipSandboxChannelResponse":
        return dc_td.DeleteApnsVoipSandboxChannelResponse.make_one(res)

    def delete_app(
        self,
        res: "bs_td.DeleteAppResponseTypeDef",
    ) -> "dc_td.DeleteAppResponse":
        return dc_td.DeleteAppResponse.make_one(res)

    def delete_baidu_channel(
        self,
        res: "bs_td.DeleteBaiduChannelResponseTypeDef",
    ) -> "dc_td.DeleteBaiduChannelResponse":
        return dc_td.DeleteBaiduChannelResponse.make_one(res)

    def delete_campaign(
        self,
        res: "bs_td.DeleteCampaignResponseTypeDef",
    ) -> "dc_td.DeleteCampaignResponse":
        return dc_td.DeleteCampaignResponse.make_one(res)

    def delete_email_channel(
        self,
        res: "bs_td.DeleteEmailChannelResponseTypeDef",
    ) -> "dc_td.DeleteEmailChannelResponse":
        return dc_td.DeleteEmailChannelResponse.make_one(res)

    def delete_email_template(
        self,
        res: "bs_td.DeleteEmailTemplateResponseTypeDef",
    ) -> "dc_td.DeleteEmailTemplateResponse":
        return dc_td.DeleteEmailTemplateResponse.make_one(res)

    def delete_endpoint(
        self,
        res: "bs_td.DeleteEndpointResponseTypeDef",
    ) -> "dc_td.DeleteEndpointResponse":
        return dc_td.DeleteEndpointResponse.make_one(res)

    def delete_event_stream(
        self,
        res: "bs_td.DeleteEventStreamResponseTypeDef",
    ) -> "dc_td.DeleteEventStreamResponse":
        return dc_td.DeleteEventStreamResponse.make_one(res)

    def delete_gcm_channel(
        self,
        res: "bs_td.DeleteGcmChannelResponseTypeDef",
    ) -> "dc_td.DeleteGcmChannelResponse":
        return dc_td.DeleteGcmChannelResponse.make_one(res)

    def delete_in_app_template(
        self,
        res: "bs_td.DeleteInAppTemplateResponseTypeDef",
    ) -> "dc_td.DeleteInAppTemplateResponse":
        return dc_td.DeleteInAppTemplateResponse.make_one(res)

    def delete_journey(
        self,
        res: "bs_td.DeleteJourneyResponseTypeDef",
    ) -> "dc_td.DeleteJourneyResponse":
        return dc_td.DeleteJourneyResponse.make_one(res)

    def delete_push_template(
        self,
        res: "bs_td.DeletePushTemplateResponseTypeDef",
    ) -> "dc_td.DeletePushTemplateResponse":
        return dc_td.DeletePushTemplateResponse.make_one(res)

    def delete_recommender_configuration(
        self,
        res: "bs_td.DeleteRecommenderConfigurationResponseTypeDef",
    ) -> "dc_td.DeleteRecommenderConfigurationResponse":
        return dc_td.DeleteRecommenderConfigurationResponse.make_one(res)

    def delete_segment(
        self,
        res: "bs_td.DeleteSegmentResponseTypeDef",
    ) -> "dc_td.DeleteSegmentResponse":
        return dc_td.DeleteSegmentResponse.make_one(res)

    def delete_sms_channel(
        self,
        res: "bs_td.DeleteSmsChannelResponseTypeDef",
    ) -> "dc_td.DeleteSmsChannelResponse":
        return dc_td.DeleteSmsChannelResponse.make_one(res)

    def delete_sms_template(
        self,
        res: "bs_td.DeleteSmsTemplateResponseTypeDef",
    ) -> "dc_td.DeleteSmsTemplateResponse":
        return dc_td.DeleteSmsTemplateResponse.make_one(res)

    def delete_user_endpoints(
        self,
        res: "bs_td.DeleteUserEndpointsResponseTypeDef",
    ) -> "dc_td.DeleteUserEndpointsResponse":
        return dc_td.DeleteUserEndpointsResponse.make_one(res)

    def delete_voice_channel(
        self,
        res: "bs_td.DeleteVoiceChannelResponseTypeDef",
    ) -> "dc_td.DeleteVoiceChannelResponse":
        return dc_td.DeleteVoiceChannelResponse.make_one(res)

    def delete_voice_template(
        self,
        res: "bs_td.DeleteVoiceTemplateResponseTypeDef",
    ) -> "dc_td.DeleteVoiceTemplateResponse":
        return dc_td.DeleteVoiceTemplateResponse.make_one(res)

    def get_adm_channel(
        self,
        res: "bs_td.GetAdmChannelResponseTypeDef",
    ) -> "dc_td.GetAdmChannelResponse":
        return dc_td.GetAdmChannelResponse.make_one(res)

    def get_apns_channel(
        self,
        res: "bs_td.GetApnsChannelResponseTypeDef",
    ) -> "dc_td.GetApnsChannelResponse":
        return dc_td.GetApnsChannelResponse.make_one(res)

    def get_apns_sandbox_channel(
        self,
        res: "bs_td.GetApnsSandboxChannelResponseTypeDef",
    ) -> "dc_td.GetApnsSandboxChannelResponse":
        return dc_td.GetApnsSandboxChannelResponse.make_one(res)

    def get_apns_voip_channel(
        self,
        res: "bs_td.GetApnsVoipChannelResponseTypeDef",
    ) -> "dc_td.GetApnsVoipChannelResponse":
        return dc_td.GetApnsVoipChannelResponse.make_one(res)

    def get_apns_voip_sandbox_channel(
        self,
        res: "bs_td.GetApnsVoipSandboxChannelResponseTypeDef",
    ) -> "dc_td.GetApnsVoipSandboxChannelResponse":
        return dc_td.GetApnsVoipSandboxChannelResponse.make_one(res)

    def get_app(
        self,
        res: "bs_td.GetAppResponseTypeDef",
    ) -> "dc_td.GetAppResponse":
        return dc_td.GetAppResponse.make_one(res)

    def get_application_date_range_kpi(
        self,
        res: "bs_td.GetApplicationDateRangeKpiResponseTypeDef",
    ) -> "dc_td.GetApplicationDateRangeKpiResponse":
        return dc_td.GetApplicationDateRangeKpiResponse.make_one(res)

    def get_application_settings(
        self,
        res: "bs_td.GetApplicationSettingsResponseTypeDef",
    ) -> "dc_td.GetApplicationSettingsResponse":
        return dc_td.GetApplicationSettingsResponse.make_one(res)

    def get_apps(
        self,
        res: "bs_td.GetAppsResponseTypeDef",
    ) -> "dc_td.GetAppsResponse":
        return dc_td.GetAppsResponse.make_one(res)

    def get_baidu_channel(
        self,
        res: "bs_td.GetBaiduChannelResponseTypeDef",
    ) -> "dc_td.GetBaiduChannelResponse":
        return dc_td.GetBaiduChannelResponse.make_one(res)

    def get_campaign(
        self,
        res: "bs_td.GetCampaignResponseTypeDef",
    ) -> "dc_td.GetCampaignResponse":
        return dc_td.GetCampaignResponse.make_one(res)

    def get_campaign_activities(
        self,
        res: "bs_td.GetCampaignActivitiesResponseTypeDef",
    ) -> "dc_td.GetCampaignActivitiesResponse":
        return dc_td.GetCampaignActivitiesResponse.make_one(res)

    def get_campaign_date_range_kpi(
        self,
        res: "bs_td.GetCampaignDateRangeKpiResponseTypeDef",
    ) -> "dc_td.GetCampaignDateRangeKpiResponse":
        return dc_td.GetCampaignDateRangeKpiResponse.make_one(res)

    def get_campaign_version(
        self,
        res: "bs_td.GetCampaignVersionResponseTypeDef",
    ) -> "dc_td.GetCampaignVersionResponse":
        return dc_td.GetCampaignVersionResponse.make_one(res)

    def get_campaign_versions(
        self,
        res: "bs_td.GetCampaignVersionsResponseTypeDef",
    ) -> "dc_td.GetCampaignVersionsResponse":
        return dc_td.GetCampaignVersionsResponse.make_one(res)

    def get_campaigns(
        self,
        res: "bs_td.GetCampaignsResponseTypeDef",
    ) -> "dc_td.GetCampaignsResponse":
        return dc_td.GetCampaignsResponse.make_one(res)

    def get_channels(
        self,
        res: "bs_td.GetChannelsResponseTypeDef",
    ) -> "dc_td.GetChannelsResponse":
        return dc_td.GetChannelsResponse.make_one(res)

    def get_email_channel(
        self,
        res: "bs_td.GetEmailChannelResponseTypeDef",
    ) -> "dc_td.GetEmailChannelResponse":
        return dc_td.GetEmailChannelResponse.make_one(res)

    def get_email_template(
        self,
        res: "bs_td.GetEmailTemplateResponseTypeDef",
    ) -> "dc_td.GetEmailTemplateResponse":
        return dc_td.GetEmailTemplateResponse.make_one(res)

    def get_endpoint(
        self,
        res: "bs_td.GetEndpointResponseTypeDef",
    ) -> "dc_td.GetEndpointResponse":
        return dc_td.GetEndpointResponse.make_one(res)

    def get_event_stream(
        self,
        res: "bs_td.GetEventStreamResponseTypeDef",
    ) -> "dc_td.GetEventStreamResponse":
        return dc_td.GetEventStreamResponse.make_one(res)

    def get_export_job(
        self,
        res: "bs_td.GetExportJobResponseTypeDef",
    ) -> "dc_td.GetExportJobResponse":
        return dc_td.GetExportJobResponse.make_one(res)

    def get_export_jobs(
        self,
        res: "bs_td.GetExportJobsResponseTypeDef",
    ) -> "dc_td.GetExportJobsResponse":
        return dc_td.GetExportJobsResponse.make_one(res)

    def get_gcm_channel(
        self,
        res: "bs_td.GetGcmChannelResponseTypeDef",
    ) -> "dc_td.GetGcmChannelResponse":
        return dc_td.GetGcmChannelResponse.make_one(res)

    def get_import_job(
        self,
        res: "bs_td.GetImportJobResponseTypeDef",
    ) -> "dc_td.GetImportJobResponse":
        return dc_td.GetImportJobResponse.make_one(res)

    def get_import_jobs(
        self,
        res: "bs_td.GetImportJobsResponseTypeDef",
    ) -> "dc_td.GetImportJobsResponse":
        return dc_td.GetImportJobsResponse.make_one(res)

    def get_in_app_messages(
        self,
        res: "bs_td.GetInAppMessagesResponseTypeDef",
    ) -> "dc_td.GetInAppMessagesResponse":
        return dc_td.GetInAppMessagesResponse.make_one(res)

    def get_in_app_template(
        self,
        res: "bs_td.GetInAppTemplateResponseTypeDef",
    ) -> "dc_td.GetInAppTemplateResponse":
        return dc_td.GetInAppTemplateResponse.make_one(res)

    def get_journey(
        self,
        res: "bs_td.GetJourneyResponseTypeDef",
    ) -> "dc_td.GetJourneyResponse":
        return dc_td.GetJourneyResponse.make_one(res)

    def get_journey_date_range_kpi(
        self,
        res: "bs_td.GetJourneyDateRangeKpiResponseTypeDef",
    ) -> "dc_td.GetJourneyDateRangeKpiResponse":
        return dc_td.GetJourneyDateRangeKpiResponse.make_one(res)

    def get_journey_execution_activity_metrics(
        self,
        res: "bs_td.GetJourneyExecutionActivityMetricsResponseTypeDef",
    ) -> "dc_td.GetJourneyExecutionActivityMetricsResponse":
        return dc_td.GetJourneyExecutionActivityMetricsResponse.make_one(res)

    def get_journey_execution_metrics(
        self,
        res: "bs_td.GetJourneyExecutionMetricsResponseTypeDef",
    ) -> "dc_td.GetJourneyExecutionMetricsResponse":
        return dc_td.GetJourneyExecutionMetricsResponse.make_one(res)

    def get_journey_run_execution_activity_metrics(
        self,
        res: "bs_td.GetJourneyRunExecutionActivityMetricsResponseTypeDef",
    ) -> "dc_td.GetJourneyRunExecutionActivityMetricsResponse":
        return dc_td.GetJourneyRunExecutionActivityMetricsResponse.make_one(res)

    def get_journey_run_execution_metrics(
        self,
        res: "bs_td.GetJourneyRunExecutionMetricsResponseTypeDef",
    ) -> "dc_td.GetJourneyRunExecutionMetricsResponse":
        return dc_td.GetJourneyRunExecutionMetricsResponse.make_one(res)

    def get_journey_runs(
        self,
        res: "bs_td.GetJourneyRunsResponseTypeDef",
    ) -> "dc_td.GetJourneyRunsResponse":
        return dc_td.GetJourneyRunsResponse.make_one(res)

    def get_push_template(
        self,
        res: "bs_td.GetPushTemplateResponseTypeDef",
    ) -> "dc_td.GetPushTemplateResponse":
        return dc_td.GetPushTemplateResponse.make_one(res)

    def get_recommender_configuration(
        self,
        res: "bs_td.GetRecommenderConfigurationResponseTypeDef",
    ) -> "dc_td.GetRecommenderConfigurationResponse":
        return dc_td.GetRecommenderConfigurationResponse.make_one(res)

    def get_recommender_configurations(
        self,
        res: "bs_td.GetRecommenderConfigurationsResponseTypeDef",
    ) -> "dc_td.GetRecommenderConfigurationsResponse":
        return dc_td.GetRecommenderConfigurationsResponse.make_one(res)

    def get_segment(
        self,
        res: "bs_td.GetSegmentResponseTypeDef",
    ) -> "dc_td.GetSegmentResponse":
        return dc_td.GetSegmentResponse.make_one(res)

    def get_segment_export_jobs(
        self,
        res: "bs_td.GetSegmentExportJobsResponseTypeDef",
    ) -> "dc_td.GetSegmentExportJobsResponse":
        return dc_td.GetSegmentExportJobsResponse.make_one(res)

    def get_segment_import_jobs(
        self,
        res: "bs_td.GetSegmentImportJobsResponseTypeDef",
    ) -> "dc_td.GetSegmentImportJobsResponse":
        return dc_td.GetSegmentImportJobsResponse.make_one(res)

    def get_segment_version(
        self,
        res: "bs_td.GetSegmentVersionResponseTypeDef",
    ) -> "dc_td.GetSegmentVersionResponse":
        return dc_td.GetSegmentVersionResponse.make_one(res)

    def get_segment_versions(
        self,
        res: "bs_td.GetSegmentVersionsResponseTypeDef",
    ) -> "dc_td.GetSegmentVersionsResponse":
        return dc_td.GetSegmentVersionsResponse.make_one(res)

    def get_segments(
        self,
        res: "bs_td.GetSegmentsResponseTypeDef",
    ) -> "dc_td.GetSegmentsResponse":
        return dc_td.GetSegmentsResponse.make_one(res)

    def get_sms_channel(
        self,
        res: "bs_td.GetSmsChannelResponseTypeDef",
    ) -> "dc_td.GetSmsChannelResponse":
        return dc_td.GetSmsChannelResponse.make_one(res)

    def get_sms_template(
        self,
        res: "bs_td.GetSmsTemplateResponseTypeDef",
    ) -> "dc_td.GetSmsTemplateResponse":
        return dc_td.GetSmsTemplateResponse.make_one(res)

    def get_user_endpoints(
        self,
        res: "bs_td.GetUserEndpointsResponseTypeDef",
    ) -> "dc_td.GetUserEndpointsResponse":
        return dc_td.GetUserEndpointsResponse.make_one(res)

    def get_voice_channel(
        self,
        res: "bs_td.GetVoiceChannelResponseTypeDef",
    ) -> "dc_td.GetVoiceChannelResponse":
        return dc_td.GetVoiceChannelResponse.make_one(res)

    def get_voice_template(
        self,
        res: "bs_td.GetVoiceTemplateResponseTypeDef",
    ) -> "dc_td.GetVoiceTemplateResponse":
        return dc_td.GetVoiceTemplateResponse.make_one(res)

    def list_journeys(
        self,
        res: "bs_td.ListJourneysResponseTypeDef",
    ) -> "dc_td.ListJourneysResponse":
        return dc_td.ListJourneysResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_template_versions(
        self,
        res: "bs_td.ListTemplateVersionsResponseTypeDef",
    ) -> "dc_td.ListTemplateVersionsResponse":
        return dc_td.ListTemplateVersionsResponse.make_one(res)

    def list_templates(
        self,
        res: "bs_td.ListTemplatesResponseTypeDef",
    ) -> "dc_td.ListTemplatesResponse":
        return dc_td.ListTemplatesResponse.make_one(res)

    def phone_number_validate(
        self,
        res: "bs_td.PhoneNumberValidateResponseTypeDef",
    ) -> "dc_td.PhoneNumberValidateResponse":
        return dc_td.PhoneNumberValidateResponse.make_one(res)

    def put_event_stream(
        self,
        res: "bs_td.PutEventStreamResponseTypeDef",
    ) -> "dc_td.PutEventStreamResponse":
        return dc_td.PutEventStreamResponse.make_one(res)

    def put_events(
        self,
        res: "bs_td.PutEventsResponseTypeDef",
    ) -> "dc_td.PutEventsResponse":
        return dc_td.PutEventsResponse.make_one(res)

    def remove_attributes(
        self,
        res: "bs_td.RemoveAttributesResponseTypeDef",
    ) -> "dc_td.RemoveAttributesResponse":
        return dc_td.RemoveAttributesResponse.make_one(res)

    def send_messages(
        self,
        res: "bs_td.SendMessagesResponseTypeDef",
    ) -> "dc_td.SendMessagesResponse":
        return dc_td.SendMessagesResponse.make_one(res)

    def send_otp_message(
        self,
        res: "bs_td.SendOTPMessageResponseTypeDef",
    ) -> "dc_td.SendOTPMessageResponse":
        return dc_td.SendOTPMessageResponse.make_one(res)

    def send_users_messages(
        self,
        res: "bs_td.SendUsersMessagesResponseTypeDef",
    ) -> "dc_td.SendUsersMessagesResponse":
        return dc_td.SendUsersMessagesResponse.make_one(res)

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

    def update_adm_channel(
        self,
        res: "bs_td.UpdateAdmChannelResponseTypeDef",
    ) -> "dc_td.UpdateAdmChannelResponse":
        return dc_td.UpdateAdmChannelResponse.make_one(res)

    def update_apns_channel(
        self,
        res: "bs_td.UpdateApnsChannelResponseTypeDef",
    ) -> "dc_td.UpdateApnsChannelResponse":
        return dc_td.UpdateApnsChannelResponse.make_one(res)

    def update_apns_sandbox_channel(
        self,
        res: "bs_td.UpdateApnsSandboxChannelResponseTypeDef",
    ) -> "dc_td.UpdateApnsSandboxChannelResponse":
        return dc_td.UpdateApnsSandboxChannelResponse.make_one(res)

    def update_apns_voip_channel(
        self,
        res: "bs_td.UpdateApnsVoipChannelResponseTypeDef",
    ) -> "dc_td.UpdateApnsVoipChannelResponse":
        return dc_td.UpdateApnsVoipChannelResponse.make_one(res)

    def update_apns_voip_sandbox_channel(
        self,
        res: "bs_td.UpdateApnsVoipSandboxChannelResponseTypeDef",
    ) -> "dc_td.UpdateApnsVoipSandboxChannelResponse":
        return dc_td.UpdateApnsVoipSandboxChannelResponse.make_one(res)

    def update_application_settings(
        self,
        res: "bs_td.UpdateApplicationSettingsResponseTypeDef",
    ) -> "dc_td.UpdateApplicationSettingsResponse":
        return dc_td.UpdateApplicationSettingsResponse.make_one(res)

    def update_baidu_channel(
        self,
        res: "bs_td.UpdateBaiduChannelResponseTypeDef",
    ) -> "dc_td.UpdateBaiduChannelResponse":
        return dc_td.UpdateBaiduChannelResponse.make_one(res)

    def update_campaign(
        self,
        res: "bs_td.UpdateCampaignResponseTypeDef",
    ) -> "dc_td.UpdateCampaignResponse":
        return dc_td.UpdateCampaignResponse.make_one(res)

    def update_email_channel(
        self,
        res: "bs_td.UpdateEmailChannelResponseTypeDef",
    ) -> "dc_td.UpdateEmailChannelResponse":
        return dc_td.UpdateEmailChannelResponse.make_one(res)

    def update_email_template(
        self,
        res: "bs_td.UpdateEmailTemplateResponseTypeDef",
    ) -> "dc_td.UpdateEmailTemplateResponse":
        return dc_td.UpdateEmailTemplateResponse.make_one(res)

    def update_endpoint(
        self,
        res: "bs_td.UpdateEndpointResponseTypeDef",
    ) -> "dc_td.UpdateEndpointResponse":
        return dc_td.UpdateEndpointResponse.make_one(res)

    def update_endpoints_batch(
        self,
        res: "bs_td.UpdateEndpointsBatchResponseTypeDef",
    ) -> "dc_td.UpdateEndpointsBatchResponse":
        return dc_td.UpdateEndpointsBatchResponse.make_one(res)

    def update_gcm_channel(
        self,
        res: "bs_td.UpdateGcmChannelResponseTypeDef",
    ) -> "dc_td.UpdateGcmChannelResponse":
        return dc_td.UpdateGcmChannelResponse.make_one(res)

    def update_in_app_template(
        self,
        res: "bs_td.UpdateInAppTemplateResponseTypeDef",
    ) -> "dc_td.UpdateInAppTemplateResponse":
        return dc_td.UpdateInAppTemplateResponse.make_one(res)

    def update_journey(
        self,
        res: "bs_td.UpdateJourneyResponseTypeDef",
    ) -> "dc_td.UpdateJourneyResponse":
        return dc_td.UpdateJourneyResponse.make_one(res)

    def update_journey_state(
        self,
        res: "bs_td.UpdateJourneyStateResponseTypeDef",
    ) -> "dc_td.UpdateJourneyStateResponse":
        return dc_td.UpdateJourneyStateResponse.make_one(res)

    def update_push_template(
        self,
        res: "bs_td.UpdatePushTemplateResponseTypeDef",
    ) -> "dc_td.UpdatePushTemplateResponse":
        return dc_td.UpdatePushTemplateResponse.make_one(res)

    def update_recommender_configuration(
        self,
        res: "bs_td.UpdateRecommenderConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateRecommenderConfigurationResponse":
        return dc_td.UpdateRecommenderConfigurationResponse.make_one(res)

    def update_segment(
        self,
        res: "bs_td.UpdateSegmentResponseTypeDef",
    ) -> "dc_td.UpdateSegmentResponse":
        return dc_td.UpdateSegmentResponse.make_one(res)

    def update_sms_channel(
        self,
        res: "bs_td.UpdateSmsChannelResponseTypeDef",
    ) -> "dc_td.UpdateSmsChannelResponse":
        return dc_td.UpdateSmsChannelResponse.make_one(res)

    def update_sms_template(
        self,
        res: "bs_td.UpdateSmsTemplateResponseTypeDef",
    ) -> "dc_td.UpdateSmsTemplateResponse":
        return dc_td.UpdateSmsTemplateResponse.make_one(res)

    def update_template_active_version(
        self,
        res: "bs_td.UpdateTemplateActiveVersionResponseTypeDef",
    ) -> "dc_td.UpdateTemplateActiveVersionResponse":
        return dc_td.UpdateTemplateActiveVersionResponse.make_one(res)

    def update_voice_channel(
        self,
        res: "bs_td.UpdateVoiceChannelResponseTypeDef",
    ) -> "dc_td.UpdateVoiceChannelResponse":
        return dc_td.UpdateVoiceChannelResponse.make_one(res)

    def update_voice_template(
        self,
        res: "bs_td.UpdateVoiceTemplateResponseTypeDef",
    ) -> "dc_td.UpdateVoiceTemplateResponse":
        return dc_td.UpdateVoiceTemplateResponse.make_one(res)

    def verify_otp_message(
        self,
        res: "bs_td.VerifyOTPMessageResponseTypeDef",
    ) -> "dc_td.VerifyOTPMessageResponse":
        return dc_td.VerifyOTPMessageResponse.make_one(res)


pinpoint_caster = PINPOINTCaster()
