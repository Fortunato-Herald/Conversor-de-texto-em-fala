#  pip install pyttsx3

import pyttsx3

#  Carrega a lib
engine = pyttsx3.init()

#  Texto que a engine vai falar
engine.say('Olá, como voce está?')
engine.say('Em qual linguagem voce programa?')

#  Executa
engine.runAndWait()