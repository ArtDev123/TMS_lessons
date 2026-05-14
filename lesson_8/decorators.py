class Solution:
    @staticmethod
    def reverse(x: int) -> int:
        if x <= (-(2**31)) or x >= (2**31 - 1):
            return 0
        x = reversed([char for char in str(x)])
        res = ""

        zero_condition: bool = True

        for char in x:
            if char == "0" and zero_condition:
                continue

            zero_condition = True
            res += char

        return res


print(Solution.reverse(100))
