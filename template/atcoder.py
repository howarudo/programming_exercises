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
    n = ii()
    a = li()

    print(sum(a) - n)
    print(*[x - 1 for x in a])

if __name__ == "__main__":
    main()
