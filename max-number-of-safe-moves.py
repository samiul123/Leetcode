def solution(nRows, nCols, currRow, currCol, laserCoordinates):
    board = [[0 for j in range(nCols)] for i in range(nRows)]
    for coordinate in laserCoordinates:
        row, col = coordinate
        for i in range(nRows):
            board[i][col - 1] = 1
        for j in range(nCols):
            board[row - 1][j] = 1

    moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    maxStepCount = 0
    for move in moves:
        newRow, newCol = currRow - 1, currCol - 1
        stepCount = 0
        while board[newRow][newCol] != 1 and (0 < newRow < nRows - 1) and (0 < newCol < nCols - 1):
            stepCount += 1
            newRow, newCol = newRow + move[0], newCol + move[1]
        maxStepCount = max(maxStepCount, stepCount)

    return maxStepCount


if __name__ == "__main__":
    print(solution(8, 8, 5, 3, [[1, 6], [2, 8]]))
