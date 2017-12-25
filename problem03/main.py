def get_input(path):
    with open(path) as inputs:
        return [sorted(list(map(int, i.split())), reverse=True) for i in inputs.readlines()]

def main(path):
    matrix = get_input(path)
    result = []
    for row in matrix:
        iter_flag = True
        for val in row:
            if iter_flag:
                for col in row[row.index(val)+1:]:
                    if float.is_integer(val / col):
                        result.append(val / col)
                        iter_flag = False
                        break
            else:
                break
    return sum(result)

if __name__ == '__main__':
    print(main('inputs.txt'))