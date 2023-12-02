"""
The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

    In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
    In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
    In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.

Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?
"""

from advent_of_code.day2.part1 import Move

optimal_mapping = {
    "A": Move.Rock,
    "B": Move.Paper,
    "C": Move.Scissors,
}

optimal_outcomes: dict[tuple[Move, str], int] = {
    (Move.Rock, "X"): Move.Scissors.value,
    (Move.Rock, "Y"): Move.Rock.value + 3,
    (Move.Rock, "Z"): Move.Paper.value + 6,
    (Move.Paper, "X"): Move.Rock.value,
    (Move.Paper, "Y"): Move.Paper.value + 3,
    (Move.Paper, "Z"): Move.Scissors.value + 6,
    (Move.Scissors, "X"): Move.Paper.value,
    (Move.Scissors, "Y"): Move.Scissors.value + 3,
    (Move.Scissors, "Z"): Move.Rock.value + 6,
}


def optimal_strategy_score(rounds: list[tuple[Move, str]]) -> int:
    score = 0
    for opponent_move, self_move in rounds:
        score += optimal_outcomes[(opponent_move, self_move)]

    return score


def parse_file(filename: str) -> list[tuple[Move, str]]:
    with open(filename) as infile:
        rounds = []
        for line in infile:
            oppoenent_move, self_strategy = line.strip().split()
            rounds.append((optimal_mapping[oppoenent_move], self_strategy))
    return rounds


if __name__ == "__main__":
    input = parse_file("data/day2.txt")

    total_score = optimal_strategy_score(input)
    print(total_score)
