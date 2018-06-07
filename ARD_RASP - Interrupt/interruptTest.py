#Created by Davide Sordi in 05/06/2018 at 21.05
from time import sleep

import RPi.GPIO as GPIO

def interruptReceived():
	print("############ INTERRUPT ############")

def main():
	while True:
		print("Waiting for interrupt")
		sleep(2)


if __name__ == "__main__":
	GPIO.setmode(GPIO.BOARD)  # to setup the numbering of pin in raspberry
	interrupt_pin = 2
	GPIO.setup(interrupt_pin, GPIO.IN)  # Interrupt pin
	GPIO.add_event_detect(interrupt_pin, GPIO.RISING, callback=interruptReceived)
	main()