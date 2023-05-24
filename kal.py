print("Приветствуем вас в нашем банкомате!")
def main ():
    print(""
          "\nВыберите режим работы:"
          "\n1.Зарегистрироваться"
          "\n2.Авторизоваться")

    mode = int(input())
    if mode == 1:
        registration()
    elif mode ==2:
        authorization()



def registration():
    """Функция регистрации нового пользователя"""
    username = input("Введите логин: ")
    password = input("Введите пароль: ")

    # открытие файла для записи
    with open("users.txt", "a") as f:
        # запись логина и пароля пользователя в файл
        f.write(f"{username}:{password}\n")

    print("Регистрация успешно завершена.")
    main()


def authorization():
    """Функция авторизации зарегистрированных пользователей"""
    username = input("Введите логин: ")
    password = input("Введите пароль: ")

    # открытие файла для чтения
    with open("users.txt", "r") as f:
        # чтение логинов и паролей всех пользователей из файла
        users = f.readlines()

    # проверка наличия введенного логина и пароля в списке пользователей
    for user in users:
        # разделение логина и пароля по символу ":" и удаление символа переноса строки ('\n')
        login, pwd = user.strip().split(":")
        if username == login and password == pwd:
            print("Авторизация успешно завершена.")
            return

    print("Неверный логин или пароль.")
main()