# pi-python-shutown

Shutdown your Pi with a GPIO button.

This script runs in the background and waits for a GPIO event, upon which it shuts down the Pi.
It is a nice introduction to interrupts in Python. Default configuration uses GPIO 17 and the event is triggered when it is pulled down (grounded).
The main loop of the script does nothing (sleeps constantly).
