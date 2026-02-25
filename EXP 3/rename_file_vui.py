import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import os

def record_audio(filename="voice.wav", duration=5, fs=44100):
    print("Speak now...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    write(filename, fs, recording)

def rename_file_from_voice(command):
    try:
        words = command.lower().split()
        old_name = words[1]
        new_name = words[3]

        os.rename(old_name, new_name)
        print(f"File renamed from {old_name} to {new_name}")
    except Exception as e:
        print("Error:", e)

def main():
    record_audio()

    recognizer = sr.Recognizer()
    with sr.AudioFile("voice.wav") as source:
        audio = recognizer.record(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        rename_file_from_voice(command)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Request error:", e)

if __name__ == "__main__":
    main()