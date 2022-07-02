class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        
        if len(A) > len(B):
            A, B = B, A
            
        total = len(A) + len(B)
        half = total // 2
        start_a, end_a = 0, len(A) - 1
        
        while True:
            mid_a = (start_a + end_a) // 2
            mid_b = half - mid_a - 2
            
            a_left = A[mid_a] if mid_a >= 0 else - math.inf
            a_right = A[mid_a + 1] if (mid_a+1) < len(A) else math.inf
            b_left = B[mid_b] if mid_b >= 0 else - math.inf
            b_right = B[mid_b + 1] if (mid_b+1) < len(B) else math.inf
            
            if a_left <= b_right and a_right >= b_left:
                if total % 2:
                    return min(a_right, b_right)
                else:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2
            elif a_left > b_right:
                end_a = mid_a - 1
            else:
                start_a = mid_a + 1
            