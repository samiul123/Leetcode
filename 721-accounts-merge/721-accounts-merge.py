import uuid

class Solution:
    def getAdjList(self, accounts):
        self.adj_list = collections.defaultdict(list)
        
        for account in accounts:
            firstEmail = account[1]
            for i in range(2, len(account)):
                self.adj_list[firstEmail].append(account[i])
                self.adj_list[account[i]].append(firstEmail)

    
    def dfs(self, mergedAccount, email):
        self.visited.add(email)

        mergedAccount.append(email)

        for adj_email in self.adj_list[email]:
            if adj_email not in self.visited:
                self.dfs(mergedAccount, adj_email)
    
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj_list = self.getAdjList(accounts)
        
        self.visited = set()
        mergedAccounts = []
        
        
        for account in accounts:
            name = account[0]
            firstEmail = account[1]
            
            if firstEmail not in self.visited:
                mergedAccount = [name]
                self.dfs(mergedAccount, firstEmail)
                mergedAccount[1:] = sorted(mergedAccount[1:])
                mergedAccounts.append(mergedAccount)
        
        return mergedAccounts
        
        
                    