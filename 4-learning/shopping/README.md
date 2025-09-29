# Shopping

This project is part of the course **CS50's Introduction to Artificial Intelligence with Python**, provided by Harvard University. The exercise is located within the unit on **Learning**, and its objective is to predict whether a user will generate revenue (make a purchase) on an online shopping website, based on their session data.

## Project Description

The dataset contains information about online shopping sessions, such as the number of administrative, informational, and product-related pages visited, session durations, bounce rates, exit rates, the month of visit, whether the user is a returning visitor, and whether the visit occurred on a weekend.

The objective is to build a **k-nearest neighbors (k-NN)** classifier (with `k=1`) that predicts whether a user will generate revenue (`Revenue = TRUE`) or not (`Revenue = FALSE`).

The program consists of three main parts:

1. **Data Loading**  
   - Reads data from `shopping.csv`.  
   - Converts categorical values (month, visitor type, weekend, revenue) into numerical representations.  
   - Produces a list of evidence (features) and labels (outcomes).  

2. **Model Training**  
   - Uses `KNeighborsClassifier` from `scikit-learn` with `n_neighbors=1`.  
   - Trains the model on a subset of the data.  

3. **Evaluation**  
   - Tests the model on unseen data.  
   - Calculates **sensitivity (true positive rate)** and **specificity (true negative rate)**.  

## How to Run

To run the project, ensure you have Python 3 installed along with the required library:

```bash
pip install scikit-learn
```

Then execute the following command in your terminal:

```bash
python shopping.py shopping.csv
```

The program will output the number of correct and incorrect predictions, as well as the sensitivity and specificity of the model.

## Example Output

```
Correct: 4200
Incorrect: 800
True Positive Rate: 0.38
True Negative Rate: 0.90
```

![Shopping Result](../../images/shopping.png)

## Files

- **`shopping.py`** → Contains the implementations of `load_data`, `train_model`, and `evaluate`.  
- **`shopping.csv`** → Dataset with online shopping session data.  
- **`shopping.png`** → Example result image.  

## Direct Access

- [**View the full source code**](./shopping.py)  
- [Back to main README](../../README.md)  

## Author

This project was completed by [**Raul Estevez**](https://raulesteveza.github.io) as part of the CS50 AI course assignments.
