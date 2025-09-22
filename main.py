import turtle
from ui import GameBoard
from logic import GameLogic
from bot import BotAI


class TicTacToeGame:
    """Основной класс игры, который объединяет все компоненты"""

    def __init__(self):
        self.board = GameBoard()
        self.game_logic = GameLogic(self.board)
        self.bot = BotAI(self.game_logic)

        # Настройка управления
        self.setup_controls()

    def setup_controls(self):
        """Настраивает управление игрой"""
        self.board.screen.onscreenclick(self.click_handler)
        self.board.screen.onkey(self.restart_game, "r")
        self.board.screen.onkey(self.switch_mode, "m")  # Переключение режима
        self.board.screen.listen()

        self.board.show_restart_hint()
        self.show_mode_hint()

    def show_mode_hint(self):
        """Показывает подсказку о режиме игры"""
        mode_pen = turtle.Turtle()
        mode_pen.speed(0)
        mode_pen.penup()
        mode_pen.hideturtle()
        mode_pen.goto(0, -240)
        mode_pen.color("green")
        mode_text = "Режим: против бота (M для смены)"
        if self.game_logic.mode == "2players":
            mode_text = "Режим: два игрока (M для смены)"
        mode_pen.write(mode_text, align="center", font=("Arial", 12, "normal"))

    def click_handler(self, x, y):
        """Обрабатывает клики мыши"""
        if self.game_logic.game_over:
            return

        cell = self.board.get_cell(x, y)
        if cell:
            row, col = cell

            # Игрок делает ход
            if self.game_logic.make_move(row, col):
                # Если игра с ботом и не закончена
                if (self.game_logic.mode == "bot" and 
                    not self.game_logic.game_over and 
                    self.game_logic.current_player == 'O'):

                    # Задержка для видимости хода бота
                    self.board.screen.ontimer(self.bot_move, 500)

    def bot_move(self):
        """Обрабатывает ход бота"""
        if (not self.game_logic.game_over and 
            self.game_logic.current_player == 'O'):
            self.bot.make_move()

    def switch_mode(self):
        """Переключает режим игры"""
        mode = self.game_logic.switch_mode()
        self.restart_game()

        # Обновляем подсказку
        for turtle in self.board.screen.turtles():
            if turtle.position() == (0, -240):
                turtle.clear()
                break

        self.show_mode_hint()

        mode_text = "против бота" if mode == "bot" else "два игрока"
        self.board.show_message(f"Режим: {mode_text}", "green")
        self.board.screen.ontimer(lambda: self.board.show_message(""), 1000)

    def restart_game(self):
        """Перезапускает игру"""
        self.game_logic.restart_game()

    def start(self):
        """Запускает игру"""
        turtle.mainloop()


# Запуск игры
if __name__ == "__main__":
    game = TicTacToeGame()
    game.start()
