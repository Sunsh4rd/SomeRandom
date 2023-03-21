def parse_input_as_dict():
    return [(surname, int(score)) for surname, score in (s.split(':') for s in input().split())]


def main():
    data = parse_input_as_dict()
    first, second = data[0], data[1]
    print(data, first, second)
    last_score = data[0][1]
    for i in range(len(data)-1):
        if data[i+1][1] > data[i][1]:
            data[i+1], data[i] = data[i], data[i+1]
        elif data[i+1][1] == last_score:
            continue
        last_score = data[i][1]
    print(data)


if __name__ == '__main__':
    main()
