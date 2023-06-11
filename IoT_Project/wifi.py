import network
import socket
import time

def connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("connecting to network...")
        sta_if.active(True)
        sta_if.connect('HUAWEI-B525s-8C62-S1', '26GG0MQH991')
        while not sta_if.isconnected():
            pass
    print("network config: ", sta_if.ifconfig())

def getHttpTest(url = 'http://detectportal.firefox.com/'):
    _, _, host, path = url.split('/', 3) 
    addr = socket.getaddrinfo(host,80)[0][-1]
    s = socket.socket()
    s.connect(addr)

    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    time.sleep(1)
    recByte = s.recv(10000)
    print(recByte)
    s.close()
    