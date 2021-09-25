CROSS = 'x'
NOUGHT = 'o'
VOID = '-'


class BoardException(Exception):
    pass


class OutOfBoardException(BoardException):
    pass


class CellAlreadyUsedException(BoardException):
    pass


class WrongInputException(Exception):
    pass


class NoMoreTurnsException(Exception):
    pass


class Dot:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Board:
    def __init__(self):
        self.field = [[VOID for _ in range(0, 3)] for _ in range(0, 3)]
        self.turns = {CROSS: [], NOUGHT: []}

    def __str__(self):
        brd = '  0 1 2 \n'
        for j in range(0, 3):
            brd += f'{j} {" ".join(self.field[j])}\n'
        return brd

    def check_correct_turn(self, dot):
        if not (0 <= dot.x <= 2 and 0 <= dot.y <= 2):
            raise OutOfBoardException
        if dot in self.turns[CROSS] or dot in self.turns[NOUGHT]:
            raise CellAlreadyUsedException

    def set_point(self, dot, symbol):
        self.field[dot.x][dot.y] = symbol
        self.turns[symbol].append(dot)
        win = self.has_line(symbol)
        if not win and len(self.turns[CROSS]) + len(self.turns[NOUGHT]) == 9:
            raise NoMoreTurnsException
        return win

    def has_line(self, symbol):
        horizontal = {}
        vertical = {}

        diagonal1 = 0
        diagonal2 = 0

        for turn in self.turns[symbol]:
            if turn.x in horizontal:
                horizontal[turn.x] += 1
            else:
                horizontal[turn.x] = 1

            if turn.y in vertical:
                vertical[turn.y] += 1
            else:
                vertical[turn.y] = 1

            if turn.x == turn.y:
                diagonal1 += 1

            if turn.x + turn.y == 2:
                diagonal2 += 1

        if 3 in horizontal.values() or 3 in vertical.values():
            return True
        elif diagonal1 == 3 or diagonal2 == 3:
            return True

        return False


class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = CROSS
        self.players = {CROSS: 'первый', NOUGHT: 'второй'}

    def start_game(self):
        Game.greet()
        self.game_loop()

    def do_turn(self):
        while True:
            try:
                turn = self.enter_coord()
            except WrongInputException as ex:
                print(ex)
            except OutOfBoardException:
                print('Вы вышли за границы доски, повторите ввод')
            except CellAlreadyUsedException:
                print('Точка уже занята, повторите ввод')
            else:
                return self.board.set_point(turn, self.current_player)

    def enter_coord(self):
        coord = input().split()
        if len(coord) != 2:
            raise WrongInputException('Неверное количество параметров')
        elif not (coord[0].isdigit() and coord[1].isdigit()):
            raise WrongInputException('Должны быть введены цифры')
        else:
            dot = Dot(int(coord[0]), int(coord[1]))
            self.board.check_correct_turn(dot)
            return dot

    def game_loop(self):
        while True:
            print(self.board)
            print(f'Ходит {self.players[self.current_player]} игрок. Введите координаты через пробел:')
            try:
                if self.do_turn():
                    print(f'{self.players[self.current_player].capitalize()} игрок выиграл!')
                    print(self.board)
                    break
            except NoMoreTurnsException:
                print(self.board)
                print("Больше ходов не осталось!")
                break
            self.current_player = NOUGHT if self.current_player == CROSS else CROSS

    @staticmethod
    def greet():
        print('-----------------------------------------------')
        print('---Добро пожаловать в игру "Крестики-нолики"---')
        print('---Для хода введите номер строки и ------------')
        print('--------номер столбца через пробел-------------')
        print('-----------------------------------------------')


if __name__ == '__main__':
    game = Game()
    game.start_game()
