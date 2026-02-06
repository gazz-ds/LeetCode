class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 1. Handle edge case: if the list is empty, there is no prefix
        if not strs:
            return ""
        
        # 2. Find the shortest string to avoid going out of bounds
        # We only need to check as many letters as the shortest word has
        shortest_word = min(strs, key=len)
        
        # 3. Outer loop: Iterate through each character index of the shortest word
        for i in range(len(shortest_word)):
            
            # 4. Grab the "target" letter from the first string at the current index
            letter_match = strs[0][i]
            
            # 5. Inner loop: Compare this "target" letter with the same index in all other strings
            # We start at index 1 because we don't need to compare the first string to itself
            for j in range(1, len(strs)):
                
                # 6. Check if the character in the current string matches our target
                if strs[j][i] != letter_match:
                    
                    # 7. If they DON'T match, the prefix ends right before this index
                    # Return the slice of the string from the start up to (but not including) i
                    return strs[0][:i]
        
        # 8. If the loops finish, it means every character in shortest_word matched perfectly
        return shortest_word