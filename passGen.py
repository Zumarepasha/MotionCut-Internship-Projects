import random   

def generate_password(length):  
    "This function accepts a parameter 'len' and returns a randomly generated password"  

    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"  
    nums = "0123456789"  
    symbols = "!@#$%^&*()"   
    passwordList = []

    charList = chars + nums + symbols

    if length > 2:   # if password length is greater than 2 then adding each element into our password
        selected_char = random.sample(chars, 1)  # atleast 1 character
        selected_nums = random.sample(nums, 1)  # atleast 1 number
        selected_symbols = random.sample(symbols, 1)  # atleast 1 symbol
        passwordList = selected_char+selected_nums+selected_symbols
    
    if len(passwordList) != length:
        x = length-len(passwordList)
        xSelect = random.sample(charList, x) # remaining characters for password
        passwordList += xSelect

    random.shuffle(passwordList) 
    pass_str = "".join(passwordList)   

    return pass_str  

def Match(length, l):
    "This function returns a unique passwords by accepting 'length' and empty list 'l' "

    z = ""
    while True:
        z  = generate_password(length)
        if not l:
            l.append(z)
            break

        else:
            if z in l:
                continue

            else:
                l.append(z)
                break
            
    return z


if __name__ == "__main__":  
    userSelection = input("\nDo you wish to generate a Password?\nPress 'Y/y' to Continue, or 'N/n' to Exit: ")

    if userSelection == 'N' or userSelection == 'n':  
        print("Thank You! See you next time.\n") 

    elif userSelection == 'Y' or userSelection == 'y':    
        length = int(input("Enter the length of the Password: "))
        times = int(input("How many Passwords do you need?: "))

        print("A randomly generated Password is:")
        l =[]
        i=0
        while i<times:
            pass_str = Match(length, l)
            print(pass_str)
            i += 1
        print()
    else:  
        print("Invalid Input! Try Again.\n")   