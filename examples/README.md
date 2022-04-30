# README

## Raspberry Pi Zero W

When used with Raspberry Pi Zero W, "pullup by DHT timeout" error occurs with high probability.
If I run it in shell for each measurement, the probability of the error occurring is considerably reduced.

### dht_read_with_error_message.py

Call the read_with_error_message method and output the return value to standard output.

### loop_dht_read_with_error_message.sh

Script to run dht_read_with_error_message.py repeatedly from shell.

### dht_simpleread_with_error_message_zero.py

Script to run dht_read_with_error_message.py repeatedly from Python.
