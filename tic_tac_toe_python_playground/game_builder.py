class BoardDoesNotHaveTheMinimalConfiguration(Exception):
    pass


class BoardDoesNotHaveTheMaximumConfiguration(Exception):
    pass


def create_board(size=3):
    if size < 3:
        raise BoardDoesNotHaveTheMinimalConfiguration()
    if size > 10:
        raise BoardDoesNotHaveTheMaximumConfiguration()

    board = []
    count = 0
    for row in range(0, size):
        board.append([])
        for col in range(0, size):
            board[row].append(count)
            count += 1
    return board
