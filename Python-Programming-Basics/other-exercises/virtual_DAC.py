# Virtual DAC

def v_dac(value):
    max_voltage = 5
    percent = value / 1023
    voltage = max_voltage * percent
    return voltage


dec_value = int(input())
volt_num = v_dac(dec_value)
print(f"Current voltage is: {volt_num}")
