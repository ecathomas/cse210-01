
board = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]

def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot} " , end="")
        print ()

print_board(board)

while True:
    user_input = input("Please enter a position 1-9 or enter q to quit.")