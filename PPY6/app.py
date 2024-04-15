import json

# Load game settings
with open('PPY6\game-init.json', 'r') as file:
    settings = json.load(file)

# Game settings
num_players = settings['num_players']
player_names = settings['player_names']
grid_size = settings['grid_size']
player_symbols = settings['player_symbols']

# Initialize the board
board = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]

# Draw a board
def print_board():
    for row in board:
        print('|' + '|'.join(row) + '|')

# Validator for move
def is_valid_move(row, col):
    return 0 <= row < grid_size and 0 <= col < grid_size and board[row][col] == ' '

# Winner checking 
def check_winner():
    winning_length = 3  

    for i in range(grid_size):
        for j in range(grid_size - winning_length + 1):
            if len(set(board[i][j:j + winning_length])) == 1 and board[i][j] != ' ':
                return board[i][j]
            column = [board[x][i] for x in range(j, j + winning_length)]
            if len(set(column)) == 1 and column[0] != ' ':
                return column[0]

    for i in range(grid_size - winning_length + 1):
        for j in range(grid_size - winning_length + 1):
            diagonal = [board[i + k][j + k] for k in range(winning_length)]
            if len(set(diagonal)) == 1 and diagonal[0] != ' ':
                return diagonal[0]
            anti_diagonal = [board[i + k][j + winning_length - k - 1] for k in range(winning_length)]
            if len(set(anti_diagonal)) == 1 and anti_diagonal[0] != ' ':
                return anti_diagonal[0]

    return None


def main():
    current_player_index = 0
    while True:
        print_board()
        row = int(input(f'{player_names[current_player_index]} choose your row (1-{grid_size}): '))-1
        col = int(input(f'{player_names[current_player_index]} choose your column (1-{grid_size}): '))-1

        if not is_valid_move(row, col):
            print("Invalid move. Try again.")
            continue

        board[row][col] = player_symbols[player_names[current_player_index]]
        winner = check_winner()
        if winner:
            print_board()
            print(f"Congratulations! {player_names[current_player_index]} wins!")
            break
        if all(all(cell != ' ' for cell in row) for row in board):
            print_board()
            print("It's a draw!")
            break
        current_player_index = (current_player_index + 1) % num_players

if __name__ == "__main__":
    main()
