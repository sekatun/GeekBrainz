#соединение
def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phon.txt')

    while (choice != 8):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('lastname ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            number = input('number ')
            print(find_by_number(phone_book, number))
        elif choice == 4:
            last_name = input('lastname ')
            new_number = input('new number ')
            print(change_number(phone_book, last_name, new_number))
        elif choice == 5:
            lastname = input('lastname ')
            phone_book = delete_by_lastname(phone_book, lastname)
            write_txt('phon.txt', phone_book)
        elif choice == 6:
            user_data = input('new data (Фамилия,Имя,Телефон,Описание): ')
            add_user(phone_book, user_data)
            write_txt('phon.txt', phone_book)
        elif choice == 7:
            index = int(input('Введите номер строки для копирования: '))
            filename = input('Введите имя файла для сохранения: ')
            CopyFile(phone_book, index, filename)
        elif choice == 8:
            write_txt('phon.txt', phone_book)
        

        choice = show_menu()

def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.strip().split(',')))
            phone_book.append(record)

    return phone_book
#Запись
def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for record in phone_book:
            s = ','.join(record.values())
            phout.write(f'{s}\n')
# 1 вывод
def print_result(phone_book):
    for idx, record in enumerate(phone_book, start=1):
        print(f"{idx}. Фамилия: {record['Фамилия']}, Имя: {record['Имя']}, Телефон: {record['Телефон']}, Описание: {record['Описание']}")
        #(f"Фамилия: {record['Фамилия']}, Имя: {record['Имя']}, Телефон: {record['Телефон']}, Описание: {record['Описание']}\n")

#выбор действий
def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Изменить номер телефона\n"
          "5. Удаление абонента\n"
          "6. Добавить абонента\n"
          "7. скопировать в новый файл\n"
          "8. Закончить работу")
    choice = int(input())
    return choice

# 2 поиск Абонента
def find_by_lastname(phone_book, last_name):
    results = [record for record in phone_book if record['Фамилия'] == last_name]
    return "\n".join([f"Фамилия: {record['Фамилия']}, Имя: {record['Имя']}, Телефон: {record['Телефон']}, Описание: {record['Описание']}" for record in results]) if results else "Абонент не найден"
# 3 По телефлну
def find_by_number(phone_book, number):
    results = [record for record in phone_book if record['Телефон'] == number]
    return "\n".join([f"Фамилия: {record['Фамилия']}, Имя: {record['Имя']}, Телефон: {record['Телефон']}, Описание: {record['Описание']}" for record in results]) if results else "Номер не найден"

# 4 изминение номера телефона
def change_number(phone_book, last_name, new_number):
    for record in phone_book:
        if record['Фамилия'] == last_name:
            record['Телефон'] = new_number
            return "Номер изменен"
    return "Абонент не найден"
# 5 удаление абонента

def delete_by_lastname(phone_book, last_name):
    updated_phone_book = [record for record in phone_book if record['Фамилия'] != last_name]
    return updated_phone_book

# 6 Добовление нового абанента
def add_user(phone_book, user_data):
    fields = ['Фамилия','Имя','Телефон','Описание']
    user_data = user_data.split(',')
    new_record = dict(zip(fields, user_data))
    phone_book.append(new_record)
# 7 Копирование в другой файл
def CopyFile(phone_book, index, filename):
    if 1 <= index <= len(phone_book):
        record = phone_book[index - 1]
        with open(filename,'w', encoding='utf-8') as phb:
            phb.write(f"Фамилия: {record['Фамилия']}, Имя: {record['Имя']}, Телефон: {record['Телефон']}, Описание: {record['Описание']}\n")
        print(f"Запись скопирована в новый файл {filename}")
    else:
        print("Ошибка")

work_with_phonebook()
