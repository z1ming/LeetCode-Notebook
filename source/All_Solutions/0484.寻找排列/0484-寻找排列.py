class Solution:
    def findPermutation(self, s: str) -> List[int]:
        nums = list(range(1, len(s) + 2))
        i = 0
        while i < len(s):
            if s[i] == "D":
                start = i
                for j in range(i, len(s)):
                    if s[j] == "D" and (j == len(s) - 1 or s[j+1] == "I"):
                        end = j + 1
                        i = end + 1
                        break
                nums[start:end + 1] = list(reversed(nums[start:end + 1]))
            else:
                i += 1

        return nums