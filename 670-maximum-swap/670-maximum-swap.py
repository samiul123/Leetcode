class Solution:
    def maximumSwap(self, num: int) -> int:
        numStr = list(str(num))
        maxDigitIdx = -1
        lIdx = -1
        rIdx = -1
        maxDigit = -1
        
        for i in range(len(numStr)-1, -1, -1):
            if int(numStr[i]) > maxDigit:
                maxDigitIdx = i
                maxDigit = int(numStr[i])
                continue
            
            if int(numStr[i]) < maxDigit:
                lIdx = i
                rIdx = maxDigitIdx
        
        if lIdx == -1:
            return num
        
        numStr[lIdx], numStr[rIdx] = numStr[rIdx], numStr[lIdx]
        
        return int("".join(numStr))
        
        
            
        