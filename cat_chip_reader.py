# coding: utf-8
import serial
ser = serial.Serial(
        port='/dev/ttyS0',
        baudrate=9600,
        bytesize=serial.EIGHTBITS,
        timeout=1,
        stopbits=serial.STOPBITS_ONE_POINT_FIVE,
        parity=serial.PARITY_NONE
)

def run():
    while Ture:
        x = ser.readline()
        if x:
            print translate(x)

test_str = ''.join(chr(int(n, 16)) for n in '02 31 37 31 41 39 32 35 33 41 33 34 38 33 30 30 31 30 30 30 30 30 30 30 30 30 30 07 F8 03'.split(' '))
def translate(input_str):
    arr = [ord(c) for c in input_str]
    card = arr[1:11]
    country = arr[11:14]
    checksum = arr[27]
    checksum_invert=arr[28]

    card_num = int('0x' + ''.join(chr(n) for n in card)[::-1], 16)
    country_num = int('0x' + ''.join(chr(n) for n in country)[::-1], 16)

    xor_result = reduce(lambda a, b: a ^ b, arr[1:27], 0)
    assert 255 - int('0x' + str(xor_result), 16) == checksum_invert
    assert arr[0] == 2
    assert arr[-1] == 3
    return card_num, country_num, xor_result
