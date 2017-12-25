def get_input(path):
    with open(path) as inputs:
        return [x.split() for x in inputs.readlines()]

def main(path):
    data = get_input(path)
    return sum([1 for elem in data if len(set(elem)) == len(elem)])

if __name__ == '__main__':
    print(main('inputs.txt'))