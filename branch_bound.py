def solve_n_queens(n):
    # Initialize the board and auxiliary structures
    board = [['.' for _ in range(n)] for _ in range(n)]
    cols = [False] * n          
    diag1 = [False] * (2 * n - 1)  
    diag2 = [False] * (2 * n - 1)  
    solutions = []

    def place_queens(row):
        if row == n:
            solution = [''.join(board[i]) for i in range(n)]
            solutions.append(solution)
            return
        
        for col in range(n):
            if not cols[col] and not diag1[row + col] and not diag2[row - col + n - 1]:
                board[row][col] = 'Q'
                cols[col] = diag1[row + col] = diag2[row - col + n - 1] = True

                place_queens(row + 1)

                board[row][col] = '.'
                cols[col] = diag1[row + col] = diag2[row - col + n - 1] = False

    place_queens(0)
    return solutions

n = 4
solutions = solve_n_queens(n)
print(f"Number of solutions for {n}-Queens problem:", len(solutions))
for solution in solutions:
    for row in solution:
        print(row)
    print()
