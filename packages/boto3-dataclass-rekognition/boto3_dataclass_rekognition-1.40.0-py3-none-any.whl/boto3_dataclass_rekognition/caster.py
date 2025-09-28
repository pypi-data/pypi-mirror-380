# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_rekognition import type_defs as bs_td


class REKOGNITIONCaster:

    def associate_faces(
        self,
        res: "bs_td.AssociateFacesResponseTypeDef",
    ) -> "dc_td.AssociateFacesResponse":
        return dc_td.AssociateFacesResponse.make_one(res)

    def compare_faces(
        self,
        res: "bs_td.CompareFacesResponseTypeDef",
    ) -> "dc_td.CompareFacesResponse":
        return dc_td.CompareFacesResponse.make_one(res)

    def copy_project_version(
        self,
        res: "bs_td.CopyProjectVersionResponseTypeDef",
    ) -> "dc_td.CopyProjectVersionResponse":
        return dc_td.CopyProjectVersionResponse.make_one(res)

    def create_collection(
        self,
        res: "bs_td.CreateCollectionResponseTypeDef",
    ) -> "dc_td.CreateCollectionResponse":
        return dc_td.CreateCollectionResponse.make_one(res)

    def create_dataset(
        self,
        res: "bs_td.CreateDatasetResponseTypeDef",
    ) -> "dc_td.CreateDatasetResponse":
        return dc_td.CreateDatasetResponse.make_one(res)

    def create_face_liveness_session(
        self,
        res: "bs_td.CreateFaceLivenessSessionResponseTypeDef",
    ) -> "dc_td.CreateFaceLivenessSessionResponse":
        return dc_td.CreateFaceLivenessSessionResponse.make_one(res)

    def create_project(
        self,
        res: "bs_td.CreateProjectResponseTypeDef",
    ) -> "dc_td.CreateProjectResponse":
        return dc_td.CreateProjectResponse.make_one(res)

    def create_project_version(
        self,
        res: "bs_td.CreateProjectVersionResponseTypeDef",
    ) -> "dc_td.CreateProjectVersionResponse":
        return dc_td.CreateProjectVersionResponse.make_one(res)

    def create_stream_processor(
        self,
        res: "bs_td.CreateStreamProcessorResponseTypeDef",
    ) -> "dc_td.CreateStreamProcessorResponse":
        return dc_td.CreateStreamProcessorResponse.make_one(res)

    def delete_collection(
        self,
        res: "bs_td.DeleteCollectionResponseTypeDef",
    ) -> "dc_td.DeleteCollectionResponse":
        return dc_td.DeleteCollectionResponse.make_one(res)

    def delete_faces(
        self,
        res: "bs_td.DeleteFacesResponseTypeDef",
    ) -> "dc_td.DeleteFacesResponse":
        return dc_td.DeleteFacesResponse.make_one(res)

    def delete_project(
        self,
        res: "bs_td.DeleteProjectResponseTypeDef",
    ) -> "dc_td.DeleteProjectResponse":
        return dc_td.DeleteProjectResponse.make_one(res)

    def delete_project_version(
        self,
        res: "bs_td.DeleteProjectVersionResponseTypeDef",
    ) -> "dc_td.DeleteProjectVersionResponse":
        return dc_td.DeleteProjectVersionResponse.make_one(res)

    def describe_collection(
        self,
        res: "bs_td.DescribeCollectionResponseTypeDef",
    ) -> "dc_td.DescribeCollectionResponse":
        return dc_td.DescribeCollectionResponse.make_one(res)

    def describe_dataset(
        self,
        res: "bs_td.DescribeDatasetResponseTypeDef",
    ) -> "dc_td.DescribeDatasetResponse":
        return dc_td.DescribeDatasetResponse.make_one(res)

    def describe_project_versions(
        self,
        res: "bs_td.DescribeProjectVersionsResponseTypeDef",
    ) -> "dc_td.DescribeProjectVersionsResponse":
        return dc_td.DescribeProjectVersionsResponse.make_one(res)

    def describe_projects(
        self,
        res: "bs_td.DescribeProjectsResponseTypeDef",
    ) -> "dc_td.DescribeProjectsResponse":
        return dc_td.DescribeProjectsResponse.make_one(res)

    def describe_stream_processor(
        self,
        res: "bs_td.DescribeStreamProcessorResponseTypeDef",
    ) -> "dc_td.DescribeStreamProcessorResponse":
        return dc_td.DescribeStreamProcessorResponse.make_one(res)

    def detect_custom_labels(
        self,
        res: "bs_td.DetectCustomLabelsResponseTypeDef",
    ) -> "dc_td.DetectCustomLabelsResponse":
        return dc_td.DetectCustomLabelsResponse.make_one(res)

    def detect_faces(
        self,
        res: "bs_td.DetectFacesResponseTypeDef",
    ) -> "dc_td.DetectFacesResponse":
        return dc_td.DetectFacesResponse.make_one(res)

    def detect_labels(
        self,
        res: "bs_td.DetectLabelsResponseTypeDef",
    ) -> "dc_td.DetectLabelsResponse":
        return dc_td.DetectLabelsResponse.make_one(res)

    def detect_moderation_labels(
        self,
        res: "bs_td.DetectModerationLabelsResponseTypeDef",
    ) -> "dc_td.DetectModerationLabelsResponse":
        return dc_td.DetectModerationLabelsResponse.make_one(res)

    def detect_protective_equipment(
        self,
        res: "bs_td.DetectProtectiveEquipmentResponseTypeDef",
    ) -> "dc_td.DetectProtectiveEquipmentResponse":
        return dc_td.DetectProtectiveEquipmentResponse.make_one(res)

    def detect_text(
        self,
        res: "bs_td.DetectTextResponseTypeDef",
    ) -> "dc_td.DetectTextResponse":
        return dc_td.DetectTextResponse.make_one(res)

    def disassociate_faces(
        self,
        res: "bs_td.DisassociateFacesResponseTypeDef",
    ) -> "dc_td.DisassociateFacesResponse":
        return dc_td.DisassociateFacesResponse.make_one(res)

    def get_celebrity_info(
        self,
        res: "bs_td.GetCelebrityInfoResponseTypeDef",
    ) -> "dc_td.GetCelebrityInfoResponse":
        return dc_td.GetCelebrityInfoResponse.make_one(res)

    def get_celebrity_recognition(
        self,
        res: "bs_td.GetCelebrityRecognitionResponseTypeDef",
    ) -> "dc_td.GetCelebrityRecognitionResponse":
        return dc_td.GetCelebrityRecognitionResponse.make_one(res)

    def get_content_moderation(
        self,
        res: "bs_td.GetContentModerationResponseTypeDef",
    ) -> "dc_td.GetContentModerationResponse":
        return dc_td.GetContentModerationResponse.make_one(res)

    def get_face_detection(
        self,
        res: "bs_td.GetFaceDetectionResponseTypeDef",
    ) -> "dc_td.GetFaceDetectionResponse":
        return dc_td.GetFaceDetectionResponse.make_one(res)

    def get_face_liveness_session_results(
        self,
        res: "bs_td.GetFaceLivenessSessionResultsResponseTypeDef",
    ) -> "dc_td.GetFaceLivenessSessionResultsResponse":
        return dc_td.GetFaceLivenessSessionResultsResponse.make_one(res)

    def get_face_search(
        self,
        res: "bs_td.GetFaceSearchResponseTypeDef",
    ) -> "dc_td.GetFaceSearchResponse":
        return dc_td.GetFaceSearchResponse.make_one(res)

    def get_label_detection(
        self,
        res: "bs_td.GetLabelDetectionResponseTypeDef",
    ) -> "dc_td.GetLabelDetectionResponse":
        return dc_td.GetLabelDetectionResponse.make_one(res)

    def get_media_analysis_job(
        self,
        res: "bs_td.GetMediaAnalysisJobResponseTypeDef",
    ) -> "dc_td.GetMediaAnalysisJobResponse":
        return dc_td.GetMediaAnalysisJobResponse.make_one(res)

    def get_person_tracking(
        self,
        res: "bs_td.GetPersonTrackingResponseTypeDef",
    ) -> "dc_td.GetPersonTrackingResponse":
        return dc_td.GetPersonTrackingResponse.make_one(res)

    def get_segment_detection(
        self,
        res: "bs_td.GetSegmentDetectionResponseTypeDef",
    ) -> "dc_td.GetSegmentDetectionResponse":
        return dc_td.GetSegmentDetectionResponse.make_one(res)

    def get_text_detection(
        self,
        res: "bs_td.GetTextDetectionResponseTypeDef",
    ) -> "dc_td.GetTextDetectionResponse":
        return dc_td.GetTextDetectionResponse.make_one(res)

    def index_faces(
        self,
        res: "bs_td.IndexFacesResponseTypeDef",
    ) -> "dc_td.IndexFacesResponse":
        return dc_td.IndexFacesResponse.make_one(res)

    def list_collections(
        self,
        res: "bs_td.ListCollectionsResponseTypeDef",
    ) -> "dc_td.ListCollectionsResponse":
        return dc_td.ListCollectionsResponse.make_one(res)

    def list_dataset_entries(
        self,
        res: "bs_td.ListDatasetEntriesResponseTypeDef",
    ) -> "dc_td.ListDatasetEntriesResponse":
        return dc_td.ListDatasetEntriesResponse.make_one(res)

    def list_dataset_labels(
        self,
        res: "bs_td.ListDatasetLabelsResponseTypeDef",
    ) -> "dc_td.ListDatasetLabelsResponse":
        return dc_td.ListDatasetLabelsResponse.make_one(res)

    def list_faces(
        self,
        res: "bs_td.ListFacesResponseTypeDef",
    ) -> "dc_td.ListFacesResponse":
        return dc_td.ListFacesResponse.make_one(res)

    def list_media_analysis_jobs(
        self,
        res: "bs_td.ListMediaAnalysisJobsResponseTypeDef",
    ) -> "dc_td.ListMediaAnalysisJobsResponse":
        return dc_td.ListMediaAnalysisJobsResponse.make_one(res)

    def list_project_policies(
        self,
        res: "bs_td.ListProjectPoliciesResponseTypeDef",
    ) -> "dc_td.ListProjectPoliciesResponse":
        return dc_td.ListProjectPoliciesResponse.make_one(res)

    def list_stream_processors(
        self,
        res: "bs_td.ListStreamProcessorsResponseTypeDef",
    ) -> "dc_td.ListStreamProcessorsResponse":
        return dc_td.ListStreamProcessorsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_users(
        self,
        res: "bs_td.ListUsersResponseTypeDef",
    ) -> "dc_td.ListUsersResponse":
        return dc_td.ListUsersResponse.make_one(res)

    def put_project_policy(
        self,
        res: "bs_td.PutProjectPolicyResponseTypeDef",
    ) -> "dc_td.PutProjectPolicyResponse":
        return dc_td.PutProjectPolicyResponse.make_one(res)

    def recognize_celebrities(
        self,
        res: "bs_td.RecognizeCelebritiesResponseTypeDef",
    ) -> "dc_td.RecognizeCelebritiesResponse":
        return dc_td.RecognizeCelebritiesResponse.make_one(res)

    def search_faces(
        self,
        res: "bs_td.SearchFacesResponseTypeDef",
    ) -> "dc_td.SearchFacesResponse":
        return dc_td.SearchFacesResponse.make_one(res)

    def search_faces_by_image(
        self,
        res: "bs_td.SearchFacesByImageResponseTypeDef",
    ) -> "dc_td.SearchFacesByImageResponse":
        return dc_td.SearchFacesByImageResponse.make_one(res)

    def search_users(
        self,
        res: "bs_td.SearchUsersResponseTypeDef",
    ) -> "dc_td.SearchUsersResponse":
        return dc_td.SearchUsersResponse.make_one(res)

    def search_users_by_image(
        self,
        res: "bs_td.SearchUsersByImageResponseTypeDef",
    ) -> "dc_td.SearchUsersByImageResponse":
        return dc_td.SearchUsersByImageResponse.make_one(res)

    def start_celebrity_recognition(
        self,
        res: "bs_td.StartCelebrityRecognitionResponseTypeDef",
    ) -> "dc_td.StartCelebrityRecognitionResponse":
        return dc_td.StartCelebrityRecognitionResponse.make_one(res)

    def start_content_moderation(
        self,
        res: "bs_td.StartContentModerationResponseTypeDef",
    ) -> "dc_td.StartContentModerationResponse":
        return dc_td.StartContentModerationResponse.make_one(res)

    def start_face_detection(
        self,
        res: "bs_td.StartFaceDetectionResponseTypeDef",
    ) -> "dc_td.StartFaceDetectionResponse":
        return dc_td.StartFaceDetectionResponse.make_one(res)

    def start_face_search(
        self,
        res: "bs_td.StartFaceSearchResponseTypeDef",
    ) -> "dc_td.StartFaceSearchResponse":
        return dc_td.StartFaceSearchResponse.make_one(res)

    def start_label_detection(
        self,
        res: "bs_td.StartLabelDetectionResponseTypeDef",
    ) -> "dc_td.StartLabelDetectionResponse":
        return dc_td.StartLabelDetectionResponse.make_one(res)

    def start_media_analysis_job(
        self,
        res: "bs_td.StartMediaAnalysisJobResponseTypeDef",
    ) -> "dc_td.StartMediaAnalysisJobResponse":
        return dc_td.StartMediaAnalysisJobResponse.make_one(res)

    def start_person_tracking(
        self,
        res: "bs_td.StartPersonTrackingResponseTypeDef",
    ) -> "dc_td.StartPersonTrackingResponse":
        return dc_td.StartPersonTrackingResponse.make_one(res)

    def start_project_version(
        self,
        res: "bs_td.StartProjectVersionResponseTypeDef",
    ) -> "dc_td.StartProjectVersionResponse":
        return dc_td.StartProjectVersionResponse.make_one(res)

    def start_segment_detection(
        self,
        res: "bs_td.StartSegmentDetectionResponseTypeDef",
    ) -> "dc_td.StartSegmentDetectionResponse":
        return dc_td.StartSegmentDetectionResponse.make_one(res)

    def start_stream_processor(
        self,
        res: "bs_td.StartStreamProcessorResponseTypeDef",
    ) -> "dc_td.StartStreamProcessorResponse":
        return dc_td.StartStreamProcessorResponse.make_one(res)

    def start_text_detection(
        self,
        res: "bs_td.StartTextDetectionResponseTypeDef",
    ) -> "dc_td.StartTextDetectionResponse":
        return dc_td.StartTextDetectionResponse.make_one(res)

    def stop_project_version(
        self,
        res: "bs_td.StopProjectVersionResponseTypeDef",
    ) -> "dc_td.StopProjectVersionResponse":
        return dc_td.StopProjectVersionResponse.make_one(res)


rekognition_caster = REKOGNITIONCaster()
