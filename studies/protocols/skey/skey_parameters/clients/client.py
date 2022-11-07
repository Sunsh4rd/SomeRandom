from hashlib import md5
from json import dump, loads
from random import getrandbits
from os.path import exists


def get_db_content():
    with open('../host/db.json', 'r', encoding='utf-8') as db_read:
        db = db_read.read()
        if not db or db == 'null':
            return {}
        else:
            return loads(db)


def user_is_in_database(user):
    if not get_db_content():
        return False
    return user in get_db_content().keys()


def create_user_params():
    user = input('Введите имя пользователя: ')
    number = getrandbits(int(input('Введите длину случайного числа: ')))
    with open(f'{user}_register.json', 'w', encoding='utf-8') as params:
        dump({'name': user, 'number': number}, params, indent=4)
    return


def save_user_in_db(user, hash):
    updated_db_content = get_db_content()
    updated_db_content.update({user: hash})
    with open('../host/db.json', 'w', encoding='utf-8') as db_write:
        dump(updated_db_content, db_write, indent=4)


def get_user_hashes(user):
    with open(f'{user}.json', 'r', encoding='utf-8') as hashes_read:
        hashes = hashes_read.read()
        return loads(hashes) if hashes else {}


def save_user_hashes(user, hashes):
    if not exists(f'{user}.json'):
        with open(f'{user}.json', 'w', encoding='utf-8') as hashes_write:
            dump({'hashes': hashes}, hashes_write, indent=4)
    else:
        user_hashes = get_user_hashes(user).get('hashes')
        with open(f'{user}.json', 'w', encoding='utf-8') as hashes_write:
            dump({'hashes': [*hashes]}, hashes_write, indent=4)


def login():
    user = input('Введите имя пользователя: ')
    if not user_is_in_database(user):
        print('Пользователь с таким именем не зарегистрирован')
        return

    if not get_user_hashes(user)['hashes']:
        print('Для данного пользователя исчерпан запас ключей, повторите регистрацию')
        return

    # last = get_user_hashes(user)['hashes'][-1]
    last = input('Введите пароль: ')
    print(f'Пользователь {user} отправляет пароль {last}')
    _hash = md5(last.encode()).hexdigest()
    print(f'Хэш этого пароля: {_hash}')
    saved_in_db = get_db_content()[f'{user}']
    print(f'Хэш, сохраненный в базе: {saved_in_db}')
    if _hash == saved_in_db:
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
            'Выберите действие:\n0 - Создание данных для регистрации пользователя\n1 - Вход в систему\n2 - Выход:\n')
        if opt == '0':
            create_user_params()
        elif opt == '1':
            login()
        elif opt == '2':
            break
        else:
            print('Ошибка, повторите ввод')


if __name__ == '__main__':
    main()
