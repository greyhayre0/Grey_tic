class GameLogic:
    """Класс для игровой логики и проверки условий"""

    def __init__(self, board):
        self.board = board
        self.current_player = 'X'
        self.game_over = False
        self.winner = None
        self.mode = "bot"  # Режим игры: "bot" или "2players"

    def check_win(self, player):
        """Проверяет, выиграл ли указанный игрок"""
        board = self.board.board

        # Проверка строк
        for i in range(3):
            if all(board[i][j] == player for j in range(3)):
                return True

        # Проверка столбцов
        for j in range(3):
            if all(board[i][j] == player for i in range(3)):
                return True

        # Проверка диагоналей
        if all(board[i][i] == player for i in range(3)):
            return True
        if all(board[i][2-i] == player for i in range(3)):
            return True

        return False

    def is_board_full(self):
        """Проверяет, заполнено ли поле"""
        for row in self.board.board:
            for cell in row:
                if cell == '':
                    return False
        return True

    def make_move(self, row, col):
        """Выполняет ход и проверяет условия игры"""
        if self.game_over or not self.board.is_cell_empty(row, col):
            return False

        # Выполняем ход
        success = self.board.make_move(row, col, self.current_player)
        if not success:
            return False

        # Проверяем победу
        if self.check_win(self.current_player):
            self.game_over = True
            self.winner = self.current_player
            color = "red" if self.current_player == 'X' else "blue"
            self.board.show_message(f"Победил {self.current_player}!", color)
            return True

        # Проверяем ничью
        if self.is_board_full():
            self.game_over = True
            self.board.show_message("Ничья!", "orange")
            return True

        # Смена игрока
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return True

    def switch_mode(self):
        """Переключает режим игры"""
        self.mode = "2players" if self.mode == "bot" else "bot"
        return self.mode

    def restart_game(self):
        """Перезапускает игру"""
        self.board.clear_board()
        self.current_player = 'X'
        self.game_over = False
        self.winner = None
        self.board.show_message("")

    def get_game_state(self):
        """Возвращает текущее состояние игры"""
        return {
            'current_player': self.current_player,
            'game_over': self.game_over,
            'winner': self.winner,
            'mode': self.mode
        }
