class BoardShouldHaveAtLeastThreeAsItsSize(Exception):
    pass


class BoardTooHugeToBeDealWith(Exception):
    pass


def create_board(size_board=3):
    if size_board < 3:
        raise BoardShouldHaveAtLeastThreeAsItsSize()

    if size_board > 15:
        return BoardTooHugeToBeDealWith()

    board = []
    count_position = 0

    for position in range(0, size_board):
        board.append([])

        for i in range(0, size_board):
            board[position].append(count_position)
            count_position += 1
    return board
