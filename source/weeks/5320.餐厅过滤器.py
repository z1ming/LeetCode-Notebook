# 给你一个餐馆信息数组 restaurants，其中  restaurants[i] = [idi, ratingi, veganFriendlyi, pricei, distancei]。你必须使用以下三个过滤器来过滤这些餐馆信息。
#
# 其中素食者友好过滤器 veganFriendly 的值可以为 true 或者 false，如果为 true 就意味着你应该只包括 veganFriendlyi 为 true 的餐馆，为 false 则意味着可以包括任何餐馆。此外，我们还有最大价格 maxPrice 和最大距离 maxDistance 两个过滤器，它们分别考虑餐厅的价格因素和距离因素的最大值。
#
# 过滤后返回餐馆的 id，按照 rating 从高到低排序。如果 rating 相同，那么按 id 从高到低排序。简单起见， veganFriendlyi 和 veganFriendly 为 true 时取值为 1，为 false 时，取值为 0 。
#
#  
#
# 示例 1：
#
# 输入：restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 1, maxPrice = 50, maxDistance = 10
# 输出：[3,1,5]
# 解释：
# 这些餐馆为：
# 餐馆 1 [id=1, rating=4, veganFriendly=1, price=40, distance=10]
# 餐馆 2 [id=2, rating=8, veganFriendly=0, price=50, distance=5]
# 餐馆 3 [id=3, rating=8, veganFriendly=1, price=30, distance=4]
# 餐馆 4 [id=4, rating=10, veganFriendly=0, price=10, distance=3]
# 餐馆 5 [id=5, rating=1, veganFriendly=1, price=15, distance=1]
# 在按照 veganFriendly = 1, maxPrice = 50 和 maxDistance = 10 进行过滤后，我们得到了餐馆 3, 餐馆 1 和 餐馆 5（按评分从高到低排序）。

class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        dic = {}
        for restaurant in restaurants:
            if veganFriendly == 0:
                if restaurant[3] <= maxPrice and restaurant[4] <= maxDistance:
                        dic[restaurant[0]] = restaurant[1]
            else:
                if restaurant[3] <= maxPrice and restaurant[4] <= maxDistance and restaurant[2] == 1:
                        dic[restaurant[0]] = restaurant[1]
        res = []
        # 按照 rating 从高到低排序。如果 rating 相同，那么按 id 从高到低排序。
        dic = sorted(dic.items(), key = lambda x:[x[1],x[0]],reverse=True)
        for i in dic:
            res.append(i[0])
        return res

