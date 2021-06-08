
def task_one():
    help_msg = '''
    * help - напечатать справку по программе.
    * add  - добавить задачу в список (название задачи запрашиваем у пользователя).
    * show - напечатать все добавленные задачи.
    * exit - выйти из программы.'''

    tasks = []
    print(help_msg)

    while True:
        input_command = input("Введите команду: ")
        if input_command == "help":
            print(help_msg)
        elif input_command == "add":
            task = input("Введите задачу: ")
            tasks.append(task)
            print("Задача {0} добавлена".format(task))
        elif input_command == "show":
            print(tasks)
        elif input_command == "exit":
            print("Спасибо за использование! До свидания!")
            input()
            break
        else:
            print("Неизвестная команда.")


def task_two():
    help_msg = '''
    * help - напечатать справку по программе.
    * add  - добавить задачу в список (название задачи запрашиваем у пользователя).
    * show - напечатать все добавленные задачи.
    * exit - выйти из программы.'''

    date_msg = '''
    * today - для задач на сегодня.
    * tomorrow - для задач на завтра.
    * other - для задач на другой день.
    '''

    today_tasks = []
    tomorrow_tasks = []
    other_tasks = []

    print(help_msg)

    while True:
        input_command = input("Введите команду: ")
        if input_command == "help":
            print(help_msg)

        elif input_command == "add":
            task = input("Введите задачу: ")
            while True:
                print(date_msg)
                input_date = input("Введите дату для задачи: ")
                if input_date == "today":
                    today_tasks.append(task)
                    print("Задача {0} добавлена на сегодня".format(task))
                elif input_date == "tomorrow":
                    tomorrow_tasks.append(task)
                    print("Задача {0} добавлена на завтра".format(task))
                elif input_date == "other":
                    other_tasks.append(task)
                    print("Задача {0} добавлена на другой день".format(task))
                else:
                    break

        elif input_command == "show":
            print(date_msg)
            while True:
                input_date = input("Введите дату для показа: ")
                if input_date == "today":
                    print(today_tasks)
                elif input_date == "tomorrow":
                    print(tomorrow_tasks)
                elif input_date == "other":
                    print(other_tasks)
                else:
                    break

        elif input_command == "exit":
            break
        else:
            print("Неизвестная команда.")


task_one()
task_two()
