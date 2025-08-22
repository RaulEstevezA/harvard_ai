# PageRank

This project is part of the course **CS50's Introduction to Artificial Intelligence with Python**, provided by Harvard University. The exercise is located within the unit on **Uncertainty**, and its objective is to implement and compare two approaches for calculating the PageRank of a set of webpages.

## Project Description

The goal of this project is to simulate and compute the **PageRank** algorithm, which estimates the importance of each page in a web network. Two different approaches are implemented:

1. **Sampling method**
   - A random surfer is simulated across the corpus of pages.
   - The transition model is used to decide the probability of moving to another page.
   - After many samples, the distribution of visits approximates the PageRank values.

2. **Iterative method**
   - The PageRank values are initialized equally for all pages.
   - In each iteration, values are redistributed according to incoming links and the damping factor.
   - The process continues until the values converge (change less than 0.001).

Both approaches must return a probability distribution (dictionary) where keys are page names and values represent their estimated PageRank, summing to 1.

## How to Run

To run the project, ensure you have Python 3 installed. Then execute the following command in your terminal:

```bash
python pagerank.py corpus0
python pagerank.py corpus1
python pagerank.py corpus2
```

Each `corpus` directory contains a set of HTML pages with hyperlinks between them.

## Example Output

```
PageRank Results from Sampling (n = 10000)
1.html: 0.2225
2.html: 0.4250
3.html: 0.3525

PageRank Results from Iteration
1.html: 0.2211
2.html: 0.4278
3.html: 0.3511
```

The values are similar across both methods, as expected.


![Program Output](../../images/pagerank.png)


## Files

- **`pagerank.py`** → Contains the implementation of the PageRank algorithm and helper functions.
- **`corpus0/`** → Small test corpus of HTML pages.
- **`corpus1/`** → Medium test corpus of HTML pages.
- **`corpus2/`** → Larger test corpus of HTML pages.

## Direct Access

- [**View the full source code**](./pagerank.py)
- [Back to main README](../../README.md)

## Author

This project was completed by [**Raul Estevez**](https://raulesteveza.github.io) as part of the CS50 AI course assignments.