import random


class BotAI:
    """Класс для искусственного интеллекта бота"""

    def __init__(self, game_logic):
        self.game_logic = game_logic
        self.board = game_logic.board

    def find_best_move(self):
        """Находит лучший ход для бота"""
        board = self.board.board

        # 1. Проверяем, может ли бот выиграть
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'O'
                    if self.game_logic.check_win('O'):
                        board[i][j] = ''
                        return i, j
                    board[i][j] = ''

        # 2. Блокируем выигрыш игрока
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'X'
                    if self.game_logic.check_win('X'):
                        board[i][j] = ''
                        return i, j
                    board[i][j] = ''

        # 3. Занимаем центр, если свободен
        if board[1][1] == '':
            return 1, 1

        # 4. Занимаем углы
        corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
        random.shuffle(corners)
        for i, j in corners:
            if board[i][j] == '':
                return i, j

        # 5. Любая свободная клетка
        empty_cells = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    empty_cells.append((i, j))

        if empty_cells:
            return random.choice(empty_cells)

        return None

    def make_move(self):
        """Бот делает ход"""
        if self.game_logic.game_over or self.game_logic.current_player != 'O':
            return False

        move = self.find_best_move()
        if move:
            row, col = move
            return self.game_logic.make_move(row, col)

        return False
