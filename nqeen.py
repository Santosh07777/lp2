N = 4
def printSolution(board):
    for row in board:
        for val in row:
            print(val, end=" ")
        print()
def isSafe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

# Recursive utility to solve N-Queens problem
def solveNQUtil(board, col):
    # Base case: If all queens are placed
    if col >= N:
        return True

    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1  

            if solveNQUtil(board, col + 1):
                return True

            board[i][col] = 0

    return False  

def solveNQ():
    board = [[0 for _ in range(N)] for _ in range(N)]

    if not solveNQUtil(board, 0):
        print("Solution does not exist")
        return False

    print("One of the solutions to the N-Queens problem is:")
    printSolution(board)
    return True
solveNQ()
