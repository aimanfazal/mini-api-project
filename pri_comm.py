import random
import string

def random_gen(len):
     char = string.ascii_letters + string.digits
     return ''.join(random.choices(char, k=len))

while True:
    prompt = input("Enter - C for coding, D for decoding or Q to quit the program:\t").upper()
    if prompt == 'C' or prompt == 'D':
        s = input("Enter the string:\t")
        words = s.split(" ")
        new_s = []
        if prompt == 'C':   #Coding
            for word in words:
                if len(word) >= 3:
                    adder = random_gen(3) + word[1:] + word[0] + random_gen(3)
                    new_s.append(adder)
                else:
                    new_s.append(word[::-1])
            print(" ".join(new_s))
        else:               #Decoding
            for word in words:
                if len(word) < 3:
                    new_s.append(word[::-1])
                else:
                    adder = word[3:-3]
                    adder = adder[-1] + adder[:-1]
                    new_s.append(adder)
            print(" ".join(new_s))
    elif prompt == 'Q':
        print("Thanks for using our program!")
        break
    else:
        print("Invalid input!")