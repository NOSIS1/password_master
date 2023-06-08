from termcolor import colored
import time
from art import tprint
import os
import bruteforce
import generation
import help
import password_test
import hash_parol


# Главное меню

def main_menu():
    clear = lambda: os.system("clear || cls")
    clear()
    try:
        tprint("password  master")
        time.sleep(3)       
        choice_v = int(input(f"1 - детальная настройка \n2 - быстрый пароль \n3 - bruteforce \n4 - проверка на надёжность\n5 - Хэширование\n6 - help\nЧисло: "))
        
        if choice_v == 1:
            print(generation.detal_gen())
                               
        elif choice_v == 2:
            print(generation.bstr_gen())
                               
        elif choice_v == 3:
            return  bruteforce.brute_force_menu()
            
        elif choice_v == 4:
            print(password_test.prover_nad())
            
        elif choice_v == 5:
            print(hash_parol.hashing_menu())
            
        elif choice_v == 6:
            print(help.help())
            
    except ValueError:
        return colored("Вам выдало ошибку: ValueError - Вы указали не тот тип данных", "red")
     
    
    time.sleep(2)        
    restart = input(f"\nХотите продолжить? Yes or No : ")
    if restart == "YES" or restart == "Yes" or restart == "yes":
        clear = lambda: os.system("clear || cls")
        clear()
        main_menu()
    
                  
    
if __name__ == "__main__":
    main_menu()
