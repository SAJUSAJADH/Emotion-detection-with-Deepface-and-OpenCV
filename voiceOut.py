import pyttsx3

def Voice_out(message):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-20)
    engine.setProperty('voice', voices[1].id)
    engine.say(message)
    engine.runAndWait()