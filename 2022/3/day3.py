def get_priority(c):
    if ord(c) > 97:
        return ord(c) - 96
    else:
        return ord(c) - 38


def part_one():
    sum = 0

    with open('day3.txt', 'r') as f:
        while line := f.readline():
            line = line.strip()
            pocket1 = set(line[0:len(line)//2])
            pocket2 = set(line[len(line)//2:])
            for item in pocket1:
                if item in pocket2:
                    sum += get_priority(item)

    return sum

def part_two():
    sum = 0

    with open('day3.txt', 'r') as f:
        while line1 := f.readline().strip():
            line2 = f.readline().strip()
            line3 = f.readline().strip()
            elf1, elf2, elf3 = set(line1), set(line2), set(line3)

            for item in elf1:
                if item in elf2 and item in elf3:
                    sum += get_priority(item)

    return sum

if __name__ == '__main__':
    print(part_one())
    print(part_two())