#Created by Davide Sordi in 13/06/2018 at 21.22

from time import sleep

import RPi.GPIO as GPIO

def interruptReceived(channel):
	"""
	:param channel: pin number (phisical) where we received an interrupt
	"""
	print("############ INTERRUPT ############   ",channel)
	GPIO.output(led_pin,1)
	sleep(1)
	GPIO.output(led_pin,0)


def main():
	while True:
		print("Waiting for interrupt")
		sleep(1)


if __name__ == "__main__":
	GPIO.setmode(GPIO.BCM)  # to setup the numbering of pin in raspberry
	interrupt_pin = 4
	led_pin = 17
	GPIO.setup(interrupt_pin, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)  # Interrupt pin
	GPIO.setup(led_pin, GPIO.OUT)  # Led pin
	GPIO.add_event_detect(interrupt_pin, GPIO.RISING, callback=interruptReceived, bouncetime=500) # bouncetime è il tempo minimo tra un interrupt e un altro
	main()