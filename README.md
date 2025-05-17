# 🧠🎙️ Deepfake Voice Cloner - Social Engineering Toolkit

Este proyecto permite clonar la voz de una persona a partir de un solo archivo de audio real. Utiliza [Tortoise TTS](https://github.com/neonbjb/tortoise-tts), un modelo de síntesis de voz basado en difusión, para generar audios artificiales con la voz clonada.

---

## ⚙️ Características

- 🎧 Convierte un archivo de audio real (.wav, .m4a, etc.) en múltiples clips
- 🧠 Usa Tortoise TTS para generar una voz clonada desde cero
- 🗣️ Sintetiza cualquier texto con la voz entrenada
- 🐍 Compatible con Python 3.10 y GPU NVIDIA

---

## 🚀 Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/DanielSitoV01D/Social-Engineering-Voice-DL
cd Social-Engineering-Voice-DL

## 📥 Requisito adicional: Clonar Tortoise TTS

Este proyecto requiere que clones manualmente el repositorio de Tortoise TTS (no viene incluido por defecto):

```bash
git clone https://github.com/neonbjb/tortoise-tts.git

## ⚠️ Aviso Legal

> ⚠️ **Advertencia de uso responsable:**  
> Este proyecto se ha desarrollado únicamente con fines educativos, de investigación y para pruebas autorizadas de seguridad.  
> 
> El uso de esta herramienta para clonar voces reales sin consentimiento explícito puede violar leyes de privacidad, propiedad intelectual y derechos de imagen.  
> 
> El autor no se hace responsable por cualquier uso indebido de este software.

---
## 🛠️ Ejemplo de uso

Una vez instalado todo, puedes generar una voz clonada con el siguiente comando:

```bash
python src/generator.py \
  --audio audios_a_clonar/audio_prueba.m4a \
  --text "Hola, soy Dani y esta es mi voz clonada." \
  --name dani \
  --output deepfake_dani.wav