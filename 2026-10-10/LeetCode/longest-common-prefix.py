class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort()
        prifix = ""
        first = strs[0]
        last = strs[len(strs)-1]
        size = min(len(first), len(last))
        for i in range(size):
            if first[i] == last[i]:
                prifix += first[i]
            else:
                return prifix
        return prifix