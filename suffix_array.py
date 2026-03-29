#!/usr/bin/env python3
"""Suffix array construction and LCP array."""
import sys

def build_suffix_array(text):
    n = len(text)
    suffixes = sorted(range(n), key=lambda i: text[i:])
    return suffixes

def build_lcp(text, sa):
    n = len(text); rank = [0] * n; lcp = [0] * n
    for i, s in enumerate(sa): rank[s] = i
    k = 0
    for i in range(n):
        if rank[i] == 0: k = 0; continue
        j = sa[rank[i] - 1]
        while i + k < n and j + k < n and text[i+k] == text[j+k]: k += 1
        lcp[rank[i]] = k
        if k > 0: k -= 1
    return lcp

def search(text, sa, pattern):
    lo, hi = 0, len(sa)
    while lo < hi:
        mid = (lo + hi) // 2
        if text[sa[mid]:sa[mid]+len(pattern)] < pattern: lo = mid + 1
        else: hi = mid
    start = lo; hi = len(sa)
    while lo < hi:
        mid = (lo + hi) // 2
        if text[sa[mid]:sa[mid]+len(pattern)] <= pattern: lo = mid + 1
        else: hi = mid
    return [sa[i] for i in range(start, lo)]

def longest_repeated(text, sa, lcp):
    if not lcp: return ""
    mx = max(range(len(lcp)), key=lambda i: lcp[i])
    return text[sa[mx]:sa[mx]+lcp[mx]]

def main():
    if len(sys.argv) < 2: print("Usage: suffix_array.py <demo|test>"); return
    if sys.argv[1] == "test":
        sa = build_suffix_array("banana")
        assert sa == [5, 3, 1, 0, 4, 2]  # a, ana, anana, banana, na, nana
        lcp = build_lcp("banana", sa)
        assert lcp[2] == 3  # ana shared
        results = search("banana", sa, "an")
        assert sorted(results) == [1, 3]
        assert search("banana", sa, "xyz") == []
        lr = longest_repeated("banana", sa, lcp)
        assert lr == "ana"
        sa2 = build_suffix_array("aaa")
        assert sa2 == [2, 1, 0]
        print("All tests passed!")
    else:
        text = sys.argv[2] if len(sys.argv) > 2 else "banana"
        sa = build_suffix_array(text)
        lcp = build_lcp(text, sa)
        print(f"SA: {sa}"); print(f"LCP: {lcp}")
        print(f"Longest repeated: {longest_repeated(text, sa, lcp)!r}")

if __name__ == "__main__": main()
