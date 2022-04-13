class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        result = []
        
        for idx, str in enumerate(strs):
            sortedStr = "".join(sorted(str))
            
            if sortedStr in dic:
                dic[sortedStr].append(str)
            else:
                dic[sortedStr] = [str]
        
        for key in dic:
            result.append(dic[key])
            
        return result