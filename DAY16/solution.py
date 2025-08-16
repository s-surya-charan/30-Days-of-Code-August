class Solution:
    def maximum69Number (self, num: int) -> int:
        num_array = list(str(num))

        for i in range(len(num_array)):
            if num_array[i] == '6':
                num_array[i] = '9'
                break
        return int("".join(num_array))
        