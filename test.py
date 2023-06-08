#def brute_force_vse():   
#    try:
#        brute_fail = input("Укажите путь до PDF-файла : ")
#        password_lenght = input("Введите длину пароля, от скольки символов - до скольки символов, например 3 - 7 : ")
#        password_lenght = [int(item) for item in password_lenght.split("-")]
#    except:
#        print("Ошибка!")
#        
#    print("Если пароль содержит только цифры, введите: 1\nЕсли пароль содержит только буквы, введите: 2\n"
#          "Если пароль содержит цифры и буквы введите: 3\nЕсли пароль содержит цифры, буквы и спецсимволы введите: 4")
#        
#    try:
#        choice = int(input(": "))
#        if choice == 1:
#            possible_symbols = digits
#        elif choice == 2:
#            possible_symbols = ascii_letters
#        elif choice == 3:
#            possible_symbols = digits + ascii_letters
#        elif choice == 4:
#            possible_symbols = digits + ascii_letters + punctuation
#        else:
#            possible_symbols = "Error"
#            print(possible_symbols)
#    except:
#        print("Error")
#        
#    start_timestamp = time.time()
#    print(f"Started at - {datetime.utcfromtimestamp(time.time()).strftime('%H:%M:%S')}")
#    
#       
#    for pass_length in range(password_lenght[0], password_lenght[1] + 1):
#        for password in itertools.product(possible_symbols, repeat=pass_length):
#            password = "".join(password)               
#            print(password)
#            try:
#                with pikepdf.open(brute_fail, password=password) as pdf:
#                    print(f"\nFinished at - {time.strftime('%H:%M:%S')}")
#                    print(f"Password cracking time - {(time.time() - start_timestamp) / 60} min")
#                    return(f"Password: {password}\n")
#                        
#            except pikepdf.PasswordError:
#                continue