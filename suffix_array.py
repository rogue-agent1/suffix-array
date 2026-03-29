#!/usr/bin/env python3
"""suffix_array - Suffix array construction and LCP array."""
import sys

def build_suffix_array(s):
    n = len(s)
    suffixes = sorted(range(n), key=lambda i: s[i:])
    return suffixes

def build_lcp(s, sa):
    n = len(s)
    rank = [0] * n
    for i, idx in enumerate(sa):
        rank[idx] = i
    lcp = [0] * n
    k = 0
    for i in range(n):
        if rank[i] == 0:
            k = 0
            continue
        j = sa[rank[i] - 1]
        while i + k < n and j + k < n and s[i + k] == s[j + k]:
            k += 1
        lcp[rank[i]] = k
        if k > 0:
            k -= 1
    return lcp

def search(s, sa, pattern):
    lo, hi = 0, len(sa) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        suffix = s[sa[mid]:]
        if suffix[:len(pattern)] == pattern:
            # find all occurrences
            results = [sa[mid]]
            for d in (-1, 1):
                i = mid + d
                while 0 <= i < len(sa) and s[sa[i]:sa[i]+len(pattern)] == pattern:
                    results.append(sa[i])
                    i += d
            return sorted(results)
        elif suffix[:len(pattern)] < pattern:
            lo = mid + 1
        else:
            hi = mid - 1
    return []

def test():
    s = "banana"
    sa = build_suffix_array(s)
    # suffixes sorted: a, ana, anana, banana, na, nana
    assert [s[i:] for i in sa] == ["a", "ana", "anana", "banana", "na", "nana"]
    lcp = build_lcp(s, sa)
    assert lcp[1] == 1  # a, ana share "a"
    assert lcp[2] == 3  # ana, anana share "ana"
    r = search(s, sa, "an")
    assert sorted(r) == [1, 3]  # "an" at positions 1 and 3
    assert search(s, sa, "xyz") == []
    print("OK: suffix_array")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test()
    else:
        print("Usage: suffix_array.py test")
