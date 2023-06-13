from machine import ADC
from machine import Pin

tempOut = ADC(27)

tempIn = ADC(4)

sf = 4095/65535 # Scale factor
volt_per_adc = (3.3 / 4095)
def MCPConverter(millivolts):
    adc_12b = millivolts * sf

    volt = adc_12b * volt_per_adc

    # MCP9700 characteristics
    dx = abs(50 - 0)
    dy = abs(0 - 0.5)

    shift = volt - 0.5

    temp = shift / (dy / dx)
    return temp


def MCPSensor():
    millivolts = tempOut.read_u16()
    temp = MCPConverter(millivolts)
    return temp

def onBoardTemp():
    ADC_voltage = tempIn.read_u16() * (3.3 / (65535))
    temperature_celcius = 27 - (ADC_voltage - 0.706)/0.001721
    return temperature_celcius