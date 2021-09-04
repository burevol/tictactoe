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
    if field[x][y] == VOID:
        return True
    else:
        print("Неверный ход. Ячейка уже занята. Повторите ввод.")
        return False


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


def do_turn(message, symbol):
    draw_field()
    print(message)
    enter_coord(symbol)


def has_line(symbol):
    horizontal = {}
    vertical = {}
    for turn in turns[symbol]:
        if turn[0] in horizontal:
            horizontal[turn[0]] += 1
        else:
            horizontal[turn[0]] = 1

        if turn[1] in vertical:
            vertical[turn[1]] += 1
        else:
            vertical[turn[1]] = 1

    if 3 in horizontal.values() or 3 in vertical.values():
        return True

    return False


def check_win(message, symbol):
    if len(turns[CROSS]) + len(turns[NOUGHT]) == 9:
        print('Не осталось свободных клеток. Ничья!')
        return True
    if has_line(symbol):
        draw_field()
        print(message)
        return True
    return False


while True:
    do_turn('Ход первого игрока. Введите координаты через пробел.', CROSS)
    if check_win('Первый игрок выиграл!', CROSS):
        break
    do_turn('Ход второго игрока. Введите координаты через пробел.', NOUGHT)
    if check_win('Второй игрок выиграл!', NOUGHT):
        break
