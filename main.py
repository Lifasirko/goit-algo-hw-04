# __________________________________________________ Перше завдання __________________________________________________ #

def total_salary(path):
    try:
        with open(path, encoding='utf-8') as f:
            salaries = [int(line.split(',')[1]) for line in f]
            total_sum = sum(salaries)
            average_salary = total_sum / len(salaries) if salaries else 0
        print(f"Загальна сума заробітної плати: {total_sum}, Середня заробітна плата: {average_salary}")
        return total_sum, average_salary
    except FileNotFoundError:
        print("Файл не знайдено.")
        return "Файл не знайдено."
    except Exception as e:
        print(f"Виникла помилка: {str(e)}")
        return f"Виникла помилка: {str(e)}"


# ___________________________________________________Друге завдання___________________________________________________ #

def get_cats_info(path):
    cats_info = []
    try:
        with open(path, encoding='utf-8') as file:
            lines = [el.strip() for el in file.readlines()]
            # print(lines)
            for line in lines:
                id, name, age = line.strip().split(',')
                cats_info.append({"id": id, "name": name, "age": age})
            return cats_info
    except FileNotFoundError:
        print("Файл не знайдено.")
        return "Файл не знайдено."
    except Exception as e:
        print(f"Виникла помилка: {str(e)}")
        return f"Виникла помилка: {str(e)}"


# C:\Users\MikeK\PycharmProjects\in_process\goit-algo-hw-04\cats_file.txt

# __________________________________________________ Третє завдання __________________________________________________ #


import sys
import pathlib
from colorama import Fore, Style


def print_directory_contents(path):
    path = pathlib.Path(path)
    if not path.is_dir():
        print(f"{Fore.RED}Вказаний шлях не є директорією або не існує.{Style.RESET_ALL}")
        return

    for item in path.iterdir():
        if item.is_dir():
            print(f"{Fore.BLUE}{item.name}{Style.RESET_ALL}")
            print_directory_contents(item)  # Рекурсивний виклик для піддиректорій
        else:
            print(f"{Fore.GREEN}{item.name}{Style.RESET_ALL}")

    # python main.py C:\Users\MikeK\PycharmProjects\in_process\goit-algo-hw-04


# ________________________________________________ Четверте завдання ________________________________________________ #


def parse_input(user_input):
    parts = user_input.strip().split(maxsplit=2)
    command = parts[0].lower()
    args = parts[1:] if len(parts) > 1 else []
    return command, args


def add_contact(contacts, name, phone):
    contacts[name] = phone
    return "Contact added."


def change_contact(contacts, name, phone):
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."


def show_phone(contacts, name):
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."


def show_all(contacts):
    return '\n'.join([f"{name}: {phone}" for name, phone in contacts.items()])


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add" and len(args) == 2:
            name, phone = args
            print(add_contact(contacts, name, phone))
        elif command == "change" and len(args) == 2:
            name, phone = args
            print(change_contact(contacts, name, phone))
        elif command == "phone" and len(args) == 1:
            name = args[0]
            print(show_phone(contacts, name))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    # main()
    # print_directory_contents(path)
    # path = input("вкажіть шлях до файла з котами")
    # print(get_cats_info(path))
    while True:
        if len(sys.argv) < 2:
            print(f"{Fore.RED}Будь ласка, вкажіть шлях до директорії як аргумент.{Style.RESET_ALL}")
        else:
            directory_path = sys.argv[1]
            print_directory_contents(directory_path)
