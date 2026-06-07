import random

user = input("What is your name? ")
us_score = 0
cp_score = 0
cp_list = ["S", "W", "G"]

win_map = {"S": "W", "W": "G", "G": "S"}
print(f"Hello {user}! Enter S for Snake, W for Water, G for Gun and Q for Quit!")

while us_score < 3 and cp_score < 3:
    us_input = input("\nUser Input: ").upper()
    if us_input == "Q":
        break
    if us_input not in cp_list:
        print("Invalid Input")
        continue
    cp_input = random.choice(cp_list)
    print("CPU Input:", cp_input)
    if us_input == cp_input:
        print(f"Draw! {us_input} at both hands")
    elif win_map[us_input] == cp_input:
        print(f"{user} wins!")
        us_score += 1
    else:
        print("CPU wins!")
        cp_score += 1
    print(f"\n\tScoreboard: {user}: {us_score}, CPU: {cp_score}")

print("\n")
if us_input == "Q":
    print(f"{user} has quit the game")
elif us_score > cp_score:
    print(f"{user} has won the game")
else:
    print(f"{user} has lost again!")