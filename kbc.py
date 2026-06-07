print("Welcome to Kaun Banega Crorepati (KBC) powered by VS Code 😁")
user = input("Aapka naam? ").title()

print(f"1️⃣- Ummeed karta hu ki khel ke niyam aapko malum honge! {user}\n2️⃣- Enter 'quit' in answer to leave the game with the money.\n3️⃣- Any input other than the four options, i.e, - a, b, c, and d will result in an incorrect answer.\nSo, let the game begin!\n")
prize = safe = 0

while True:

    print('Q1. Which of these animals is known as the "ship of the desert"?\nA) Elephant B) Camel C) Horse D) Rhino"')
    answer = input("Answer: ").lower()
    if answer == 'quit':
        break
    elif answer == 'b':
        prize = 1000
        safe = prize
        print(f"Correct! You have won ₹ {prize} 💰")
    else:
        print("Sorry, correct option: b")
        break
    
    print('Q2. In which sport is the term "googly" commonly used?\nA) Football B) Cricket C) Hockey D) Tennis')
    answer = input("Answer: ").lower()
    if answer == 'quit':
        break
    elif answer == 'b':
        prize = 2000
        safe = prize
        print(f"Correct! You have won ₹ {prize} 💰")
    else:
        print("Sorry, correct option: b")
        break

    print('Q3. Which festival is known as the "Festival of Lights" in India?\nA) Holi B) Diwali C) Eid D) Christmas')
    answer = input("Answer: ").lower()
    if answer == 'quit':
        break
    elif answer == 'b':
        prize = 3000
        safe = prize
        print(f"Correct! You have won ₹ {prize} 💰")
    else:
        print("Sorry, correct option: b")
        break
    
    print('Q4. Which of these is the capital city of India?\nA) Mumbai B) Kolkata C) New Delhi D) Chennai')
    answer = input("Answer: ").lower()
    if answer == 'quit':
        break
    elif answer == 'c':
        prize = 5000
        safe = prize
        print(f"Correct! You have won ₹ {prize} 💰")
    else:
        print("Sorry, correct option: c")
        break

    print("🔥- Pahla Padav: ₹ 10,000!")
    print('Q5. Which planet is known as the Red Planet due to its reddish appearance?\nA) Jupiter B) Mars C) Venus D) Mercury')
    answer = input("Answer: ").lower()
    if answer == 'quit':
        break
    elif answer == 'b':
        prize = 10000
        safe = prize
        print(f"Correct! You have won ₹ {prize} 💰")
    else:
        print("Sorry, correct option: b")
        break
    
    print('Q6. Who wrote the Indian national anthem, "Jana Gana Mana"?\nA) Rabindranath Tagore B) Mahatma Gandhi C) Subhas Chandra Bose D) Bankim Chandra Chatterjee')
    answer = input("Answer: ").lower()
    if answer == 'quit':
        break
    elif answer == 'a':
        prize = 20000
        print(f"Correct! You have won ₹ {prize} 💰")
    else:
        print("Sorry, correct option: a")
        break
    
    print('Q7. Which river is considered the holiest in Hinduism?\nA) Yamuna B) Godavari C) Ganga D) Brahmaputra')
    answer = input("Answer: ").lower()
    if answer == 'quit':
        break
    elif answer == 'c':
        prize = 40000
        print(f"Correct! You have won ₹ {prize} 💰")
    else:
        print("Sorry, correct option: c")
        break

    print('Q8. In which year did India win its first Cricket World Cup?\nA) 1975 B) 1983 C) 1992 D) 2007')
    answer = input("Answer: ").lower()
    if answer == 'quit':
        break
    elif answer == 'b':
        prize = 80000
        print(f"Correct! You have won ₹ {prize} 💰")
    else:
        print("Sorry, correct option: b")
        break
    
    print('Q9. Which gas, discovered on the sun before Earth, is the second most abundant element in the universe?\nA) Oxygen B) Nitrogen C) Helium D) Hydrogen')
    answer = input("Answer: ").lower()
    if answer == 'quit':
        break
    elif answer == 'c':
        prize = 160000
        print(f"Correct! You have won ₹ {prize} 💰")
    else:
        print("Sorry, correct option: c")
        break
   
    print("🔥- Dusra Padav: ₹ 3,20,000")
    print('Q10. Who was the first woman Prime Minister of India?\nA) Sonia Gandhi B) Indira Gandhi C) Pratibha Patil D) Sushma Swaraj')
    answer = input("Answer: ").lower()
    if answer == 'quit':
        break
    elif answer == 'b':
        prize = 320000
        safe = prize
        print(f"Correct! You have won ₹ {prize} 💰")
    else:
        print("Sorry, correct option: b")
        break
   
    print('Q11. Which Indian scientist is known as the "Missile Man of India" for his contributions to missile and space technology?\nA) Homi J. Bhabha B) C.V. Raman C) A.P.J. Abdul Kalam D) Vikram Sarabhai')
    answer = input("Answer: ").lower()
    if answer == 'quit':
        break
    elif answer == 'c':
        prize = 640000
        print(f"Correct! You have won ₹ {prize} 💰")
    else:
        print("Sorry, correct option: c")
        break
    
    print('Q12. In which Indian state is the ancient city of Hampi, a UNESCO World Heritage Site, located?\nA) Tamil Nadu B) Karnataka C) Andhra Pradesh D) Maharashtra')
    answer = input("Answer: ").lower()
    if answer == 'quit':
        break
    elif answer == 'b':
        prize = 1250000
        print(f"Correct! You have won ₹ {prize} 💰")
    else:
        print("Sorry, correct option: b")
        break

    print('Q13. Which Indian freedom fighter is associated with the slogan "Inquilab Zindabad"?\nA) Bhagat Singh B) Mangal Pandey C) Bal Gangadhar Tilak D) Lala Lajpat Rai')
    answer = input("Answer: ").lower()
    if answer == 'quit':
        break
    elif answer == 'a':
        prize = 2500000
        print(f"Correct! You have won ₹ {prize} 💰")
    else:
        print("Sorry, correct option: a")
        break
    
    print('Q14. Which of these Indian classical dance forms originated in Andhra Pradesh?\nA) Bharatanatyam B) Kathak C) Kuchipudi D) Odissi')
    answer = input("Answer: ").lower()
    if answer == 'quit':
        break
    elif answer == 'c':
        prize = 5000000
        print(f"Correct! You have won ₹ {prize} 💰")
    else:
        print("Sorry, correct option: c")
        break
    
    print("🔥🔥🔥- Aakhri Padav: ₹1,00,00,000 🤑")
    print('Q15. In 2023, which Indian space mission achieved the first-ever soft landing near the lunar south pole?\nA) Mangalyaan B) Chandrayaan-3 C) Aditya-L1 D) Gaganyaan')
    answer = input("Answer: ").lower()
    if answer == 'quit':
        break
    elif answer == 'c':
        prize = 10000000
        answer = 'jackpot'
        break
    else:
        print("Sorry, correct option: c")
        break

if answer == 'quit':
    print(f"\nDear {user}, Congratulations! You are leaving this KBC program with Rs {prize}. 🔥")
elif answer == 'jackpot':
    print(f"\nCongratulations {user}! You are the jackpot winner - ₹1,00,00,000.")
else:
    print(f"\nUnfortunately, you won only Rs {safe}.")