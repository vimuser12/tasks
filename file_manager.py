#!/usr/bin/env python3
# coding: utf-8

import os
from functions import *

def main():   
    while True:
        
        print("Choose an action:")
        print("1. Create folder")
        print("2. Delete folder")
        print("3. Move")
        print("4. Create file")
        print("5. Write text to file")
        print("6. View file contents")
        print("7. Delete file")
        print("8. Copy file")
        print("9. Move file")
        print("10. Rename file")
        
        choice = input("Enter the choice: ")
        choice = int(choice)
        
        if choice == 1:
            folder_name = input("Enter the name of the folder: ")
            create_folder(folder_name)
            
        elif choice == 2:
            folder_name = input("Enter the name of the folder: ")
            delete_folder(folder_name)
            
        elif choice == 3:
            print("Choose where do you want to move:")
            print("1. Up")
            print("2. Another folder (in the main folder)")
            
            choice2 = input("Enter the choice: ")
            
            if choice2 == 1:
                move_up()
            else:
                folder_name2 = input("Enter the name of the folder: ")
                move_to(folder_name2)
                
        elif choice == 4:
            file_name = input("Enter the name of the file: ")
            create_file(file_name)
        
        elif choice == 5:
            file_name = input("Enter the name of the file: ")
            write_to(file_name)
            
        elif choice == 6:
            file_name = input("Enter the name of the file: ")
            view_context(file_name)
            
        elif choice == 7:
            file_name = input("Enter the name of the file: ")
            delete_file(file_name)
            
        elif choice == 8:
            file_name = input("Enter the name of the file: ")
            copy_file(file_name)
            
        elif choice == 9:
            file_name = input("Enter the name of the file: ")
            move_file(file_name)
            
        elif choice == 10:
            file_name = input("Enter the name of the file: ")
            rename_file(file_name)

        else:
            print("Input error")

if __name__ == "__main__":
    main()
