class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for idx, num in enumerate(nums):
            remaining = target - num
            if remaining in visited:
                return [idx, visited[remaining]]
            visited[num] = idx
        return []
