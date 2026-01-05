ESIR (Even Starting I Rock) - AI Voice Assistant
ESIR is a locally hosted, voice-activated AI assistant designed to provide a conversational interface similar to J.A.R.V.I.S. It integrates offline speech recognition, application control, and advanced Large Language Models (LLMs) to create a helpful, human-like companion.
---
🚀 Project Intention & Motivation
The primary motivation behind creating ESIR was to bridge the gap between standard Python 
scripting and modern AI integration. The goal was to build a system that is not just a 
chatbot, but a functional tool that can interact with the user's operating system (opening 
apps) while maintaining a consistent personality.
---
This project serves as a practical exploration into:

Human-Computer Interaction (HCI): Moving beyond keyboard/mouse to voice commands.

Local AI Independence: Running powerful AI models (Ollama) and Speech Recognition (Vosk) 
entirely on the local machine for privacy and speed, without relying on cloud APIs.
---
🌟 Key Features
Voice-to-Text Engine: 
Uses Vosk for high-accuracy, offline speech recognition. It dynamically adjusts for ambient noise.

Intelligent Responses:
Powered by Ollama (Mistral-Nemo), enabling the assistant to understand context, nuance, and answer complex queries with a specific persona.

System Automation: 
Capable of launching applications on command (e.g., "Launch Chrome").

Text-to-Speech (TTS): Speaks responses back to the user using pyttsx4 for a hands-free experience.

Custom Persona: Configured via system prompting to act as "ESIR," a concise, helpful, and character-driven assistant that addresses the user as "BOSS."
---
🧠 Concepts & Learning Outcomes
This project touches upon several critical software engineering and AI concepts:

1. Modular Programming
The project is structured into distinct modules to maintain clean code:

main.py: The central controller managing the event loop.

logic.py: Handles input processing (Speech Recognition).

voice_assistance.py: Handles output processing (Text-to-Speech).

LLM_ini.py: Manages the interface with the AI model.

2. Large Language Model (LLM) Integration
Prompt Engineering: The project utilizes a "System Prompt" (stored in _cache_.txt) to condition the model. This teaches the AI who it is (ESIR), how to behave (concise, no AI disclaimers), and how to handle imperfect speech inputs.

Context Management: (Implemented via file handling) The concept of maintaining a conversation history so the AI remembers previous turns of the dialogue.

3. Audio Processing
Signal Processing: Understanding energy thresholds (recognizer.energy_threshold) to distinguish between silence, background noise, and active speech.

JSON Parsing: Handling complex JSON responses from the Vosk recognizer to extract raw text.
---
🛠️ Tech Stack
Language: Python

LLM Backend: Ollama (running mistral-nemo)

Speech Recognition: Vosk, SpeechRecognition

Text-to-Speech: pyttsx4

App Automation: AppOpener
---
📦 Installation & Setup
Prerequisites
Python: Ensure Python is installed.
Ollama
Vosk Model:
Install Dependencies
Run the following command to install the required Python libraries:
pip install pyttsx4 SpeechRecognition vosk ollama AppOpener
(Note: You may also need pyaudio. If installation fails, look up specific installation instructions for PyAudio for your OS).
---
🏃 Usage
Ensure your microphone is connected.
Run the main script:
Bash
python main.py
Speak! ESIR will introduce itself.

General Chat: Ask any question, and it will respond.

Open Apps: Say "Launch" followed by the app name (e.g., "Launch Calculator").

Exit: Say "Stop" to end the program.
---
📂 File Structure
main.py: Entry point. Runs the infinite loop for listening and responding.

logic.py: Contains the listen() function which sets up the microphone and Vosk recognizer.

voice_assistance.py: Contains the say() function for TTS output.

LLM_ini.py: Wrapper class for the Ollama API.

_cache_.txt: Stores the system prompt and conversation history.

"Even Starting I Rock"