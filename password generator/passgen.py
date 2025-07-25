import random
import hashlib
import requests

def user_input_validation():
    while True:
        pass_1 = True
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
            continue

        if pass_1 == True:
            break
    
    while True:
        pass_2 = True
        try:
            temp = input("Special Characters? (1 (yes) / 0 (no)): ")
            if int(temp) != 1 and int(temp) != 0:
                raise Exception("Input must be 0 or 1")
            use_special_char = bool(int(temp))
            pass_2 = True
        except:
            pass_2 = False
            print("entered invalid option. Try again.")

        if pass_2 == True:
            break
        
    if pass_1 == True and pass_2 == True:
        return length,use_special_char

def random_pass_gen(length,use_special_char):
    password = ""
    if use_special_char == True:
        for i in range(0,length):
            password += chr(random.randint(33,126))
    else:
        i = 0
        while i < length:
            temp = random.randint(33,126)
            if (temp > 47 and temp < 58) or (temp > 64 and temp < 91) or (temp > 96 and temp < 123):
                password += chr(temp)
                i += 1
    
    return password

def pwned_pass(password):
    hash_pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    pfx = hash_pass[:5]
    sfx = hash_pass[5:]
    url = f'https://api.pwnedpasswords.com/range/{pfx}'
    response = requests.get(url)
    hashes = (line.split(':') for line in response.text.splitlines())
    for rsfx,count in hashes:
        if rsfx == sfx:
            return int(count)
        
    return 0

def get_not_breached(password,length,use_special_char):
    count = pwned_pass(password)
    while count > 0:
        password = random_pass_gen(length,use_special_char)
        count = pwned_pass(password)

    
    return password

def main():
    a,b = user_input_validation()
    temp = random_pass_gen(a,b)
    password = get_not_breached(temp,a,b)
    print(password)

if __name__ == "__main__":
    main()