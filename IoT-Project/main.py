import sensors
from time import sleep
import wifi

wifi.connect()

def main():
    print("ready")
    while True:
        sensors.pin.toggle()
        sleep(1)
main()