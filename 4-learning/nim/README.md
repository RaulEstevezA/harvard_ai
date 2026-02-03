# Nim

This project is part of the course **CS50's Introduction to Artificial Intelligence with Python**, within the unit on **Learning**.  
The objective of this exercise is to implement a reinforcement learning agent that learns to play the game of Nim using **Q-learning**.

## Project Description

Nim is a turn-based game played with multiple piles of objects. On each turn, a player removes one or more objects from a single pile. In this version of the game (misère Nim), the player who removes the **last object loses**.

The goal of this project is to build an AI that learns the optimal strategy by playing against itself repeatedly. Over many simulated games, the AI updates Q-values for `(state, action)` pairs and gradually improves its decision-making.

The program is structured around two main classes:

- **`Nim`** → Implements the game logic (piles, moves, players, and win conditions).
- **`NimAI`** → Implements a Q-learning agent that learns from experience.

The learning process is based on:

- **Q-values** stored as `(state, action)` pairs.
- **Alpha (learning rate)** to control how strongly new experiences affect existing knowledge.
- **Epsilon (exploration rate)** to balance exploration (random moves) and exploitation (best known moves).

## How It Works

The project consists of three main stages:

1. **Game Definition**
   - Represents the current state as a list of pile sizes.
   - Represents actions as `(pile_index, objects_removed)`.
   - Provides all valid actions for any given state.

2. **Training (Reinforcement Learning)**
   - The AI plays thousands of games against itself.
   - After each move, Q-values are updated using the Q-learning formula.
   - The agent uses an epsilon-greedy strategy to sometimes explore random actions.

3. **Playing Against the AI**
   - After training, a human player can play against the learned model.
   - During gameplay, the AI selects actions greedily (no exploration).

## How to Run

Make sure you have Python 3 installed.

To train the AI and play a game, run:

```bash
python play.py
```

By default, the program will train the AI and then allow you to play against it in the terminal.

You can adjust the number of training games directly in the code if you want to experiment with different training sizes.

## Example Output

Below is an example of what the terminal interaction may look like after training (your exact output may differ depending on the number of training games and random choices during play):

```text
Training AI for 10000 games...
Done training.

Piles:
Pile 0: 1
Pile 1: 3
Pile 2: 5
Pile 3: 7

Your turn
Choose Pile: 2
Choose Count: 3

AI's turn
AI chose to take 1 from pile 1

...
Game Over!
Winner is: AI
```

![Nim Result](../../images/nim.png)

## Key Concepts Implemented

- Q-learning update rule:

```
Q(s, a) ← Q(s, a) + α * ((reward + future_reward) − Q(s, a))
```

- Epsilon-greedy action selection.
- State representation using tuples for dictionary keys.
- Reinforcement learning through self-play.

## Files

- **`nim.py`** → Contains the implementation of the Nim game logic and the Q-learning agent (`Nim` and `NimAI` classes).
- **`play.py`** → Entry point of the program. Trains the AI and allows a human player to play against it from the terminal.

## Direct Access

- [**View the full source code**](./nim.py)  
- [Back to main README](../../README.md)

## Author

This project was completed by [**Raul Estevez**](https://raulesteveza.github.io) as part of the CS50 AI course assignments.
