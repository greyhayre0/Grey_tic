import turtle


class GameBoard:
    """Класс для отрисовки и управления игровым полем"""

    def __init__(self):
        # Настройка экрана
        self.screen = turtle.Screen()
        self.screen.title("Крестики-нолики")
        self.screen.setup(500, 500)
        self.screen.bgcolor("white")

        # Игровое поле 3x3
        self.board = [['' for _ in range(3)] for _ in range(3)]

        # Настройка черепашек
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.hideturtle()

        self.text_pen = turtle.Turtle()
        self.text_pen.speed(0)
        self.text_pen.hideturtle()

        self.draw_board()

    def draw_board(self):
        """Рисует игровое поле"""
        self.pen.pensize(5)
        self.pen.color("black")

        # Вертикальные линии
        for i in range(1, 3):
            self.pen.penup()
            self.pen.goto(-150 + i * 100, -150)
            self.pen.pendown()
            self.pen.goto(-150 + i * 100, 150)

        # Горизонтальные линии
        for i in range(1, 3):
            self.pen.penup()
            self.pen.goto(-150, -150 + i * 100)
            self.pen.pendown()
            self.pen.goto(150, -150 + i * 100)

    def draw_x(self, row, col):
        """Рисует крестик в указанной клетке"""
        x = -100 + col * 100
        y = 100 - row * 100

        self.pen.color("red")
        self.pen.pensize(8)

        # Первая диагональ
        self.pen.penup()
        self.pen.goto(x - 30, y - 30)
        self.pen.pendown()
        self.pen.goto(x + 30, y + 30)

        # Вторая диагональ
        self.pen.penup()
        self.pen.goto(x + 30, y - 30)
        self.pen.pendown()
        self.pen.goto(x - 30, y + 30)

    def draw_o(self, row, col):
        """Рисует нолик в указанной клетке"""
        x = -100 + col * 100
        y = 100 - row * 100

        self.pen.color("blue")
        self.pen.pensize(8)

        self.pen.penup()
        self.pen.goto(x, y - 30)
        self.pen.pendown()
        self.pen.circle(30)

    def get_cell(self, x, y):
        """Определяет, в какую клетку попал клик"""
        if -150 <= x <= 150 and -150 <= y <= 150:
            col = (x + 150) // 100
            row = (150 - y) // 100
            return int(row), int(col)
        return None

    def is_cell_empty(self, row, col):
        """Проверяет, свободна ли клетка"""
        return self.board[row][col] == ''

    def make_move(self, row, col, player):
        """Выполняет ход и рисует символ"""
        if not self.is_cell_empty(row, col):
            return False

        self.board[row][col] = player

        if player == 'X':
            self.draw_x(row, col)
        else:
            self.draw_o(row, col)

        return True

    def clear_board(self):
        """Очищает игровое поле"""
        self.screen.clear()
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.pen.reset()
        self.pen.speed(0)
        self.pen.hideturtle()
        self.text_pen.reset()
        self.text_pen.speed(0)
        self.text_pen.hideturtle()
        self.draw_board()

    def show_message(self, message, color="black"):
        """Показывает сообщение на экране"""
        self.text_pen.clear()
        self.text_pen.penup()
        self.text_pen.goto(0, 200)
        self.text_pen.color(color)
        self.text_pen.write(message, align="center", font=("Arial", 20, "bold"))

    def show_restart_hint(self):
        """Показывает подсказку о перезапуске"""
        restart_pen = turtle.Turtle()
        restart_pen.speed(0)
        restart_pen.penup()
        restart_pen.hideturtle()
        restart_pen.goto(0, -220)
        restart_pen.color("purple")
        restart_pen.write("Нажмите R для перезапуска", align="center", 
                         font=("Arial", 12, "normal"))
