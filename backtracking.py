n = 16


def print_board(board):
    range_aux = range(n)
    for i in range_aux:
        for j in range_aux:
            print(board[i][j], end=" ")
        print("\n")


def is_valid(board, i, j):
    k = 0
    while k < j:
        if board[i][k]:
            return 0
        k += 1
    s = i - 1
    k = j - 1
    while k >= 0 and s >= 0:
        if board[s][k]:
            return 0
        k -= 1
        s -= 1
    s = i + 1
    k = j - 1
    while k >= 0 and s < n:
        if board[s][k]:
            return 0
        s += 1
        k -= 1
    return 1


def solve(board, j):
    if j == n:
        print("\n\n### Solution ###\n\n")
        print_board(board)
    for i in range(n):
        if is_valid(board, i, j):
            board[i][j] = 1
            solve(board, j + 1)
            board[i][j] = 0


def main():
    board = [[0 for a in range(n)] for b in range(n)]
    # print_board(board)
    solve(board, 0)


main()
