#This script will shutdown your Pi if you hold a button pressed for more than 2 seconds.
#Accidental presses (less than 2 sec) will not cause a shutdown.
#The button is connected on GPIO 17 but you can change it to any free GPIO you have.

from time import sleep
import subprocess
import RPi.GPIO as GPIO

CHANNEL = 17 # GPIO channel 17. It will work on any GPIO channel you choose. Look online for the Pi GPIO diagram.

GPIO.setmode(GPIO.BCM) #Use BCM numbering scheme.
GPIO.setup(CHANNEL, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Setup the channel as input with a 50K Ohm pull up. A push button will ground the selected pin.

def shutdown(CHANNEL):
    print('Button press = negative edge detected on channel %s'%CHANNEL)
    button_press_timer = 0
    
    while (GPIO.input(CHANNEL) == False): #While button is pressed down
        button_press_timer += 1 #Keep counting until button is released
        sleep(1) #Wait for one second before counting again.
        
        if (button_press_timer > 2) : #If pressed for more than 2 seconds
            print "long press > 2 : ", button_press_timer #Report event in the console
                    # do what you need to do before halting. You can add other system actions here.
            subprocess.call(['shutdown -h now &'], shell=True)
            break
    while (GPIO.input(CHANNEL) == True):
        print "reset timer"
        button_press_timer = 0
        break
                
GPIO.add_event_detect(CHANNEL, GPIO.FALLING, callback=shutdown, bouncetime=200) #Detect a falling edge on channel 17 and debounce it with 200mSec. This is an interrupt.

#Make an empty loop to keep the process running while it is waiting for the interrupt. You can add code here or make it sleep to free CPU resources.
try:
    while True:

        sleep (10) #Sleep for as long as you want, or replace it with your code to do other things.

except KeyboardInterrupt:
    GPIO.cleanup()       #Clean up GPIO on CTRL+C exit
GPIO.cleanup()           #Clean up GPIO on normal exit
