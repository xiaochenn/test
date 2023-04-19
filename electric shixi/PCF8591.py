import smbus
import time

bus = smbus.SMBus(1)

def setup(Addr):
    global address
    address = Addr


def read(chn):
    try:
        if chn == 0:
            bus.write_byte(address, 0x40)
        if chn == 1:
            bus.write_byte(address, 0x41)
        if chn == 2:
            bus.write_byte(address, 0x42)
        if chn == 3:
            bus.write_byte(address, 0x43)
        bus.read_byte(address)
    except Exception as e:
        print("Address: %s" % address)
        print(e)
    return bus.read_byte(address)


def write(val):
    try:
        temp = val
        temp = int(temp)
        bus.write_byte_data(address, 0x40, temp)
    except Exception as e:
        print("Error: Device address: 0x%2x" % address)
        print(e)


if __name__ == "__main__":
    setup(0x48)
    while True:
        print('电位计 AIN3 = ', read(3))
        print('光敏电阻 AIN0 = ', read(0))
        print('热敏电阻 AIN1 = ', read(1))
        tmp = read(0)
        tmp =tmp * (255 - 125) / 255 + 125
        write(tmp)
        time.sleep(1)
