import random
from termcolor import colored
import time
import string

#Быстрый пароль

def bstr_gen():
    try:
        bk_an = string.ascii_letters
        bk = "йцукенгшщзхъфывапролджэячсмитьбю"
        bk_ru = bk + bk.upper()
        zim = "1234567890!@#$%^&*(_-+=;:/?"
        dobav_ru = input("Добавить русские буквы Yes or No : ")
        
        if dobav_ru == "YES" or dobav_ru == "Yes" or dobav_ru == "yes":
            nabor = bk_an + bk_ru + zim
        else:
            nabor = bk_an + zim
        
        answer = ""
        skok_bstr = int(input("Количество символов в пароле : "))
        if skok_bstr <= 0:
            return colored("Вы указали 0 символов!", "red")
        count_bstr = 0
        while count_bstr <= skok_bstr:
            if count_bstr == skok_bstr:
                break
            else:
                answer += random.choice(nabor)
                count_bstr += 1
                
        return (f"\nВаш пароль: {answer[::-1]}")
    except ValueError:
        return colored("Вам выдало ошибку: ValueError - Вы указали не тот тип данных", "red")

#--------------------------------------------------------------------------------------------

#Детальная настройка

def detal_gen():
    try:
        yaziki = ["Ru", "RU", "ru", "EU", "eu", "Eu"]
        yaz = input("Язык EU or RU : ")
        if yaz in yaziki:
            pass
        else:
            return colored("Ошибка, такого языка нет!", "red")
        
        time.sleep(1)
        skok = int(input("Количество символов : "))
        time.sleep(1)
        sim = input("Использовать ли спец.символы Yes or No : ")
        time.sleep(1)
        chisl = input("Использовать ли числа Yes or No : ")
        time.sleep(1)
        
        bk = "йцукенгшщзхъфывапролджэячсмитьбю"
        bykv_ru = bk + bk.upper()
        bykv_ang = string.ascii_letters
        sim_is = "!@№;%:?*(-)=+<>,/?][{"
        chisl_is = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        count = 0
        
        
        str_answer = ""
        
        if skok == 0:
            return colored("Вы указали 0 символов!", "red")
        else:
            while count <= skok:
                
                
                if yaz == "RU" or yaz == "Ru" or yaz == "rU" or yaz == "ru":
                   chifr = random.randint(1,2)
                   if chifr == 1:
                       str_answer += random.choice(bykv_ru)
                       count += 1
                       if count == skok:
                        break
                                     
                if yaz == "EU" or yaz == "Eu" or yaz == "eU" or yaz == "eu":
                    chifr = random.randint(1,2)
                    if chifr == 1:
                       str_answer += random.choice(bykv_ang)
                       count += 1
                       if count == skok:
                        break
                    
                if sim == "YES" or sim == "Yes" or sim == "yes":
                    chifr = random.randint(1,2)
                    if chifr == 1:
                       str_answer += random.choice(sim_is)
                       count += 1
                       if count == skok:
                        break
                    
                if chisl == "YES" or chisl == "Yes" or chisl == "yes":
                    chifr = random.randint(1,2)
                    if chifr == 1:
                       str_answer += random.choice(chisl_is)
                       count += 1
                       if count == skok:
                        break
                    
                    
                if count == skok:
                    break
                
        request = input("Вам нужно сохранить файл с паролем? YES or NO : ")
        if request == "YES" or request == "Yes" or request == "yes":
            time.sleep(1)
            way = input("Укажите путь куда сохранить : ")
            try:
                with open(way, "a", encoding="utf-8") as fl:
                    fl.write(str_answer[::-1])
                return "Пароль успешно сохранён!"
            
            except PermissionError:
                return colored(f"""\nВы должны указать путь до txt файла в который сохраниться пароль!
Если файла не окажется в директории, то файл будет создан. 
C:/Users/Пользователь/Desktop/parol.txt - верно, пароль будет сохранён в файл parol.txt""", "red")
        else:
            sluch = random.randint(1,2)
            if sluch == 1:
                return (f"\nВаш пароль: {str_answer[::-1]}")
            else:
                return (f"\nВаш пароль: {str_answer}")
            
        
    except ValueError:
        return colored("Вам выдало ошибку: ValueError - где то вы указали не тот тип данных", "red")