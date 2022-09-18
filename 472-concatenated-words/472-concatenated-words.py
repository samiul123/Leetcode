class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordSet = set(words)
        res = []
        
        def isConcatenated(word, wordSet, memo):
            if word in memo:
                return memo[word]
            
            if word == "":
                return True
            
            # for subWord in wordSet:
            #     if word.startswith(subWord):
            #         remaining = word[len(subWord):]
            #         if isConcatenated(remaining, wordSet, memo):
            #             memo[word] = True
            #             return True
            check = ""
            for i in range(len(word)):
                check += word[i]
                if check in wordSet:
                    remaining = word[len(check):]
                    if isConcatenated(remaining, wordSet, memo):
                        memo[word] = True
                        return True
                    
            memo[word] = False
            return False
        
        for word in wordSet:
            memo = {}
            wordSet.remove(word)
            if isConcatenated(word, wordSet, memo):
                res.append(word)
            wordSet.add(word)
        
        return res
        
        
#         wordSet = set(words)
#         print(wordSet)
#         res = set()
#         def helper(s):
#             print(s)
#             if not s: return True
            
#             check = ''
#             for i in range(len(s)):
#                 check += s[i]
#                 print("check: ", check)
#                 if check in wordSet:                    # Found the substring in wordSet
#                     if helper(s[i + 1:]): return True   # If you found this substring in wordSet then do recursion for the leftover string
                
#             return False
        
#         for word in wordSet:
#             print("word", word)
#             wordSet.remove(word)                        # We need to not match the word with itself
#             if helper(word): 
#                 print("Adding word: ", word)
#                 res.add(word)
#             wordSet.add(word)
#         return res