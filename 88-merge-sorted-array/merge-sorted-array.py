class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        # Merge nums2 into nums1
        nums1[m:] = nums2[:n]

        # Sort nums1 in-place
        nums1.sort()