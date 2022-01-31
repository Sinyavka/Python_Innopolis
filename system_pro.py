# Написана небольшая система с тестами по 3-ем языкам программирования
# В файле users записаны логины и пароли, в файл block добавляется IP адресс, пользователя,
# который трижды ввел пароль неправильно
# Каждый тест можно пройти раз в 24 часа

import random
import datetime
import os
import socket

# Проверка не заблокирован ли пользователь
def check_block():
    s = socket.gethostbyname(socket.gethostname())
    with open('block.txt', 'r') as f:
        lines = f.read().splitlines()
    for line in lines:
        if s in line:
            return True
    return False


def read_file(test):
    questions = []
    with open(f'dirTests\\{test}', encoding='utf-8') as f:
        lines = f.read().splitlines()
    for i in range(0, len(lines), 6):
        q = [lines[i], lines[i+1:i+5], int(lines[i+5])]
        questions.append(q)
    return questions


def start_test(questions):
    count_right_answers = 0
    for i, q in enumerate(questions):
        print(f'{i+1}.{q[0]}')
        for j, answer in enumerate(q[1]):
            print(f'{j+1}){answer}')
        user_answer = int(input('Выберите ответ: '))
        if user_answer == q[2]:
            count_right_answers += 1
    percent = count_right_answers * 100 / len(questions)
    return percent


def convert_to_mark(percent):
    if percent >= 80:
        return 5
    elif 60 < percent <= 80:
        return 4
    elif percent >= 40:
        return 3
    else:
        return 2

# Чтение файла в словарь (ключ - логин, значение - пароль)
def read_users():
    logpass = {}
    with open('users.txt') as file:
        lines = file.read().splitlines()
    for line in lines:
        key,value = line.split()
        logpass[key] = value
    return logpass


def write_result(login, mark,test):
    with open('result.txt', 'a') as f:
        f.write(f'{login};{mark};{datetime.datetime.now().strftime("%d.%m.%Y %H:%M")};{test}\n')

# Функция выбора теста (показываем все файлы из директории) и выбираем
def select_test():
    files = os.listdir("dirTests")
    for i,file in enumerate(files):
        print(f'{i}.{file}')
    n = int(input())
    return files[n]


def enter_user(users):
    for i in range(3):
        login = input('Введите логин: ')
        password = input('Введите пароль: ')
        if login in users and users[login] == password:
            return login
        else:
            print('Пароль или логин введены неверно')
    with open('block.txt', 'a') as f:
        f.write(socket.gethostbyname(socket.gethostname()))

    return None

# Проверка сколько времени прошло с момента последнего прохождения теста
def check_time(login,test):
    if os.path.exists('result.txt') is False:
        return True
    with open('result.txt', 'r') as f:
        lines = f.read().split('\n')

    for line in lines:
        if login in line.split(';') and test in line.split(';'):
            d = line.split(';')[2]
            date_ob = datetime.datetime.strptime(d,"%d.%m.%Y %H:%M")
            delta = datetime.datetime.now() - date_ob
            if delta.days == 0:
                return False

    return True




def main():
    if check_block():
        print('Вы заблокированы')
        return
    users = read_users()
    user = enter_user(users)
    if user is None:
        return
    test = select_test()
    if check_time(user, test) is True:
        questions = read_file(test)
        random.shuffle(questions)
        percent = start_test(questions)
        mark = convert_to_mark(percent)
        print(mark)

        write_result(user, mark, test)
    else:
        print('Нельзя пройти тест, прошло менее 24 часов с послдней попытки')

if __name__ == '__main__':
    main()