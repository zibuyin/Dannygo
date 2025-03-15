import speech_recognition as sr
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import subprocess
import osascript
import time
import os
import pyautogui

def rename_txt_files(directory):
    # Iterate over all files in the given directory
    print(f"Checking directory: {directory}")
    for filename in os.listdir(directory):
        print(f"Found file: {filename}")
        # Check if the file has a .txt extension
        if filename.endswith(".txt"):
            # Construct the new filename by changing the extension to .dannygo
            new_name = os.path.splitext(filename)[0] + ".dannygo"

            # Full path for the old and new file names
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_name)

            print(f"Renaming {old_path} to {new_path}")
            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed {filename} to {new_name}")
        else:
            print(f"Skipping {filename}, not a .txt file")

def speech_to_text(directory):
    """
    Continuously listen for speech and convert it to text.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please start speaking...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
        while True:
            try:
                # Continuously listen to the microphone
                audio = recognizer.listen(source)
                print("Recognizing...")

                # Use Google Speech Recognition to convert speech to text
                text = recognizer.recognize_google(audio, language="en-US")
                print(f"Recognition result: {text}")

                # Check if any of the keywords are detected
                if any(keyword in text.lower() for keyword in ["danny", "dan", "go"]):
                    print("Keyword detected!")
                    osascript.osascript("set volume output volume 40")

                    # Open the video file
                    subprocess.run(["open", "demo.mp4"])

                    # Wait for QuickTime to open
                    time.sleep(0.5)
                    webbrowser.open("https://www.youtube.com/channel/UC3wCAOfSB0W9iuKDDtNJeGw")
                    time.sleep(2.5)

                    # Use pyautogui to click on the "Subscribe" button
                    pyautogui.click(590, 400)  # Adjust this to match the location of the subscribe button
                    webbrowser.open("https://youtu.be/QHPi3tVbq6U?si=1ePgILYm5NyFhc8Y&t=43")
                    time.sleep(1.6)
                    pyautogui.click(1032, 647)  # Adjust this to match the location you want to click

                    # Rename .txt files in the directory
                    rename_txt_files(directory)
                    return True  # Return True if 'danny', 'dan', or 'go' is detected
            except sr.UnknownValueError:
                print("Sorry, could not understand your speech.")
            except sr.RequestError as e:
                print(f"Could not connect to the speech recognition service: {e}")
                break  # Exit loop if there's a request error

# Usage: specify the directory for renaming files
directory = "/Users/nathanyin/PycharmProjects/Scrapyard/macos"  # Replace with the actual path of your directory
speech_to_text(directory)