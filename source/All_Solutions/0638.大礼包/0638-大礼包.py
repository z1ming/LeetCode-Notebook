class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        def shopping(special, needs):  # 从special里刚好购买needs所需的最低花费
            if not sum(needs):  # needs已没有
                return 0
            # 先过滤掉special里已经有某一种物品超过了needs的礼包
            special = list(filter(lambda x: all(x[i] <= needs[i] for i in range(l)), special))
            if not special:  # 如果过滤后为空，那么返回直接以单品购买needs的价格
                return sum(needs[i]*price[i] for i in range(l))
            res = []
            for pac in special:  # 回溯，收集本次购买每种礼包的花费加上若购买该礼包后剩余needs递归的最低花费
                res.append(pac[-1]+shopping(special, [needs[i]-pac[i] for i in range(l)]))
            return min(res)  # 返回本次购买的几种选择中的最低花费

        l = len(price)
        # 先过滤掉不比原价买划算的礼包
        special = list(filter(lambda x: x[-1] < sum(x[i]*price[i] for i in range(l)), special))
        return shopping(special, needs)