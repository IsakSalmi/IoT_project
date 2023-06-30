from machine import ADC
from machine import Pin


sf = 4095/65535 # Scale factor
volt_per_adc = (3.3 / 4095)

def MCPConverter(millivolts):
    """To convert the value from a MCP9700 sensor

    Args:
        millivolts (float): the given value that the MCP9700 sensor give

    Returns:
        float: the actual temp in celsius
    """
    adc_12b = millivolts * sf

    volt = adc_12b * volt_per_adc

    # MCP9700 characteristics
    dx = abs(50 - 0)
    dy = abs(0 - 0.5)

    shift = volt - 0.5

    temp = shift / (dy / dx)
    return temp

temp_out = ADC(28)
temp_in = ADC(27)
def MCPSensor():
    """Get two temperaturs from a pico w on the pin 28 and 27

    Returns:
        float:the two temperatures 
    """
    list_in = []
    list_out = []
    for i in range(11):
        millivolts_out = temp_out.read_u16()
        millivolts_in = temp_in.read_u16()
        list_in.append(MCPConverter(millivolts_in))
        list_out.append(MCPConverter(millivolts_out))
    list_in.sort()
    list_out.sort()
    return list_in[5],list_out[5]


digitalPin = Pin(26, Pin.IN)
def WinSensor():
    """Get the bool from a Pulse sensor hall effect digital

    Returns:
        bool: if the sensor have been triggerd
    """
    digitalValue = digitalPin.value()
    if digitalValue == True:
        return True
    else:
        return False

