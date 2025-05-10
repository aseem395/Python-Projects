# We have created a program to give shoutouts based on the input list given by the user.
import win32com.client as wincom
input = input("Enter the name of the person: ")
l = input.split()
speak = wincom.Dispatch("SAPI.SpVoice")
for people in l:
    text = f"Shoutout to {people}"
    speak.Speak(text)
