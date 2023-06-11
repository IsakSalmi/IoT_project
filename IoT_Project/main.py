import IoT_Project.sensors as sensors
from time import sleep
import IoT_Project.wifi as wifi

wifi.connect()
wifi.getHttpTest()
def main():
    while True:
        sensors.pin.toggle()
        sleep(1)
main()