def get_input(path):
    with open(path) as inputs:
        return [list(map(int, i.split())) for i in inputs.readlines()]

def main(path):
    matrix = get_input(path)
    return sum([max(i) - min(i) for i in matrix])

if __name__ == '__main__':
    print(main('inputs.txt'))