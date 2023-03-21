from os import popen


def main():
    mount = popen(f'df {__file__}').readlines()[1]
    mount = mount[:mount.index(' ')]
    print(mount)
    with open(mount, 'rb') as f:
        print(f.read(128))
    print(int('0x1e0', base=16))
    skip = 4096
    while True:
        free_space = popen(f'sudo xxd -s {skip} -l 512 {mount}').readlines()
        for i in free_space:
            print(i[:8],i[10:49])
            if i[10:49] != '0000 0000 0000 0000 0000 0000 0000 0000':
                skip += 512
                break
        else:
            break


if __name__ == "__main__":
    main()