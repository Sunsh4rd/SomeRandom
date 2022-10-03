from os.path import exists
import json
from os import popen, stat


def get_system_info():
    output = popen('cat /sys/class/dmi/id/bios*').read().splitlines()
    system_info = {'bios': popen(
        'sudo dmidecode -t 0').read().replace('\t', '').splitlines()[4:-1]}
    system_info.update(
        {'cpu': popen('sudo dmidecode -t 4').read().replace('\t', '').splitlines()[4:-1]})
    system_info.update(
        {'board': popen('sudo dmidecode -t 2').read().replace('\t', '').splitlines()[4:-1]})
    system_info.update(
        {'net': popen('ifconfig -a | grep ether').read().replace('        ', '').splitlines()})
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
