import tkinter as tk
import speech_recognition as sr
import pyttsx3
import threading

# Initialize voice engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Choose voice

# Speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Listen to voice
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        status_label.config(text="Listening...")
        recognizer.pause_threshold = 1
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio)
            status_label.config(text="You said: " + command)
            response = basic_response(command.lower())
            speak(response)
        except Exception as e:
            status_label.config(text="Sorry, I didn't get that.")
            speak("Sorry, I didn't get that.")

# Basic response logic (no OpenAI)
def basic_response(command):
    if "hello" in command:
        return "Hello! How can I help you?"
    elif "your name" in command:
        return "My name is ERA."
    elif "time" in command:
        from datetime import datetime
        now = datetime.now().strftime("%I:%M %p")
        return f"The time is {now}"
    elif "bye" in command:
        return "Goodbye!"
    else:
        return "I don't understand, but I'm learning!"

# Start voice recognition in a new thread
def start_listening():
    threading.Thread(target=listen).start()

# GUI
root = tk.Tk()
root.title("ERA - Voice Assistant")
root.geometry("400x200")

title_label = tk.Label(root, text="ERA Voice Assistant", font=("Helvetica", 16))
title_label.pack(pady=10)

listen_button = tk.Button(root, text="Speak", font=("Helvetica", 14), command=start_listening)
listen_button.pack(pady=20)

status_label = tk.Label(root, text="Click Speak and talk...", wraplength=300)
status_label.pack()

root.mainloop()


