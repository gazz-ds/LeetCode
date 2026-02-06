class Solution:
    def romanToInt(self, s: str) -> int:
        dict_val = {"I":1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = 0
        for i in range(len(s)):
            current = s[i]
            value1 = dict_val[current]
           
            if i < len(s)-1:
                preceding = s[i+1]
                value2 = dict_val[preceding]

                if value1 < value2:
                    sum -= value1
                else:
                    sum += value1
            else:
                sum += value1
        return sum