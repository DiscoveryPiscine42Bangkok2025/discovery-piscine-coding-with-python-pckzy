from checkmate import checkmate

def main():
    board1 = """\
R...
.K..
..P.
....\
"""

    board2 = """\
K..
...
..R\
"""

    board3 = """\
.K.
..P
K..\
"""

    board4 = """\
R...
....
..P.
....\
"""

    board5 = """\
R...
......
..P.
....\
"""

    checkmate(board1)
    checkmate(board2)
    checkmate(board3)
    checkmate(board4)
    checkmate(board5)

if __name__ == "__main__":
    main()