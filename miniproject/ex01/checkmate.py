def pawn_algorithm(board_size, pawn_position):
    can_check = []
    x = pawn_position[0]
    y = pawn_position[1]
    if x-1 > 0 and y-1 > 0:
        can_check.append([x-1, y-1])
    if x+1 < board_size and y-1 > 0:
        can_check.append([x+1, y-1])
    return can_check

def bishop_algorithm(board_size, bishop_position):
    can_check = []
    x, y = bishop_position
    for i in range(1, board_size):
        if x+i <= board_size and y+i <= board_size:
            can_check.append([x+i, y+i])
        if x-i > 0 and y-i > 0:
            can_check.append([x-i, y-i])
        if x+i <= board_size and y-i > 0:
            can_check.append([x+i, y-i])
        if x-i > 0 and y+i <= board_size:
            can_check.append([x-i, y+i])
    return can_check

def rook_algorithm(board_size, rook_position):
    can_check = []
    x, y = rook_position
    for i in range(1, board_size+1):
        if i < board_size+1 and [x, i] != rook_position:
            can_check.append([x, i])
        if i < board_size+1 and [i, y] != rook_position:
            can_check.append([i, y])
    return can_check

def queen_algorithm(board_size, queen_position):
    return bishop_algorithm(board_size, queen_position) + rook_algorithm(board_size, queen_position)

def board_position(table):
    rows = table.split("\n")
    k, b, p, q, r = [], [], [], [], []
    y=1
    for cols in rows:
        x=1
        for char in cols:
            if char == "K":
                k = [x, y]
            if char == "B":
                b = [x, y]
            if char == "P":
                p = [x, y]
            if char == "Q":
                q = [x, y]
            if char == "R":
                r = [x, y]
            x+=1
        y+=1
    return [k, b, p, q, r]

def check_numebers_king(table):
    count_king = table.count('K')
    return False if count_king != 1 else True

def check_board_size(table):
    rows = table.split('\n')
    size = len(rows)

    for cols in rows:
        if len(cols) != len(rows):
            return False, size

    return True, size

def checkmate(table):
    king_check = check_numebers_king(table)
    board_valid_size, size = check_board_size(table)
    if king_check == False or board_valid_size == False:
        return print("Error!! Check the number of Kings or Size not balance")

    units = board_position(table)
    check_all = []

    if units[1] != []:
        check_all += bishop_algorithm(size, units[1])
    if units[2] != []:
        check_all += pawn_algorithm(size, units[2])
    if units[3] != []:
        check_all += queen_algorithm(size, units[3])
    if units[4] != []:
        check_all += rook_algorithm(size, units[4])

    if units[0] in check_all:
        return print("Success")
    else:
        return print("Fail")