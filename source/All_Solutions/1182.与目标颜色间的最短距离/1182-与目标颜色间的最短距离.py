class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        from bisect import bisect_left

        def take_closest(myList, myNumber):
            """
            myList为有序数组, 如何在有序数组中快速插入myNumber,
            并返回应该插入的索引位置
            """
            left, right = 0, len(myList)-1

            while left <= right:
                mid = (left + right) // 2

                # 如果找到合适位置, 返回
                if myList[mid] >= myNumber:
                    # 判断mid是否为0
                    if mid == 0:
                        return 0
                    elif myList[mid-1] < myNumber:
                        return mid
                    
                    right = mid - 1
                else:
                    left = mid + 1
            
            return left
                

        from collections import defaultdict
        from bisect import bisect_left
        color_index_dict = defaultdict(list)

        for ix, color in enumerate(colors):
            color_index_dict[color].append(ix)
        
        ans = []
        for query in queries:
            start = query[0]
            taregt_list = color_index_dict[query[1]]
            if len(taregt_list) == 0:
                ans.append(-1)
                continue

            # 二分查找
            return_index = take_closest(taregt_list, start)

            if return_index == 0:
                ans.append(abs(taregt_list[return_index]-start)) 
            elif return_index == len(taregt_list):
                ans.append(abs(taregt_list[-1] - start))
            elif taregt_list[return_index] - start > start - taregt_list[return_index-1]:
                ans.append(abs(start - taregt_list[return_index-1]))
            else:
                ans.append(abs(taregt_list[return_index] - start))        
        
        return ans


