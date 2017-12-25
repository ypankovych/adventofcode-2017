def get_input(path):
    with open(path) as inputs:
        return list(map(int, list(inputs.read())))

def main(path):
    inputs = get_input(path)
    return sum([i*2 for i, j in zip(inputs[:len(inputs)//2], inputs[len(inputs)//2:]) if i == j])

if __name__ == '__main__':
    print(main('inputs.txt'))