import heapq

def part_one():
    calories: list[list[int]] = []
    with open('day1.txt', 'r') as f:
        cur_elf_cals: list[int] = [] 
        while line := f.readline():
            if line.strip() == '':
                calories.append(cur_elf_cals)
                cur_elf_cals = []
                continue
            cur_elf_cals.append(int(line))

    return max(map(sum, calories))


def part_two():
    calories: list[list[int]] = []
    with open('day1.txt', 'r') as f:
        cur_elf_cals: list[int] = [] 
        while line := f.readline():
            if line.strip() == '':
                calories.append(cur_elf_cals)
                cur_elf_cals = []
                continue
            cur_elf_cals.append(int(line))

    return sum(heapq.nlargest(3, map(sum, calories)))



if __name__ == '__main__':
    print(part_one())
    print(part_two())