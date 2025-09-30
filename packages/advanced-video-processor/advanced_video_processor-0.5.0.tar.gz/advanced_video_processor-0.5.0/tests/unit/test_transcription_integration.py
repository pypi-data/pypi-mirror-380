"""Test transcription integration with VideoProcessor."""

from pathlib import Path
from unittest.mock import Mock, patch

from video_processor.ai.models import TranscriptionResult
from video_processor.config import ProcessorConfig
from video_processor.core.processor import VideoProcessor


class TestTranscriptionIntegration:
    """Test transcription integration with the main video processor."""

    def test_processor_initialization_without_transcription(self):
        """Test processor initializes correctly without transcription."""
        config = ProcessorConfig(
            base_path=Path("/tmp/test"),
            enable_transcription=False,
        )
        processor = VideoProcessor(config)
        assert processor.transcriber is None

    def test_processor_initialization_with_transcription_disabled_by_default(self):
        """Test processor has transcription disabled by default."""
        config = ProcessorConfig(base_path=Path("/tmp/test"))
        processor = VideoProcessor(config)
        assert processor.transcriber is None

    def test_processor_initialization_with_transcription_enabled(self):
        """Test processor initializes transcriber when enabled."""
        config = ProcessorConfig(
            base_path=Path("/tmp/test"),
            enable_transcription=True,
        )
        processor = VideoProcessor(config)
        assert processor.transcriber is not None
        assert hasattr(processor.transcriber, "transcribe_video")

    @patch("video_processor.core.processor.VideoMetadata")
    @patch("video_processor.core.processor.ThumbnailGenerator")
    @patch("video_processor.core.processor.VideoEncoder")
    @patch("video_processor.core.processor.LocalStorageBackend")
    def test_transcription_config_parameters(
        self, mock_storage, mock_encoder, mock_thumbnails, mock_metadata
    ):
        """Test transcription configuration parameters are passed correctly."""
        config = ProcessorConfig(
            base_path=Path("/tmp/test"),
            enable_transcription=True,
            whisper_model="small",
            ollama_host="custom-host",
            ollama_port=8888,
            transcription_domain_context="technical",
        )
        processor = VideoProcessor(config)

        assert processor.transcriber is not None
        # Verify the transcriber was initialized with the correct Ollama settings
        assert processor.transcriber.ollama_client.host == "custom-host"
        assert processor.transcriber.ollama_client.port == 8888

    @patch("video_processor.core.processor.VideoMetadata")
    @patch("video_processor.core.processor.ThumbnailGenerator")
    @patch("video_processor.core.processor.VideoEncoder")
    @patch("video_processor.core.processor.LocalStorageBackend")
    @patch("asyncio.get_event_loop")
    def test_process_video_with_transcription_success(
        self, mock_get_loop, mock_storage, mock_encoder, mock_thumbnails, mock_metadata
    ):
        """Test video processing with successful transcription."""
        # Mock the async event loop
        mock_loop = Mock()
        mock_get_loop.return_value = mock_loop

        # Create mock transcription result
        mock_transcription_result = Mock(spec=TranscriptionResult)
        mock_transcription_result.video_path = Path("/test/video.mp4")
        mock_transcription_result.language = "en"
        mock_transcription_result.duration = 60.0

        mock_loop.run_until_complete.return_value = mock_transcription_result

        # Mock storage backend
        mock_storage_instance = Mock()
        mock_storage_instance.create_directory.return_value = None
        mock_storage.return_value = mock_storage_instance

        # Mock encoder
        mock_encoder_instance = Mock()
        mock_encoder_instance.encode_video.return_value = Path("/output/video.mp4")
        mock_encoder.return_value = mock_encoder_instance

        # Mock thumbnail generator
        mock_thumbnail_instance = Mock()
        mock_thumbnail_instance.generate_thumbnail.return_value = Path("/output/thumb.jpg")
        mock_thumbnail_instance.generate_sprites.return_value = (
            Path("/output/sprites.jpg"),
            Path("/output/sprites.vtt")
        )
        mock_thumbnails.return_value = mock_thumbnail_instance

        # Mock metadata extractor
        mock_metadata_instance = Mock()
        mock_metadata_instance.extract_metadata.return_value = {
            "duration": 60.0,
            "video_360": {"is_360_video": False}
        }
        mock_metadata.return_value = mock_metadata_instance

        config = ProcessorConfig(
            base_path=Path("/tmp/test"),
            enable_transcription=True,
        )
        processor = VideoProcessor(config)

        # Mock the transcriber's save method
        processor.transcriber.save_transcription_results = Mock(
            return_value=(Path("/output/transcript.json"), Path("/output/transcript.txt"))
        )

        # Create a mock input file
        input_path = Path("/test/input.mp4")

        with patch("pathlib.Path.exists", return_value=True):
            result = processor.process_video(input_path)

        # Verify transcription was called and results included
        assert result.transcription_json == Path("/output/transcript.json")
        assert result.transcription_text == Path("/output/transcript.txt")
        mock_loop.run_until_complete.assert_called_once()
        processor.transcriber.save_transcription_results.assert_called_once_with(
            mock_transcription_result, result.output_path
        )

    @patch("video_processor.core.processor.VideoMetadata")
    @patch("video_processor.core.processor.ThumbnailGenerator")
    @patch("video_processor.core.processor.VideoEncoder")
    @patch("video_processor.core.processor.LocalStorageBackend")
    def test_process_video_transcription_failure_graceful(
        self, mock_storage, mock_encoder, mock_thumbnails, mock_metadata
    ):
        """Test video processing continues gracefully when transcription fails."""
        # Mock storage backend
        mock_storage_instance = Mock()
        mock_storage_instance.create_directory.return_value = None
        mock_storage.return_value = mock_storage_instance

        # Mock encoder
        mock_encoder_instance = Mock()
        mock_encoder_instance.encode_video.return_value = Path("/output/video.mp4")
        mock_encoder.return_value = mock_encoder_instance

        # Mock thumbnail generator
        mock_thumbnail_instance = Mock()
        mock_thumbnail_instance.generate_thumbnail.return_value = Path("/output/thumb.jpg")
        mock_thumbnail_instance.generate_sprites.return_value = (
            Path("/output/sprites.jpg"),
            Path("/output/sprites.vtt")
        )
        mock_thumbnails.return_value = mock_thumbnail_instance

        # Mock metadata extractor
        mock_metadata_instance = Mock()
        mock_metadata_instance.extract_metadata.return_value = {
            "duration": 60.0,
            "video_360": {"is_360_video": False}
        }
        mock_metadata.return_value = mock_metadata_instance

        config = ProcessorConfig(
            base_path=Path("/tmp/test"),
            enable_transcription=True,
        )
        processor = VideoProcessor(config)

        # Mock transcription to raise an exception
        with patch("asyncio.get_event_loop") as mock_get_loop:
            mock_loop = Mock()
            mock_get_loop.return_value = mock_loop
            mock_loop.run_until_complete.side_effect = Exception("Transcription failed")

            input_path = Path("/test/input.mp4")

            with patch("pathlib.Path.exists", return_value=True):
                result = processor.process_video(input_path)

            # Verify processing succeeded despite transcription failure
            assert result.transcription_json is None
            assert result.transcription_text is None
            assert result.encoded_files  # Video processing should still work
            assert result.thumbnails  # Thumbnail generation should still work

    def test_transcription_constants_integration(self):
        """Test that transcription constants are properly integrated."""
        from video_processor.constants import TRANSCRIPTION

        # Verify key transcription constants exist
        assert "whisper_models" in TRANSCRIPTION
        assert "ollama" in TRANSCRIPTION
        assert "audio_extraction" in TRANSCRIPTION

        # Verify whisper model configurations
        assert "base" in TRANSCRIPTION["whisper_models"]
        assert "accuracy" in TRANSCRIPTION["whisper_models"]["base"]

        # Verify ollama configurations
        assert "default_host" in TRANSCRIPTION["ollama"]
        assert "default_port" in TRANSCRIPTION["ollama"]

        # Verify audio extraction settings
        assert "sample_rate" in TRANSCRIPTION["audio_extraction"]
        assert TRANSCRIPTION["audio_extraction"]["sample_rate"] == 16000
