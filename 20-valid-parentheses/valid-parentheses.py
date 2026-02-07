class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in "([{":
                stack.append(s[i])
            elif s[i] not in "([{":
                if not stack:
                    return False
                else:
                    pop_item = stack.pop()
                    if s[i] == ")" and pop_item != "(":
                        return False
                    if s[i] == "]" and pop_item != "[":
                        return False
                    if s[i] == "}" and pop_item != "{":
                        return False               
        return len(stack) == 0