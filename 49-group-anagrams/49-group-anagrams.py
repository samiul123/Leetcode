class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        
        for idx, str in enumerate(strs):
            sortedStr = tuple(sorted(str))
            
            if sortedStr in dic:
                dic[sortedStr].append(str)
            else:
                dic[sortedStr] = [str]
            
        return dic.values()