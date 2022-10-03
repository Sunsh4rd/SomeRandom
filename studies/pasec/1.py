from os.path import exists
import json
from os import popen, stat


def get_system_info():
    output = popen('cat /sys/class/dmi/id/bios*').read().splitlines()
    bios_parts = ['release_date', 'revision', 'vendor', 'version']
    system_info = {"bios": dict(zip(bios_parts, output))}
    system_info.update(json.loads(popen('lscpu -J').read()))
    system_info.update({'net': popen('lspci').read()})
    return system_info


def main():
    if exists('info.json'):
        if stat('info.json').st_size == 0:
            print('Записывается текущее аппаратное окружение')
            with open('info.json', 'w', encoding='utf-8') as info:
                json.dump(get_system_info(), info, indent=4)
        else:
            print('Проверка изменений в аппаратном окружении')
            with open('info.json', 'r', encoding='utf-8') as info:
                system_info_from_file = json.load(info)

            current_system_info = get_system_info()

            if system_info_from_file == current_system_info:
                print('Изменений не обнаружено')
            else:
                print(
                    'Обнаружены изменения в аппаратном окружении, записаны в файл changes.json')
                changes = list(filter(lambda x: x[0] != x[1], zip(
                    current_system_info, system_info_from_file)))
                print(changes)
                # print(system_info_from_file)
                # print(current_system_info)
                # for i in range(len(current_system_info)):
                #     if current_system_info[i] == system_info_from_file[i]:
                #         print(current_system_info[i], sep=' ')
                #     else:
                #         break
                # print(*zip(current_system_info, system_info_in_file))
                # print(list(filter(lambda x: x[0] != x[1], zip(
                # system_info_in_file, current_system_info))))
    else:
        print('Необходимый файл не найден')


if __name__ == '__main__':
    main()
