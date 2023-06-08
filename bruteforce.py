import time
from art import tprint
import os
import pikepdf
from tqdm import tqdm
import itertools
from string import digits, punctuation, ascii_letters
from datetime import datetime
import main
import threading
from queue import Queue



def brute_force_menu():
    clear = lambda: os.system("clear || cls")
    clear()
    tprint("bruteforce")
    try:
        print(f"1 - bruteforce pdf-файла по словарю\n2 - bruteforce pdf-файла без словаря\n3 - обратно в меню")
        otvet = int(input("Число: "))
        if otvet == 1:
            print(brute_force_slovar())
        elif otvet == 2:
            print(brute_force_vse())
        elif otvet == 3:
            clear = lambda: os.system("clear || cls")
            main.main_menu()
                    
    except ValueError:
        return "Вам выдало ошибку: ValueError - Вы указали не тот тип данных"
    
# bruteforce по словарю
    
def brute_force_slovar():
    sbornik_parol = input("Укажите путь до словаря : ")
    brute_fail = input("Укажите путь до PDF-файла : ")
    
    passwords = [line.strip() for line in open(sbornik_parol)]
    
    for password in tqdm(passwords, "Расшифровка pdf-файла"):
        try:
            with pikepdf.open(brute_fail, password=password) as pdf:
                return(f"\nПароль: {password}")
                    
        except pikepdf.PasswordError:
            continue
        
 
#bruteforce без словаря
def brute_force_vse():   
    try:
        brute_fail = input("Укажите путь до PDF-файла : ")
        password_lenght = input("Введите длину пароля, от скольки символов - до скольки символов, например 3 - 7 : ")
        password_lenght = [int(item) for item in password_lenght.split("-")]
    except:
        print("Ошибка!")
        
    print("Если пароль содержит только цифры, введите: 1\nЕсли пароль содержит только буквы, введите: 2\n"
          "Если пароль содержит цифры и буквы введите: 3\nЕсли пароль содержит цифры, буквы и спецсимволы введите: 4")
        
    try:
        choice = int(input(": "))
        if choice == 1:
            possible_symbols = digits
        elif choice == 2:
            possible_symbols = ascii_letters
        elif choice == 3:
            possible_symbols = digits + ascii_letters
        elif choice == 4:
            possible_symbols = digits + ascii_letters + punctuation
        else:
            possible_symbols = "Error"
            print(possible_symbols)
    except:
        print("Error")
        
    start_timestamp = time.time()
    print(f"Started at - {datetime.utcfromtimestamp(time.time()).strftime('%H:%M:%S')}")
    
       
    for pass_length in range(password_lenght[0], password_lenght[1] + 1):
        for password in itertools.product(possible_symbols, repeat=pass_length):
            password = "".join(password)               
            print(password)
            try:
                with pikepdf.open(brute_fail, password=password) as pdf:
                    print(f"\nFinished at - {time.strftime('%H:%M:%S')}")
                    print(f"Password cracking time - {(time.time() - start_timestamp) / 60} min")
                    return(f"Password: {password}\n")
                        
            except pikepdf.PasswordError:
                continue