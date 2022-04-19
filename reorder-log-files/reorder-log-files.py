class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        contentIdMap = collections.defaultdict(list)
        for log in logs:
            words = log.split(maxsplit=2)
            if words[1].isalpha():
                contentIdMap[" ".join(words[1:len(words)])].append(words[0])
        
        # print(contentIdMap)
        
        for key in contentIdMap:
            if len(contentIdMap[key]) > 0:
                contentIdMap[key] = sorted(contentIdMap[key])
        # print(contentIdMap)
        
        reorderedLogs = []
        for key in sorted(contentIdMap):
            for id in contentIdMap[key]:
                reorderedLogs.append(id + " " + key)
            
        
        for log in logs:
            words = log.split(maxsplit=2)
            if words[1].isdigit():
                reorderedLogs.append(log)
        
        # print(reorderedLogs)
        return reorderedLogs
        