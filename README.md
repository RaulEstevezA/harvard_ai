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

**[2 - Uncertainty](./2-uncertainty)**  

This unit introduces probabilistic reasoning as a fundamental tool for artificial intelligence. Unlike propositional logic, which deals with absolute truths, probabilistic models capture uncertainty and allow agents to make informed decisions in situations where outcomes are not deterministic.

- **Probability basics**:
  - Random variables and probability distributions.  
  - Conditional probability: `P(A|B)` and its role in reasoning under uncertainty.  
  - Bayes’ Rule as a method for updating beliefs given new evidence.  

- **Inference with probabilities**:
  - The concept of *joint probability distributions* and marginalization.  
  - Representing uncertainty about causes and effects in complex environments.  

- **Applications in AI**:
  - Probabilistic models for reasoning under incomplete information.  
  - Foundations for algorithms in natural language processing, computer vision, and decision making under risk.  

These concepts are foundational for building agents that can operate effectively in real-world environments, where uncertainty is inevitable.

**Exercises:**
- [PageRank](./2-uncertainty/pagerank)  
  Implements Google’s PageRank algorithm using two approaches: sampling (simulating a random surfer) and iteration (repeatedly redistributing probabilities until convergence). The project demonstrates how probability distributions can represent the importance of web pages.  

- [Heredity](./2-uncertainty/heredity)  
  Models genetic inheritance and trait expression in families. The program calculates joint probabilities that individuals have 0, 1, or 2 copies of a gene, and whether they exhibit a trait, taking into account inheritance from parents, mutation rates, and conditional probabilities. Results are normalized to produce valid probability distributions for each person.

**[3 - Optimization](./3-optimization)**  

This unit introduces optimization as a way to solve complex problems by finding the best assignment of values under given constraints. Unlike search algorithms that explore paths in a graph, optimization methods often work directly with variables and domains, applying heuristics and consistency checks to prune the search space.

- **Local search**:  
  - Hill climbing and its variants (steepest ascent, stochastic, random restarts).  
  - Exploration vs. exploitation trade-offs when navigating large state spaces.  

- **Constraint Satisfaction Problems (CSPs)**:  
  - Problems defined by variables, their domains, and constraints between them.  
  - Unary and binary constraints, and techniques to enforce node and arc consistency.  
  - The AC-3 algorithm for pruning inconsistent values from domains.  

- **Heuristics for efficiency**:  
  - Minimum Remaining Values (MRV) heuristic to select variables.  
  - Degree heuristic as a tie-breaker.  
  - Least Constraining Value (LCV) heuristic to order domain values.  

These methods provide a framework for efficiently solving problems where brute-force search would be intractable, making optimization a central tool in artificial intelligence.

**Exercises:**
- [Crossword](./3-optimization/crossword)  
  Generates crossword puzzles by modeling them as a constraint satisfaction problem. Each slot in the grid is a variable with words as its domain. The solver enforces node and arc consistency, applies heuristics (MRV, degree, LCV), and uses backtracking search to assign words in a way that satisfies all overlaps. The program outputs a completed crossword grid or reports when no solution exists.

**[4 - Learning](./4-learning)**  

This unit introduces machine learning, where systems improve their performance on a task through experience rather than being explicitly programmed. Learning allows AI to generalize from examples and make predictions about unseen data.

- **Supervised learning**:  
  - Training a model with labeled data to predict outcomes for new inputs.  
  - Concepts of training, testing, overfitting, and generalization.  
  - Evaluation metrics such as sensitivity (true positive rate) and specificity (true negative rate).  

- **Nearest-neighbor classifiers**:  
  - Predicting labels based on similarity to training examples.  
  - k-nearest neighbors (k-NN) and the effect of different values of *k*.  

- **Reinforcement learning**:  
  - Agents learn strategies by interacting with an environment.  
  - Concepts of states, actions, rewards, and policies.  
  - Q-learning as a method to approximate optimal action-value functions.  

These approaches form the foundation of many modern AI systems, from recommendation engines to game-playing agents, by allowing them to adapt and improve through data or interaction.

**Exercises:**
- [Shopping](./4-learning/shopping)  
  Implements a supervised learning model using **k-nearest neighbors (k=1)** to predict whether a user will generate revenue on an online shopping website based on session data. The program loads and processes categorical and numerical features, trains the classifier, and evaluates it in terms of sensitivity and specificity.  

- [Nim](./4-learning/nim)  
  Implements a reinforcement learning agent that learns to play the game of Nim through self-play. The agent uses **Q-learning** to update its strategy, gradually improving performance and approaching optimal play without being explicitly programmed with the game’s solution.  

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
