import win32com.client as wincom
l = ["Rahul", "Nishant", "Harry"]
speak = wincom.Dispatch("SAPI.SpVoice")
for people in l:
    text = f"Shoutout to {people}"
    speak.Speak(text)