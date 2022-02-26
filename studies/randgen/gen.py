import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', type=int)
    parser.add_argument('-b', type=int)
    parser.add_argument('-s', '--some', type=int, default=3)
    args = parser.parse_args()
    print(args)
    print(args.a + args.b + args.some)


if __name__ == '__main__':
    main()
