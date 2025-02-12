import json
from deep_translator import GoogleTranslator

# Load the transcription JSON
with open("transcription.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Translator (Hindi to English)
translator = GoogleTranslator(source="hi", target="en")

# Translate the main text
data["translated_text"] = translator.translate(data["text"])

# Translate each segment
for segment in data["segments"]:
    segment["translated_text"] = translator.translate(segment["text"])

# Save the translated data
with open("translated_transcription.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("🔹 Translation complete! Saved to translated_transcription.json")
