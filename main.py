import whisper
from tqdm import tqdm

#configurações
VIDEO_PATH = "video.mp4"
OUTPUT_TXT = "transcription.txt"
MODEL_NAME = "small" 

# carregar o modelo 
model = whisper.load_model(MODEL_NAME).to("cuda")

print(f"[INFO] Transcrevendo '{VIDEO_PATH}' com modelo '{MODEL_NAME}'...\n")

result = model.transcribe(
    VIDEO_PATH,
    verbose=True,
    fp16=False,
    word_timestamps= False)

# mostra o texto completo:
print("\n[TRANSCRIÇÃO COMPLETA]\n")
print(result["text"])

# salvar a transcrição em um arquivo de texto
with open(OUTPUT_TXT, "w", encoding="utf-8") as f:
    for seg in tqdm (result["segments"], desc="Salvando transcrição"):
        start = seg["start"]
        end = seg["end"]
        text = seg["text"].strip()
        f.write(f"[{start:.2f} --> {end:.2f}] {text}\n")
        print(f"\n[INFO] Transcrição salva em '{OUTPUT_TXT}'")