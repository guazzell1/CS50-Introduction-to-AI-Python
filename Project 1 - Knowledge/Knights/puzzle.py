from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

A_said_Knave = Symbol("A said 'I am a Knave'")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # ou é Knight ou é Knave, mas nao os dois
    Or(AKnight, AKnave),
    Not(And(AKnave, AKnight)),

    # se A for Knight => é verdade que A é knight e knave ao mesmo tempo, se A for Knave => nao é verdade que A é knight e knave ao mesmo tempo
    Implication(AKnight, And(AKnave, AKnight)),
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # ou é Knight ou é Knave, mas nao os dois - Tanto para A quanto para B
    Or(AKnight, AKnave),
    Not(And(AKnave, AKnight)),
    Or(BKnight, BKnave),
    Not(And(BKnave, BKnight)),

    # fala do A
    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave))),

    #fala do B
    
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # ou é Knight ou é Knave, mas nao os dois - Tanto para A quanto para B
    Or(AKnight, AKnave),
    Not(And(AKnave, AKnight)),
    Or(BKnight, BKnave),
    Not(And(BKnave, BKnight)),

    # fala do A
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),

    # fala do B
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # ou é Knight ou é Knave, mas nao os dois - Tanto para A quanto para B e C
    Or(AKnight, AKnave),
    Not(And(AKnave, AKnight)),
    Or(BKnight, BKnave),
    Not(And(BKnave, BKnight)),
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),

    # fala do A
    Or(
        # I am a knight
        And(
            Implication(AKnight, AKnight), 
            Implication(AKnave, Not(AKnight))
        ),

        # I am a knave
        And(
            Implication(AKnight, AKnave),
            Implication(AKnave, Not(AKnave))
        )
    ),

    # fala do B
    # sobre A
    Implication(BKnight, A_said_Knave),
    Implication(BKnave, Not(A_said_Knave)),

    Implication(A_said_Knave, And(
        Implication(AKnight, AKnave),
        Implication(AKnave, Not(AKnave))
    )
    ),
    # sobre C
    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),

    # fala do C
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))
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
