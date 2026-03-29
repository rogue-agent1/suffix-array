#!/usr/bin/env python3
"""Suffix array construction. Zero dependencies."""

def build_suffix_array(s):
    n = len(s)
    sa = list(range(n))
    sa.sort(key=lambda i: s[i:])
    return sa

def build_lcp_array(s, sa):
    n = len(s)
    rank = [0] * n
    for i, idx in enumerate(sa): rank[idx] = i
    lcp = [0] * n
    k = 0
    for i in range(n):
        if rank[i] == 0: k = 0; continue
        j = sa[rank[i] - 1]
        while i + k < n and j + k < n and s[i+k] == s[j+k]: k += 1
        lcp[rank[i]] = k
        if k: k -= 1
    return lcp

def search_suffix_array(s, sa, pattern):
    lo, hi = 0, len(sa) - 1
    matches = []
    while lo <= hi:
        mid = (lo + hi) // 2
        suffix = s[sa[mid]:]
        if suffix[:len(pattern)] == pattern:
            # Found, expand both directions
            matches.append(sa[mid])
            i = mid - 1
            while i >= 0 and s[sa[i]:sa[i]+len(pattern)] == pattern:
                matches.append(sa[i]); i -= 1
            i = mid + 1
            while i < len(sa) and s[sa[i]:sa[i]+len(pattern)] == pattern:
                matches.append(sa[i]); i += 1
            return sorted(matches)
        elif suffix[:len(pattern)] < pattern: lo = mid + 1
        else: hi = mid - 1
    return []

if __name__ == "__main__":
    s = "banana"
    sa = build_suffix_array(s)
    print("SA:", sa)
    print("Suffixes:", [s[i:] for i in sa])
