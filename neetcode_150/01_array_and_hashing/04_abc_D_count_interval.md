# ABC 233 D - Count Interval

[problem link](https://atcoder.jp/contests/abc233/tasks/abc233_d)


```python
import sys
from collections import Counter, defaultdict, deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(map(int, input().split()))


def si():
    return input().strip()


def main():
    NK = li()
    N = NK[0]
    K = NK[1]
    As = li()

    map = defaultdict(int) # (prefix_sum -> index_count)
    map[0] += 1
    cur_sum = 0
    ans = 0
    for i in range(len(As)):
        cur_sum += As[i]
        if (cur_sum - K) in map:
            ans += map[(cur_sum - K)]
        map[cur_sum] += 1
    print(ans)
    return



if __name__ == "__main__":
    main()
```
