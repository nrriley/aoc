
def part_one():
    opponent_moves: list[str] = []
    my_moves: list[str] = []

    with open('day2.txt', 'r') as f:
        while line := f.readline():
            opponent_moves.append(line[0])
            my_moves.append(line[2])

    my_score = 0
    for op, me in zip(opponent_moves, my_moves):
        if me == 'X':
            my_score += 1
            if op == 'A':
                my_score += 3
            elif op == 'C':
                my_score += 6
        elif me == 'Y':
            my_score += 2
            if op == 'B':
                my_score += 3
            elif op == 'A':
                my_score += 6
        elif me == 'Z':
            my_score += 3
            if op == 'C':
                my_score += 3
            elif op == 'B':
                my_score += 6

    return my_score


def part_two():
    opponent_moves: list[str] = []
    outcomes: list[str] = []

    with open('day2.txt', 'r') as f:
        while line := f.readline():
            opponent_moves.append(line[0])
            outcomes.append(line[2])

    my_score = 0
    for op, outcome in zip(opponent_moves, outcomes):
        if outcome == 'X':
            my_score += 0
            if op == 'A':
                my_score += 3
            elif op == 'B':
                my_score += 1
            elif op == 'C':
                my_score += 2
        elif outcome == 'Y':
            my_score += 3
            if op == 'A':
                my_score += 1
            elif op == 'B':
                my_score += 2
            elif op == 'C':
                my_score += 3
           
        elif outcome == 'Z':
            my_score += 6
            if op == 'A':
                my_score += 2
            elif op == 'B':
                my_score += 3
            elif op == 'C':
                my_score += 1
            

    return my_score

if __name__ == '__main__':
    print(part_one())
    print(part_two())