class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n_row = len(board)
        n_col = len(board[0])
        visited = [[False for col in range(n_col)] for row in range(n_row)]
        search_idx = 0
        
        for i in range(n_row):
            for j in range(n_col):
                if board[i][j] != word[search_idx]:
                    continue
                if self.traverse(board, i, j, word, search_idx, visited):
                    return True
        return False
    
    
    def traverse(self, board, row, col, word, search_idx, visited):
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[row] or search_idx >= len(word)):
            return False
        
        if board[row][col] != word[search_idx]:
            return False
        
        if visited[row][col]:
            return False
        
        visited[row][col] = True
        
        if search_idx == len(word) - 1:
            return True
        
        if self.traverse(board, row+1, col, word, search_idx + 1, visited):
            return True
        if self.traverse(board, row-1, col, word, search_idx + 1, visited):
            return True
        if self.traverse(board, row, col+1, word, search_idx + 1, visited):
            return True
        if self.traverse(board, row, col-1, word, search_idx + 1, visited):
            return True
        
        visited[row][col] = False