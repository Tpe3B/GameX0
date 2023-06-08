def greet():

    print("Приветствуем игроков в игре")
    print("Крестики-Нолики")
    print("-------------------")
    print("Формат ввода: Координаты X и Y")

def show():
    print()
    print("   | 0 | 1 | 2 | ")
    print("----------------")
    for i, row in enumerate(field):
        row_str = f" {i} | {' | '.join(row)} | "
        print(row_str)
        print("----------------")
    print()
def ask():
    while True:
        cords = input("Ваш ход: ").split()
        if len(cords) != 2:
            print("Введите 2 координаты:")
            continue

        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите 2 координаты:")
            continue

        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты вне игрового поля:")
            continue

        if field[x][y] != " ":
            print("Клетка уже занята")
            continue

        return x, y
def check_win():
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[i][j])
        if symbols == ["X", "X", "X"]:
            print('Победил Х')
            return True
        if symbols == ["0", "0", "0"]:
            print('Победил 0')
            return True

    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[j][i])
        if symbols == ["X", "X", "X"]:
            print('Победил Х')
            return True
        if symbols == ["0", "0", "0"]:
            print('Победил 0')
            return True

    symbols = []
    for j in range(3):
        symbols.append(field[i][i])
    if symbols == ["X", "X", "X"]:
        print('Победил Х')
        return True
    if symbols == ["0", "0", "0"]:
        print('Победил 0')
        return True

    symbols = []
    for j in range(3):
        symbols.append(field[i][2 - i])
    if symbols == ["X", "X", "X"]:
        print('Победил Х')
        return True
    if symbols == ["0", "0", "0"]:
        print('Победил 0')
        return True

    return False

greet()
field = [[" "] * 3 for i in range(3) ]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print("Ходит X")
    else:
        print("Ходит 0")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print("Победила дружба")
        break
