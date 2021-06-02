def task_one():
    print("")
    input_date = input("Введите дату: ")
    input_task = input("Введите задачу: ")
    date_and_task = input_date + ": " + input_task
    print(date_and_task)
    input("Нажмите Enter для продолжения: ")


def task_two():
    print("")
    input_date_1 = input("Введите дату: ")
    input_task_1 = input("Введите задачу: ")
    input_date_2 = input("Введите дату: ")
    input_task_2 = input("Введите задачу: ")
    input_date_3 = input("Введите дату: ")
    input_task_3 = input("Введите задачу: ")

    date_and_task_1 = input_date_1 + ": " + input_task_1
    date_and_task_2 = input_date_2 + ": " + input_task_2
    date_and_task_3 = input_date_3 + ": " + input_task_3

    print(date_and_task_1)
    print(date_and_task_2)
    print(date_and_task_3)
    input("Нажмите Enter для продолжения: ")


def task_three():
    dates_and_tasks = {}
    print("")
    for counter in range(3):
        input_date = input("Введите дату: ")
        input_task = input("Введите задачу: ")
        dates_and_tasks[input_date] = input_task
    input("Нажмите Enter для продолжения: ")


task_one()
task_two()
task_three()
