# 最大级深maxLevl=16，power=2分链表，随机数的上限maxRand
maxLevel = 16
power = 2
maxRand = power ** maxLevel - 1
# 随机函数，这里就相当于[1 ... 65535]取随机，然后再对2取对数，可保证插入深度在[1 ... 16]这些数字里呈指数分布
randLevel = lambda: maxLevel - int(math.log(random.randint(1, maxRand), power))

# 三个属性，跳表本体的值，向右的指针，向下的指针
class SkipNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.down = None

class Skiplist:
    def __init__(self):
        # 初始化左右正负无穷墙壁
        left = [SkipNode(-float('inf')) for _ in range(maxLevel)]
        right = [SkipNode(float('inf')) for _ in range(maxLevel)]
        # 把墙壁交联在一起
        for i in range(maxLevel - 1):
            left[i].right = right[i]
            left[i].down = left[i + 1]
            right[i].down = right[i + 1]
        # 最后一层单独处理，只有向右指向，没有向下指向
        left[-1].right = right[-1]
        # 跳表初始指针为左壁的首元素
        self.head = left[0]

    def search(self, target: int) -> bool:
        # 从初始指针开始进行跳跃迭代，找不到的node迟早为None，跳出循环自动返回None，线上测试和False等价
        node = self.head
        while node:
            if node.right.value > target:
                node = node.down
            elif node.right.value < target:
                node = node.right
            else:
                return True

    def add(self, num: int) -> None:
        # 用prev数组存储往下跳跃前的跳表指针，方便之后插入指针时前后交联，免去双向指针处理
        prev = []
        # 原理依旧是指针迭代
        node = self.head
        while node:
            # 碰到右边大于等于自己时就往下跳，帮助prev生成完整的指针数组
            if node.right.value >= num:
                prev.append(node)
                node = node.down
            else:
                node = node.right
        # 待插入的指针数组，长度按概率进行随机
        arr = [SkipNode(num) for _ in range(randLevel())]
        # 用zip把prev后续的元素与新的指针数组交联在一次即可完成跳表插入
        t = SkipNode(None)
        for p, a in zip(prev[maxLevel - len(arr): ], arr):
            a.right = p.right
            p.right = a
            t.down = a
            t = a

    def erase(self, num: int) -> bool:
        # ans为输出标志，erase的结构和search结构类似，依旧是指针迭代
        ans = False
        node = self.head
        while node:
            if node.right.value > num:
                node = node.down
            elif node.right.value < num:
                node = node.right
            else:
                # 存在相等时就修改输出标志
                ans = True
                # 删除node.right的在跳表中的关系
                node.right = node.right.right
                node = node.down
        return ans

