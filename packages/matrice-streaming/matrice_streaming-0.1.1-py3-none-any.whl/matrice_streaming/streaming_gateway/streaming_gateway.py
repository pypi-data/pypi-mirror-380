import json
import logging
import time
import threading
from typing import Dict, List, Optional
from .camera_streamer import CameraStreamer
from .streaming_gateway_utils import StreamingGatewayUtil, InputStream


class StreamingGateway:
    """Simplified streaming gateway that leverages MatriceDeployClient's capabilities.

    Supports both frame-based streaming (sending individual images) and video-based
    streaming (sending video chunks) based on the model_input_type configuration.

    Now includes optional post-processing capabilities for model results.

    Prevents multiple deployments or background streams from being started simultaneously
    using simple class-level tracking.

    Example usage:
        # Traditional usage with manual input config
        frame_input = create_camera_frame_input(camera_index=0, fps=30)
        video_input = create_camera_video_input(
            camera_index=0,
            fps=30,
            video_duration=5.0,  # 5-second chunks
            video_format="mp4"
        )

        gateway = StreamingGateway(
            session=session,
            service_id="your_service_id",
            inputs_config=[video_input],
            output_config=output_config
        )

        gateway.start_streaming()

        # To stop all streams from any instance:
        StreamingGateway.stop_all_active_streams()
    """

    # Class-level tracking of active instances
    _active_instances: Dict[str, "StreamingGateway"] = {}  # service_id -> instance
    _class_lock = threading.RLock()

    def __init__(
        self,
        session,
        streaming_gateway_id: str = None,
        server_id: str = None,
        server_type: str = None,
        inputs_config: List[InputStream] = None,
        stream_config: Dict = None,
        enable_intelligent_transmission: bool = False,
        force_restart: bool = False,
    ):
        """Initialize StreamingGateway.

        Args:
            session: Session object for authentication
            streaming_gateway_id: ID of the streaming gateway
            inputs_config: List of InputStream configurations (optional, will be fetched if not provided)
            stream_config: Configuration for MatriceStream (defaults to Kafka)
            enable_intelligent_transmission: Whether to enable intelligent frame transmission
            force_restart: Whether to force stop existing streams and restart (use with caution)
        """
        if not session:
            raise ValueError("Session is required")

        if not streaming_gateway_id:
            raise ValueError("streaming_gateway_id is required")

        self.session = session
        self.streaming_gateway_id = streaming_gateway_id
        self.force_restart = force_restart

        # Initialize StreamingGatewayUtil for API interactions
        self.gateway_util = StreamingGatewayUtil(session, streaming_gateway_id, server_id)

        # Get input configurations from API if not provided
        if inputs_config is None:
            logging.info("Fetching input configurations from API")
            self.inputs_config = self.gateway_util.get_input_streams()
        else:
            self.inputs_config = inputs_config if isinstance(inputs_config, list) else [inputs_config]

        if not self.inputs_config:
            raise ValueError("No input configurations available")

        # Validate each input config
        for i, config in enumerate(self.inputs_config):
            if not isinstance(config, InputStream):
                raise ValueError(f"Input config {i} must be an InputStream instance")

        # Initialize CameraStreamer with MatriceStream
        self.camera_streamer = CameraStreamer(
            session=self.session,
            service_id=streaming_gateway_id,
            server_type=server_type,
            stream_config=stream_config,
            enable_intelligent_transmission=enable_intelligent_transmission
        )

        # State management with proper synchronization
        self.is_streaming = False
        self.result_thread: Optional[threading.Thread] = None
        self._stop_streaming = threading.Event()
        self._state_lock = threading.RLock()
        self._my_stream_keys = set()

        # Statistics
        self.stats = {
            "start_time": None,
            "results_received": 0,
            "errors": 0,
            "last_error": None,
            "last_error_time": None,
        }

        logging.info(f"StreamingGateway initialized for streaming gateway {self.streaming_gateway_id}")

    def _register_as_active(self):
        """Register this instance as active."""
        with self.__class__._class_lock:
            self.__class__._active_instances[self.streaming_gateway_id] = self
        logging.info(f"Registered as active instance for streaming gateway {self.streaming_gateway_id}")

    def _unregister_as_active(self):
        """Unregister this instance from active tracking."""
        with self.__class__._class_lock:
            if self.streaming_gateway_id in self.__class__._active_instances:
                if self.__class__._active_instances[self.streaming_gateway_id] is self:
                    del self.__class__._active_instances[self.streaming_gateway_id]

        logging.info(f"Unregistered active instance for streaming gateway {self.streaming_gateway_id}")

    def stop_all_active_streams(self):
        """Stop all active streams across all streaming gateways."""

        if not self.force_restart:
            return

        logging.warning(
            f"Force stopping existing streams for streaming gateway {self.streaming_gateway_id}"
        )

        with self.__class__._class_lock:
            if self.streaming_gateway_id in self.__class__._active_instances:
                existing_instance = self.__class__._active_instances[self.streaming_gateway_id]

                try:
                    # Stop the existing instance
                    existing_instance.stop_streaming()
                    logging.info(
                        f"Force stopped existing streams for streaming gateway {self.streaming_gateway_id}"
                    )
                except Exception as e:
                    logging.warning(f"Error during force stop: {e}")

                # Wait a moment for cleanup
                time.sleep(1.0)

        logging.info("Stopping all active streams...")

    def start_streaming(self) -> bool:
        """Start streaming using CameraStreamer and notify API.
        Returns:
            bool: True if streaming started successfully, False otherwise
        """
        with self._state_lock:
            if self.is_streaming:
                logging.warning("Streaming is already active on this instance")
                return False

        # Validate that we have inputs to stream
        if not self.inputs_config:
            logging.error("No input configurations available for streaming")
            return False

        # Force stop existing streams if requested
        self.stop_all_active_streams()
        
        # Register as active instance
        self._register_as_active()

        
        # try:
            # result = self.gateway_util.update_status("starting")
            # if result:
            #     logging.info("Updated streaming gateway status to 'starting'")
            # else:
            #     logging.warning("Failed to update streaming gateway status to 'starting'")
        # except Exception as exc:
        #     logging.error(f"Error updating streaming gateway status: {exc}")

        # Start streaming for each input
        started_streams = []
        try:
            for i, input_config in enumerate(self.inputs_config):
                stream_key = input_config.camera_key or f"stream_{i}"
                
                # Register the topic for this stream key
                if input_config.camera_input_topic:
                    self.camera_streamer.register_stream_topic(stream_key, input_config.camera_input_topic)
                else:
                    logging.warning(f"No input topic specified for camera {input_config.camera_key}, using default")

                # Start background streaming using CameraStreamer
                success = self.camera_streamer.start_background_stream(
                    input=input_config.source,
                    fps=input_config.fps,
                    stream_key=stream_key,
                    stream_group_key=input_config.camera_group_key,
                    quality=input_config.quality,
                    width=input_config.width,
                    height=input_config.height,
                    simulate_video_file_stream=input_config.simulate_video_file_stream,
                    camera_location=input_config.camera_location,
                )

                if not success:
                    logging.error(
                        f"Failed to start streaming for input {input_config.source}", exc_info=True
                    )
                    # Stop already started streams
                    if started_streams:
                        logging.info("Stopping already started streams due to failure")
                        self.stop_streaming()

                    return False

                started_streams.append(stream_key)
                self._my_stream_keys.add(stream_key)
                logging.info(f"Started streaming for camera: {input_config.camera_key}")

            with self._state_lock:
                self._stop_streaming.clear()
                self.is_streaming = True
                self.stats["start_time"] = time.time()

            
            # try:
            #     start_result = self.gateway_util.start_streaming()
            #     if start_result:
            #         logging.info("Successfully notified API of streaming start")
                    # status_result = self.gateway_util.update_status("active")
                    # if status_result:
                    #     logging.info("Updated streaming gateway status to 'active'")
            #     else:
            #         logging.warning("Failed to notify API of streaming start")
            # except Exception as exc:
            #     logging.error(f"Error notifying API of streaming start: {exc}")

            logging.info(
                f"Started streaming successfully with {len(self.inputs_config)} inputs"
            )
            return True

        except Exception as exc:
            logging.error(f"Error starting streaming: {exc}", exc_info=True)
            # Update status to error via API
            # try:
            #     self.gateway_util.update_status("error")
            # except Exception:
            #     pass  # Don't fail on status update error
            
            # Clean up on error
            try:
                self.stop_streaming()
            except Exception as cleanup_exc:
                logging.error(f"Error during cleanup: {cleanup_exc}", exc_info=True)
            return False

    def stop_streaming(self):
        """Stop all streaming operations."""
        with self._state_lock:
            if not self.is_streaming:
                logging.warning("Streaming is not active")
                return

            logging.info("Stopping streaming...")
            self._stop_streaming.set()
            self.is_streaming = False

        # Stop camera streaming
        if self.camera_streamer:
            try:
                self.camera_streamer.stop_streaming()
            except Exception as exc:
                logging.error(f"Error stopping camera streaming: {exc}", exc_info=True)

        # Wait for result thread to finish
        if self.result_thread and self.result_thread.is_alive():
            self.result_thread.join(timeout=10.0)
            if self.result_thread.is_alive():
                logging.warning("Result thread did not stop gracefully")

        self.result_thread = None

        # Notify API that streaming stopped
        try:
            stop_result = self.gateway_util.stop_streaming()
            # if stop_result:
            #     logging.info("Successfully notified API of streaming stop")
            #     status_result = self.gateway_util.update_status("stopped")
            #     if status_result:
            #         logging.info("Updated streaming gateway status to 'stopped'")
            # else:
            #     logging.warning("Failed to notify API of streaming stop")
        except Exception as exc:
            logging.error(f"Error notifying API of streaming stop: {exc}", exc_info=True)

        # Unregister from active tracking
        self._unregister_as_active()

        # Clear stream keys
        self._my_stream_keys.clear()

        logging.info("Streaming stopped")

    def get_statistics(self) -> Dict:
        """Get streaming statistics.

        Returns:
            Dict with streaming statistics
        """
        with self._state_lock:
            stats = self.stats.copy()

        if stats["start_time"]:
            runtime = time.time() - stats["start_time"]
            stats["runtime_seconds"] = runtime
            if runtime > 0:
                stats["results_per_second"] = stats["results_received"] / runtime
            else:
                stats["results_per_second"] = 0
        else:
            stats["runtime_seconds"] = 0
            stats["results_per_second"] = 0

        # Add streaming status
        stats["is_streaming"] = self.is_streaming
        stats["my_stream_keys"] = list(self._my_stream_keys)
        
        # Add camera streamer statistics if available
        if self.camera_streamer:
            try:
                stats["transmission_stats"] = self.camera_streamer.get_transmission_stats()
            except Exception as exc:
                logging.warning(f"Failed to get transmission stats: {exc}")

        return stats

    def get_config(self) -> Dict:
        """Get current configuration.

        Returns:
            Dict with current configuration
        """
        inputs_config_dict = []
        for config in self.inputs_config:
            inputs_config_dict.append({
                'source': config.source,
                'fps': config.fps,
                'quality': config.quality,
                'width': config.width,
                'height': config.height,
                'camera_id': config.camera_id,
                'camera_key': config.camera_key,
                'camera_group_key': config.camera_group_key,
                'camera_location': config.camera_location,
                'simulate_video_file_stream': config.simulate_video_file_stream,
            })
        
        return {
            "streaming_gateway_id": self.streaming_gateway_id,
            "inputs_config": inputs_config_dict,
            "force_restart": self.force_restart,
        }

    def save_config(self, filepath: str):
        """Save current configuration to file.

        Args:
            filepath: Path to save configuration
        """
        config = self.get_config()
        with open(filepath, "w") as f:
            json.dump(config, f, indent=2)


    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.stop_streaming()
