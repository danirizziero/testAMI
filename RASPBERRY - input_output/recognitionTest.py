import sys
import wave
import getopt
import time
import alsaaudio  # FUNZIONA SOLO SU LINUX, ALSA è IL GESTORE INPUT/OUTPUT DI LINUX

# speech recognition packages
import speech_recognition as sr
from os import path

from . import inputTest

def yes_or_no(file):

    # FILE contenente la risposta:

    AUDIO_FILE = 'testANSWER.wav'

    letsGo = 1 
    i=0

    while(letsGo):

        #nel caso di input live, SCOMMENTATE
        inputTest()

        # use the audio file as the audio source
        r = sr.Recognizer()

        with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)  # read the entire audio file

        try:
            recognisedAnswer = r.recognize_sphinx(audio)
        except sr.UnknownValueError:
            return -1  # COMUNICO L'ERRORE E L'UTENTE DEVE REINSERIRE
            pass

        #    D E B U G 

        # # recognize speech using Sphinx
        # try:
        #     print("Sphinx thinks you said --> " + r.recognize_sphinx(audio))
        # except sr.UnknownValueError:
        #     print("Sphinx could not understand audio")
        # except sr.RequestError as e:
        #     print("Sphinx error; {0}".format(e))

        # todo da modificare in modo che riconosca un range di parole foneticamente simili

        if (recognisedAnswer == "yes"): #OK
            print("\n\t\thai detto YES")
        else: #OK
            if (recognisedAnswer == "no"):
                print("\n\t\thai detto NO")
        else #ho riconosciuto un altra parola! LA SALVO!!
            recognisedWords[i] = recognisedAnswer
            i+=1
            print("\n\t\tAltra parola trovata! --> ", recognisedWords[i])


        print("\n\nAltro input? 1/0")
        read(letsGo)
    


    print("\nEcco le parole estranee riconosciute")
    print(recognisedWords)
    read(letsGo)


