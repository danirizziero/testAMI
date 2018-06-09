#Created by Davide Sordi in 09/06/2018 at 22.28
from time import sleep

import RPi.GPIO as GPIO

def main():
	while True:
		print("Send interrupt")
		#HERE WE SEND AN IMPULSE
		GPIO.output(interrupt_pin,GPIO.HIGH)
		GPIO.output(interrupt_pin,GPIO.LOW)
		sleep(3)


if __name__ == "__main__":
	GPIO.setmode(GPIO.BCM)  # to setup the numbering of pin in raspberry
	interrupt_pin = 4
	GPIO.setup(interrupt_pin, GPIO.OUT)  # Interrupt pin
	main()