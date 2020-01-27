class SnakeGame:

    def __init__(self, width: int, height: int, food):
        self.snake = list()
        self.snake.append([0, 0])
        self.head = [0, 0]
        self.foods = food
        self.width = width
        self.height = height
        self.score = 0

    def move(self, direction: str) -> int:
        x, y = self.head
        if direction == 'U':
            x -= 1
        elif direction == 'L':
            y -= 1
        elif direction == 'R':
            y += 1
        elif direction == 'D':
            x += 1
        if x < 0 or y < 0 or x > self.height-1 or y > self.width - 1:
            return -1
        
        self.head = [x, y]
        self.snake = [self.head] + self.snake
        if self.foods and self.head == self.foods[0]:
            self.score += 1
            self.foods = self.foods[1:]
        else:
            self.snake = self.snake[:-1]
        if self.head in self.snake[1:]:
            return -1
        return self.score