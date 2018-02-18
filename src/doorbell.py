#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep, time
import requests, sys

# Include our configuration.
import config

# Setup GPIO board and pin mode.
GPIO.setmode(GPIO.BCM)
GPIO.setup(config.pin, GPIO.IN)

# We save the last time the doorbell was rung.
last = 0

# Main event handler.
def main():

	global last

	# Wait for the bell to ring.
	GPIO.wait_for_edge(config.pin, GPIO.FALLING)

	# Compare the current timestamp with the previous
	# timestamp to prevent notification spam.
	timestamp = time()
	if (timestamp - last < config.timeout):
		print('[!] Doorbell is (still) ringing, however since the last ring was ' +
			  'within %s seconds we ignore this.' % (config.timeout))
		sleep(config.timeout - (timestamp - last))
		return main()

	# Notify the user of the ring!
	notify(config.method, timestamp)

	# Update the last time we notified the user.
	last = time()

	# Return to the beginning of the event handler.
	return main()

def notify(method, timestamp):

	print('[*] Ring ring!')

	if (method == 'pushover'):

		# Send a message to the endpoint of Pushover.
		endpoint = 'https://api.pushover.net/1/messages.json'
		r = requests.post(endpoint, json = {
			'token': config.token,
			'user': config.user,
			'message': config.message,
			'timestamp': timestamp
		})
		print('[*] Sent message to Pushover (%s)' % (r.status_code))
		return r.status_code

	else:
		print('[!] Unknown method %s for notify()' % (method))

# Run main function in try/catch block,
# so we can catch a CTRL+C and clean up GPIO
# states before gracefully exiting.
try:
	main()
except KeyboardInterrupt:
	print('Cleaning up..')
	GPIO.cleanup()
	sys.exit(0)
