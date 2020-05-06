rows = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
combinations = set()


def field_update():
    columns = [[rows[indx][i] for indx in range(3)] for i in range(3)]
    horizontal = ["".join(rows[indx]) for indx in range(3)]
    vertical = ["".join(columns[indx]) for indx in range(3)]
    cross = ["".join([rows[0][0], rows[1][1], rows[2][2]]),
             "".join([rows[2][0], rows[1][1], rows[0][2]])]

    combinations.clear()
    combinations.update(horizontal, vertical, cross)


def field_check():
    if "OOO" in combinations:
        if "XXX" in combinations:
            print("Impossible")
        else:
            print("O wins")
            return True
    elif "XXX" in combinations:
        print("X wins")
        return True
    elif not any([symbol == ' ' for row in rows for symbol in row]):
        print("Draw")
        return True


def field_print():
    print("-" * 9)
    [print("|", " ".join(rows[indx]), "|") for indx in range(3)]
    print("-" * 9)


def is_number(coordinates):
    return all([coordinates[i].isdigit() for i in range(len(coordinates))])


def in_range(coordinates):
    return all([1 <= int(coordinates[i]) <= 3 for i in range(len(coordinates))])


def is_occupied(coordinates):
    return rows[coordinates[0]][coordinates[1]] != ' '


def revert_coordinates(coordinates):
    return -int(coordinates[1]), int(coordinates[0]) - 1


field_print()
X_OR_O = 'X'  # first move by X
while True:
    raw_coordinates = input("Enter the coordinates: > ").split()
    if not is_number(raw_coordinates):
        print("You should enter numbers!")
        continue
    if not in_range(raw_coordinates):
        print("Coordinates should be from 1 to 3!")
        continue
    coordinates = revert_coordinates(raw_coordinates)
    if is_occupied(coordinates):
        print("This cell is occupied! Choose another one!")
        continue

    rows[coordinates[0]][coordinates[1]] = X_OR_O
    field_update()
    field_print()
    if field_check():
        break
    X_OR_O = 'O' if X_OR_O == 'X' else 'X'
