from dataclasses import dataclass
from typing import Optional, Union, Tuple, Dict, List
import logging
from matrice_common.session import Session

@dataclass
class InputStream:
    """Configuration for input sources."""
    source: Union[int, str]  # Camera index, file path, or stream URL
    fps: int = 10
    quality: int = 100
    width: Optional[int] = 640
    height: Optional[int] = 480
    camera_id: Optional[str] = None
    camera_key: Optional[str] = "Unknown Camera"
    camera_group_key: Optional[str] = "Unknown Camera Group"
    camera_location: Optional[str] = "Unknown Camera Location"
    camera_input_topic: str = None
    camera_connection_info: dict = None
    simulate_video_file_stream: bool = False

class StreamingGatewayUtil:

    def __init__(self, session: Session, streaming_gateway_id: str, server_id: str = None):
        self.session = session
        self.streaming_gateway_id = streaming_gateway_id
        self.server_id = server_id
        if not self.server_id and self.streaming_gateway_id:
            self.server_id = self.get_streaming_gateway_by_id().get("serverId")

    def _parse_response(self, resp: dict):
        if resp.get("success"):
            return resp.get("data")
        else:
            logging.error("Request failed with payload: %s", resp, exc_info=True)
        return None

    def get_streaming_gateway_by_id(self):
        if not self.streaming_gateway_id:
            raise ValueError("Streaming gateway ID is required")
        return self._parse_response(
            self.session.rpc.get(
                f"/v1/inference/get_streaming_gateways/{self.streaming_gateway_id}"
            )
        )
#     {'id': '68c43cee7b628ecd0d44c0ca',
#   'accountNumber': '2276842692221978464767135',
#   'accountType': 'enterprise',
#   'gatewayName': 'Test_App_Deployment',
#   'description': 'Testing',
#   'status': 'created',
#   'actionRecordID': '000000000000000000000000',
#   'startTime': '0001-01-01T00:00:00Z',
#   'lastStreamTime': '0001-01-01T00:00:00Z',
#   'serverId': '68c43ceed0e26ec0da43eb3a',
#   'serverType': 'redis',
#   'networkSettings': {'IPAddress': '0.0.0.0',
#    'port': 80,
#    'accessScale': 'regional',
#    'region': 'US'},
#   'userID': '6819bdda7481e811e530a84a',
#   'createdAt': '2025-09-12T15:31:58.359Z',
#   'updatedAt': '2025-09-12T15:31:59.298Z'}

    def get_camera_groups(self):
        return self._parse_response(
            self.session.rpc.get(
                f"/v1/inference/all_camera_groups_by_gateway_id/{self.streaming_gateway_id}"
            )
        )
#         [{'id': '68bfdc599c892544110d024b',
#   'accountNumber': '2276842692221978464767135',
#   'cameraGroupName': 'Testing Cam 21',
#   'locationId': '68be42397d9f7cbe2efa4fee',
#   'streamingGatewayId': '68be77a634feaa4ecc8ee942',
#   'defaultStreamSettings': {'make': 'Model',
#    'model': 'Modle 2',
#    'aspectRatio': '16:9',
#    'height': 1080,
#    'width': 1920,
#    'videoQuality': 80,
#    'streamingFPS': 30},
#   'createdAt': '2025-09-09T07:50:49.339Z',
#   'updatedAt': '2025-09-09T07:50:49.339Z'}]

    def get_cameras(self):
        return self._parse_response(
            self.session.rpc.get(
                f"/v1/inference/all_camera_by_streaming_gateway_id/{self.streaming_gateway_id}"
            )
        )
#     [{'id': '68bfdd509c892544110d024d',
#   'accountNumber': '2276842692221978464767135',
#   'cameraName': 'Cam_Test',
#   'cameraGroupId': '68bfdc599c892544110d024b',
#   'streamingGatewayId': '68be77a634feaa4ecc8ee942',
#   'cameraFeedPath': '',
#   'simulationVideoPath': 'https://s3.us-west-2.amazonaws.com/dev.application.predictions/2adb24f1495e9afe086fcamera-video-1757404340861.mp4',
#   'protocolType': 'FILE',
#   'customStreamSettings': {},
#   'createdAt': '2025-09-09T07:54:56.189Z',
#   'updatedAt': '2025-09-09T07:54:56.189Z'}]

    def get_simulated_stream_url(self, camera_id: str):
        return self._parse_response(
            self.session.rpc.get(f"/v1/inference/get_simulated_stream_url/{camera_id}")
        )
    #     {'streamType': 'FILE',
    # 'url': 'https://s3.us-west-2.amazonaws.com/dev.application.predictions/2adb24f1495e9afe086fcamera-video-1757404340861.mp4?X-Amz-Algorithm=AWS4-HMA'}

    def get_streaming_input_topics(self):
        return self._parse_response(
            self.session.rpc.get(
                f"/v1/inference/get_topics_by_streaming_id_and_server_id/{self.streaming_gateway_id}/{self.server_id}?topicType=input"
            )
        )
