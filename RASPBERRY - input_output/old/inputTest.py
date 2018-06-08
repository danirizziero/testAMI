import sys
import wave
import getopt
import time
import alsaaudio  # FUNZIONA SOLO SU LINUX, ALSA è IL GESTORE INPUT/OUTPUT DI LINUX

# speech recognition packages
import speech_recognition as sr
from os import path

def inputTest():
    """
    Ritorna la risposta vocale dall'utente, elaborando la sua risposta vocale ("YES"=true | "NO"=false)
    Ripete l'input 3 volte, poi torna -1 = "no response"
    :return: boolean
    """

    # Setting del dispositivo di input
    inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK, device='default')
    inp.setchannels(1)  # MONO
    inp.setrate(16000)  # SAMPLING RATE = 16K
    inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
    inp.setperiodsize(160)

    # fase1 - INPUT SONORO
    ANSWER = open('testANSWER.wav', 'wb')

    loops = 4000  # così dovrebbe registrare 4 secondi
    while loops > 0:
        loops -= 1
        # Read data from device
        l, data = inp.read()

        if l:
            ANSWER.write(data)
            print(loops)
            time.sleep(.001)

    print("Completato!")
    read(loops)
