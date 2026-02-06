class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        shortest_word = min(strs, key=len)
        
        for i in range(len(shortest_word)):
            letter_match = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != letter_match:
                    return strs[0][:i]
        return shortest_word
