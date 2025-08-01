# CS50’s Introduction to Artificial Intelligence with Python

This repository contains my personal progress and solutions for the course **[CS50’s Introduction to Artificial Intelligence with Python](https://www.edx.org/learn/artificial-intelligence/harvard-university-cs50-s-introduction-to-artificial-intelligence-with-python)**, offered by Harvard University.

The course explores foundational concepts in artificial intelligence, focusing on practical implementation using Python. It covers topics such as graph search algorithms, knowledge representation, logic, planning, learning, and natural language processing.

## Course Objectives

- Understand key concepts of artificial intelligence and how they are applied in real-world scenarios.
- Implement fundamental AI algorithms using Python.
- Gain hands-on experience with search, optimization, logic inference, and machine learning.

## Course Topics and Exercises

Each folder corresponds to a main topic in the course. Inside each, you will find one or more exercises:

**[0 - Search](./0-search)** 
 
This lesson introduces fundamental search algorithms and problem-solving strategies used in AI:

- **Search problem definition**: start state, goal state, successor function, and cost metrics.
- **Uninformed (blind) search**:
  - **Depth‑First Search (DFS)**: explores one branch fully using a stack (LIFO); not guaranteed to be optimal or complete in infinite graphs.
  - **Breadth‑First Search (BFS)**: explores layer by layer using a queue (FIFO); guaranteed to find the shortest path (in terms of number of actions) and complete in finite graphs.
- **Informed (heuristic) search**:
  - **Greedy Best‑First Search**: uses a heuristic function `h(n)` to estimate closeness to the goal.
  - **A\***: combines path cost and heuristic (`f(n) = g(n) + h(n)`), with admissible and consistent heuristics ensuring optimality and completeness.
- **Other strategies introduced**:
  - **Iterative Deepening DFS (IDDFS)**: combines the memory efficiency of DFS with the completeness of BFS.
  - Overview of **Bidirectional Search**, **Uniform‑Cost Search**, and **Alpha‑Beta Pruning** as strategies applied in different contexts.

These concepts are essential for modeling problems as graphs and implementing search strategies using data structures like stacks, queues, and priority queues.

**Exercises:**
- [Degrees](./0-search/degrees)  
  Implements BFS to find the shortest "degree of separation" between two actors based on shared movie roles.

- [Tic Tac Toe](./0-search/tictactoe)  
  Implements an unbeatable AI using the Minimax algorithm to play a perfect game of Tic Tac Toe.

**[1 - Knowledge](./1-knowledge)**  

This unit introduces propositional logic as a tool to represent knowledge and perform inference in artificial intelligence. It focuses on how an agent can deduce facts from known rules and facts using logical reasoning, rather than brute-force search.

- **Propositional logic**:
  - Logical symbols and connectives: `∧` (and), `∨` (or), `¬` (not), `→` (implication), and `↔` (biconditional).
  - Truth tables and models: determining when a logical sentence is satisfied in a given world.
  - Inference rules: including **Modus Ponens**, **Modus Tollens**, and equivalence transformations such as **De Morgan’s Laws** and **distributive properties**.
- **Knowledge bases (KB)**:
  - A collection of logical sentences that represent facts and rules about the world.
  - Use of the `model_check` function to determine whether a given conclusion logically follows from the KB.
- **Symbolic AI**:
  - Emphasizes formal logic and structured reasoning rather than numerical heuristics.
  - Forms the basis for many expert systems and reasoning engines.

These concepts are foundational for building agents that reason with certainty and can deduce truths about the environment from limited information.

**Exercises:**
- [Knights](./1-knowledge/knights)  
  Uses propositional logic to determine the identity (Knight or Knave) of characters in logical puzzles based on their statements. Implements a knowledge base for each puzzle and applies inference rules to reach conclusions.

- [Minesweeper](./1-knowledge/minesweeper)  
  Builds an AI agent that plays the game of Minesweeper using logical deduction. The AI maintains a knowledge base of safe and unsafe cells and deduces new information as it uncovers the board.
  

**2 - Inference**  
_(to be completed)_

**3 - Optimization**  
_(to be completed)_

**4 - Learning**  
_(to be completed)_

**5 - Neural Networks**  
_(to be completed)_

**6 - Language**  
_(to be completed)_

---

Each exercise includes:
- A dedicated `README.md`
- The full source code
- Any necessary datasets or test files
- (Optionally) screenshots or output examples in the `/images` folder

## License

This repository is licensed under the [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) license.
