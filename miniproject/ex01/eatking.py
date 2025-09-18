import random

def pawn_algorithm(board_size, pawn_position):
    can_check = []
    x, y = pawn_position
    if x-1 >= 1 and y-1 >= 1:
        can_check.append((x-1, y-1))
    if x+1 <= board_size and y-1 >= 1:
        can_check.append((x+1, y-1))
    return can_check

def bishop_algorithm(board_size, bishop_position):
    can_check = []
    x, y = bishop_position
    for i in range(1, board_size):
        if x+i <= board_size and y+i <= board_size:
            can_check.append((x+i, y+i))
        if x-i >= 1 and y-i >= 1:
            can_check.append((x-i, y-i))
        if x+i <= board_size and y-i >= 1:
            can_check.append((x+i, y-i))
        if x-i >= 1 and y+i <= board_size:
            can_check.append((x-i, y+i))
    return can_check

def rook_algorithm(board_size, rook_position):
    can_check = []
    x, y = rook_position
    for i in range(1, board_size+1):
        if i != y:
            can_check.append((x, i))
        if i != x:
            can_check.append((i, y))
    return can_check

def queen_algorithm(board_size, queen_position):
    return bishop_algorithm(board_size, queen_position) + rook_algorithm(board_size, queen_position)

def print_board(size, king_pos):
    print("  ", end="")
    for c in range(1, size+1):
        print(c, end=" ")
    print()
    
    for r in range(1, size+1):
        print(r, end=" ")
        for c in range(1, size+1):
            if (c, r) == king_pos:
                print("K", end=" ")
            else:
                print(".", end=" ")
        print()


def main():
    size = int(input("ใส่ขนาดของกระดาน (>=3): "))

    king_pos = (random.randint(1, size), random.randint(1, size))
    print_board(size, king_pos)

    while True:
        piece = input("เลือกตัวหมาก (B=bishop, P=pawn, Q=queen, R=rook): ").upper()
        if piece in ["B", "P", "Q", "R"]:
            break
        else:
            print("!! โปรดเลือกตัวหมากใหม่ !!")

    col = int(input(f"Enter column (1-{size}): "))
    row = int(input(f"Enter row (1-{size}): "))
    pos = (col, row)

    if piece == "B":
        moves = bishop_algorithm(size, pos)
    elif piece == "P":
        moves = pawn_algorithm(size, pos)
    elif piece == "Q":
        moves = queen_algorithm(size, pos)
    elif piece == "R":
        moves = rook_algorithm(size, pos)
    else:
        print("Invalid piece")
        return

    if king_pos in moves:
        print("\nCongratz! คายติง")
    else:
        print("\nYou Suck! คลอดลิง")

if __name__ == "__main__":
    main()
