#  -*- coding: UTF-8 -*-

import smbus
import time

def scan_i2c_addresses(bus_num, start_address, end_address):
    bus = smbus.SMBus(bus_num)
    found_devices = {}

    for address in range(start_address, end_address + 1):
        try:
            bus.write_quick(address)
            found_devices[address] = "Found"
        except OSError:
            found_devices[address] = "Not Found"
        time.sleep(0.01)
    return found_devices

if __name__ == "__main__":
    # ָ��I2C���߱�ţ����磺��Raspberry Pi��ͨ����1��
    bus_number = 4

    # ��Ҫɨ���I2C��ַ��Χ
    start_address = 0x03
    end_address = 0x7F

    while True:
        # ɨ��I2C��ַ
        results = scan_i2c_addresses(bus_number, start_address, end_address)

        # ��ӡɨ����
        for address, status in results.items():
            print(f"Address 0x{address:02X}: {status}")

        # �ӳ�һ��ʱ����ٴ�ɨ��
