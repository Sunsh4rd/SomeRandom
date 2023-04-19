import string


def index_of_coincidence_avg(seq1, seq2):
    alph = string.ascii_lowercase
    return sum(seq1.count(a) / len(seq1) * seq2.count(a) / len(seq2) for a in alph)


def index_of_coincidence(seq1, seq2):
    return len(list(filter(lambda pair: pair[0] == pair[1], zip(seq1, seq2)))) / min(len(seq1), len(seq2))


def main():
    print(index_of_coincidence('bbcdf', 'abcdef'))
    print(index_of_coincidence_avg('the', 'the'))


if __name__ == '__main__':
    main()
