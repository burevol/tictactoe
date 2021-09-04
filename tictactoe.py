CROSS = 'x'
NOUGHT = 'o'
VOID = '-'

field = [[VOID for j in range(0, 3)] for i in range(0, 3)]
turns = {CROSS: [], NOUGHT: []}


def draw_field():
    print('  0 1 2 ')
    for j in range(0, 3):
        print(f'{j} {" ".join(field[j])}')


def check_correct_coord(x, y):
    if 0 <= x <= 2 and 0 <= y <= 2:
        return True
    else:
        print('Неверные координаты ячейки. Повторите ввод.')
        return False


def check_free_zone(x, y):
    if not field[x][y] == VOID:
        print("Неверный ход. Ячейка уже занята. Повторите ввод.")
        return False
    else:
        return True


def player_turn(x, y, symbol):
    if check_correct_coord(x, y) and check_free_zone(x, y):
        field[x][y] = symbol
        turns[symbol].append((x, y))
        return True
    else:
        return False


def enter_coord(symbol):
    while True:
        x, y = (map(int, (input().split())))
        if player_turn(x, y, symbol):
            break

def do_turn()

def check_win(symbol):
    return False


while True:
    draw_field()
    print('Ход первого игрока. Введите координаты через пробел.')
    enter_coord(CROSS)
    if check_win(CROSS):
        print("Первый игрок выиграл!")
        break
    draw_field()
    print('Ход второго игрока. Введите координаты через пробел.')
    enter_coord(NOUGHT)
    if check_win(NOUGHT):
        print("Второй игрок выиграл!")
