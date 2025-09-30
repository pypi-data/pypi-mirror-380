import json
import re
import threading
import warnings
from pathlib import Path

warnings.filterwarnings("ignore", message="Couldn't find ffmpeg or avconv")

try:
    from .dump import dump  # noqa: F401
except ImportError:
    dump = None


class TTSError(Exception):
    pass


# Voice configuration presets
VOICE_PRESETS = {
    "fast": {
        "rate": 250,
        "description": "Fast speech for quick updates",
    },
    "normal": {
        "rate": 175,
        "description": "Normal speech rate (default)",
    },
    "slow": {
        "rate": 125,
        "description": "Slower speech for detailed explanations",
    },
    "natural": {
        "engine": "gtts",
        "description": "Natural voice using Google TTS (requires internet)",
    },
    "premium": {
        "engine": "openai",
        "voice": "alloy",
        "description": "Premium quality using OpenAI TTS (requires API key)",
    },
}


class SpeakingFilter:
    """Controls what types of messages should be spoken."""

    def __init__(self, config=None):
        """
        Initialize speaking filter.

        Args:
            config: Dict with filter settings or preset name
        """
        # Default: speak everything
        self.speak_confirmations = True
        self.speak_errors = True
        self.speak_warnings = True
        self.speak_assistant = True
        self.speak_tool_output = False  # Usually too verbose
        self.speak_file_ops = True

        if config:
            self.load_config(config)

    def load_config(self, config):
        """Load configuration from dict or preset name."""
        if isinstance(config, str):
            # Load preset
            config = self.get_preset(config)

        if isinstance(config, dict):
            self.speak_confirmations = config.get(
                "confirmations", self.speak_confirmations
            )
            self.speak_errors = config.get("errors", self.speak_errors)
            self.speak_warnings = config.get("warnings", self.speak_warnings)
            self.speak_assistant = config.get("assistant", self.speak_assistant)
            self.speak_tool_output = config.get("tool_output", self.speak_tool_output)
            self.speak_file_ops = config.get("file_ops", self.speak_file_ops)

    @staticmethod
    def get_preset(preset_name):
        """Get speaking filter preset configuration."""
        presets = {
            "all": {
                "confirmations": True,
                "errors": True,
                "warnings": True,
                "assistant": True,
                "tool_output": True,
                "file_ops": True,
            },
            "minimal": {
                "confirmations": True,
                "errors": True,
                "warnings": False,
                "assistant": False,
                "tool_output": False,
                "file_ops": False,
            },
            "important": {
                "confirmations": True,
                "errors": True,
                "warnings": True,
                "assistant": False,
                "tool_output": False,
                "file_ops": False,
            },
            "assistant_only": {
                "confirmations": False,
                "errors": False,
                "warnings": False,
                "assistant": True,
                "tool_output": False,
                "file_ops": False,
            },
            "voice_conversation": {
                "confirmations": True,
                "errors": True,
                "warnings": True,
                "assistant": True,
                "tool_output": False,
                "file_ops": False,
            },
        }
        return presets.get(preset_name, presets["important"])

    def should_speak(self, message_type):
        """Check if a message type should be spoken."""
        type_map = {
            "confirmation": self.speak_confirmations,
            "error": self.speak_errors,
            "warning": self.speak_warnings,
            "assistant": self.speak_assistant,
            "tool_output": self.speak_tool_output,
            "file_op": self.speak_file_ops,
        }
        return type_map.get(message_type, True)

    def to_dict(self):
        """Export filter configuration as dict."""
        return {
            "confirmations": self.speak_confirmations,
            "errors": self.speak_errors,
            "warnings": self.speak_warnings,
            "assistant": self.speak_assistant,
            "tool_output": self.speak_tool_output,
            "file_ops": self.speak_file_ops,
        }


