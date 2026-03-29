#!/usr/bin/env python3
"""Suffix array construction and LCP array."""
import sys

def build_suffix_array(s):
    n = len(s)
    sa = sorted(range(n), key=lambda i: s[i:])
    return sa

def build_lcp(s, sa):
    n = len(s)
    rank = [0]*n
    for i, si in enumerate(sa):
        rank[si] = i
    lcp = [0]*n
    k = 0
    for i in range(n):
        if rank[i] == 0:
            k = 0
            continue
        j = sa[rank[i]-1]
        while i+k < n and j+k < n and s[i+k] == s[j+k]:
            k += 1
        lcp[rank[i]] = k
        if k: k -= 1
    return lcp

def search(s, sa, pattern):
    lo, hi = 0, len(sa)
    while lo < hi:
        mid = (lo+hi)//2
        if s[sa[mid]:sa[mid]+len(pattern)] < pattern:
            lo = mid+1
        else:
            hi = mid
    start = lo
    hi = len(sa)
    while lo < hi:
        mid = (lo+hi)//2
        if s[sa[mid]:sa[mid]+len(pattern)] <= pattern:
            lo = mid+1
        else:
            hi = mid
    return [sa[i] for i in range(start, lo)]

def test():
    s = "banana"
    sa = build_suffix_array(s)
    suffixes = [s[i:] for i in sa]
    assert suffixes == sorted(suffixes)
    lcp = build_lcp(s, sa)
    r = search(s, sa, "ana")
    assert sorted(r) == [1, 3]
    r2 = search(s, sa, "xyz")
    assert r2 == []
    print("  suffix_array: ALL TESTS PASSED")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test": test()
    else: print("Suffix array + LCP")
