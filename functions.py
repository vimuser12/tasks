#!/usr/bin/env python3
# coding: utf-8

import os
import shutil

def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
        print(f"Folder '{folder_name}' created successfully.")
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists.")
    except PermissionError:
        print(f"Permission denied to create folder '{folder_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_folder(folder_name):
    try:
        os.rmdir(folder_name)
        print(f"Folder '{folder_name}' deleted successfully.")
    except FileNotFoundError:
        print(f"Folder '{folder_name}' not found.")
    except OSError as e:
        print(f"Error: {e}")

CURRENT_DIRECTORY = os.getcwd()

def move_up():
    global CURRENT_DIRECTORY
    if CURRENT_DIRECTORY == "/home/wuw/File_Manager":
        print("You are already in the main folder.")
    else:
        os.chdir("..")
        CURRENT_DIRECTORY = os.getcwd()
        print("Moved up to:", CURRENT_DIRECTORY)

def move_to(folder_name):
    global CURRENT_DIRECTORY
    new_directory = os.path.join(CURRENT_DIRECTORY, folder_name)
    if os.path.exists(new_directory) and os.path.isdir(new_directory):
        os.chdir(new_directory)
        CURRENT_DIRECTORY = os.getcwd()
        print("Moved to:", CURRENT_DIRECTORY)
    else:
        print("Folder not found within the current directory:", folder_name)

def create_file(file_name):
    try:
        with open(file_name, 'w'):
            pass
        print(f"File '{file_name}' created successfully.")
    except FileExistsError:
        print(f"File '{file_name}' already exists.")
    except PermissionError:
        print(f"Permission denied to create file '{file_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

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
    try:
        with open(file_name, 'r') as file:
            contents = file.read()
            print(f"Contents of '{file_name}':")
            print(contents)
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except PermissionError:
        print(f"Permission denied to read file '{file_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f"File '{file_name}' deleted successfully.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except PermissionError:
        print(f"Permission denied to delete file '{file_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def copy_file(file_name):
    destination = input("Enter the destination directory: ")
    try:
        shutil.copy(file_name, destination)
        print(f"File '{file_name}' copied to '{destination}' successfully.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except PermissionError:
        print(f"Permission denied to copy file '{file_name}' to '{destination}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def move_file(file_name):
    destination = input("Enter the destination directory: ")
    try:
        shutil.move(file_name, destination)
        print(f"File '{file_name}' moved to '{destination}' successfully.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except PermissionError:
        print(f"Permission denied to move file '{file_name}' to '{destination}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def rename_file(file_name):
    new_name = input("Enter the new name for the file: ")
    try:
        os.rename(file_name, new_name)
        print(f"File '{file_name}' renamed to '{new_name}' successfully.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except PermissionError:
        print(f"Permission denied to rename file '{file_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

