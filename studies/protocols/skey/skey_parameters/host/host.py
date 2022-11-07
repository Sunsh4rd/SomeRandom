from hashlib import md5
from json import dump, load, loads
from os.path import exists


def get_db_content():
    with open('db.json', 'r', encoding='utf-8') as db_read:
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
    with open('db.json', 'w', encoding='utf-8') as db_write:
        dump(updated_db_content, db_write, indent=4)


def get_user_hashes(user):
    if not exists(f'../clients/{user}.json'):
        return {}
    with open(f'../clients/{user}.json', 'r', encoding='utf-8') as hashes_read:
        hashes = hashes_read.read()
        return loads(hashes) if hashes else {}


def save_user_hashes(user, hashes):
    if not exists(f'../clients/{user}.json'):
        with open(f'../clients/{user}.json', 'w', encoding='utf-8') as hashes_write:
            dump({'hashes': hashes}, hashes_write, indent=4)
    else:
        user_hashes = get_user_hashes(user).get('hashes')
        with open(f'../clients/{user}.json', 'w', encoding='utf-8') as hashes_write:
            dump({'hashes': [*hashes]}, hashes_write, indent=4)


def register_user():
    user = input('Имя пользователя: ')
    number_in = int(input('Введите число: '))

    if not exists(f'../clients/{user}_register.json'):
        print('Необходимо произвести генерацию параметров пользователя перед регистрацией в системе')
        return

    with open(f'../clients/{user}_register.json') as params:
        parameters = load(params)
        name, number = parameters['name'], parameters['number']

    # if user_is_in_database(name) and get_user_hashes(name)['hashes']:
    #     print('Пользователь с таким именем уже зарегестрирован')
    #     return

    n = int(input('Введите параметр n (число одноразовых паролей): '))

    hashes = generate_hashes(number_in, n)
    save_user_in_db(name, hashes[-1])
    save_user_hashes(name, hashes[:-1])
    print(f'Пользователь {name} зарегистрирован')
    return


def main():
    while True:
        opt = input(
            'Выберите действие:\n0 - Регистрация пользователя в системе\n1 - Выход:\n')
        if opt == '0':
            register_user()
        elif opt == '1':
            break
        else:
            print('Ошибка, повторите ввод')


if __name__ == '__main__':
    main()
