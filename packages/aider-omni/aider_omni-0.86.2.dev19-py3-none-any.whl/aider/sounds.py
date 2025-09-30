import threading
import warnings
from pathlib import Path

warnings.filterwarnings("ignore", message="Couldn't find ffmpeg or avconv")

try:
    from pydub import AudioSegment
    from pydub.playback import play
except ImportError:
    AudioSegment = None
    play = None

class SoundEffects:
    """A class to handle playing sound effects for different events."""

    def __init__(self, enabled=True, verbose=False, sounds_dir="sounds"):
        """
        Initialize SoundEffects.

        Args:
            enabled (bool): Whether sound effects are enabled.
            verbose (bool): Print debug information.
            sounds_dir (str): Directory where sound files are located.
        """
        self.enabled = enabled
        self.verbose = verbose
        self.lock = threading.Lock()
        self.sounds_dir = Path(sounds_dir)

        self.sound_map = {
            "start": "start.mp3",
            "success": "success.mp3",
            "failure": "failure.mp3",
            "message": "message.mp3",
            "tool_call": "tool_call.mp3",
        }

        if self.enabled and not play:
            if self.verbose:
                print("pydub not installed. Sound effects will be disabled. Install with: pip install pydub")
            self.enabled = False

    def play(self, event):
        """
        Play a sound effect for a given event.

        Args:
            event (str): The name of the event.
        """
        if not self.enabled or event not in self.sound_map:
            return

        sound_file = self.sounds_dir / self.sound_map[event]
        
        thread = threading.Thread(target=self._play_sync, args=(sound_file,))
        thread.daemon = True
        thread.start()

    def _play_sync(self, sound_file):
        """Synchronously play a sound file."""
        import os
        import sys

        with self.lock:
            try:
                if self.verbose:
                    print(f"Playing sound: {sound_file}")

                # Suppress ffmpeg logs
                old_stderr = sys.stderr
                old_stdout = sys.stdout
                devnull = None
                try:
                    devnull = open(os.devnull, 'w')
                    sys.stderr = devnull
                    sys.stdout = devnull

                    # Set environment variable to suppress ffmpeg logs
                    old_loglevel = os.environ.get('FFREPORT')
                    os.environ['FFREPORT'] = 'level=-8'

                    # Assumes mp3, could be extended to handle other formats based on extension
                    sound = AudioSegment.from_file(sound_file)
                    play(sound)
                finally:
                    sys.stderr = old_stderr
                    sys.stdout = old_stdout
                    if devnull:
                        devnull.close()
                    # Restore environment variable
                    if old_loglevel is not None:
                        os.environ['FFREPORT'] = old_loglevel
                    elif 'FFREPORT' in os.environ:
                        del os.environ['FFREPORT']

            except FileNotFoundError:
                if self.verbose:
                    print(f"Sound file not found: {sound_file}")
            except Exception as e:
                if self.verbose:
                    print(f"Error playing sound {sound_file}: {e}")

if __name__ == "__main__":
    # This is a simple test that will likely fail if sound files are not present.
    print("Testing sound effects...")
    # Assuming you run this from the project root, and there's a 'sounds' dir.
    sfx = SoundEffects(enabled=True, verbose=True)
    
    sfx.play("start")
    sfx.play("success")
    
    import time
    time.sleep(2) # Give sounds time to play
    print("Test complete.")
