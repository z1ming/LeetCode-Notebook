class Solution:
    def solveEquation(self, equation: str) -> str:
        formula = equation.split("=")
        
        def get_count(formula):
            num_list = []
            pre_symbol = "+"
            x_count = 0
            num = 0
            for c in formula:
                # 不是运算符
                if c != "+" and c != "-":
                    if c == "x":
                        add_x = 1 if len(num_list) == 0 else int("".join(num_list))
                        if pre_symbol == "+":
                            x_count += add_x
                        else:
                            x_count -= add_x
                        num_list = [] # 清空列表
                    else:
                        # 是数字
                        num_list.append(c)
                # 是运算符
                else:
                    if len(num_list) != 0:
                        num = eval(str(num) + pre_symbol + "".join(num_list))
                    pre_symbol = c
                    num_list = []
            # 最后遗漏的数字
            if len(num_list) != 0:
                num = eval(str(num) + pre_symbol + "".join(num_list))
            return [x_count, num]
        
        left = get_count(formula[0])
        right = get_count(formula[1])

        x_count = left[0] - right[0]
        num = left[1] - right[1]
                
        # 计算结果
        if x_count == 0 and num == 0:
            return "Infinite solutions"
        if x_count == 0 and num != 0:
            return "No solution"
        return "x=" + str(-num // x_count)

