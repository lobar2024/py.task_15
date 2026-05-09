import random

class SnakeGame:
    def __init__(self, rows=10, cols=10):
        self.rows, self.cols = rows, cols
        self.snake  = [(rows//2, cols//2)]
        self.direction = (0, 1)
        self.score  = 0
        self._place_food()

    def _place_food(self):
        empty = [(r,c) for r in range(self.rows)
                       for c in range(self.cols)
                       if (r,c) not in self.snake]
        self.food = random.choice(empty) if empty else None

    def turn(self, direction):
        dirs = {"UP":(-1,0),"DOWN":(1,0),"LEFT":(0,-1),"RIGHT":(0,1)}
        if direction in dirs:
            dr,dc = dirs[direction]
            cr,cc = self.direction
            if (dr,dc) != (-cr,-cc):  # teskari yo'nalish taqiqlangan
                self.direction = (dr,dc)

    def step(self):
        head = self.snake[0]
        new  = (head[0]+self.direction[0], head[1]+self.direction[1])

        if (new[0] < 0 or new[0] >= self.rows or
            new[1] < 0 or new[1] >= self.cols or
            new in self.snake):
            return "game_over"

        self.snake.insert(0, new)
        if new == self.food:
            self.score += 10
            self._place_food()
        else:
            self.snake.pop()
        return "ok"

    def display(self):
        for r in range(self.rows):
            row = ""
            for c in range(self.cols):
                if (r,c) == self.snake[0]: row += "H"
                elif (r,c) in self.snake:  row += "o"
                elif (r,c) == self.food:   row += "F"
                else:                      row += "."
            print(row)
        print(f"Score: {self.score}")

if __name__ == "__main__":
    game = SnakeGame(6, 6)
    moves = ["RIGHT","RIGHT","DOWN","DOWN","LEFT"]
    for m in moves:
        game.turn(m)
        status = game.step()
        if status == "game_over":
            print("O'yin tugadi!"); break
    game.display()
