# Parser

This project is part of the course **CS50's Introduction to Artificial Intelligence with Python**, within the unit on **Language** (Natural Language Processing).  
The objective of this exercise is to implement a context-free grammar (CFG) based parser capable of analyzing the syntactic structure of simple English sentences.

## Project Description

Parsing is a core problem in natural language processing. A parser attempts to determine how words in a sentence relate to each other by identifying their grammatical structure.

In this project, a parser is built using a **context-free grammar (CFG)** and NLTK’s `ChartParser`. The grammar defines:

- The valid vocabulary of the language (terminal symbols)
- The allowed syntactic structures (nonterminal rules)

Given an input sentence, the program generates one or more parse trees representing possible grammatical interpretations.

## How It Works

The program operates in several stages:

1. **Preprocessing**
   - The input sentence is tokenized using NLTK.
   - All tokens are converted to lowercase.
   - Tokens without alphabetic characters are removed.

2. **Grammar Definition**
   - Terminal symbols define the allowed words.
   - Nonterminal rules define how phrases and sentences are formed.

3. **Parsing**
   - The sentence is parsed using NLTK’s `ChartParser`.
   - Valid parse trees are generated according to the grammar.

4. **Noun Phrase Chunking**
   - The parse tree is analyzed to extract noun phrase chunks (NP).
   - Only minimal noun phrases (those without nested NP subtrees) are returned.

## How to Run

It is **recommended to use a Python virtual environment** to avoid dependency conflicts.

Create and activate a virtual environment, then install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

If NLTK raises a tokenizer resource error, download the required data once:

```bash
python3
```

```python
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
exit()
```

### Execution

Run the parser and enter a sentence when prompted:

```bash
python3 parser.py
```

You may also provide a file containing a sentence:

```bash
python3 parser.py sentences/1.txt
```

## Example Output

Example input:

```text
Sentence: holmes sat in the armchair
```

Example result (simplified):

```text
(S
  (NP holmes)
  (VP sat
    (PP in
      (NP the armchair))))
```

Noun Phrase Chunks:

```text
holmes
the armchair
```

![Result](../../images/parser.png)

## Key Concepts Implemented

- Context-Free Grammars (CFG)
- Syntactic parsing
- Natural Language Processing (NLP)
- Tree structures and traversal
- Noun Phrase (NP) chunk extraction

## Files

- **`parser.py`** → Main program. Defines the grammar, preprocesses input, parses sentences, and extracts NP chunks.

## Direct Access

- [**View the source code**](./parser.py)  
- [Back to main README](../../README_en.md)

## Author

This project was completed by **Raul Estevez** as part of the CS50 AI course assignments.
