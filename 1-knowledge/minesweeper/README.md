# Minesweeper

This project is part of the course **CS50's Introduction to Artificial Intelligence with Python**, provided by Harvard University. The exercise is located within the unit on **Knowledge**, and its objective is to apply propositional logic to model and solve the game of Minesweeper.

## Project Description

In this exercise, we implement an AI agent capable of playing Minesweeper.  
The AI uses logical inference to keep track of cells that are known to be safe or to contain mines, based on the rules of the game and the information revealed after each move.

The program manages:
- **Known safes** and **known mines**.
- **Logical sentences** representing sets of cells and the number of mines they contain.
- **Inference**: deducing new safe cells or mines by comparing sentences and applying subset rules.
- Making **safe moves** when possible, or choosing a random move when no certain move is available.

The AI progressively updates its knowledge base after each move to improve decision-making.

## How to Run

### 1. Clone the repository
```bash
git clone <your-repository-url>
cd <repository-folder>
```

### 2. Create a virtual environment (optional but recommended)
```bash
python3 -m venv .venv
source .venv/bin/activate   # On Linux/macOS
.venv\Scripts\activate      # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the program
```bash
python runner.py
```

This will start an interactive window where you can play Minesweeper against the AI.  
The AI will make moves automatically when it is its turn.

## Example Output

When running the AI, the game window displays the current board. The AI marks known mines with flags and reveals safe cells, avoiding mines whenever logically possible.


![Program Output](../../images/minesweeper.png)


## Files

- **`minesweeper.py`** → Contains the game logic and the AI implementation.
- **`runner.py`** → Launches the graphical interface and runs the game.
- **`requirements.txt`** → Lists the required Python packages.

## Direct Access

- [**View the full source code**](./minesweeper.py)
- [Back to main README](../../README.md)

## Author

This project was completed by [**Raul Estevez**](https://raulesteveza.github.io) as part of the CS50 AI course assignments.
