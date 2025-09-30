"""Ollama client for transcript enhancement."""

import logging
from typing import Any

from ..constants import TRANSCRIPTION

logger = logging.getLogger(__name__)


class OllamaClient:
    """Handles communication with Ollama service for transcript enhancement."""

    def __init__(self, host: str = None, port: int = None) -> None:
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.host = host or TRANSCRIPTION["ollama"]["default_host"]
        self.port = port or TRANSCRIPTION["ollama"]["default_port"]
        self.base_url = f"http://{self.host}:{self.port}"
        self.timeout = TRANSCRIPTION["ollama"]["timeout_seconds"]
        self.connection_timeout = TRANSCRIPTION["ollama"]["connection_timeout"]

    async def check_connection(self) -> dict[str, Any]:
        """Check Ollama connection and get available models."""
        try:
            # Import httpx only when needed (optional dependency)
            import httpx

            async with httpx.AsyncClient(timeout=self.connection_timeout) as client:
                response = await client.get(f"{self.base_url}/api/tags")
                if response.status_code != 200:
                    raise ConnectionError(f"HTTP {response.status_code}")

                models_data = response.json()
                models = [model["name"] for model in models_data.get("models", [])]

                # Find best available model
                preferred = TRANSCRIPTION["ollama"]["preferred_models"]
                selected_model = None

                for model in preferred:
                    if model in models:
                        selected_model = model
                        break

                if not selected_model and models:
                    selected_model = models[0]  # Fallback to first available

                logger.info(f"Connected to Ollama at {self.host}:{self.port}")
                logger.info(f"Available models: {', '.join(models)}")
                if selected_model:
                    logger.info(f"Selected model: {selected_model}")

                return {
                    "connected": True,
                    "models": models,
                    "selected_model": selected_model,
                }

        except ImportError:
            logger.warning("httpx not available - install with: uv add httpx")
            return {"connected": False, "models": [], "selected_model": None}
        except Exception as e:
            logger.warning(f"Cannot connect to Ollama: {e}")
            return {"connected": False, "models": [], "selected_model": None}

    async def enhance_transcript(
        self, text: str, model_name: str, domain_context: str = "general"
    ) -> str | None:
        """Enhance transcript using Ollama for better formatting and clarity."""
        try:
            # Import httpx only when needed
            import httpx

            prompt = self._build_enhancement_prompt(text, domain_context)

            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.base_url}/api/generate",
                    json={
                        "model": model_name,
                        "prompt": prompt,
                        "stream": False,
                        "options": {
                            "temperature": TRANSCRIPTION["ollama"]["temperature"],
                            "top_p": TRANSCRIPTION["ollama"]["top_p"],
                            "max_tokens": TRANSCRIPTION["ollama"]["max_tokens"],
                        },
                    },
                )

                if response.status_code == 200:
                    result = response.json()
                    enhanced_text = result.get("response", "").strip()

                    min_length = TRANSCRIPTION["ollama"]["enhancement_min_length"]
                    if enhanced_text and len(enhanced_text) > min_length:
                        return enhanced_text
                    else:
                        logger.warning(
                            "Ollama enhancement produced short result, using original"
                        )
                        return text
                else:
                    logger.error(f"Ollama API error: {response.status_code}")
                    return None

        except ImportError:
            logger.warning("httpx not available for Ollama integration")
            return text
        except Exception as e:
            logger.error(f"Ollama enhancement failed: {e}")
            return text

    def _build_enhancement_prompt(self, text: str, domain_context: str) -> str:
        """Build enhancement prompt based on domain context."""
        if domain_context == "technical":
            context_instructions = """
The transcript may contain:
- Technical terms and specifications
- Step-by-step instructions
- Tool names and procedures
- Measurement specifications
- Industry-specific terminology
"""
        elif domain_context == "educational":
            context_instructions = """
The transcript may contain:
- Educational content and explanations
- Q&A sessions or discussions
- Academic or professional terminology
- Instructional sequences
"""
        else:
            context_instructions = """
The transcript contains general spoken content that may include:
- Conversational language
- Various topics and discussions
- Mixed formal and informal speech
"""

        return f"""Please clean up and enhance this video transcript for better readability.

{context_instructions}

Please:
1. Fix grammar and punctuation
2. Format as clear, readable sentences
3. Maintain all specific terms, measurements, and technical details exactly as spoken
4. Add appropriate paragraph breaks for different topics/sections
5. Keep the original tone and meaning
6. Do NOT add information that wasn't in the original transcript
7. Remove filler words (um, uh, etc.) but preserve natural speech patterns

Raw transcript:
{text}

Enhanced transcript:"""
