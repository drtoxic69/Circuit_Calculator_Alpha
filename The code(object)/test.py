import pyttsx3

engine = pyttsx3.init()

# rate = engine.getProperty('rate')   
# engine.setProperty('rate', 250)
engine.say('i was raised by the wolves, ate till they full')
engine.runAndWait()