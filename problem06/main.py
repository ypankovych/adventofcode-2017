from collections import Counter

def get_input(path):
    with open(path) as inputs:
        return [x.split() for x in inputs.readlines()]

def main(path):
    data = get_input(path)
    return sum([1 for i in data if not [1 for j in i for x in i[i.index(j)+1:] if Counter(j) == Counter(x)]])
    
if __name__ == '__main__':
    print(main('inputs.txt'))