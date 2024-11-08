from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        # Calculate the maximum value with maximumBit bits
        max_xor = (1 << maximumBit) - 1
        xor_sum = 0
        result = []

        # Compute the initial XOR of all elements
        for num in nums:
            xor_sum ^= num

        # Process the queries in reverse
        for num in reversed(nums):
            # Find k that maximizes the XOR
            result.append(max_xor ^ xor_sum)
            # Update xor_sum by removing the last element
            xor_sum ^= num

        return result
