# 假设Andy和Doris想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。
#
# 你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设总是存在一个答案。
#
# 示例 1:
#
# 输入:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# 输出: ["Shogun"]
# 解释: 他们唯一共同喜爱的餐厅是“Shogun”。
# 方法：使用哈希表
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hash = {}
        # 如果有多个共同的词，索引和相同且恰好为最小，那么一个key对应多个value，故采用列表实现
        str_list = []
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list2[j] == list1[i]:
                    if hash.get(i+j):
                        hash[i+j].append(list2[j])
                    else:
                        hash[i+j] = [list2[j]]
        min_key = len(list1) + len(list2)
        for k,value in hash.items():
            min_key = min(min_key,k)
        return hash[min_key]