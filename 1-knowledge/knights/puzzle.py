from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Not        →   ¬ (negación)
# And        →   ∧ (conjunción)
# Or         →   ∨ (disyunción)
# =>         →   → (implicación)
# <=>        →   ↔ (bicondicional)

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And( 
    
    # Introducing all character options
    Not(And(AKnight, AKnave)),                  # can't be Knight and Knave at the same time
    Or(AKnight, AKnave),                        # or Knight or Knave

    # What did A say?
    Implication(AKnight, And(AKnight, AKnave))  # only can be Knight if Knight ∧ Knave

)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(

    # Introducing all character options
    Or(AKnave, AKnight),                            # or A Knight or Knave
    Not(And(AKnight, AKnave)),                      # can't be A Knight and Knave at the same time
    Or(BKnave, BKnight),                            # or B Knight or Knave
    Not(And(BKnight, BKnave)),                      # can't be B Knight and Knave at the same time

    # What did A say?
    Implication(AKnight, And(AKnave, BKnave)),      # if A say the true because is a Knight, A is Knave and B is a Knave
    Implication(AKnave, Not(And(AKnave, BKnave)))   # if A don't say the true because is a Knave, A is Knave and B is a Knight

    # B didn't say nothing
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    
    # Introducing all character options
    Or(AKnave, AKnight),                                                        # or A Knight or Knave
    Not(And(AKnight, AKnave)),                                                  # can't be A Knight and Knave at the same time
    Or(BKnave, BKnight),                                                        # or B Knight or Knave
    Not(And(BKnight, BKnave)),                                                  # can't be B Knight and Knave at the same time

    # What did A say?
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),       # if A is Knight, the 2 are the same (Knights or Knave)
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),   # if A is Knave, the 2 are not the same (Knights or Knave)

    # What did B say?
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),       # if B is Knight, the 2 are diferents
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight)))),   # if B is Knave, the 2 are not diferents

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(

    # Introducing all character options
    Or(AKnave, AKnight),                    # or A Knight or Knave
    Not(And(AKnight, AKnave)),              # can't be A Knight and Knave at the same time
    Or(BKnave, BKnight),                    # or B Knight or Knave
    Not(And(BKnight, BKnave)),              # can't be B Knight and Knave at the same time
    Or(CKnave, CKnight),                    # or C Knight or Knave
    Not(And(CKnight, CKnave)),              # can't be C Knight and Knave at the same time

    # What did A say?
    # A said one of the two phrases, but we don't know which one, so it is not formalized
    Not(Implication(AKnight, AKnave)),      # if A is a Knight, cant say he is a Knave

    # What did B say?
    Implication(BKnight, AKnave),           # if B Knight saw the true about A
    Implication(BKnave, Not(AKnave)),       # if B Knight didn't say the true about A
    Implication(BKnight, CKnave),           # if B Knight saw the true about C
    Implication(BKnave, Not(CKnave)),       # if B Knave didn't say the true about C

    # What did C say?
    Implication(CKnight, AKnight),          # if C Knight saw the true about A
    Implication(CKnave, Not(AKnight)),      # if C Knave saw the true about A

)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
