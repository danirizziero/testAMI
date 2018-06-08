import sys
import wave
import getopt
import time
import alsaaudio  # FUNZIONA SOLO SU LINUX, ALSA è IL GESTORE INPUT/OUTPUT DI LINUX

def comm_to_user(message):


    FileDaRiprodurre = 'TEST.wav'  # path del file da riprodurre
    f = wave.open(FileDaRiprodurre, 'rb')  # file da riprodurre, aperto
    device = alsaaudio.PCM(device='default')  # il device è quello di default

    # Setting del device
    device.setchannels(f.getnchannels())
    device.setrate(f.getframerate())
    device.setformat(alsaaudio.PCM_FORMAT_S16_LE)
    periodsize = f.getframerate() / 8  # dimensione dei chunck da riprodurre uno dopo l'altro!
    device.setperiodsize(f.getframerate() / 8)

    data = f.readframes(periodsize)  # LEGGO DAL FILE AUDIO
    while data:
        device.write(data)  # SCRIVO SUL DEVICE --> RIPRODUCO IL FILE PEZZO PER PEZZO
        data = f.readframes(periodsize)

    f.close()  # chiudo il file audio