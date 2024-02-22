#!/bin/bash

import subprocess

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print("\n\nscript started\n")

while (True):
	if GPIO.input(17) > 0:
		print("P_ptaszek")
		subprocess.call(["/usr/bin/xdotool", "key", "0x0070"])
		time.sleep(0.3)

	if GPIO.input(27) > 0:
		print("L_lampka")
		subprocess.call(["/usr/bin/xdotool", "key", "0x006c"])
		time.sleep(0.3)

	if GPIO.input(22) > 0:
		print("R_restart")
		subprocess.call(["/usr/bin/xdotool", "key", "0x0072"])
		time.sleep(0.3)