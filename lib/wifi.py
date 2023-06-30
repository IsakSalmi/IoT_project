import network
import socket
import time
import lib.config as config

def connect():
    """connect to the wifi
    """
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("connecting to network...")
        sta_if.active(True)
        sta_if.connect(config.SSID, config.PASSWORD)
        while not sta_if.isconnected():
            pass
    print("network config: ", sta_if.ifconfig())

def getHttpTest(url = 'http://detectportal.firefox.com/'):
    """Get a test packet from a given URL

    Args:
        url (str, optional): A test URL to get a pcakt from. Defaults to 'http://detectportal.firefox.com/'.
    """
    _, _, host, path = url.split('/', 3) 
    addr = socket.getaddrinfo(host,80)[0][-1]
    s = socket.socket()
    s.connect(addr)

    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    time.sleep(1)
    recByte = s.recv(10000)
    print(recByte)
    s.close()
    