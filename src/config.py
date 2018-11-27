#!/usr/bin/python3

# Listen to BCM 17 (physical pin 11).
pin = 17

# How long should we wait between rings before sending another notification?
# (in seconds)
timeout = 30

# Select the method of notification you'd like to receive.
# You can choose from: pushover, ..
method = 'pushover'

# What should the message say?
message = 'Someone\'s at the door!'

# Set a Pushover API token.
token = 'xxx'
user = 'xxx'
device = 'myDevice'
