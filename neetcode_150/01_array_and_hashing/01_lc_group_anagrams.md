# Leetcode 49 - Group Anagrams

[leetcode link](https://leetcode.com/problems/group-anagrams/description/)

```python
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        memo = defaultdict(list)
        for s in strs:
            keys = [0] * 26
            for l in s:
                keys[ord(l) - ord('a')] += 1
            memo[tuple(keys)].append(s)
        return list(memo.values())
```
