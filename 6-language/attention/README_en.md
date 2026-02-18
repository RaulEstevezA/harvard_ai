# Attention

This project is part of the course **CS50's Introduction to Artificial Intelligence with Python**, within the unit on **Language** (Natural Language Processing).

The goal of this exercise is to inspect and visualize the **self-attention mechanism** used by transformer-based language models.

## Project Description

Transformer models such as BERT rely on self-attention to evaluate relationships between tokens in a sentence. Each token can dynamically assign importance to other tokens, allowing the model to capture contextual dependencies without relying solely on sequential processing.

In this project, attention weights are extracted from a pretrained BERT masked language model and rendered as grayscale diagrams. These visualizations provide insight into how the model distributes attention across tokens at different layers and heads.

## How It Works

The program operates in several stages:

1. **Input Processing**
   - The user provides a sentence containing a `[MASK]` token.
   - The sentence is tokenized using a pretrained tokenizer.

2. **Model Inference**
   - A pretrained BERT masked language model is loaded.
   - The model outputs attention matrices for each layer and head.

3. **Attention Visualization**
   - Attention scores are converted into grayscale values.
   - One diagram is generated per layer and attention head.

## How to Run

It is **recommended to use a Python virtual environment** to avoid dependency conflicts.

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

If running on macOS and TensorFlow/Keras compatibility issues arise:

```bash
export TF_USE_LEGACY_KERAS=1
```

### Execution

Run the program and enter a sentence when prompted:

```bash
python mask.py
```

Example input:

```text
Text: The capital of France is [MASK].
```

## Output

The program generates multiple PNG files representing attention patterns:

- `Attention_LayerX_HeadY.png`

Each diagram corresponds to one transformer layer and one attention head. Lighter cells represent higher attention scores, while darker cells represent lower scores.

![Result](../../images/attention.png)

## Key Concepts Implemented

- Self-attention mechanism
- Transformer architecture
- Attention layers and heads
- Token relationships in language models
- Visual interpretation of attention matrices

## Files

- **`mask.py`** → Main program. Loads the model, extracts attentions, and generates diagrams.
- **`requirements.txt`** → Python dependencies.

## Direct Access

- [View the source code](./mask.py)  
- [Back to main README](../../README_en.md)

## Author

This project was completed by [**Raul Estevez**](https://raulesteveza.github.io) as part of the CS50 AI coursework.
