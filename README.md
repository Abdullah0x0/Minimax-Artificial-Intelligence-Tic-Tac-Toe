# Tic-Tac-Toe with AI Opponent

This project enhances the classic Tic-Tac-Toe game by introducing an Artificial Intelligence (AI) opponent and the ability to choose a custom board size, ranging from the traditional 3x3 up to a more challenging 5x5 grid. Compete against an AI that utilizes the minimax algorithm and a heuristic evaluation to make its moves, making each game engaging and unpredictable.

## Features

- **Customizable Board Size**: Choose between a standard 3x3 board or a larger board (up to 5x5) for extended gameplay.
- **Single Player Mode**: Test your skills against a challenging AI opponent.
- **Heuristic Evaluation AI**: The AI strategically evaluates board states to decide on its moves, providing a tough challenge.
- **Command Line Interface**: Simple and intuitive gameplay through the command line.
- **Automatic Win/Draw Detection**: Automatically detects wins or draws, displaying the game's outcome and final board state.

## Requirements

- Python 3.x
- NumPy library

## Installation

1. Make sure Python 3.x is installed on your system. If not, download it from [python.org](https://www.python.org/).
2. Install NumPy via pip:
   ```
   pip install numpy
   ```

## How to Play

1. Download `minimax-AI.py` or clone this repository to your machine.
2. Open a terminal or command prompt.
3. Navigate to the directory containing `minimax-AI.py`.
4. Execute the script with Python:
   ```
   python minimax-AI.py
   ```
5. At the start, you'll be prompted to choose the board size. Enter a number from 3 to 5.
6. Make your moves by entering the row and column numbers separated by a comma (e.g., `0,1` for the first row and second column).

## How It Works

The game begins by prompting the player to choose a board size. The AI evaluates the board using a heuristic function, considering both its potential moves and the player's, to decide on the best course of action. The game alternates turns between the player and the AI until one emerges victorious or the board fills up, resulting in a draw.

## Contributing

Contributions to this project are welcome, from adding new features and enhancing the AI logic to fixing bugs and improving performance. Fork this repository and submit your pull requests to contribute.

## License

This Tic-Tac-Toe project is open-source and distributed under the [MIT License](https://opensource.org/licenses/MIT).
