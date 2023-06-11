from machine import ADC
from machine import Pin

tempOut = ADC(27)

tempIn = ADC(4)

pin = Pin("LED",Pin.OUT)

def MCPSensor():
    adc_value = tempOut.read_u16()
    volt = (3.3/65535) * adc_value
    degC = (100 * volt) - 50
    return degC

def onBoardTemp():
    ADC_voltage = tempIn.read_u16() * (3.3 / (65535))
    temperature_celcius = 27 - (ADC_voltage - 0.706)/0.001721
    return temperature_celcius