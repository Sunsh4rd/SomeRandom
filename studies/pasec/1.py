from os.path import exists
import json
from os import popen, stat


def get_system_info():
    output = popen('cat /sys/class/dmi/id/bios*').read().splitlines()
    bios_parts = ['release_date', 'revision', 'vendor', 'version']
    system_info = {"bios": dict(zip(bios_parts, output))}
    system_info.update(json.loads(popen('lscpu -J').read()))
    system_info.update({'net': popen('lspci').read().splitlines()})
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
                changes = {}
                for k, v in current_system_info.items():
                    if v != system_info_from_file[k]:
                        changes.update({k: v})
                with open('changes.json', 'w', encoding='utf-8') as ch:
                    json.dump(changes, ch, indent=4)

    else:
        print('Необходимый файл не найден')


if __name__ == '__main__':
    main()
