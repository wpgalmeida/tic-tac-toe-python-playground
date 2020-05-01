def create_board(size=3):
    board = []
    count = 0

    for row in range(0, size):
        board.append([])
        for col in range(0, size):
            board[row].append(count)
            count += 1

    return board