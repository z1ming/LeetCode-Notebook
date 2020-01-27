class Solution:
    def parseTernary(self, expression: str) -> str:
        if len(expression) == 1:
            return expression
        condition = expression[0]
        position = 2
        left_count = 1
        while position < len(expression):
            if expression[position] == "?":
                left_count += 1
            elif expression[position] == ":":
                left_count -= 1
            if left_count == 0:
                break
            position += 1
        if condition == "T":
            return self.parseTernary(expression[2:position])
        else:
            return self.parseTernary(expression[position + 1:])


