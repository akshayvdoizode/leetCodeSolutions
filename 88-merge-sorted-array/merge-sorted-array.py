class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
       nums1[m:] = nums2
       nums1.sort() 
       nums1 = [num for num in nums1 if num != 0]
        