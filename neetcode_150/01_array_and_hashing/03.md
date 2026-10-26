# Leetcode 347 - Top K Frequent Elements

[problem link](https://leetcode.com/problems/top-k-frequent-elements/)


```python
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        _map = Counter(nums)
        heap = []
        for ke, va in _map.items():
            heapq.heappush(heap, (va, ke))
            if len(heap) > k:
                heapq.heappop(heap)
        return [v[1] for v in heap]
```
