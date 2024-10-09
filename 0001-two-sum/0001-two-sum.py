class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the value and index of numbers
        num_map = {}
        
        # Iterate through the list
        for i, num in enumerate(nums):
            # Calculate the difference needed to reach the target
            diff = target - num
            
            # If the difference is already in the map, return the indices
            if diff in num_map:
                return [num_map[diff], i]
            
            # Otherwise, store the current number and its index in the map
            num_map[num] = i
