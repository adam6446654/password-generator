def user_input_validation():
    while True:
        pass_1 = True
        pass_2 = True
        try:
            length = int(input("Password Length: "))
            while length < 0 or length > 16:
                pass_1 = False
                print("Password length is less than 0 or greater than 16")
                length = int(input("Password Length: "))
            pass_1 = True
        except:
            pass_1 = False
            print("Entered invalid data type. try again.")

        try:
            temp = input("Special Characters? (1 (yes) / 0 (no)): ")
            use_special_char = bool(int(temp))
            pass_2 = True
        except:
            pass_2 = False
            print("entered invalid option. Try again.")
        
        if pass_1 == True and pass_2 == True:
            return length,use_special_char

def random_pass_gen(length,use_special_char):
    password = ""
    if use_special_char == True:
        for i in range(0,length):
            password += chr(random.randint(33,126))
    else:
        for i in range(0,length):
            temp = random.randint(33,126)
            if (temp > 47 and temp < 58) or (temp > 64 and temp < 91) or (temp > 96 and temp < 123):
                password += chr(temp)
    
    return password