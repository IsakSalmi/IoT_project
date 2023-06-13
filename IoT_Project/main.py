import IoT_Project.sensors as sensors
from time import sleep
from time import ticks_ms
import IoT_Project.wifi as wifi
import machine
import ubinascii 
from IoT_Project.mqtt import MQTTClient

# Adafruit IO (AIO) configuration

pin = machine.Pin("LED",machine.Pin.OUT)
def sub_cb(topic, msg):          # sub_cb means "callback subroutine"
    print((topic, msg))          # Outputs the message that was received. Debugging use.
    if msg == b"ON":             # If message says "ON" ...
        pin.value(1)  # ... then LED on
    elif msg == b"OFF":          # If message says "OFF" ...
        pin.value(0)   # ... then LED off
    else:                        # If any other message is received ...
        print("Unknown message")


def send_temp(temp):

    print("Publishing: {0} to {1} ... ".format(temp, OUTDOOR_TEMP), end='')
    try:
        client.publish(topic=OUTDOOR_TEMP, msg=str(temp))
        print("DONE")
    except Exception as e:
        print("FAILED")


AIO_SERVER = "io.adafruit.com"
AIO_PORT = 1883
AIO_USER = "IsakSalmi02"
AIO_KEY = "aio_yxhH42lGpa3WGD7KSnlJgoL6BWZt"
AIO_CLIENT_ID = ubinascii.hexlify(machine.unique_id())  # Can be anything
AIO_CONTROL_FEED = "IsakSalmi02/feeds/iot-project.lamp"
OUTDOOR_TEMP = "IsakSalmi02/feeds/iot-project.outdoortempsensor"
INDOOR_TEMP = "IsakSalmi02/feeds/iot-project.indoortempsensor"


wifi.connect()
wifi.getHttpTest()

client = MQTTClient(AIO_CLIENT_ID, AIO_SERVER, AIO_PORT, AIO_USER, AIO_KEY)
client.set_callback(sub_cb)
client.connect()
client.subscribe(AIO_CONTROL_FEED)
print("Connected to %s, subscribed to %s topic" % (AIO_SERVER, AIO_CONTROL_FEED))

def main():
    temp = sensors.MCPSensor()
    send_temp(temp)
    #client.check_msg()
    sleep(10)
    

if __name__ == "__main__":
    try:
        while True:
            main()
    finally:                  # If an exception is thrown ...
        client.disconnect()   # ... disconnect the client and clean up.
        client = None
        print("Disconnected from Adafruit IO.")
        #machine.reset()