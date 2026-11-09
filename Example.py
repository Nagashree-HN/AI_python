# CSCI 538: Assignment 02
# Question 2(d): N-Queen Problem
# Name: Nagashree Herambapura Nagaraja
# CWID: 50434952

# Number of Queens
print("Enter the number of queens")
N = int(input())

# Initialize the chessboard
board = [[0] * N for _ in range(N)]

# List used to save all valid solutions
solutions = []


def is_attack(i, j):
    # Check if there is already a queen in the same row or column
    for k in range(0, N):
        if board[i][k] == 1 or board[k][j] == 1:
            return True

    # Check both diagonals
    for k in range(0, N):
        for l in range(0, N):
            if (k + l == i + j) or (k - l == i - j):
                if board[k][l] == 1:
                    return True

    return False


def N_queen(n):
    # If n becomes 0, all N queens have been placed successfully
    if n == 0:
        # Save a copy of the current board
        solutions.append([row[:] for row in board])
        return

    # Place one queen in each row
    i = N - n

    for j in range(0, N):
        # Place the queen only if this position is safe
        if (not is_attack(i, j)) and (board[i][j] != 1):
            board[i][j] = 1

            # Try to place the remaining queens
            N_queen(n - 1)

            # Backtrack and try another position
            board[i][j] = 0


# Start solving the problem
N_queen(N)

# Print assignment information
print("\nName: Nagashree Herambapura Nagaraja")
print("CWID: 50434952")
print("Number of Queens N:", N)

# Print three solutions side by side
for i in range(0, len(solutions), 3):

    group = solutions[i:i + 3]

    # Print solution headings
    heading = ""
    for j in range(len(group)):
        heading += ("Solution " + str(i + j + 1)).ljust(32)

    print("\n" + heading)

    # Print the boards side by side
    for row in range(N):
        line = ""

        for solution in group:
            line += str(solution[row]).ljust(32)

        print(line)

# Print total number of solutions
print("\nTotal number of solutions for N =", N, ":", len(solutions))