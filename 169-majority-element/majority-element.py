class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occurrences = {}
        
        # Count occurrences of each element in the array
        for element in nums:
            # If the element is already in the dictionary, increment its count
            if element in occurrences:
                occurrences[element] += 1
            # If the element is not in the dictionary, add it with count 1
            else:
                occurrences[element] = 1

        def check_majority(d: dict, value):
            for key, count in d.items():  # Iterate over key-value pairs in the dictionary
                if count > value:  # Check if count exceeds the threshold value
                    return key
        
        # Calculate the threshold value
        value = len(nums) // 2
        
        # Return the majority element
        return check_majority(occurrences, value)
