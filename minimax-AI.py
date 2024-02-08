import numpy as np
BOARD_SIZE = 3 # Default board size = 3


class TicTacToeVariant:

  def __init__(self):
    # Initialize the game board with empty cells
    self.board = np.full((BOARD_SIZE, BOARD_SIZE), ' ')
    # Initialize the current player to 'X'
    self.current_player = 'X'

  def display_board(self):
    # Display the current state of the game board
    print("\n")
    for row in self.board:
      print(" |".join(row))
      print("-" * (3 * BOARD_SIZE - 1))

  def make_move(self, row, col):
    # Make a move on the board if the selected cell is empty
    if self.board[row][col] == ' ':
      self.board[row][col] = self.current_player
      self.switch_player()
      return True
    return False

  def switch_player(self):
    # Switch the current player ('X' to 'O', or 'O' to 'X')
    self.current_player = 'O' if self.current_player == 'X' else 'X'

  def is_winner(self, player):
    # Check if the given player has won the game: Check rows, columns, and diagonals
    for i in range(BOARD_SIZE):
      if all(self.board[i][j] == player for j in range(BOARD_SIZE)) or \
         all(self.board[j][i] == player for j in range(BOARD_SIZE)):
        return True
    if all(self.board[i][i] == player for i in range(BOARD_SIZE)) or \
       all(self.board[i][BOARD_SIZE - 1 - i] == player for i in range(BOARD_SIZE)):
      return True
    return False


  def is_board_full(self):
    # Check if the game board is full (i.e. no more moves can be made)
    return all(cell != ' ' for row in self.board for cell in row)


class AIPlayer:

  def __init__(self, player):
    # Initialize the AI player with 'O'
    self.player = player

  def heuristic_eval(self, board):
    # Evaluate the current state of the board using a simple heuristic function
    score = 0
    for i in range(BOARD_SIZE):
      for j in range(BOARD_SIZE):
        if board[i][j] == 'O':
          score += 1
        elif board[i][j] == 'X':
          score -= 1
    return score


  def minimax_with_heuristic(self, board, depth, alpha, beta, maximizing_player):
    # Minimax algorithm with alpha-beta pruning and a heuristic evaluation
    if board.is_winner('X'):
      return -1
    elif board.is_winner('O'):
      return 1
    elif board.is_board_full():
      return 0

    if depth == 0:
      return self.heuristic_eval(board.board) 

    if maximizing_player:
      max_eval = float('-inf')
      for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
          if board.board[i][j] == ' ':
            board.board[i][j] = 'O'
            eval = self.minimax_with_heuristic(board, depth - 1, alpha, beta, False)
            board.board[i][j] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
              break  # Beta cut-off
      return max_eval
    else:
      min_eval = float('inf')
      for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
          if board.board[i][j] == ' ':
            board.board[i][j] = 'X'
            eval = self.minimax_with_heuristic(board, depth - 1, alpha, beta, True)
            board.board[i][j] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
              break  # Alpha cut-off
      return min_eval

  # Find the best move for the AI player using minimax with alpha-beta pruning and heuristic
  def get_best_move_with_heuristic(self, board):
    best_move = None
    best_eval = float('-inf')
    alpha = float('-inf')
    beta = float('inf')
    # num of empty cells calculated before every AI turn
    empty_cells = sum(1 for row in board.board for cell in row if cell == ' ')
    
    if BOARD_SIZE > 3: # Larger boards
      # In order to balance the computational efficiency and have a good AI response time.
      depth = min(4, empty_cells)
    else: # For the conventional 3x3 board
      # Results in optimal play without comprimising AI strategic decision making.
      depth = empty_cells
   
    for i in range(BOARD_SIZE):
      for j in range(BOARD_SIZE):
        if board.board[i][j] == ' ':
          board.board[i][j] = 'O'
          eval = self.minimax_with_heuristic(board, depth, alpha, beta, False)
          board.board[i][j] = ' '
          if eval > best_eval:
            best_eval = eval
            best_move = (i, j)
          alpha = max(alpha, eval)
    return best_move

# Game mode selection
def game_type_choice():
  global BOARD_SIZE
  print("Select Game mode:")
  print("1. Traditional (3x3 board)")
  print("2. Custom")

  while True:
    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
      BOARD_SIZE = 3
      print("\nPlayer marker: X | AI marker: 0")
      print("\nGet 3 X's (Horizontally, Vertically or Diagonally) in a row to win!")
      return BOARD_SIZE
    elif choice == '2':
      while True:
        try:
          BOARD_SIZE = int(input("Enter preferred board size (3 - 5): "))
          if BOARD_SIZE < 3 or BOARD_SIZE > 5:
            print("Invalid input. Board size range = 3 - 5.")
            continue
          print("\nPlayer marker: X | AI marker: 0")
          print(f"\nGet {BOARD_SIZE} X's (Horizontally, Vertically or Diagonally) in a row to win!\n")
          return BOARD_SIZE
        except ValueError:
          print("Invalid input. Please enter a valid number.")
    else:
      print("Invalid input. Please try again")


def play_game():
  print("Welcome to Tic-Tac-Toe!\n")
  game_type_choice()
  board = TicTacToeVariant()
  ai_player = AIPlayer('O')

  player_moves = 0
  ai_moves = 0

  while True:
    board.display_board()
    if board.current_player == 'X':
      # Player's move
      move_input = input(
          "Enter your move (row (0 - {}),col (0 - {})):  ".format(
              BOARD_SIZE - 1, BOARD_SIZE - 1))
      try:
        row, col = map(int, move_input.split(','))
        if not (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE):
          print("Invalid move. Try again.")
          continue
        if not board.make_move(row, col):
          print("Invalid move. Try again.")
          continue
        print(f"Player X moves to: ({row}, {col})")  # Player's move
        player_moves += 1
      except ValueError:
        print("Invalid input. Please enter two integers separated by a comma.")
        continue
    else:
      # AI's move
      print("AI is making a move...")
      ai_move = ai_player.get_best_move_with_heuristic(board)
      if ai_move is None:
        print("AI cannot make a move. It's a draw!")
        break
      board.make_move(*ai_move)
      print(f"Player O (AI) moves to: {ai_move}")  # AI's move
      ai_moves += 1

    # Check game outcome
    if board.is_winner('X'):
      board.display_board()
      print("Player X wins!")
      print("Player X Moves Played: ", player_moves)
      break
    elif board.is_winner('O'):
      board.display_board()
      print("Player O (AI) wins!")
      print("AI Moves Played: ", ai_moves)
      break
    elif board.is_board_full():
      board.display_board()
      print("It's a draw!")
      print("Player X Moves Played: ", player_moves)
      print("AI Moves Played: ", ai_moves)
      break

# Start the game
play_game()