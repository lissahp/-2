class MyBigInt:
    def __init__(self):
        self.data = 0

    def setHex(self, hexString):
        self.data = int(hexString, 16)

    def getHex(self):
        return hex(self.data).replace("0x", "")

    def INV(self):
        return MyBigInt()  

    def XOR(self, other):
        result = MyBigInt()
        result.data = self.data ^ other.data
        return result

    def OR(self, other):
        result = MyBigInt()
        result.data = self.data | other.data
        return result

    def AND(self, other):
        result = MyBigInt()
        result.data = self.data & other.data
        return result

    def shiftR(self, n):
        result = MyBigInt()
        result.data = self.data >> n
        return result

    def shiftL(self, n):
        result = MyBigInt()
        result.data = self.data << n
        return result

numberA = MyBigInt()
numberB = MyBigInt()
numberC = MyBigInt()
numberA.setHex("51bf608414ad5726a3c1bec098f77b1b54ffb2787f8d528a74c1d7fde6470ea4")
numberB.setHex("403db8ad88a3932a0b7e8189aed9eeffb8121dfac05c3512fdb396dd73f6331c")

numberC = numberA.XOR(numberB)
print("XOR:", numberC.getHex())

numberC = numberA.OR(numberB)
print("OR:", numberC.getHex())

numberC = numberA.AND(numberB)
print("AND:", numberC.getHex())

numberC = numberA.INV()
print("INV:", numberC.getHex())

numberC = numberA.shiftR(5)
print("Shift Right:", numberC.getHex())

numberC = numberA.shiftL(3)
print("Shift Left:", numberC.getHex())

