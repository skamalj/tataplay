import json
import librosa
import soundfile as sf
from pyannote.audio.pipelines.speaker_diarization import SpeakerDiarization

# Load the pretrained diarization model
pipeline = SpeakerDiarization.from_pretrained("pyannote/speaker-diarization")

# Define input audio file
audio_file = "tataplay.mp3"

# Run diarization
diarization = pipeline(audio_file)

# Load full audio
audio, sr = librosa.load(audio_file, sr=16000)

# Store speaker info
speaker_data = []

# Process each speaker's segment
for i, (turn, _, speaker) in enumerate(diarization.itertracks(yield_label=True)):
    start_time, end_time = turn.start, turn.end
    segment = audio[int(start_time * sr): int(end_time * sr)]

    # Save extracted speaker audio
    output_file = f"speaker_{speaker}_{i}.wav"
    sf.write(output_file, segment, sr)
    
    # Store timestamp info
    speaker_data.append({
        "speaker": speaker,
        "start_time": start_time,
        "end_time": end_time,
        "audio_file": output_file
    })

# Save speaker mapping to JSON
with open("speaker_data.json", "w") as f:
    json.dump(speaker_data, f, indent=4)

print("🔹 Speaker audio extracted & saved!")
