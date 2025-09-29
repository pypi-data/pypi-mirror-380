import base64
import logging
import cv2
import threading
import time
import hashlib
import uuid
import numpy as np
from datetime import datetime, timezone
from typing import Dict, Optional, Union, Tuple, Any
from matrice_common.stream.matrice_stream import MatriceStream, StreamType
from matrice_common.optimize.transmission import ClientTransmissionHandler


class CameraStreamer:
    def __init__(
        self,
        session,
        service_id: str,
        server_type: str,
        stream_config: Dict = None,
        threshold_a: float = 0.95,
        threshold_b: float = 0.85,
        enable_intelligent_transmission: bool = False,
        strip_input_content: bool = False,
    ):
        """Initialize CameraStreamer.

        Args:
            session: Session object for making RPC calls
            service_id: ID of the deployment
            server_type: Type of server (kafka or redis)
            stream_config: Configuration for MatriceStream (defaults to Kafka)
            threshold_a: High similarity threshold for skipping transmission (default: 0.95)
            threshold_b: Medium similarity threshold for difference transmission (default: 0.85)
            enable_intelligent_transmission: Whether to enable intelligent frame transmission
        """
        self.streaming_threads = []
        self.session = session
        self.service_id = service_id
        self.server_type = server_type.lower()
        self.input_order = {}  # Dictionary to track input counter for each stream key
        self._stop_streaming = False
        self.video_start_times = {}  # Track video start times for timestamp calculation

        # Initialize MatriceStream
        if stream_config is None:
            stream_config = {}
        
        self.matrice_stream = MatriceStream(StreamType.REDIS if self.server_type == "redis" else StreamType.KAFKA, **stream_config)
        self.stream_support = True  # MatriceStream is always supported
        
        # Intelligent transmission components
        self.enable_intelligent_transmission = enable_intelligent_transmission
        self.threshold_a = threshold_a
        self.threshold_b = threshold_b
        self.txh = ClientTransmissionHandler(
            threshold_a=threshold_a, threshold_b=threshold_b
        )
        # When enabled, still build and validate input, but send empty base64 content
        # (only safe once downstream supports out-of-band frame retrieval)
        self.strip_input_content = strip_input_content

        # Transmission statistics
        self.frames_sent = 0
        self.frames_skipped = 0
        self.frames_diff_sent = 0
        self.bytes_saved = 0
        
        # Latency statistics for the previous message per stream
        self.last_read_times = {}  # Dict[stream_key, float]
        self.last_write_times = {}  # Dict[stream_key, float]
        self.last_process_times = {}  # Dict[stream_key, float]
        
        # Topic mapping for each stream key
        self.stream_topics = {}  # Dict[stream_key, topic_name]
        self.setup_topics = set()  # Set of topics that have been setup
    
    def setup_stream_for_topic(self, topic: str):
        """Setup the MatriceStream for a specific topic."""
        try:
            if topic not in self.setup_topics:
                # Setup for producing to this topic
                self.matrice_stream.setup(topic)
                self.setup_topics.add(topic)
                
                logging.info(f"MatriceStream setup complete for topic: {topic}")
            return True
        except Exception as e:
            logging.error(f"Failed to setup MatriceStream for topic {topic}: {str(e)}")
            return False

    def register_stream_topic(self, stream_key: str, topic: str):
        """Register a topic for a specific stream key."""
        self.stream_topics[stream_key] = topic
        logging.info(f"Registered topic '{topic}' for stream key '{stream_key}'")

    def get_topic_for_stream(self, stream_key: str) -> Optional[str]:
        """Get the topic for a specific stream key."""
        return self.stream_topics.get(stream_key)

    def _get_stream_key_for_timing(self, stream_key: Optional[str]) -> str:
        """Get normalized stream key for timing data."""
        return stream_key if stream_key is not None else "default"

    def _get_last_timings(self, stream_key: Optional[str]) -> Tuple[float, float, float]:
        """Get last timing data for a specific stream."""
        key = self._get_stream_key_for_timing(stream_key)
        read_time = self.last_read_times.get(key, 0.0)
        write_time = self.last_write_times.get(key, 0.0)
        process_time = self.last_process_times.get(key, 0.0)
        return read_time, write_time, process_time

    def _update_last_timings(self, stream_key: Optional[str], read_time: float, write_time: float, process_time: float) -> None:
        """Update last timing data for a specific stream."""
        key = self._get_stream_key_for_timing(stream_key)
        self.last_read_times[key] = read_time
        self.last_write_times[key] = write_time
        self.last_process_times[key] = process_time

    def _determine_transmission_strategy(
        self, frame: np.ndarray, stream_key: str
    ) -> Tuple[str, Dict]:
        if not self.enable_intelligent_transmission:
            self.txh.frame_cache[stream_key] = frame.copy()
            return "full", {"reason": "intelligent_disabled"}
        return self.txh.decide_transmission(frame, stream_key)

    def _validate_stream_params(
        self, fps: int, quality: int, width: Optional[int], height: Optional[int]
    ) -> bool:
        """Validate common streaming parameters."""
        if fps <= 0:
            logging.error("FPS must be positive")
            return False
        if quality < 1 or quality > 100:
            logging.error("Quality must be between 1 and 100")
            return False
        if width is not None and width <= 0:
            logging.error("Width must be positive")
            return False
        if height is not None and height <= 0:
            logging.error("Height must be positive")
            return False
        return True

    def _check_stream_support(self) -> bool:
        """Check if streaming is supported."""
        if not self.stream_support:
            logging.error(
                "Kafka stream support not available, Please check if Kafka is enabled in the deployment and reinitialize the client"
            )
            return False
        return True

    def _setup_video_capture(
        self, input: Union[str, int], width: Optional[int], height: Optional[int]
    ) -> Tuple[cv2.VideoCapture, str]:
        """Set up video capture with proper configuration."""
        stream_type = "unknown"
        # Handle different input types
        if isinstance(input, int) or (isinstance(input, str) and input.isdigit()):
            cap = cv2.VideoCapture(int(input) if isinstance(input, str) else input)
            logging.info(f"Opening webcam device: {input}")
            stream_type = "camera"
        elif isinstance(input, str) and input.startswith("rtsp"):
            cap = cv2.VideoCapture(input)
            logging.info(f"Opening RTSP stream: {input}")
            stream_type = "rtsp"
        elif isinstance(input, str) and input.startswith("http"):
            cap = cv2.VideoCapture(input)
            logging.info(f"Opening HTTP stream: {input}")
            stream_type = "http"
        else:
            cap = cv2.VideoCapture(input)
            logging.info(f"Opening video source: {input}")
            stream_type = "video_file"

        if not cap.isOpened():
            logging.error(f"Failed to open video source: {input}")
            raise RuntimeError(f"Failed to open video source: {input}")

        # Set properties for cameras and RTSP streams
        if isinstance(input, int) or (isinstance(input, str) and input.isdigit()):
            cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)  # Minimize buffering for real-time
            if width is not None:
                cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
            if height is not None:
                cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        elif isinstance(input, str) and input.startswith("rtsp"):
            # For RTSP streams, set minimal buffer to prevent frame accumulation
            cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

        return cap, stream_type

    def _get_video_properties(self, cap: cv2.VideoCapture) -> Dict:
        """Get video properties from capture object."""
        return {
            "original_fps": float(round(cap.get(cv2.CAP_PROP_FPS), 2)),
            "frame_count": cap.get(cv2.CAP_PROP_FRAME_COUNT),
            "width": int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            "height": int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
        }

    def _get_high_precision_timestamp(self) -> str:
        """Get high precision timestamp with microsecond granularity."""
        return datetime.now(timezone.utc).strftime("%Y-%m-%d-%H:%M:%S.%f UTC")

    def _calculate_video_timestamp(
        self, stream_key: str, frame_number: int, fps: float
    ) -> str:
        """Calculate video timestamp from start of video.

        The timestamp is returned in human-readable ``HH:MM:SS:mmm`` format
        where *mmm* represents milliseconds.  This makes it easier to locate
        frames in recordings that are longer than 60 seconds.
        """
        # Lazily initialise the start-time dictionary to keep backward
        # compatibility even though it is no longer used for formatting.
        if stream_key not in self.video_start_times:
            self.video_start_times[stream_key] = time.time()

        # Calculate the elapsed time in seconds since the beginning of the
        # video based solely on frame number and FPS.
        total_seconds = frame_number / fps if fps else 0.0

        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)
        milliseconds = int(round((total_seconds - int(total_seconds)) * 1000))

        return f"{hours:02d}:{minutes:02d}:{seconds:02d}:{milliseconds:03d}"

    def _handle_frame_read_failure(
        self,
        input: Union[str, int],
        cap: cv2.VideoCapture,
        retry_count: int,
        max_retries: int,
        width: Optional[int],
        height: Optional[int],
        simulate_video_file_stream: bool = False,
        retry_cycle_count: int = 0,
        max_retry_cycles: int = 0,
        cooldown_period: float = 5.0,
    ) -> Tuple[cv2.VideoCapture, int, int]:
        """Handle frame read failures with retry logic."""
        if retry_count >= max_retries:
            if isinstance(input, int) or (isinstance(input, str) and input.isdigit()):
                # For cameras, try to reopen with cooldown and multiple cycles
                retry_cycle_count += 1

                if retry_cycle_count > max_retry_cycles and max_retry_cycles != 0:
                    logging.error(f"Exceeded maximum retry cycles ({max_retry_cycles}) for camera, stopping stream")
                    raise RuntimeError(f"Failed to reopen camera after {max_retry_cycles} retry cycles")

                if max_retry_cycles == 0:
                    logging.info(f"Attempting to reopen camera (retry cycle {retry_cycle_count}/∞)...")
                else:
                    logging.info(f"Attempting to reopen camera (retry cycle {retry_cycle_count}/{max_retry_cycles})...")
                cap.release()

                # Apply cooldown period between retry cycles
                logging.info(f"Waiting {cooldown_period} seconds before retry cycle...")
                time.sleep(cooldown_period)

                cap = cv2.VideoCapture(int(input) if isinstance(input, str) else input)
                if not cap.isOpened():
                    logging.warning(f"Failed to reopen camera on retry cycle {retry_cycle_count}, will retry after cooldown")
                    # Don't raise exception here, just return and try again in the next cycle
                    return cap, 0, retry_cycle_count  # Reset retry count but keep cycle count

                # Reapply resolution settings
                if width is not None:
                    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
                if height is not None:
                    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

                logging.info(f"Successfully reopened camera on retry cycle {retry_cycle_count}")
                return cap, 0, retry_cycle_count  # Reset retry count but keep cycle count
            else:
                # For video files, check if we should restart or stop
                if simulate_video_file_stream:
                    logging.info(
                        f"End of video file reached, restarting from beginning: {input}"
                    )
                    cap.release()
                    time.sleep(10)  # Brief pause before reopening
                    cap = cv2.VideoCapture(input)
                    if not cap.isOpened():
                        raise RuntimeError(f"Failed to reopen video file: {input}")
                    return cap, 0, retry_cycle_count  # Reset retry count
                else:
                    # Normal behavior - end of stream
                    logging.info(f"End of stream reached for input: {input}")
                    raise StopIteration("End of stream reached")

        time.sleep(0.1)  # Short delay before retry
        return cap, retry_count, retry_cycle_count

    def _resize_frame_if_needed(
        self, frame, width: Optional[int], height: Optional[int]
    ):
        """Resize frame if dimensions are specified and different from current."""
        if width is not None or height is not None:
            current_height, current_width = frame.shape[:2]
            target_width = width if width is not None else current_width
            target_height = height if height is not None else current_height

            if target_width != current_width or target_height != current_height:
                frame = cv2.resize(frame, (target_width, target_height))
        return frame

    def _get_next_input_order(self, stream_key: Optional[str]) -> int:
        """Get the next input order for a given stream key."""
        key = stream_key if stream_key is not None else "default"
        if key not in self.input_order:
            self.input_order[key] = 0
        self.input_order[key] += 1
        return self.input_order[key]

    def _get_video_format(self, input: Union[str, int]) -> str:
        """Get video format extension from input."""
        if isinstance(input, str) and "." in input:
            return "." + input.split("?")[0].split(".")[-1].lower()
        return ".mp4"

    def _calculate_frame_skip(self, original_fps: float, target_fps: int) -> int:
        """Calculate how many frames to skip for RTSP streams to achieve target FPS."""
        if original_fps <= 0 or target_fps <= 0:
            return 1

        frame_skip = max(1, int(original_fps / target_fps))
        logging.info(
            f"Original FPS: {original_fps}, Target FPS: {target_fps}, Frame skip: {frame_skip}"
        )
        return frame_skip

    # Removed: metadata building is centralized in ClientTransmissionHandler

    def start_stream(
        self,
        input: Union[str, int],
        fps: int = 10,
        stream_key: Optional[str] = None,
        stream_group_key: Optional[str] = None,
        quality: int = 95,
        width: Optional[int] = None,
        height: Optional[int] = None,
        simulate_video_file_stream: bool = False,
        is_video_chunk: bool = False,
        chunk_duration_seconds: Optional[float] = None,
        chunk_frames: Optional[int] = None,
        camera_location: Optional[str] = None,
    ) -> bool:
        """Start a stream input to the Kafka stream in the current thread.
        
        Args:
            input: Video input source (camera index, file path, or URL)
            fps: Target frames per second
            stream_key: Unique identifier for this stream
            stream_group_key: Group identifier for this stream
            quality: JPEG compression quality (1-100)
            width: Target frame width (optional)
            height: Target frame height (optional)
            simulate_video_file_stream: Whether to simulate video file as stream
            is_video_chunk: Whether to send video chunks instead of frames
            chunk_duration_seconds: Duration of video chunks in seconds
            chunk_frames: Maximum number of frames per chunk
            camera_location: Physical location of the camera (e.g., "Building A, Floor 2, Room 205")
        """
        if not self._check_stream_support():
            return False

        if not self._validate_stream_params(fps, quality, width, height):
            return False

        try:
            self._stream_inputs(
                input=input,
                fps=fps,
                stream_key=stream_key,
                stream_group_key=stream_group_key,
                quality=quality,
                width=width,
                height=height,
                simulate_video_file_stream=simulate_video_file_stream,
                is_video_chunk=is_video_chunk,
                chunk_duration_seconds=chunk_duration_seconds,
                chunk_frames=chunk_frames,
                camera_location=camera_location,
            )
            return True
        except Exception as exc:
            logging.error("Failed to start streaming: %s", str(exc))
            return False
        except KeyboardInterrupt:
            logging.info("Keyboard interrupt, stopping streaming")
            self.stop_streaming()
            return False

    def start_background_stream(
        self,
        input: Union[str, int],
        fps: int = 10,
        stream_key: Optional[str] = None,
        stream_group_key: Optional[str] = None,
        quality: int = 95,
        width: Optional[int] = None,
        height: Optional[int] = None,
        simulate_video_file_stream: bool = False,
        is_video_chunk: bool = False,
        chunk_duration_seconds: Optional[float] = None,
        chunk_frames: Optional[int] = None,
        camera_location: Optional[str] = None,
    ) -> bool:
        """Start a stream input to the Kafka stream in a background thread.
        
        Args:
            input: Video input source (camera index, file path, or URL)
            fps: Target frames per second
            stream_key: Unique identifier for this stream
            stream_group_key: Group identifier for this stream
            quality: JPEG compression quality (1-100)
            width: Target frame width (optional)
            height: Target frame height (optional)
            simulate_video_file_stream: Whether to simulate video file as stream
            is_video_chunk: Whether to send video chunks instead of frames
            chunk_duration_seconds: Duration of video chunks in seconds
            chunk_frames: Maximum number of frames per chunk
            camera_location: Physical location of the camera (e.g., "Building A, Floor 2, Room 205")
        """
        if not self._check_stream_support():
            return False

        if not self._validate_stream_params(fps, quality, width, height):
            return False

        try:
            thread = threading.Thread(
                target=self._stream_inputs,
                args=(
                    input,
                    fps,
                    stream_key,
                    stream_group_key,
                    quality,
                    width,
                    height,
                    simulate_video_file_stream,
                    is_video_chunk,
                    chunk_duration_seconds,
                    chunk_frames,
                    camera_location,
                ),
                daemon=True,
            )
            self.streaming_threads.append(thread)
            thread.start()
            return True
        except Exception as exc:
            logging.error("Failed to start streaming thread: %s", str(exc))
            return False

    def _stream_inputs(
        self,
        input: Union[str, int],
        fps: int = 10,
        stream_key: Optional[str] = None,
        stream_group_key: Optional[str] = None,
        quality: int = 95,
        width: Optional[int] = None,
        height: Optional[int] = None,
        simulate_video_file_stream: bool = False,
        is_video_chunk: bool = False,
        chunk_duration_seconds: Optional[float] = None,
        chunk_frames: Optional[int] = None,
        camera_location: Optional[str] = None,
    ) -> None:
        """Stream inputs from a video source to Kafka."""
        quality = max(1, min(100, quality))
        cap = None

        try:
            # Get the topic for this stream key  
            topic = self.get_topic_for_stream(stream_key)
            if not topic:
                logging.error(f"No topic registered for stream key '{stream_key}', cannot start streaming")
                return
                
            # Setup MatriceStream for this topic
            if not self.setup_stream_for_topic(topic):
                logging.error(f"Failed to setup MatriceStream for topic '{topic}', cannot start streaming")
                return
                    
            cap, stream_type = self._setup_video_capture(input, width, height)
            # Get video properties including original FPS
            video_props = self._get_video_properties(cap)

            actual_width = video_props["width"]
            actual_height = video_props["height"]
            # Override with specified dimensions if provided
            if width is not None:
                actual_width = width
            if height is not None:
                actual_height = height

            # Calculate frame skip for RTSP streams to handle high FPS sources
            frame_skip = 1
            is_rtsp_stream = isinstance(input, str) and input.startswith("rtsp")
            if is_rtsp_stream and video_props["original_fps"] > fps:
                frame_skip = self._calculate_frame_skip(
                    video_props["original_fps"], fps
                )

            retry_count = 0
            max_retries = 3
            consecutive_failures = 0
            max_consecutive_failures = 10
            frame_counter = 0
            processed_frame_counter = 0
            retry_cycle_count = 0
            max_retry_cycles = 0  # Allow multiple retry cycles for cameras, 0 for infinite retry cycles
            cooldown_period = 5.0  # Cooldown period in seconds between retry cycles

            while not self._stop_streaming:
                start_time = time.time()
                
                # Measure read time from camera/stream
                read_start_time = time.time()
                ret, frame = cap.read()
                read_time = time.time() - read_start_time

                if not ret:
                    retry_count += 1
                    consecutive_failures += 1
                    logging.warning(
                        f"Failed to read frame, retry {retry_count}/{max_retries}"
                    )

                    if consecutive_failures >= max_consecutive_failures:
                        logging.error("Too many consecutive failures, stopping stream")
                        break

                    try:
                        cap, retry_count, retry_cycle_count = self._handle_frame_read_failure(
                            input,
                            cap,
                            retry_count,
                            max_retries,
                            width,
                            height,
                            simulate_video_file_stream,
                            retry_cycle_count,
                            max_retry_cycles,
                            cooldown_period,
                        )
                    except (RuntimeError, StopIteration):
                        break
                    continue

                # Reset counters on successful frame read
                retry_count = 0
                consecutive_failures = 0
                retry_cycle_count = 0  # Reset retry cycle count on successful read
                frame_counter += 1

                # For RTSP streams, use frame skipping instead of time delays
                if is_rtsp_stream:
                    # Process only every Nth frame to achieve target FPS
                    if frame_counter % frame_skip != 0:
                        continue
                    processed_frame_counter += 1
                else:
                    processed_frame_counter = frame_counter

                # Resize frame if needed
                frame = self._resize_frame_if_needed(frame, width, height)

                # Prepare payload and metadata via transmission handler
                try:
                    input_bytes, frame_metadata, strategy = (
                        self.txh.prepare_transmission(
                            frame,
                            stream_key=stream_key or "default",
                            input_source=input,
                            video_props=video_props,
                            fps=fps,
                            quality=quality,
                            actual_width=actual_width,
                            actual_height=actual_height,
                            stream_type=stream_type,
                            frame_counter=processed_frame_counter,
                            is_video_chunk=is_video_chunk,
                            chunk_duration_seconds=chunk_duration_seconds,
                            chunk_frames=chunk_frames,
                            camera_location=camera_location,
                        )
                    )
                except Exception as exc:
                    logging.error(f"Transmission preparation failed: {exc}")
                    continue

                # Update simple counters
                if strategy == "skip":
                    self.frames_skipped += 1
                elif strategy == "difference":
                    self.frames_diff_sent += 1

                # Get previous message timing data for this stream
                last_read_time, last_write_time, last_process_time = self._get_last_timings(stream_key)
                
                # Add previous message timing data to current metadata
                frame_metadata.update({
                    "last_read_time_sec": last_read_time,
                    "last_write_time_sec": last_write_time,
                    "last_process_time_sec": last_process_time,
                })

                # Measure write time to Kafka and produce
                write_start_time = time.time()
                produce_success = self.produce_request(
                    input_bytes,
                    stream_key,
                    stream_group_key,
                    metadata=frame_metadata,
                    topic=topic,
                )
                write_time = time.time() - write_start_time
                
                # Calculate total process time for current message
                process_time = read_time + write_time
                
                # Update timing data for next message for this stream
                self._update_last_timings(stream_key, read_time, write_time, process_time)

                if produce_success:
                    if strategy == "full":
                        self.frames_sent += 1
                else:
                    logging.warning("Failed to produce to Kafka stream")

                # For non-RTSP streams, maintain desired FPS with time delays
                if not is_rtsp_stream:
                    frame_interval = 1.0 / fps
                    processing_time = time.time() - start_time
                    sleep_time = max(0, frame_interval - processing_time)
                    if sleep_time > 0:
                        time.sleep(sleep_time)

        except Exception as exc:
            logging.error(f"Error in streaming thread: {str(exc)}")
        except KeyboardInterrupt:
            logging.info("Keyboard interrupt, stopping streaming")
        finally:
            if cap is not None:
                cap.release()
                logging.info(f"Released video source: {input}")

    def _construct_input_stream(
        self,
        input_data: bytes,
        metadata: Dict = {},
        stream_key: Optional[str] = None,
        stream_group_key: Optional[str] = None,
        topic: Optional[str] = None,
    ) -> Dict:
        """Construct the input stream dictionary."""
        if not input_data and (metadata or {}).get("transmission_strategy") != "skip":
            logging.error("Input data cannot be empty (except for skip strategy)")
            return {}

        # Compute content payload (optionally strip) and input hash
        if input_data:
            content_value = base64.b64encode(input_data).decode("utf-8")
        else:
            content_value = ""

        if self.strip_input_content:
            # Preserve hash/metadata while omitting payload bytes in message body
            content_value = ""

        stream_info = {
            "broker": self.matrice_stream.config.get('bootstrap_servers', 'localhost:9092'),
            "topic": topic or "default_topic",
            "stream_time": self._get_high_precision_timestamp(),
        }

        input_stream = {
            "ip_key_name": self.service_id,
            "stream_info": stream_info,
            "feed_type": (
                "disk" if metadata.get("stream_type") == "video_file" else "camera"
            ),
            "original_fps": metadata.get("original_fps", metadata.get("fps", 30.0)),
            "stream_fps": metadata.get("fps", 30.0),
            "stream_unit": (
                "segment" if metadata.get("is_video_chunk", False) else "frame"
            ),
            "input_order": self._get_next_input_order(stream_key),
            "frame_count": (
                1
                if not metadata.get("is_video_chunk", False)
                else int(
                    metadata.get("chunk_duration_seconds", 1.0)
                    * metadata.get("fps", 30)
                )
            ),
            "start_frame": metadata.get("start_frame"),
            "end_frame": metadata.get("end_frame"),
            "video_codec": "h265",
            "bw_opt_alg": None,
            "original_resolution": {
                "width": metadata.get("width", 1024),
                "height": metadata.get("height", 1080),
            },
            "stream_resolution": {
                "width": metadata.get("width", 1024),
                "height": metadata.get("height", 1080),
            },
            "camera_info": {
                "camera_name": stream_key,
                "camera_group": stream_group_key,
                "location": metadata.get("camera_location", "Unknown Location")
                },
            "latency_stats": {
                "last_read_time_sec": metadata.get("last_read_time_sec", 0),
                "last_write_time_sec": metadata.get("last_write_time_sec", 0),
                "last_process_time_sec": metadata.get("last_process_time_sec", 0),
            },
            "content": content_value,
            "input_hash": (
                hashlib.md5(input_data, usedforsecurity=False).hexdigest()
                if input_data
                else None
            ),
        }
        # Pass through selected metadata fields to server for intelligent transmission/caching
        passthrough_keys = {
            "transmission_strategy",
            "similarity_score",
            "skip_reason",
            "difference_metadata",
            "video_timestamp",
            "video_properties",
            "frame_sample_rate",
            "is_video_chunk",
            "chunk_duration_seconds",
            "video_format",
            "stream_type",
            "reference_input_hash",
            "last_read_time_sec",
            "last_write_time_sec",
            "last_process_time_sec",
        }
        for k, v in (metadata or {}).items():
            if k in passthrough_keys and v is not None:
                input_stream[k] = v

        return {
            # Globally unique id per frame message across all pipelines
            "frame_id": uuid.uuid4().hex,
            "input_name": f"{input_stream['stream_unit']}_{input_stream['input_order']}",
            "input_unit": input_stream["stream_unit"],
            "input_stream": input_stream,
        }

    def produce_request(
        self,
        input_data: bytes,
        stream_key: Optional[str] = None,
        stream_group_key: Optional[str] = None,
        metadata: Optional[Dict] = None,
        topic: Optional[str] = None,
        timeout: float = 60.0,
    ) -> bool:
        """Simple function to produce a stream request to MatriceStream."""
        try:
            # Use the topic for this stream key, fall back to provided topic, then default
            actual_topic = topic or self.get_topic_for_stream(stream_key) or "default_topic"
            
            message = self._construct_input_stream(
                input_data, metadata or {}, stream_key, stream_group_key, actual_topic
            )
            self.matrice_stream.add_message(
                topic_or_channel=actual_topic, 
                message=message, 
                key=str(stream_key)
            )
            return True
        except Exception as exc:
            logging.error("Failed to produce request: %s", str(exc))
            return False


    async def async_produce_request(
        self,
        input_data: bytes,
        stream_key: Optional[str] = None,
        stream_group_key: Optional[str] = None,
        metadata: Optional[Dict] = None,
        topic: Optional[str] = None,
        timeout: float = 60.0,
    ) -> bool:
        """Produce a unified stream request to MatriceStream asynchronously."""
        try:
            # Use the topic for this stream key, fall back to provided topic, then default
            actual_topic = topic or self.get_topic_for_stream(stream_key) or "default_topic"
            
            message = self._construct_input_stream(
                input_data, metadata or {}, stream_key, stream_group_key, actual_topic
            )
            # Setup async stream if not already setup
            if not self.matrice_stream.is_async_setup():
                await self.matrice_stream.async_setup(actual_topic)
                
            await self.matrice_stream.async_add_message(
                topic_or_channel=actual_topic, 
                message=message, 
                key=str(stream_key)
            )
            return True
        except Exception as exc:
            logging.error(
                "Failed to add request to stream asynchronously: %s", str(exc)
            )
            return False

    def stop_streaming(self) -> None:
        """Stop all streaming threads."""
        self._stop_streaming = True
        for thread in self.streaming_threads:
            if thread.is_alive():
                thread.join(timeout=2.0)
        self.streaming_threads = []
        self._stop_streaming = False
        logging.info("All streaming threads stopped")

    def get_transmission_stats(self) -> Dict[str, Any]:
        """Get intelligent transmission statistics.

        Returns:
            Dictionary with transmission statistics
        """
        total_frames = self.frames_sent + self.frames_skipped + self.frames_diff_sent
        skip_rate = (self.frames_skipped / total_frames) if total_frames > 0 else 0.0
        diff_rate = (self.frames_diff_sent / total_frames) if total_frames > 0 else 0.0
        full_rate = (self.frames_sent / total_frames) if total_frames > 0 else 0.0

        return {
            "frames_sent_full": self.frames_sent,
            "frames_skipped": self.frames_skipped,
            "frames_diff_sent": self.frames_diff_sent,
            "total_frames_processed": total_frames,
            "skip_rate": skip_rate,
            "diff_rate": diff_rate,
            "full_rate": full_rate,
            "bytes_saved": self.bytes_saved,
            "intelligent_transmission_enabled": self.enable_intelligent_transmission,
            "threshold_a": self.threshold_a,
            "threshold_b": self.threshold_b,
            "cached_streams": len(self.txh.frame_cache),
            "latency_stats": {
                "per_stream": {
                    stream_key: {
                        "last_read_time_sec": read_time,
                        "last_write_time_sec": write_time,
                        "last_process_time_sec": process_time,
                    }
                    for stream_key, (read_time, write_time, process_time) in zip(
                        self.last_read_times.keys(),
                        zip(
                            self.last_read_times.values(),
                            self.last_write_times.values(),
                            self.last_process_times.values(),
                        ),
                    )
                },
                "active_streams": list(self.last_read_times.keys()),
            },
        }

    def reset_transmission_stats(self) -> None:
        """Reset transmission statistics."""
        self.frames_sent = 0
        self.frames_skipped = 0
        self.frames_diff_sent = 0
        self.bytes_saved = 0
        # Reset latency statistics for all streams
        self.last_read_times.clear()
        self.last_write_times.clear()
        self.last_process_times.clear()
        # Clear frame cache to prevent memory leaks
        if self.txh:
            self.txh.frame_cache.clear()
            self.txh.last_frame_hashes.clear()
        logging.info("Reset transmission statistics and cleared frame cache")

    def reset_stream_timing_stats(self, stream_key: Optional[str] = None) -> None:
        """Reset timing statistics for a specific stream or all streams."""
        if stream_key is None:
            # Reset all streams
            self.last_read_times.clear()
            self.last_write_times.clear()
            self.last_process_times.clear()
            logging.info("Reset timing statistics for all streams")
        else:
            # Reset specific stream
            key = self._get_stream_key_for_timing(stream_key)
            self.last_read_times.pop(key, None)
            self.last_write_times.pop(key, None)
            self.last_process_times.pop(key, None)
            logging.info(f"Reset timing statistics for stream '{key}'")

    def get_stream_timing_stats(self, stream_key: Optional[str] = None) -> Dict[str, Any]:
        """Get timing statistics for a specific stream."""
        if stream_key is None:
            # Return all streams data
            return {
                "per_stream": {
                    stream_key: {
                        "last_read_time_sec": read_time,
                        "last_write_time_sec": write_time,
                        "last_process_time_sec": process_time,
                    }
                    for stream_key, (read_time, write_time, process_time) in zip(
                        self.last_read_times.keys(),
                        zip(
                            self.last_read_times.values(),
                            self.last_write_times.values(),
                            self.last_process_times.values(),
                        ),
                    )
                },
                "active_streams": list(self.last_read_times.keys()),
            }
        else:
            # Return specific stream data
            read_time, write_time, process_time = self._get_last_timings(stream_key)
            return {
                "stream_key": stream_key or "default",
                "last_read_time_sec": read_time,
                "last_write_time_sec": write_time,
                "last_process_time_sec": process_time,
            }

    async def close(self) -> None:
        """Close all client connections including MatriceStream."""
        errors = []

        # Stop all streaming threads
        try:
            self.stop_streaming()
        except Exception as exc:
            error_msg = f"Error stopping streaming threads: {str(exc)}"
            logging.error(error_msg)
            errors.append(error_msg)

        # Try to close MatriceStream connections
        try:
            await self.matrice_stream.async_close()
            self.matrice_stream.close()
            logging.info("Successfully closed MatriceStream connections")
        except Exception as exc:
            error_msg = f"Error closing MatriceStream connections: {str(exc)}"
            logging.error(error_msg)
            errors.append(error_msg)

        # Report all errors if any occurred
        if errors:
            error_summary = "\n".join(errors)
            logging.error("Errors occurred during close: %s", error_summary)
