class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []
        
        for i in s:
            if i == '#':
                if stack_s:
                    stack_s.pop()
            else:
                stack_s.append(i)
                
        for i in t:
            if i == '#':
                if stack_t:
                    stack_t.pop()
            else:
                stack_t.append(i)
                
        while stack_s and stack_t:
            s_top = stack_s.pop()
            t_top = stack_t.pop()
            if s_top != t_top:
                return False
    
        
        if stack_s or stack_t:
            return False
        
        return True
                
        
        