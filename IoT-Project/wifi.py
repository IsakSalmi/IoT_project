import network

def connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("connecting to network...")
        sta_if.active(True)
        sta_if.connect('HUAWEI-B525s-8C62-S1', '26GG0MQH991')
        while not sta_if.isconnected():
            pass
    print("network config: ", sta_if.ifconfig())
    