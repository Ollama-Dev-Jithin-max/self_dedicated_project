import pyttsx4 as pt
engine = pt.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def say (command):
 type(command)==str
 engine.say(command)
 engine.runAndWait()