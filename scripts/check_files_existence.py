import os
import sys

def check_files(directory_path, file_list_path):
    # Проверяем, существует ли директория
    if not os.path.isdir(directory_path):
        print(f"Директория '{directory_path}' не существует.")
        return

    # Проверяем, существует ли файл со списком файлов
    if not os.path.isfile(file_list_path):
        print(f"Файл '{file_list_path}' не существует.")
        return

    # Читаем список файлов из текстового файла
    with open(file_list_path, 'r', encoding='utf-8') as file:
        files_to_check = [line.strip() for line in file.readlines()]

    # Проверяем наличие каждого файла в директории
    missing_files = []
    for file_name in files_to_check:
        file_path = os.path.join(directory_path, file_name)
        if not os.path.isfile(file_path):
            missing_files.append(file_name)

    # Выводим результат
    if missing_files:
        print("Отсутствующие файлы:")
        for file_name in missing_files:
            print(file_name)
    else:
        print("Все файлы присутствуют.")

if __name__ == "__main__":
    # Проверяем, что переданы правильные аргументы
    if len(sys.argv) != 3:
        print("Использование: py script.py directory_path files.txt")
    else:
        directory_path = sys.argv[1]
        file_list_path = sys.argv[2]
        check_files(directory_path, file_list_path)