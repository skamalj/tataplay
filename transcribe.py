import whisper
import json

# Load Whisper model
model = whisper.load_model("large-v3-turbo")

# Transcribe audio
#audio_path = "separated_audio/htdemucs/media_1_audio/vocals.wav"
audio_path="tataplay2.mp3"
result = model.transcribe(audio_path, language="hi")

# Extract useful data
transcription_data = {
    "text": result["text"],  # Full transcription
    "language": result["language"],  # Detected language
    "segments": [],
}

for segment in result["segments"]:
    transcription_data["segments"].append({
        "start": segment["start"],
        "end": segment["end"],
        "text": segment["text"],
        "confidence": segment.get("confidence", 1.0),  # Confidence score
    })

# Save as JSON
with open("transcription.json", "w", encoding="utf-8") as file:
    json.dump(transcription_data, file, indent=4, ensure_ascii=False)

print(f"Transcription saved to transcription.json (Detected Language: {result['language']})")
