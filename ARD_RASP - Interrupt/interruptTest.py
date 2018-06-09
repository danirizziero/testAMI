#Created by Davide Sordi in 05/06/2018 at 21.05
from time import sleep

import RPi.GPIO as GPIO

def interruptReceived(channel):
	"""

	:param channel: pin number (phisical) where we received an interrupt
	"""
	print("############ INTERRUPT ############   ",channel)

def main():
	while True:
		print("Waiting for interrupt")
		sleep(1)


if __name__ == "__main__":
	GPIO.setmode(GPIO.BCM)  # to setup the numbering of pin in raspberry
	interrupt_pin = 4
	GPIO.setup(interrupt_pin, GPIO.IN)  # Interrupt pin
	GPIO.add_event_detect(interrupt_pin, GPIO.RISING, callback=interruptReceived, bouncetime=500) # bouncetime è il tempo minimo tra un interrupt e un altro
	main()