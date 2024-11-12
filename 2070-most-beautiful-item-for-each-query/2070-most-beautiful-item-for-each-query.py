from typing import List
from bisect import bisect_right

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # Step 1: Sort items based on price
        items.sort()
        
        # Step 2: Create a prefix max array for beauty
        max_beauty = []
        current_max = 0
        for price, beauty in items:
            current_max = max(current_max, beauty)
            max_beauty.append((price, current_max))
        
        # Step 3: Sort queries and keep track of original indices
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
        result = [0] * len(queries)
        
        # Step 4: Use binary search to find the maximum beauty for each query
        for index, query in sorted_queries:
            # Use binary search to find the rightmost item with price <= query
            pos = bisect_right(max_beauty, (query, float('inf'))) - 1
            if pos >= 0:
                result[index] = max_beauty[pos][1]
        
        return result
