                                                        # Guess the number


import random
winning_no = random.randint(1,50)                    # randint(strt,end) --> returns a random integer number within specified range.
i = 1

print("\n\t\t\t*WELCOME TO THE NUMBER GUESSING GAME*")
print("\t*YOU HAVE TO GUESS THE NUMBER BETWEEN 1 to 50 IN 5 GUESSES*")


while i<=5 :
    num = int(input("\nGuessed the number : "))

    if num > winning_no:
        if num in range (winning_no+1, winning_no+4 ):
            print("\nYou are too close!, Enter a little smaller no.")
        else:
            print("\nToo Large!, Enter a smaller no.")
            # print(f"\t\t ({5-i} takes left)")

    elif num < winning_no:
        if num in range (winning_no-3 , winning_no ):
            print("\nYou are too close!, Enter a little Larger no.")
        else:
            print("\nToo small!, Enter a Larger no.")
            # #print(f"\t\t ({5-i} takes left)")

    else:
        print("\n\t*_*_*_*YOU WON_*_*_*_*")
        print(f"You have guessed the number in {i} guesses")
        break

    print(f"{5-i} guess are left.....")
    i += 1

else:
    print("\n\t-----!GAME OVER!-------")






