from TTS.api import TTS
import torch
from TTS.tts.configs.xtts_config import XttsConfig

# Load XTTS model
torch.serialization.add_safe_globals([XttsConfig])
tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False).to("cpu")

# Reference audio (original speaker in any language)
reference_audio = "speaker_SPEAKER_01_0.wav"

# Generate speech in Hindi using the speaker's voice style
tts.tts_to_file(
    text="Geeta ji, Tata Sky becoming Tata Play is a very historical moment.",
    file_path="output_english.wav",
    speaker_wav=reference_audio,
    language="en"
)
