import sys
import wave
import getopt

if __name__ == "__main__":
	#registra 3 secondi dalla (scheda,device) = (1,0), sample rate 8kHz, format S16_LE
	sh.arecord("-Dhw:1,0","--format=S16_LE","-d 3","--rate=8000","newRecordingTest.wav")

def input_test():
	sh.arecord("-Dhw:1,0","--format=S16_LE","-d 3","--rate=8000","newRecordingTest.wav")
