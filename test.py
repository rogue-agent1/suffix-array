from suffix_array import build_suffix_array, build_lcp_array, search_suffix_array
s = "banana"
sa = build_suffix_array(s)
suffixes = [s[i:] for i in sa]
assert suffixes == sorted(suffixes)
lcp = build_lcp_array(s, sa)
assert lcp[0] == 0  # first has no predecessor
matches = search_suffix_array(s, sa, "ana")
assert sorted(matches) == [1, 3]
assert search_suffix_array(s, sa, "xyz") == []
assert search_suffix_array(s, sa, "ban") == [0]
print("suffix_array tests passed")
