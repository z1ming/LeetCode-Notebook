给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。前三名运动员将会被分别授予 “金牌”，“银牌” 和“ 铜牌”（"Gold Medal", "Silver Medal", "Bronze Medal"）。

(注：分数越高的选手，排名越靠前。)

示例 1:

输入: [5, 4, 3, 2, 1]
输出: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
解释: 前三名运动员的成绩为前三高的，因此将会分别被授予 “金牌”，“银牌”和“铜牌” ("Gold Medal", "Silver Medal" and "Bronze Medal").
余下的两名运动员，我们只需要通过他们的成绩计算将其相对名次即可。

class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        dic = {}
        nums_sort = sorted(nums,reverse=True)
        for i in range(len(nums_sort)):
            if i == 0:
                dic[nums_sort[i]] = 'Gold Medal'
            elif i == 1:
                dic[nums_sort[i]] = 'Silver Medal'
            elif i == 2:
                dic[nums_sort[i]] = 'Bronze Medal'
            else:
                dic[nums_sort[i]] = str(i+1)
        for j in range(len(nums)):
            nums[j] = dic[nums[j]]
        return nums
