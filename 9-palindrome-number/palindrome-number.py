class Solution:

    def isPalindrome(self, x: int) -> bool:

        num = str(x)

        j = len(num)

        for i in range(j//2):

            if num[i] != num[-(i + 1)]:

                return False

        return True