class TextToSpeech:
    """Text-to-speech handler with support for multiple engines."""

    def __init__(
        self,
        engine="gtts",
        enabled=False,
        rate=None,
        voice=None,
        verbose=False,
        preset=None,
        speaking_filter=None,
    ):
        """
        Initialize TextToSpeech.

        Args:
            engine: TTS engine to use ('pyttsx3', 'gtts', 'openai')
            enabled: Whether TTS is enabled
            rate: Speech rate (words per minute for pyttsx3)
            voice: Voice ID to use (engine-specific)
            verbose: Print debug information
            preset: Voice preset name (overrides engine/rate/voice)
            speaking_filter: SpeakingFilter instance or preset name
        """
        # Apply preset if specified
        if preset and preset in VOICE_PRESETS:
            preset_config = VOICE_PRESETS[preset]
            engine = preset_config.get("engine", engine)
            rate = preset_config.get("rate", rate)
            voice = preset_config.get("voice", voice)

        self.engine_name = engine
        self.enabled = enabled
        self.rate = rate
        self.voice = voice
        self.verbose = verbose
        self.engine = None
        self.lock = threading.Lock()
        self.active_threads = []  # Track active speaking threads

        # Initialize speaking filter
        if speaking_filter is None:
            self.filter = SpeakingFilter()
        elif isinstance(speaking_filter, str):
            self.filter = SpeakingFilter(speaking_filter)
        elif isinstance(speaking_filter, SpeakingFilter):
            self.filter = speaking_filter
        else:
            self.filter = SpeakingFilter(speaking_filter)

        if self.enabled:
            self._initialize_engine()

    def _initialize_engine(self):
        """Initialize the selected TTS engine."""
        try:
            if self.engine_name == "gtts":
                self._init_gtts()
            elif self.engine_name == "openai":
                self._init_openai()
            else:
                raise TTSError(f"Unknown TTS engine: {self.engine_name}")
        except Exception as e:
            if self.verbose:
                print(f"Failed to initialize TTS engine '{self.engine_name}': {e}")
            self.enabled = False
            raise TTSError(f"Failed to initialize TTS: {e}")


    def _init_gtts(self):
        """Initialize gTTS (Google Text-to-Speech)."""
        try:
            import gtts  # noqa: F401

            self.gtts = gtts
            if self.verbose:
                print("gTTS initialized (requires internet connection)")
        except ImportError:
            raise TTSError("gTTS not installed. Install with: pip install gtts")

    def _init_openai(self):
        """Initialize OpenAI TTS."""
        try:
            from openai import OpenAI

            self.openai_client = OpenAI()
            if self.verbose:
                print("OpenAI TTS initialized")
        except ImportError:
            raise TTSError("OpenAI not installed. Install with: pip install openai")
        except Exception as e:
            raise TTSError(f"OpenAI TTS initialization failed: {e}")

    def _clean_text(self, text):
        """Clean text for better TTS output."""
        # Remove markdown formatting
        text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)  # Bold
        text = re.sub(r"\*(.+?)\*", r"\1", text)  # Italic
        text = re.sub(r"`(.+?)`", r"\1", text)  # Inline code
        text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)  # Code blocks

        # Remove URLs (just say "link")
        text = re.sub(r"https?://\S+", "link", text)

        # Clean up excessive whitespace
        text = re.sub(r"\s+", " ", text)

        return text.strip()

    def _summarize_text(self, text, max_length=200):
        """
        Summarize long text for speech.
        Uses OpenRouter with grok-4-fast to summarize if API key is available.
        Otherwise, it truncates.
        """
        cleaned = self._clean_text(text)
        if len(cleaned) <= max_length:
            return cleaned

        def truncate_text():
            # Simple truncation fallback
            truncated = cleaned[:max_length]
            last_period = truncated.rfind(".")
            last_question = truncated.rfind("?")
            last_exclamation = truncated.rfind("!")

            cut_point = max(last_period, last_question, last_exclamation)
            if cut_point > max_length * 0.6:  # If we found a good break point
                return truncated[: cut_point + 1]
            else:
                return truncated.rsplit(" ", 1)[0] + "..."

        import os
        try:
            from openai import OpenAI
        except ImportError:
            if self.verbose:
                print("OpenAI not installed, falling back to truncation for summarization.")
            return truncate_text()

        api_key = os.environ.get("OPENROUTER_API_KEY")
        if not api_key:
            return truncate_text()

        try:
            client = OpenAI(
                api_key=api_key,
                base_url="https://openrouter.ai/api/v1",
            )

            prompt = f"Summarize the following text in a single, short sentence (less than {max_length} characters) to be spoken aloud. Be concise and natural sounding. Here is the text:\n\n{cleaned}"

            response = client.chat.completions.create(
                model="x-ai/grok-4-fast:free",
                messages=[
                    {"role": "system", "content": "You are a summarization assistant for a text-to-speech system."},
                    {"role": "user", "content": prompt},
                ],
                max_tokens=100,
                temperature=0.5,
            )
            summary = response.choices[0].message.content.strip()
            # Ensure summary is not empty
            if summary:
                return summary
            else:
                return truncate_text()
        except Exception as e:
            if self.verbose:
                print(f"Failed to summarize text with OpenRouter: {e}")
            
            return truncate_text()

    def speak(
        self,
        text,
        priority="normal",
        summarize=False,
        max_length=200,
        message_type=None,
    ):
        """
        Speak the given text.

        Args:
            text: Text to speak
            priority: 'high' (always speak), 'normal' (speak if enabled), 'low' (only if verbose)
            summarize: If True, summarize long text before speaking
            max_length: Maximum length for summarization
            message_type: Type of message (confirmation, error, warning, assistant, tool_output, file_op)
        """
        if not self.enabled:
            return

        if not text or not text.strip():
            return

        # Check speaking filter
        if message_type and not self.filter.should_speak(message_type):
            return

        # Handle priority filtering
        if priority == "low" and not self.verbose:
            return

        # Clean and optionally summarize text
        if summarize:
            speech_text = self._summarize_text(text, max_length)
        else:
            speech_text = self._clean_text(text)

        if not speech_text:
            return

        # Speak in a separate thread to avoid blocking
        thread = threading.Thread(target=self._speak_sync_wrapper, args=(speech_text,))
        thread.daemon = True
        self.active_threads.append(thread)
        thread.start()

    def _speak_sync_wrapper(self, text):
        """Wrapper for _speak_sync that removes thread from active list when done."""
        try:
            self._speak_sync(text)
        finally:
            # Remove this thread from active threads
            current_thread = threading.current_thread()
            if current_thread in self.active_threads:
                self.active_threads.remove(current_thread)

    def _speak_sync(self, text):
        """Synchronously speak text (called in thread)."""
        with self.lock:
            try:
                if self.engine_name == "gtts":
                    self._speak_gtts(text)
                elif self.engine_name == "openai":
                    self._speak_openai(text)
            except Exception as e:
                if self.verbose:
                    print(f"TTS error: {e}")

    def wait_for_speech_completion(self, timeout=30.0):
        """Wait for all active speech threads to complete.

        Args:
            timeout: Maximum time to wait in seconds (default: 30.0)
        """
        import time
        start_time = time.time()

        while self.active_threads:
            # Check timeout
            if time.time() - start_time > timeout:
                break

            # Join threads with short timeout
            for thread in list(self.active_threads):
                if thread.is_alive():
                    thread.join(timeout=0.1)
                else:
                    if thread in self.active_threads:
                        self.active_threads.remove(thread)

            # Small sleep to avoid busy waiting
            if self.active_threads:
                time.sleep(0.1)

    def _speak_gtts(self, text):
        """Speak using gTTS."""
        import os
        import sys
        import tempfile
        import subprocess

        from pydub import AudioSegment
        from pydub.effects import speedup
        from pydub.playback import play

        # Suppress ffmpeg logs more aggressively
        old_stderr = sys.stderr
        old_stdout = sys.stdout
        devnull = None
        try:
            devnull = open(os.devnull, 'w')
            sys.stderr = devnull
            sys.stdout = devnull

            # Also set environment variable to suppress ffmpeg logs
            old_loglevel = os.environ.get('FFREPORT')
            os.environ['FFREPORT'] = 'level=-8'

            # Create temporary file
            with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as fp:
                temp_file = fp.name

            try:
                # Generate speech
                tts = self.gtts.gTTS(text=text, lang="en")
                tts.save(temp_file)

                # Play audio with suppressed output
                sound = AudioSegment.from_mp3(temp_file)

                if self.rate:
                    speed_factor = self.rate / 175.0  # Assuming 175 WPM is normal
                    if speed_factor > 0 and speed_factor != 1.0:
                        sound = speedup(sound, playback_speed=speed_factor)

                play(sound)
            finally:
                try:
                    os.unlink(temp_file)
                except Exception:
                    pass
                # Restore environment variable
                if old_loglevel is not None:
                    os.environ['FFREPORT'] = old_loglevel
                elif 'FFREPORT' in os.environ:
                    del os.environ['FFREPORT']
        finally:
            sys.stderr = old_stderr
            sys.stdout = old_stdout
            if devnull:
                devnull.close()

    def _speak_openai(self, text):
        """Speak using OpenAI TTS."""
        import os
        import sys
        import tempfile

        from pydub import AudioSegment
        from pydub.playback import play

        # Suppress ffmpeg logs more aggressively
        old_stderr = sys.stderr
        old_stdout = sys.stdout
        devnull = None
        try:
            devnull = open(os.devnull, 'w')
            sys.stderr = devnull
            sys.stdout = devnull

            # Also set environment variable to suppress ffmpeg logs
            old_loglevel = os.environ.get('FFREPORT')
            os.environ['FFREPORT'] = 'level=-8'

            with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as fp:
                temp_file = fp.name

            try:
                response = self.openai_client.audio.speech.create(
                    model="tts-1",
                    voice=self.voice or "alloy",
                    input=text,
                )

                response.stream_to_file(temp_file)

                # Play audio with suppressed output
                sound = AudioSegment.from_mp3(temp_file)
                play(sound)
            finally:
                try:
                    os.unlink(temp_file)
                except Exception:
                    pass
                # Restore environment variable
                if old_loglevel is not None:
                    os.environ['FFREPORT'] = old_loglevel
                elif 'FFREPORT' in os.environ:
                    del os.environ['FFREPORT']
        finally:
            sys.stderr = old_stderr
            sys.stdout = old_stdout
            if devnull:
                devnull.close()



