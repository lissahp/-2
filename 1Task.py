class BigNumber:
    def __init__(self, value=0):
        self.data = bytearray(value.to_bytes((value.bit_length() + 7) // 8, 'big'))

    def set_from_hex_string(self, hex_string):
        hex_string = hex_string.lstrip('0x') 
        if len(hex_string) % 2 == 1:
            hex_string = '0' + hex_string  
        self.data = bytearray.fromhex(hex_string)

    def get_hex_string(self):
        return '0x' + self.data.hex()

    def set_from_decimal_string(self, decimal_string):
        value = int(decimal_string)
        self.__init(value)

    def get_decimal_string(self):
        return str(int.from_bytes(self.data, 'big'))

def test_big_number():
    num = BigNumber()

    num.set_from_hex_string("1A3F")
    assert num.get_hex_string() == "0x1a3f"

    num.set_from_hex_string("7F")
    assert num.get_hex_string() == "0x7f"

    num.set_from_hex_string("ABCD1234")
    assert num.get_hex_string() == "0xabcd1234"

    num.set_from_decimal_string("12345")
    assert num.get_decimal_string() == "12345"

    num.set_from_decimal_string("0")
    assert num.get_decimal_string() == "0"

    num.set_from_decimal_string("987654321")
    assert num.get_decimal_string() == "987654321"


if __name__ == '__main__':
    test_big_number()
    print("All tests passed.")
