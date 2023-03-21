import json
import math


def get_sample(file):
    with open(file, 'r') as f:
        return json.load(f)


def get_entropy(sample):
    eps = 0.000001
    for p in sample.values():
        if p < 0 or p > 1.0:
            print('Вероятность не может быть меньше нуля или больше единицы')
            return
    if abs(sum(sample.values()) - 1.0) > eps:
        print('Неверные значения вероятностей')
        return

    return -(sum((pi * math.log2(pi) for pi in sample.values())))


def main():
    sample = get_sample('studies\kmzi\sample.json')
    print('Текущее распределение:')
    for v, p in sample.items():
        print(v, p)

    if not get_entropy(sample):
        exit(0)

    print('Значение энтропии для данного распределения:', get_entropy(sample))
    print('Минимальное значение энтропии всегда 0')
    print('Максимальное значение энтропии:', math.log2(len(sample)))


if __name__ == '__main__':
    main()
