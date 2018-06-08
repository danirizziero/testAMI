import sys
import wave
import getopt
import sh

if __name__ == "__main__":
	#riproduce un file che va bene come formato
	#(scheda,device) = (0,0), sample rate 8kHz, format S16_LE
	sh.aplay("-Dhw:0,0","--format=S16_LE","--rate=8000","newTESTok.wav")

	

def comm_to_user(message):
	fileToPlay = message+'.wav'
	sh.aplay("-Dhw:0,0","--format=S16_LE","--rate=8000",fileToPlay)
