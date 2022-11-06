from os import system
from os.path import exists
from hashlib import md5
from json import dump, load, loads
from random import getrandbits, randint


def get_db_content():
    with open('skey_parameters/host/db.json', 'r', encoding='utf-8') as db_read:
        db = db_read.read()
        if not db or db == 'null':
            return {}
        else:
            return loads(db)


def user_is_in_database(user):
    if not get_db_content():
        return False
    return user in get_db_content().keys()


def generate_hashes(number, n):
    hashes = []
    first = md5(bytes(number)).hexdigest()
    hashes.append(first)
    for _ in range(n):
        new = md5(first.encode()).hexdigest()
        hashes.append(new)
        first = new
    return hashes


def save_user_in_db(user, hash):
    updated_db_content = get_db_content()
    updated_db_content.update({user: hash})
    with open('skey_parameters/host/db.json', 'w', encoding='utf-8') as db_write:
        dump(updated_db_content, db_write, indent=4)


def get_user_hashes(user):
    with open(f'skey_parameters/clients/{user}.json', 'r', encoding='utf-8') as hashes_read:
        hashes = hashes_read.read()
        return loads(hashes) if hashes else {}


def save_user_hashes(user, hashes):
    if not exists(f'skey_parameters/clients/{user}.json'):
        with open(f'skey_parameters/clients/{user}.json', 'w', encoding='utf-8') as hashes_write:
            dump({'hashes': hashes}, hashes_write, indent=4)
    else:
        user_hashes = get_user_hashes(user).get('hashes')
        with open(f'skey_parameters/clients/{user}.json', 'w', encoding='utf-8') as hashes_write:
            dump({'hashes': [*hashes]}, hashes_write, indent=4)


def create_user_params():
    user = input('Введите имя пользователя: ')
    number = getrandbits(int(input('Введите длину случайного числа: ')))
    with open(f'skey_parameters/clients/{user}_paramaters.json', 'w', encoding='utf-8') as params:
        dump({'name': user, 'number': number}, params, indent=4)
    # with open(f'skey_parameters/clients/{user}.py', 'w', encoding='utf-8') as prog:
    #     prog.write(f'print(\'{user}\')')
    return


def register_user():
    user = input('Имя пользователя: ')

    if not exists(f'skey_parameters/clients/{user}_paramaters.json'):
        print('Необходимо произвести генерацию параметров пользователя перед регистрацией в системе')
        return

    if user_is_in_database(user) and get_user_hashes(user)['hashes']:
        print('Пользователь с таким именем уже зарегестрирован')
        return

    n = int(input('Введите параметр n (число одноразовых паролей): '))
    with open(f'skey_parameters/clients/{user}_paramaters.json') as params:
        parameters = load(params)
        name, number = parameters['name'], parameters['number']
    hashes = generate_hashes(number, n)
    save_user_in_db(user, hashes[-1])
    save_user_hashes(user, hashes[:-1])
    print(f'Пользователь {user} зарегистрирован')
    return
    # if not user_is_in_database(user):


def login():
    user = input('Введите имя пользователя: ')
    if not user_is_in_database(user):
        print('Пользователь с таким именем не зарегистрирован')
        return

    if not get_user_hashes(user)['hashes']:
        print('Для данного пользователя исчерпан запас ключей, повторите регистрацию')
        return

    last = get_user_hashes(user)['hashes'][-1]
    _hash = md5(last.encode()).hexdigest()
    if _hash == get_db_content()[f'{user}']:
        print('Вход выполнен успешно')
        updhashes = get_user_hashes(user)['hashes']
        updhashes.remove(last)
        save_user_hashes(user, updhashes)
        save_user_in_db(user, last)
    else:
        print('Вход не выполнен')


def main():
    while True:
        opt = input(
            'Выберите действие:\n0 - Генерация параметров пользователя для регистрации\n1 - Регистрация пользователя в системе\n2 - Вход в систему\n3 - Выход:\n')
        if opt == '0':
            create_user_params()
        elif opt == '1':
            register_user()
        elif opt == '2':
            login()
        elif opt == '3':
            break
        else:
            print('Ошибка, повторите ввод')


if __name__ == '__main__':
    main()
