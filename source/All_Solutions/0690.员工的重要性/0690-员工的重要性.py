class Solution:
    def getImportance(self, employees, id):

        importance = {e.id: e.importance for e in employees}        # 重要性字典{员工: 重要性}
        subordinates = {e.id: e.subordinates for e in employees}    # 下属字典{员工: 下属列表}

        def get_subordinates(id):                   # 获得员工的直接与间接下属
            all_staff = []                          # 结果列表
            queue = [id]                            # 申请队列
            while queue:                            # 只要队列不为空
                staff = queue.pop(0)                # 队尾元素出队
                all_staff.append(staff)             # 结果加入到结果列表中
                queue.extend(subordinates[staff])   # 该员工的下属批量入队
            return all_staff                        # 返回最终员工数量

        return sum([importance[staff] for staff in get_subordinates(id)]) 