# frequency_t -> store frequency of letters in t
# have to maintain a window in s which contains letters as many as in t
# if window maintains this property while being shrinked, have to update 
#    the minWindow size
# Otherwise, expand the window
# finally return the substring which corresponds to the minWindow size

# Here I am only storing frequency of letters in t
# In Worst case,it will be O(t) + O(s) (which is basically same as O(t))
# So, Overall O(t)

# TIme complexity -> O(t+2s) -> 2 because both left and right pointer may come 
# across same character 
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_t_frequency = collections.defaultdict(int)
        for char in t:
            char_t_frequency[char] += 1
        
        left, right = 0, 0
        # (size, left, right)
        min_window = (math.inf, 0, 0)
        char_window_frequency = collections.defaultdict(int)
        formation_progress = 0
        
        while right < len(s):
            if s[right] in char_t_frequency:
                char_window_frequency[s[right]] += 1
                
                if char_window_frequency[s[right]] == char_t_frequency[s[right]]:
                    formation_progress += 1
                    
            while left <= right and formation_progress == len(char_t_frequency):
                if s[left] in char_window_frequency:
                    current_window_size = right - left + 1
                    if current_window_size < min_window[0]:
                        min_window = (current_window_size, left, right)

                    char_window_frequency[s[left]] -= 1

                    if char_window_frequency[s[left]] < char_t_frequency[s[left]]:
                        formation_progress -= 1
                left += 1
            right += 1
        
        return "" if min_window[0] == math.inf else s[min_window[1]:min_window[2]+1]
                
                