#Remember to install pulseaudio and vlc
#sudo apt-get install vlc pulseaudio
import vlc
import time
import RPi.GPIO as GPIO

#Config for GPIOs
lightningPin = 18 #GPIO18
GPIO.setmode(GPIO.BCM)
GPIO.setup(lightningPin, GPIO.OUT)

#Logging and globals - Set this to False for production release
verboseLogging = True

############################
# Should the program loop!??
shouldLoop = True
############################


duration = 0
vlcPlayer = vlc.MediaPlayer("Sound.mp3")


#Create a function that sets up VLC
def startMusic():
    print("Starting up VLC")
    vlcPlayer.play()

#Create a log function that writes a message and how long we have been running
def logFunction(inMessage):
    if(verboseLogging):
        print(inMessage + ": " + str(duration))

def bigFlashFunction():
    #Much big such wow
    logFunction("Big flash function")
    GPIO.output(lightningPin, 1)
    time.sleep(0.1)
    GPIO.output(lightningPin, 0)
    time.sleep(0.1)
    GPIO.output(lightningPin, 1)
    time.sleep(0.1)
    GPIO.output(lightningPin, 0)
    time.sleep(0.1)
    GPIO.output(lightningPin, 1)
    time.sleep(0.1)
    GPIO.output(lightningPin, 0)
    

def littleFlashFunction():
    logFunction("little flash function")
    GPIO.output(lightningPin, 1)
    time.sleep(0.2)
    GPIO.output(lightningPin, 0)
    time.sleep(0.2)
    GPIO.output(lightningPin, 1)
    time.sleep(0.2)
    GPIO.output(lightningPin, 0)

def mediumFlashFunction():
    logFunction("medium flash function")
    GPIO.output(lightningPin, 1)
    time.sleep(0.1)
    GPIO.output(lightningPin, 0)
    time.sleep(0.1)
    GPIO.output(lightningPin, 1)
    time.sleep(0.1)
    GPIO.output(lightningPin, 0)

#Create the main loop to be run
def mainLoop():
    #If VLC is still playing, continue the loop
    if(vlcPlayer.get_state() == vlc.State(1) or vlcPlayer.get_state() == vlc.State(3)):
        logFunction("VLC is still playing")

        if(duration == 1):
            littleFlashFunction()

        if(duration == 3):
            littleFlashFunction()

        if(duration == 5):
            littleFlashFunction()

        if(duration == 15):
            bigFlashFunction()
            
        if(duration == 21):
            mediumFlashFunction()
            
        if(duration == 29):
            mediumFlashFunction()

        if(duration == 40):
            mediumFlashFunction()

        if(duration == 56):
            bigFlashFunction()

        if(duration == 70):
            bigFlashFunction()

        if(duration == 83):
            bigFlashFunction()

        if(duration == 95):
            littleFlashFunction()
        
        #Let's keep a track of how long we have been playing for debugging
        global duration
        duration += 1
        
        #Because python is lame, we should delay here for a bit as to not trip the maximum recursion ammount
        time.sleep(1)

        #Call the main loop so we keep going
        mainLoop();
    else:
        if(shouldLoop):
            #Set the duration to zero as we are looping
            global duration
            duration = 0

            #Start the music again
            startMusic()

            #Continue looping
            mainLoop();
        else:
            print("That's all, Folks!")

#######################
# Program Starts Here #
#######################

#Setup Music
startMusic()

#Start the main loop
mainLoop()