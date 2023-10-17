class MyBigInt:
    def __init__(self):
        self.value = 0

    def setHex(self, hex_str):
        self.value = int(hex_str, 16)

    def getHex(self):
        return hex(self.value)[2:]

    def __operate(self, other, operation):
        result = MyBigInt()
        if operation == 'XOR':
            result.value = self.value ^ other.value
        elif operation == 'OR':
            result.value = self.value | other.value
        elif operation == 'AND':
            result.value = self.value & other.value
        elif operation == 'ADD':
            result.value = self.value + other.value
        elif operation == 'SUB':
            result.value = self.value - other.value
        elif operation == 'MUL':
            result.value = self.value * other.value
        return result

    def INV(self):
        self.value = ~self.value

    def XOR(self, other):
        return self.__operate(other, 'XOR')

    def OR(self, other):
        return self.__operate(other, 'OR')

    def AND(self, other):
        return self.__operate(other, 'AND')

    def shiftR(self, n):
        self.value = self.value >> n

    def shiftL(self, n):
        self.value = self.value << n

    def ADD(self, other):
        return self.__operate(other, 'ADD')

    def SUB(self, other):
        return self.__operate(other, 'SUB')

    def MUL(self, other):
        return self.__operate(other, 'MUL')
    
numberA = MyBigInt()
numberB = MyBigInt()
numberC = MyBigInt()

numberA.setHex("51bf608414ad5726a3c1bec098f77b1b54ffb2787f8d528a74c1d7fde6470ea4")
numberB.setHex("403db8ad88a3932a0b7e8189aed9eeffb8121dfac05c3512fdb396dd73f6331c")
numberC = numberA.XOR(numberB)
print("XOR result:", numberC.getHex())

numberA.setHex("36f028580bb02cc8272a9a020f4200e346e276ae664e45ee80745574e2f5ab80")
numberB.setHex("70983d692f648185febe6d6fa607630ae68649f7e6fc45b94680096c06e4fadb")
numberC = numberA.ADD(numberB)
print("ADD result:", numberC.getHex())

numberA.setHex("33ced2c76b26cae94e162c4c0d2c0ff7c13094b0185a3c122e732d5ba77efebc")
numberB.setHex("22e962951cb6cd2ce279ab0e2095825c141d48ef3ca9dabf253e38760b57fe03")
numberC = numberA.SUB(numberB)
print("SUB result:", numberC.getHex())

numberA.setHex("7d7deab2affa38154326e96d350deee1")
numberB.setHex("97f92a75b3faf8939e8e98b96476fd22")
numberC = numberA.MUL(numberB)
print("MUL result:", numberC.getHex())
