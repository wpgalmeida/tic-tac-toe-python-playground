def create_board(size_board=3):
    #TODO: precisa tratar para receber apenas int
    if size_board < 3:
        return "tabuleiro precisa ter 3 ou mais linhas"

    if size_board > 15:
        return "tabuleiro muito grande escolha um numero menor"

    board = []

    for position in range(0, size_board):
        board.append([])

        for i in range(0, size_board):
            board[position].append(None)

    return board
