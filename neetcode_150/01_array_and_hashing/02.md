# ABC 206 C - Swappable

[problem link](https://atcoder.jp/contests/abc206/tasks/abc206_c)


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
    N = ii()
    As = li()

    counter = defaultdict(int)
    ans = 0
    for i in range(len(As)):
        ans += i
        ans -= counter[As[i]]
        counter[As[i]] += 1
    print(ans)
    return

if __name__ == "__main__":
    main()
```
