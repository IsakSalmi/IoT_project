
import IoT_Project.sensors as sensors
import IoT_Project.wifi as wifi
from IoT_Project.mqtt import MQTTClient
import IoT_Project.config as config

from time import sleep
from time import ticks_ms
import machine
import ubinascii 



def send_temp(temp_in, temp_out):
    """sends both variables to the connected adafruit

    Args:
        temp_in (float): the temperature indoor
        temp_out (float): the temperature outdoor
    """
    
    try:
        client.publish(topic=config.OUTDOOR_TEMP, msg=str(temp_out))
        client.publish(topic=config.INDOOR_TEMP, msg=str(temp_in))
    except Exception as e:
        print("FAILED")

def send_window_command(command):
    """sends the given variables to the connected adafruit

    Args:
        command (int): the window command, 1 is for "you need to open"
                          0 is for "you need to close"
    """
    try:
        client.publish(topic=config.WINDOW_SENSOR, msg=str(command))
    except Exception as e:
        print("FAILED")

def send_window_status(status):
    """sends the given variables to the connected adafruit

    Args:
        status (bool): The status of the window. True is for open and False is for closed
    """
    try:
        if(status == True):
            client.publish(topic=config.WINDOW_STATUS, msg=str(1))
        else:
            client.publish(topic=config.WINDOW_STATUS, msg=str(0))
    except Exception as e:
        print("FAILED")

#connecting to the internet
wifi.connect()
wifi.getHttpTest()

#conecting to adafruit
AIO_CLIENT_ID = ubinascii.hexlify(machine.unique_id())
client = MQTTClient(AIO_CLIENT_ID, config.AIO_SERVER, config.AIO_PORT, config.AIO_USER, config.AIO_KEY)
client.connect()



def main():
    can_send_massage = True
    last_window_comand = False
    
    while True:
        # get all the needed variables from the sensors
        temp = sensors.MCPSensor()
        window = sensors.WinSensor()
        
        #send the window status to adafruit
        send_window_status(window)

        #if we have a change from the window sensor we can now 
        #send a new message
        if(last_window_comand != window):
            can_send_massage = True

        print("temp in: {}, temp out: {}".format(temp[0],temp[1]))
        print("window: {}, can_send_massage: {}\n".format(window, can_send_massage))
        
        #if we have a closed window, indoor temp is higer 
        #then outdoor temp and we can send a messages to adafruit to be able to 
        #call the action in adafruit
        if(((temp[0] - 1) > temp[1]) and (window == True) and (can_send_massage == True)):
            send_window_command(1)
            can_send_massage = False
            
        #the same as above but in reverse order. 
        elif(((temp[1] - 1) > temp[0]) and (window == False) and (can_send_massage == True)):
            send_window_command(0)
            can_send_massage = False
        
        #send both temp to the adafruit server 
        send_temp(temp[0],temp[1])

        last_window_comand = window
        sleep(10)
    

if __name__ == "__main__":
    try:
        main()
    finally:                  # If an exception is thrown ...
        client.disconnect()   # ... disconnect the client and clean up.
        client = None
        print("Disconnected from Adafruit IO.")
        machine.reset()