#         [{'id': '68bfdd509c892544110d024e',
#   'accountNumber': '2276842692221978464767135',
#   'cameraId': '68bfdd509c892544110d024d',
#   'streamingGatewayId': '68be77a634feaa4ecc8ee942',
#   'topicName': '68bfdd509c892544110d024d_input_topic',
#   'topicType': 'input'}]

    def get_streaming_output_topics(self):
        return self._parse_response(
            self.session.rpc.get(
                f"/v1/inference/get_topics_by_streaming_id_and_server_id/{self.streaming_gateway_id}/{self.server_id}?topicType=output"
            )
        )

    def get_input_streams(self) -> List[InputStream]:
        """Get cameras as list of InputStream objects with proper configuration."""
        cameras = self.get_cameras()
        camera_groups = self.get_camera_groups()
        input_topics = self.get_streaming_input_topics()
        
        if not cameras:
            logging.warning("No cameras found for streaming gateway", exc_info=True)
            return []
        
        # Create lookup dictionaries
        camera_group_lookup = {group['id']: group for group in (camera_groups or [])}
        topic_lookup = {topic['cameraId']: topic['topicName'] for topic in (input_topics or [])}
        
        input_streams = []
        
        for camera in cameras:
            camera_id = camera['id']
            camera_group_id = camera.get('cameraGroupId')
            camera_group = camera_group_lookup.get(camera_group_id, {})
            
            # Get default settings from camera group
            default_settings = camera_group.get('defaultStreamSettings', {})
            custom_settings = camera.get('customStreamSettings', {})
            
            # Merge settings (custom overrides default)
            settings = {**default_settings, **custom_settings}
            
            # Determine source URL
            source = camera.get('cameraFeedPath', '')
            simulate_video = False
            
            if camera.get('protocolType') == 'FILE':
                # Get simulated stream URL for file type cameras
                stream_url_data = self.get_simulated_stream_url(camera_id)
                if stream_url_data and stream_url_data.get('url'):
                    source = stream_url_data['url']
                    simulate_video = True
                else:
                    # Fallback to simulation video path
                    source = camera.get('simulationVideoPath', '')
                    simulate_video = True
            
            # Get input topic for this camera
            input_topic = topic_lookup.get(camera_id)
            
            # Create InputStream object
            input_stream = InputStream(
                source=source,
                fps=settings.get('streamingFPS', 10),
                quality=settings.get('videoQuality', 100),
                width=settings.get('width', 640),
                height=settings.get('height', 480),
                camera_id=camera_id,
                camera_key=camera.get('cameraName', 'Unknown Camera'),
                camera_group_key=camera_group.get('cameraGroupName', 'Unknown Camera Group'), # TODO: change to location not id
                camera_location=camera_group.get('locationId', 'Unknown Camera Location'),
                camera_input_topic=input_topic,
                camera_connection_info=camera,
                simulate_video_file_stream=simulate_video
            )
            
            input_streams.append(input_stream)
            
        logging.info(f"Created {len(input_streams)} input streams for streaming gateway", exc_info=True)
        return input_streams
    
    def start_streaming(self) -> Optional[Dict]:
        """
        Start the streaming gateway.
        
        Returns:
            Dict: API response data or None if failed
        """
        path = f"/v1/inference/start_streaming_gateway/{self.streaming_gateway_id}"
        
        resp = self.session.rpc.post(path=path, payload={})
        
        return self._parse_response(resp)
    
    def stop_streaming(self) -> Optional[Dict]:
        """
        Stop the streaming gateway.
        
        Returns:
            Dict: API response data or None if failed
        """
        path = f"/v1/inference/stop_streaming_gateway/{self.streaming_gateway_id}"
        
        resp = self.session.rpc.post(path=path, payload={})
        
        return self._parse_response(resp)
    
    def update_status(self, status: str) -> Optional[Dict]:
        """
        Update the status of the streaming gateway.
        
        Args:
            status: New status (active, inactive, starting, stopped, etc.)
        
        Returns:
            Dict: API response data or None if failed
        """
        if not status:
            logging.error("Status is required", exc_info=True)
            return None
        
        path = f"/v1/inference/update_streaming_gateway_status/{self.streaming_gateway_id}"
        payload = {"status": status}
        
        resp = self.session.rpc.put(path=path, payload=payload)
        
        return self._parse_response(resp)