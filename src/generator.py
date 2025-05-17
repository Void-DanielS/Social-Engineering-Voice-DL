import argparse
import os
import sys
from pathlib import Path
from pydub import AudioSegment
from scipy.io.wavfile import write
import numpy as np

# Agregar el módulo tortoise manualmente al path
sys.path.append(os.path.abspath("tortoise-tts"))

from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_voice

# Rutas base
OUTPUT_FOLDER = "output"
VOICES_FOLDER = "tortoise-tts/voices"

def prepare_voice_clips(input_audio_path, voice_name):
    print(f"[+] Preparando voz personalizada: {voice_name}")
    
    # Crear carpeta de voz si no existe
    voice_path = os.path.join(VOICES_FOLDER, voice_name)
    os.makedirs(voice_path, exist_ok=True)

    # Cargar y convertir audio
    audio = AudioSegment.from_file(input_audio_path)
    audio = audio.set_channels(1).set_frame_rate(22050).set_sample_width(2)

    # Cortar en clips de 5 segundos
    clip_length_ms = 5000
    chunks = [audio[i:i + clip_length_ms] for i in range(0, len(audio), clip_length_ms)]

    print(f"[+] Cortando audio en {len(chunks)} clips...")

    for idx, chunk in enumerate(chunks[:5]):  # máx 5 clips
        clip_filename = os.path.join(voice_path, f"{idx+1}.wav")
        chunk.export(clip_filename, format="wav")
        print(f"[✔] Clip {idx+1} guardado en {clip_filename}")

def generate_audio(text, voice_name, output_filename):
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    print(f"[+] Generando deepfake con voz: {voice_name}")
    
    # Iniciar Tortoise
    tts = TextToSpeech()

    # Cargar voz personalizada
    voices_path = [os.path.abspath(VOICES_FOLDER)]
    try:
        voice_samples, conditioning_latents = load_voice(voice_name, voices_path)
    except KeyError:
        print(f"[!] No se encontró la voz '{voice_name}'. Usando voz aleatoria.")
        voice_samples, conditioning_latents = None, None
        voice_name = "random"

    # Generar audio con voz clonada o random
    audio = tts.tts(text, voice_samples=voice_samples, conditioning_latents=conditioning_latents)

    # Guardar resultado manualmente
    output_path = os.path.join(OUTPUT_FOLDER, output_filename)
    audio_numpy = audio.cpu().numpy()
    write(output_path, 24000, audio_numpy)
    print(f"[✔] Deepfake generado en: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clonador de voz con deepfake usando audio real")
    parser.add_argument("--audio", type=str, required=True, help="Ruta del archivo de audio real (ej: audios/dani.wav)")
    parser.add_argument("--text", type=str, required=True, help="Texto que dirá el deepfake")
    parser.add_argument("--name", type=str, required=True, help="Nombre de la voz personalizada (carpeta)")
    parser.add_argument("--output", type=str, default="deepfake.wav", help="Archivo de salida .wav")

    args = parser.parse_args()

    prepare_voice_clips(args.audio, args.name)
    generate_audio(args.text, args.name, args.output)
