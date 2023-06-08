import hashlib
import os
from art import tprint
import main

def hashing_menu():
    clear = lambda: os.system("clear || cls")
    clear()
    tprint("Hashing")
    try:
        print(f"1 - md5\n2 - sha256\n3 - sha1\n4 - sha224\n5 - sha512\n6 - sha384\n7 - обратно в меню")
        otvet = int(input("Число: "))
        if otvet == 1:
            return hash_md5() 
        elif otvet == 2:
            return hash_sha256()
            
        elif otvet == 3:
            return hash_sha1()
            
        elif otvet == 4:
            return hash_sha224()
            
        elif otvet == 5:
            return hash_sha512()
            
        elif otvet == 6:
            return hash_sha384()
            
        elif otvet == 7:
            clear = lambda: os.system("clear || cls")
            main.main_menu()
                    
    except ValueError:
        return "Вам выдало ошибку: ValueError - Вы указали не тот тип данных"
    
def hash_md5():
    word = input(f'\nВведите то что нужно зашифровать: ')
    print("")
    word = hashlib.md5(word.encode())
    return f'Ваш хэш: {word.hexdigest()}'
    
def hash_sha256():
    word = input(f'\nВведите то что нужно зашифровать: ')
    print("")
    word = hashlib.sha256(word.encode())
    return f'Ваш хэш: {word.hexdigest()}'

def hash_sha1():
    word = input(f'\nВведите то что нужно зашифровать: ')
    print("")
    word = hashlib.sha1(word.encode())
    return f'Ваш хэш: {word.hexdigest()}'

def hash_sha224():
    word = input(f'\nВведите то что нужно зашифровать: ')
    print("")
    word = hashlib.sha224(word.encode())
    return f'Ваш хэш: {word.hexdigest()}'

def hash_sha512():
    word = input(f'\nВведите то что нужно зашифровать: ')
    print("")
    word = hashlib.sha512(word.encode())
    return f'Ваш хэш: {word.hexdigest()}'

def hash_sha384():
    word = input(f'\nВведите то что нужно зашифровать: ')
    print("")
    word = hashlib.sha384(word.encode())
    return f'Ваш хэш: {word.hexdigest()}'
    

    
    