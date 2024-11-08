class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bcount = [0] * 24
        for i in range(24):
            for num in candidates:
                if (num & (1 << i)) != 0:
                    bcount[i] += 1
                
        return max(bcount)