class StreamingTTS:
    """Manages real-time TTS during text streaming.

    Buffers incoming text chunks, detects complete sentences, and speaks them
    immediately via a background worker thread for non-blocking operation.
    """

    def __init__(self, tts_engine, delay=0.0, chunk_sentences=1):
        """Initialize streaming TTS.

        Args:
            tts_engine: TextToSpeech instance to use for speaking
            delay: Optional delay in seconds before speaking each sentence
            chunk_sentences: Number of sentences to accumulate before speaking
        """
        self.tts = tts_engine
        self.buffer = ""  # Accumulates chunks
        self.spoken_text = ""  # Track what's been spoken
        self.delay = delay
        self.chunk_sentences = max(1, chunk_sentences)  # Minimum 1
        self.active = False
        self.speaking_thread = None

        # Use queue for thread-safe communication
        import queue
        self.queue = queue.Queue()

        # Track if we're inside a code block
        self.in_code_block = False
        self.code_fence_count = 0

        # Sentence chunking buffer
        self.sentence_chunk_buffer = []

    def start(self):
        """Start the streaming TTS background worker."""
        if self.active:
            return

        self.active = True
        self.buffer = ""
        self.spoken_text = ""
        self.in_code_block = False
        self.code_fence_count = 0
        self.sentence_chunk_buffer = []

        # Start background worker thread
        self.speaking_thread = threading.Thread(target=self._speaking_worker, daemon=True)
        self.speaking_thread.start()

    def stop(self):
        """Stop the streaming TTS and clean up."""
        if not self.active:
            return

        self.active = False
        # Send shutdown signal
        self.queue.put(None)

        if self.speaking_thread and self.speaking_thread.is_alive():
            self.speaking_thread.join(timeout=2.0)

    def add_chunk(self, text_chunk):
        """Add new text chunk, detect & speak complete sentences.

        Args:
            text_chunk: New text chunk from LLM stream
        """
        if not self.active or not text_chunk:
            return

        self.buffer += text_chunk

        # Track code blocks (triple backticks)
        self.code_fence_count += text_chunk.count("```")
        self.in_code_block = (self.code_fence_count % 2) == 1

        # Don't speak code content
        if self.in_code_block:
            return

        # Extract complete sentences
        sentences = self._extract_complete_sentences()

        for sentence in sentences:
            # Clean sentence
            cleaned = self._clean_sentence_for_speech(sentence)
            if cleaned.strip():
                # Add to chunk buffer
                self.sentence_chunk_buffer.append(cleaned)
                self.spoken_text += sentence
                # Remove spoken part from buffer
                self.buffer = self.buffer[len(sentence):].lstrip()

                # Speak when we have enough sentences
                if len(self.sentence_chunk_buffer) >= self.chunk_sentences:
                    combined = " ".join(self.sentence_chunk_buffer)
                    self.queue.put(combined)
                    self.sentence_chunk_buffer = []

    def finalize(self):
        """Speak any remaining buffered text and stop."""
        if not self.active:
            return

        # Speak any accumulated chunks
        if self.sentence_chunk_buffer:
            combined = " ".join(self.sentence_chunk_buffer)
            self.queue.put(combined)
            self.sentence_chunk_buffer = []

        # Speak remaining buffer if it's not code
        if self.buffer.strip() and not self.in_code_block:
            cleaned = self._clean_sentence_for_speech(self.buffer)
            if cleaned.strip():
                self.queue.put(cleaned)
                self.spoken_text += self.buffer
                self.buffer = ""

        self.stop()

        # Wait for all TTS threads to complete
        if self.tts:
            self.tts.wait_for_speech_completion()

    def _extract_complete_sentences(self):
        """Extract complete sentences from buffered text.

        Returns:
            List of complete sentences
        """
        sentences = []

        # Pattern: Match text ending with . ! ? followed by space/capital/newline
        # Use lookahead to not consume the next character
        pattern = r'([^.!?]*[.!?])(?=\s+[A-Z\n]|\s*$)'

        for match in re.finditer(pattern, self.buffer):
            sentence = match.group(1)

            # Check if this is a real sentence boundary
            if self._is_sentence_boundary(sentence):
                sentences.append(sentence)

        return sentences

    def _is_sentence_boundary(self, text):
        """Check if punctuation marks a true sentence boundary.

        Args:
            text: Text to check

        Returns:
            True if this is a sentence boundary, False for abbreviations/decimals
        """
        text = text.strip()

        # Exclude common abbreviations
        false_endings = ['Dr.', 'Mr.', 'Mrs.', 'Ms.', 'Prof.',
                        'e.g.', 'i.e.', 'etc.', 'vs.', 'Inc.',
                        'U.S.', 'U.K.', 'Ph.D.', 'M.D.']

        for ending in false_endings:
            if text.endswith(ending):
                return False

        # Check for decimal numbers (e.g., "3.14")
        if re.search(r'\d+\.\d*$', text):
            return False

        # Check for file extensions or version numbers
        if re.search(r'\.\w+$', text) and len(text.split('.')[-1]) <= 4:
            # Could be .txt, .py, v1.0, etc.
            if not text[-1].isupper():  # Not likely a sentence if lowercase ending
                return False

        # Minimum length check (avoid single-letter abbreviations)
        if len(text) < 10:
            return False

        return True

    def _clean_sentence_for_speech(self, sentence):
        """Clean sentence for speech by removing markdown and code.

        Args:
            sentence: Raw sentence text

        Returns:
            Cleaned text suitable for speech
        """
        # Remove markdown formatting
        sentence = re.sub(r'\*\*(.+?)\*\*', r'\1', sentence)  # Bold
        sentence = re.sub(r'\*(.+?)\*', r'\1', sentence)  # Italic
        sentence = re.sub(r'`(.+?)`', r'\1', sentence)  # Inline code

        # Replace URLs with "link"
        sentence = re.sub(r'https?://\S+', 'link', sentence)

        # Remove markdown headers
        sentence = re.sub(r'^#+\s+', '', sentence)

        # Clean up excessive whitespace
        sentence = re.sub(r'\s+', ' ', sentence)

        return sentence.strip()

    def _speaking_worker(self):
        """Background thread that speaks queued sentences."""
        import time

        while self.active:
            try:
                # Get next sentence (with timeout to check active flag)
                sentence = self.queue.get(timeout=0.1)

                if sentence is None:  # Shutdown signal
                    break

                # Optional delay between sentences
                if self.delay > 0:
                    time.sleep(self.delay)

                # Speak the sentence
                if sentence.strip() and self.tts and self.tts.enabled:
                    # Use normal priority, no summarization (already sentence-sized)
                    self.tts.speak(
                        sentence,
                        priority="normal",
                        summarize=False,
                        message_type="assistant"
                    )

            except Exception:
                # Queue.get timeout or other error - continue
                continue


if __name__ == "__main__":
    # Simple test
    tts = TextToSpeech(engine="pyttsx3", enabled=True, verbose=True)
    tts.speak("Hello! This is a test of the text to speech system.", priority="high")
    print("Test complete")
