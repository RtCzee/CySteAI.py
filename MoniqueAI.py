import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime 
import wikipedia 
import pyjokes

listener = sr.Recogniser()
engine = pyttsx3.init()
voices = engine.getproperty('voices') 
engine.setProperty('voice',voices[2].id)


def talk(text):
  engine.say(text)
  engine.runandwait()


def take_command():
  try:
    with sr.microphone () as source:
      print("listening")

      voice = listener.listener(source)
      command=listener.recognise_google(voice)
      command = command.lower()
      if'Monique' in command:
        command = command.replace('Monique','')
        print(command)
  except:
    pass
    return command

def run_Monique():
  command = take_command()
  print(command)
  if 'play'in command:
    song  = command.replace('play', '')
    talk('im playing'+ song)
    pywhatkit.playonyt(song)
  elif 'time'in command:
    time=datetime.datetime.now().strftime('%I:%M:%S %P')
    talk('Let me see hmmmmmm the current time is'+time)
  elif 'who is' in command:
   person = command.replace('who is','')
   info = wikipedia.summary(person, 1)
   print(info)
   talk(info)
  elif 'are u single' in command:
    talk('no , I am in a strong relationship with your wifi')
  elif 'joke' in command:
    talk(pyjokes.get_joke())  
  elif 'who are you' in command:
    talk('i am Monique , your AI assistant')
  elif 'who created you' in command:
    talk('my creator is Didintle Mokgore who is new to python but yet he coded me ') 

while True:
  run_monique()







       
      