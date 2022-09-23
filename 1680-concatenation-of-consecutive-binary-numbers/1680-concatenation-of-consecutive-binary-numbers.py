# n = 3
# 123
# log1 + log2 + log3
# log(n!)

class Solution:
    def getBinaryNumber(self, decimalNumber: int, binary: list) -> int:
        if decimalNumber < 1:
            return 0
        self.getBinaryNumber(decimalNumber // 2, binary)
        binary.append(str(decimalNumber % 2))
        return "".join(binary)
    
    def getDecimalNumber(self, binaryNumber):
        number = 0
        length = len(binaryNumber)
        for i in range(length - 1, -1, -1):
            number += 2**(length - i - 1) * int(binaryNumber[i])
        return number
    
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        concatenation = "".join(bin(i)[2:] for i in range(n + 1))
        return int(concatenation, 2) % MOD
        # concatenatedBinary = []
        # for i in range(1, n+1):
        #     concatenatedBinary.append(self.getBinaryNumber(i, []))
        # concatenatedBinaryStr = "".join(concatenatedBinary)
        # return self.getDecimalNumber(concatenatedBinaryStr) % ((10**9)+7)
        