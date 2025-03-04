Minutes of Meeting AI - Automated Transcription & Summarization

📌 Overview

Minutes of Meeting AI is an advanced AI-powered tool that transforms spoken meetings into structured summaries with key discussion points, takeaways, and action items. This project integrates state-of-the-art AI models to automate the process of generating meeting minutes, making it ideal for professionals, businesses, and organizations that rely on efficient documentation.

This tool leverages:

🎙️ Whisper AI for highly accurate speech-to-text transcription

🧠 LLaMA-3.1 for context-aware summarization



🚀 Features

✅ Upload an audio file of a meeting (supports .mp3, .wav, etc.)
✅ AI-generated transcription using Whisper AI
✅ Automatic summarization with key discussion points and action items
✅ Structured markdown output for easy reading




🏗️ Technologies Used

Python 🐍

Whisper AI (for transcription) 🎙️

LLaMA-3.1 (for summarization) 🤖

Hugging Face Transformers 🏆

BitsAndBytes Quantization ⚡

PyTorch (for deep learning execution) 🔥




BitsAndBytes Quantization for Optimization

To run LLaMA-3.1 efficiently, especially on limited resources, we use quantization techniques to reduce memory usage while maintaining performance.

This configuration:

Loads the model in 4-bit precision instead of the usual 16-bit or 32-bit.

Uses double quantization to improve numerical stability.

Uses bfloat16 (Brain Floating Point) for faster computations.

This results in lower memory consumption and faster inference, making it feasible to run large models on consumer-grade GPUs or cloud environments.



💡 Credits

Developed by Atharva Mahindrakar

🛠️Powered by Whisper AI and LLaMA-3.1

📌 Contributions are welcome! Feel free to open an issue or submit a PR. 🤝
