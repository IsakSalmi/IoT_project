import IoT_Project.sensors as sensors
from time import sleep
import IoT_Project.wifi as wifi
import machine
import ubinascii 
from mqtt import MQTTClient

# Adafruit IO (AIO) configuration
AIO_SERVER = "io.adafruit.com"
AIO_PORT = 1883
AIO_USER = "Your_Adafruit_User_Name"
AIO_KEY = "Your_Adafruit_Application_Key"
AIO_CLIENT_ID = ubinascii.hexlify(machine.unique_id())  # Can be anything
AIO_CONTROL_FEED = "Your_lights_Feed_Address"
AIO_RANDOMS_FEED = "Your_randoms_Feed_Address"

wifi.connect()
wifi.getHttpTest()
def main():
    

if __name__ == "__main__":
    try:
        while True:
            main()
    except:
        print("somthing whent wrong")
        machine.reset()