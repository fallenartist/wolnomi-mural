# Raspberry Pi

## Kiosk

https://www.raspberrypi.com/tutorials/how-to-use-a-raspberry-pi-in-kiosk-mode/

## Monitor

https://gist.github.com/simlun/1b27b14d707abbba8fc1

## GPIO

Przypisanie pinów GPIO do klawiszy klawiatury - edytuj plik `/boot/firmware/config.txt`:

```
[all]
dtoverlay=gpio-key,gpio=23,active_low=0,gpio_pull=down,label=touch_P,keycode=25
dtoverlay=gpio-key,gpio=13,active_low=0,gpio_pull=down,label=touch_L,keycode=38
dtoverlay=gpio-key,gpio=19,active_low=0,gpio_pull=down,label=touch_R,keycode=19
```

## Shelly Mini:

Install `evdev`:
`source /home/mural/myenv/bin/activate`
`pip install evdev`

Create a Python script named `toggle_shelly.py` in the `/home/mural/mural` directory:
```
import requests
from evdev import InputDevice, categorize, ecodes

# URL to toggle the relay
SHELLY_URL = "http://192.168.1.140/relay/0?turn=toggle"

# Path to the input device (keyboard)
DEVICE_PATH = '/dev/input/event1'

def toggle_relay():
	try:
		response = requests.get(SHELLY_URL)
		if response.status_code == 200:
			print("Relay toggled successfully.")
		else:
			print(f"Failed to toggle relay: {response.status_code}")
	except requests.RequestException as e:
		print(f"Error toggling relay: {e}")

def main():
	try:
		device = InputDevice(DEVICE_PATH)
		print(f"Listening for key events on {DEVICE_PATH}...")
	except FileNotFoundError:
		print(f"Device {DEVICE_PATH} not found. Please check the device path.")
		return

	for event in device.read_loop():
		if event.type == ecodes.EV_KEY:
			key_event = categorize(event)
			if key_event.keystate == key_event.key_down:
				print(f"Key {key_event.keycode} pressed.")
				if key_event.keycode == 'KEY_L':
					toggle_relay()
				elif key_event.keycode == 'KEY_ESC':
					print("Exiting...")
					break

if __name__ == "__main__":
	main()
```

Finding the Correct Input Device Path:
`ls /dev/input/`
`sudo evtest /dev/input/eventX`

Replace X with the number of each event device until you find the one corresponding to your GPIO key.

Running the Script:
`sudo python3 /home/mural/mural/toggle_shelly.py`

Automating the Script on Boot
`sudo nano /etc/systemd/system/toggle_shelly.service`

```
[Unit]
Description=Toggle Shelly Relay on Key Press
After=network.target

[Service]
ExecStart=/home/mural/myenv/bin/python /home/mural/mural/toggle_shelly.py
Restart=on-failure
User=mural

[Install]
WantedBy=multi-user.target
```

Reload systemd and enable the service:
`sudo systemctl daemon-reload`
`sudo systemctl enable toggle_shelly.service`
`sudo systemctl start toggle_shelly.service`

Check the status of the service:
`sudo systemctl status toggle_shelly.service`
