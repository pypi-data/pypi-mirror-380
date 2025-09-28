# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_location import type_defs as bs_td


class LOCATIONCaster:

    def batch_delete_device_position_history(
        self,
        res: "bs_td.BatchDeleteDevicePositionHistoryResponseTypeDef",
    ) -> "dc_td.BatchDeleteDevicePositionHistoryResponse":
        return dc_td.BatchDeleteDevicePositionHistoryResponse.make_one(res)

    def batch_delete_geofence(
        self,
        res: "bs_td.BatchDeleteGeofenceResponseTypeDef",
    ) -> "dc_td.BatchDeleteGeofenceResponse":
        return dc_td.BatchDeleteGeofenceResponse.make_one(res)

    def batch_evaluate_geofences(
        self,
        res: "bs_td.BatchEvaluateGeofencesResponseTypeDef",
    ) -> "dc_td.BatchEvaluateGeofencesResponse":
        return dc_td.BatchEvaluateGeofencesResponse.make_one(res)

    def batch_get_device_position(
        self,
        res: "bs_td.BatchGetDevicePositionResponseTypeDef",
    ) -> "dc_td.BatchGetDevicePositionResponse":
        return dc_td.BatchGetDevicePositionResponse.make_one(res)

    def batch_put_geofence(
        self,
        res: "bs_td.BatchPutGeofenceResponseTypeDef",
    ) -> "dc_td.BatchPutGeofenceResponse":
        return dc_td.BatchPutGeofenceResponse.make_one(res)

    def batch_update_device_position(
        self,
        res: "bs_td.BatchUpdateDevicePositionResponseTypeDef",
    ) -> "dc_td.BatchUpdateDevicePositionResponse":
        return dc_td.BatchUpdateDevicePositionResponse.make_one(res)

    def calculate_route(
        self,
        res: "bs_td.CalculateRouteResponseTypeDef",
    ) -> "dc_td.CalculateRouteResponse":
        return dc_td.CalculateRouteResponse.make_one(res)

    def calculate_route_matrix(
        self,
        res: "bs_td.CalculateRouteMatrixResponseTypeDef",
    ) -> "dc_td.CalculateRouteMatrixResponse":
        return dc_td.CalculateRouteMatrixResponse.make_one(res)

    def create_geofence_collection(
        self,
        res: "bs_td.CreateGeofenceCollectionResponseTypeDef",
    ) -> "dc_td.CreateGeofenceCollectionResponse":
        return dc_td.CreateGeofenceCollectionResponse.make_one(res)

    def create_key(
        self,
        res: "bs_td.CreateKeyResponseTypeDef",
    ) -> "dc_td.CreateKeyResponse":
        return dc_td.CreateKeyResponse.make_one(res)

    def create_map(
        self,
        res: "bs_td.CreateMapResponseTypeDef",
    ) -> "dc_td.CreateMapResponse":
        return dc_td.CreateMapResponse.make_one(res)

    def create_place_index(
        self,
        res: "bs_td.CreatePlaceIndexResponseTypeDef",
    ) -> "dc_td.CreatePlaceIndexResponse":
        return dc_td.CreatePlaceIndexResponse.make_one(res)

    def create_route_calculator(
        self,
        res: "bs_td.CreateRouteCalculatorResponseTypeDef",
    ) -> "dc_td.CreateRouteCalculatorResponse":
        return dc_td.CreateRouteCalculatorResponse.make_one(res)

    def create_tracker(
        self,
        res: "bs_td.CreateTrackerResponseTypeDef",
    ) -> "dc_td.CreateTrackerResponse":
        return dc_td.CreateTrackerResponse.make_one(res)

    def describe_geofence_collection(
        self,
        res: "bs_td.DescribeGeofenceCollectionResponseTypeDef",
    ) -> "dc_td.DescribeGeofenceCollectionResponse":
        return dc_td.DescribeGeofenceCollectionResponse.make_one(res)

    def describe_key(
        self,
        res: "bs_td.DescribeKeyResponseTypeDef",
    ) -> "dc_td.DescribeKeyResponse":
        return dc_td.DescribeKeyResponse.make_one(res)

    def describe_map(
        self,
        res: "bs_td.DescribeMapResponseTypeDef",
    ) -> "dc_td.DescribeMapResponse":
        return dc_td.DescribeMapResponse.make_one(res)

    def describe_place_index(
        self,
        res: "bs_td.DescribePlaceIndexResponseTypeDef",
    ) -> "dc_td.DescribePlaceIndexResponse":
        return dc_td.DescribePlaceIndexResponse.make_one(res)

    def describe_route_calculator(
        self,
        res: "bs_td.DescribeRouteCalculatorResponseTypeDef",
    ) -> "dc_td.DescribeRouteCalculatorResponse":
        return dc_td.DescribeRouteCalculatorResponse.make_one(res)

    def describe_tracker(
        self,
        res: "bs_td.DescribeTrackerResponseTypeDef",
    ) -> "dc_td.DescribeTrackerResponse":
        return dc_td.DescribeTrackerResponse.make_one(res)

    def forecast_geofence_events(
        self,
        res: "bs_td.ForecastGeofenceEventsResponseTypeDef",
    ) -> "dc_td.ForecastGeofenceEventsResponse":
        return dc_td.ForecastGeofenceEventsResponse.make_one(res)

    def get_device_position(
        self,
        res: "bs_td.GetDevicePositionResponseTypeDef",
    ) -> "dc_td.GetDevicePositionResponse":
        return dc_td.GetDevicePositionResponse.make_one(res)

    def get_device_position_history(
        self,
        res: "bs_td.GetDevicePositionHistoryResponseTypeDef",
    ) -> "dc_td.GetDevicePositionHistoryResponse":
        return dc_td.GetDevicePositionHistoryResponse.make_one(res)

    def get_geofence(
        self,
        res: "bs_td.GetGeofenceResponseTypeDef",
    ) -> "dc_td.GetGeofenceResponse":
        return dc_td.GetGeofenceResponse.make_one(res)

    def get_map_glyphs(
        self,
        res: "bs_td.GetMapGlyphsResponseTypeDef",
    ) -> "dc_td.GetMapGlyphsResponse":
        return dc_td.GetMapGlyphsResponse.make_one(res)

    def get_map_sprites(
        self,
        res: "bs_td.GetMapSpritesResponseTypeDef",
    ) -> "dc_td.GetMapSpritesResponse":
        return dc_td.GetMapSpritesResponse.make_one(res)

    def get_map_style_descriptor(
        self,
        res: "bs_td.GetMapStyleDescriptorResponseTypeDef",
    ) -> "dc_td.GetMapStyleDescriptorResponse":
        return dc_td.GetMapStyleDescriptorResponse.make_one(res)

    def get_map_tile(
        self,
        res: "bs_td.GetMapTileResponseTypeDef",
    ) -> "dc_td.GetMapTileResponse":
        return dc_td.GetMapTileResponse.make_one(res)

    def get_place(
        self,
        res: "bs_td.GetPlaceResponseTypeDef",
    ) -> "dc_td.GetPlaceResponse":
        return dc_td.GetPlaceResponse.make_one(res)

    def list_device_positions(
        self,
        res: "bs_td.ListDevicePositionsResponseTypeDef",
    ) -> "dc_td.ListDevicePositionsResponse":
        return dc_td.ListDevicePositionsResponse.make_one(res)

    def list_geofence_collections(
        self,
        res: "bs_td.ListGeofenceCollectionsResponseTypeDef",
    ) -> "dc_td.ListGeofenceCollectionsResponse":
        return dc_td.ListGeofenceCollectionsResponse.make_one(res)

    def list_geofences(
        self,
        res: "bs_td.ListGeofencesResponseTypeDef",
    ) -> "dc_td.ListGeofencesResponse":
        return dc_td.ListGeofencesResponse.make_one(res)

    def list_keys(
        self,
        res: "bs_td.ListKeysResponseTypeDef",
    ) -> "dc_td.ListKeysResponse":
        return dc_td.ListKeysResponse.make_one(res)

    def list_maps(
        self,
        res: "bs_td.ListMapsResponseTypeDef",
    ) -> "dc_td.ListMapsResponse":
        return dc_td.ListMapsResponse.make_one(res)

    def list_place_indexes(
        self,
        res: "bs_td.ListPlaceIndexesResponseTypeDef",
    ) -> "dc_td.ListPlaceIndexesResponse":
        return dc_td.ListPlaceIndexesResponse.make_one(res)

    def list_route_calculators(
        self,
        res: "bs_td.ListRouteCalculatorsResponseTypeDef",
    ) -> "dc_td.ListRouteCalculatorsResponse":
        return dc_td.ListRouteCalculatorsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_tracker_consumers(
        self,
        res: "bs_td.ListTrackerConsumersResponseTypeDef",
    ) -> "dc_td.ListTrackerConsumersResponse":
        return dc_td.ListTrackerConsumersResponse.make_one(res)

    def list_trackers(
        self,
        res: "bs_td.ListTrackersResponseTypeDef",
    ) -> "dc_td.ListTrackersResponse":
        return dc_td.ListTrackersResponse.make_one(res)

    def put_geofence(
        self,
        res: "bs_td.PutGeofenceResponseTypeDef",
    ) -> "dc_td.PutGeofenceResponse":
        return dc_td.PutGeofenceResponse.make_one(res)

    def search_place_index_for_position(
        self,
        res: "bs_td.SearchPlaceIndexForPositionResponseTypeDef",
    ) -> "dc_td.SearchPlaceIndexForPositionResponse":
        return dc_td.SearchPlaceIndexForPositionResponse.make_one(res)

    def search_place_index_for_suggestions(
        self,
        res: "bs_td.SearchPlaceIndexForSuggestionsResponseTypeDef",
    ) -> "dc_td.SearchPlaceIndexForSuggestionsResponse":
        return dc_td.SearchPlaceIndexForSuggestionsResponse.make_one(res)

    def search_place_index_for_text(
        self,
        res: "bs_td.SearchPlaceIndexForTextResponseTypeDef",
    ) -> "dc_td.SearchPlaceIndexForTextResponse":
        return dc_td.SearchPlaceIndexForTextResponse.make_one(res)

    def update_geofence_collection(
        self,
        res: "bs_td.UpdateGeofenceCollectionResponseTypeDef",
    ) -> "dc_td.UpdateGeofenceCollectionResponse":
        return dc_td.UpdateGeofenceCollectionResponse.make_one(res)

    def update_key(
        self,
        res: "bs_td.UpdateKeyResponseTypeDef",
    ) -> "dc_td.UpdateKeyResponse":
        return dc_td.UpdateKeyResponse.make_one(res)

    def update_map(
        self,
        res: "bs_td.UpdateMapResponseTypeDef",
    ) -> "dc_td.UpdateMapResponse":
        return dc_td.UpdateMapResponse.make_one(res)

    def update_place_index(
        self,
        res: "bs_td.UpdatePlaceIndexResponseTypeDef",
    ) -> "dc_td.UpdatePlaceIndexResponse":
        return dc_td.UpdatePlaceIndexResponse.make_one(res)

    def update_route_calculator(
        self,
        res: "bs_td.UpdateRouteCalculatorResponseTypeDef",
    ) -> "dc_td.UpdateRouteCalculatorResponse":
        return dc_td.UpdateRouteCalculatorResponse.make_one(res)

    def update_tracker(
        self,
        res: "bs_td.UpdateTrackerResponseTypeDef",
    ) -> "dc_td.UpdateTrackerResponse":
        return dc_td.UpdateTrackerResponse.make_one(res)

    def verify_device_position(
        self,
        res: "bs_td.VerifyDevicePositionResponseTypeDef",
    ) -> "dc_td.VerifyDevicePositionResponse":
        return dc_td.VerifyDevicePositionResponse.make_one(res)


location_caster = LOCATIONCaster()
