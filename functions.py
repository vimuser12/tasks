#!/usr/bin/env python3
# coding: utf-8

# Импорт модулей для работы с файловой системой
import os
import shutil

# Функция для создания папки
def create_folder(folder_name):
  """
  Создает папку с указанным именем.

  Args:
      folder_name (str): Имя создаваемой папки.

  Returns:
      None
  """
  try:
    # Пытается создать папку
    os.mkdir(folder_name)
    print(f"Папка '{folder_name}' создана успешно.")
  except FileExistsError:
    # Обработка ошибки: папка уже существует
    print(f"Папка '{folder_name}' уже существует.")
  except PermissionError:
    # Обработка ошибки: недостаточно прав для создания папки
    print(f"Нет разрешения на создание папки '{folder_name}'.")
  except Exception as e:
    # Обработка других исключений
    print(f"Произошла ошибка: {e}")

# Функция для удаления папки
def delete_folder(folder_name):
  """
  Удаляет папку с указанным именем.

  Args:
      folder_name (str): Имя удаляемой папки.

  Returns:
      None
  """
  try:
    # Пытается удалить папку
    os.rmdir(folder_name)
    print(f"Папка '{folder_name}' удалена успешно.")
  except FileNotFoundError:
    # Обработка ошибки: папка не найдена
    print(f"Папка '{folder_name}' не найдена.")
  except OSError as e:
    # Обработка других ошибок удаления
    print(f"Ошибка: {e}")

# Текущая рабочая директория
CURRENT_DIRECTORY = os.getcwd()

# Функция для перемещения вверх по дереву каталогов
def move_up():
  """
  Перемещает на уровень выше в дереве каталогов.
  """
  global CURRENT_DIRECTORY
  if CURRENT_DIRECTORY == "/home/wuw/File_Manager":
    print("Вы уже находитесь в главной папке.")
  else:
    # Перемещение на уровень выше
    os.chdir("..")
    # Обновление текущей рабочей директории
    CURRENT_DIRECTORY = os.getcwd()
    print(f"Перемещено вверх: {CURRENT_DIRECTORY}")

# Функция для перемещения в другую папку
def move_to(folder_name):
  """
  Перемещает в указанную папку.

  Args:
      folder_name (str): Имя папки, в которую нужно перейти.
  """
  global CURRENT_DIRECTORY
  # Формирование полного пути к новой папке
  new_directory = os.path.join(CURRENT_DIRECTORY, folder_name)
  if os.path.exists(new_directory) and os.path.isdir(new_directory):
    # Проверка существования и типа папки
    os.chdir(new_directory)
    # Обновление текущей рабочей директории
    CURRENT_DIRECTORY = os.getcwd()
    print(f"Перемещено в: {CURRENT_DIRECTORY}")
  else:
    print(f"Папка '{folder_name}' не найдена в текущей директории.")

# Функция для создания файла
def create_file(file_name):
  """
  Создает пустой файл с указанным именем.

  Args:
      file_name (str): Имя создаваемого файла.

  Returns:
      None
  """
  try:
    # Пытается создать файл
    with open(file_name, 'w'):
      pass
    print(f"Файл '{file_name}' создан успешно.")
  except FileExistsError:
    # Обработка ошибки: файл уже существует
    print(f"Файл '{file_name}' уже существует.")
  except PermissionError:
    # Обработка ошибки: недостаточно прав для создания файла
    print(f"Нет разрешения на создание файла '{file_name}'.")
  except Exception as e:
    # Обработка других исключений
    print(f"Произошла ошибка: {e}")
def write_to(file_name):
    text = input("Enter the text to write to the file: ")
    try:
        with open(file_name, 'w') as file:
            file.write(text)
        print(f"Text written to '{file_name}' successfully.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except PermissionError:
        print(f"Permission denied to write to file '{file_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_context(file_name):
  """
  Выводит содержимое указанного файла на экран.
  """
  try:
    # Открывает файл в режиме чтения
    with open(file_name, 'r') as file:
      contents = file.read()
      # Печатает содержимое файла
      print(f"Contents of '{file_name}':")
      print(contents)
  except FileNotFoundError:
    # Обрабатывает ошибку отсутствия файла
    print(f"File '{file_name}' not found.")
  except PermissionError:
    # Обрабатывает ошибку при отсутствии прав на чтение
    print(f"Permission denied to read file '{file_name}'.")
  except Exception as e:
    # Обрабатывает другие исключения
    print(f"An error occurred: {e}")

def delete_file(file_name):
  """
  Удаляет указанный файл.
  """
  try:
    # Удаляет файл с помощью os.remove
    os.remove(file_name)
    print(f"File '{file_name}' deleted successfully.")
  except FileNotFoundError:
    # Обрабатывает ошибку отсутствия файла
    print(f"File '{file_name}' not found.")
  except PermissionError:
    # Обрабатывает ошибку при отсутствии прав на удаление
    print(f"Permission denied to delete file '{file_name}'.")
  except Exception as e:
    # Обрабатывает другие исключения
    print(f"An error occurred: {e}")

def copy_file(file_name):
  """
  Копирует указанный файл в указанную директорию.
  """
  destination = input("Enter the destination directory: ")
  try:
    # Копирует файл с помощью shutil.copy
    shutil.copy(file_name, destination)
    print(f"File '{file_name}' copied to '{destination}' successfully.")
  except FileNotFoundError:
    # Обрабатывает ошибку отсутствия файла или директории
    print(f"File '{file_name}' not found.")
  except PermissionError:
    # Обрабатывает ошибку отсутствия прав на копирование
    print(f"Permission denied to copy file '{file_name}' to '{destination}'.")
  except Exception as e:
    # Обрабатывает другие исключения
    print(f"An error occurred: {e}")

def move_file(file_name):
  """
  Перемещает указанный файл в указанную директорию.
  """
  destination = input("Enter the destination directory: ")
  try:
    # Перемещает файл с помощью shutil.move
    shutil.move(file_name, destination)
    print(f"File '{file_name}' moved to '{destination}' successfully.")
  except FileNotFoundError:
    # Обрабатывает ошибку отсутствия файла или директории
    print(f"File '{file_name}' not found.")
  except PermissionError:
    # Обрабатывает ошибку отсутствия прав на перемещение
    print(f"Permission denied to move file '{file_name}' to '{destination}'.")
  except Exception as e:
    # Обрабатывает другие исключения
    print(f"An error occurred: {e}")

def rename_file(file_name):
  """
  Переименовывает указанный файл.
  """
  new_name = input("Enter the new name for the file: ")
  try:
    # Переименовывает файл с помощью os.rename
    os.rename(file_name, new_name)
    print(f"File '{file_name}' renamed to '{new_name}' successfully.")
  except FileNotFoundError:
    # Обрабатывает ошибку отсутствия файла
    print(f"File '{file_name}' not found.")
  except PermissionError:
    # Обрабатывает ошибку отсутствия прав на переименование
    print(f"Permission denied to rename file '{file_name}'.")
  except Exception as e:
    # Обрабатывает другие исключения
    print(f"An error occurred: {e}")


