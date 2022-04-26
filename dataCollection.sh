#!/bin/bash

# Collect data from accelerometer
python3 accel.py &

# Collect data from temperature probe
python3 temp.py &

#gps location
python3 Location.py &

# Collect data from microphone
python recorder.py &

# Collect data from heartrate monitor
timeout 30s gatttool -t random -b D9:B0:FA:49:40:87 --char-write-req --handle=0x0011 --value=0100 --listen | stdbuf -o0 cut -d ' ' -f 7 > hr_hex.txt

# Convert heartrates from hex to base10
python3 hex.py



