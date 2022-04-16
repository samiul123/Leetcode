class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        left = 0
        right = 0
        
        bannedSet = set()
        for word in banned:
            bannedSet.add(word)
        
        # specialChars = set(" ", "!", "?", "'", ",", ";", ".")
        specialChars = set(" !?',;.")
        wordCount = collections.defaultdict(int)
        maxFrequency = - math.inf
        maxFrequentWord = ""
        
        while right < len(paragraph):
            currChar = paragraph[right]
            
            # print("CurrChar: {}".format(currChar))
            # print("specialChars: ", specialChars)
            
            if currChar in specialChars:
                currWord = paragraph[left:right].lower()
                # print("Left: {}, Right: {}, CurrWord: {}".format(left, right, currWord))
                if currWord not in bannedSet:
                    wordCount[currWord] += 1
                    if wordCount[currWord] > maxFrequency:
                        maxFrequency = wordCount[currWord]
                        maxFrequentWord = currWord
                    # print("MaxFrequency: {}, MaxFrequentWord: {}".format(maxFrequency, maxFrequentWord))
                
                # if right == len(paragraph) - 1 and currChar not in specialChars:
                #     right += 1
                #     continue
                
                if currChar == ' ':
                    right += 1
                else:
                    while right < len(paragraph) and paragraph[right] != " ":
                        right += 1
                    right += 1
                left = right
            elif right == len(paragraph) - 1:
                currWord = paragraph[left:right+1].lower()
                # print("Left: {}, Right: {}, CurrWord: {}".format(left, right, currWord))
                if currWord not in bannedSet:
                    wordCount[currWord] += 1
                    if wordCount[currWord] > maxFrequency:
                        maxFrequency = wordCount[currWord]
                        maxFrequentWord = currWord
                right += 1
            else:
                right += 1    
        
        return maxFrequentWord