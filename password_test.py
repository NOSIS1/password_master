import string


def prover_nad():
    password = input("Введите пароль для проверки : ")
    
    upper = any([1 if i in string.ascii_uppercase else 0 for i in password])
    lower = any([1 if i in string.ascii_lowercase else 0 for i in password])
    simvols = any([1 if i in string.punctuation else 0 for i in password])
    digits = any([1 if i in string.digits else 0 for i in password])
    lenght = len(password)
    
    if lenght >= 10:
        lenght = True
    else:
        lenght = False
        
    answer = [upper, lower, simvols, digits, lenght]
    
    count = 0
    
    for i in range(len(answer)):
        if answer[i] == True:
            count += 1
            
    return f"\nПароль надёжн на {count} из 5" 