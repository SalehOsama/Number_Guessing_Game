                                                        # Guess the number
winning_no = 23
i = 1

print("\n\t\t\t*WELCOME TO THE NUMBER GUESSING GAME*")
print("\t*YOU HAVE TO GUESS THE NUMBER BETWEEN 1 to 50 IN 5 GUESSES*")


while i<=5 :
    num = int(input("\nGuessed the number : "))

    if num > winning_no:
        if num in range (winning_no, winning_no+4 ):
            print("\nYou are too close1, Enter a little smaller no.")
        else:
            print("\nToo high!, Enter a smaller no.")

    elif num < winning_no:
        if num in range (winning_no-3 , winning_no ):
            print("\nYou are too close1, Enter a little Greater no.")
        else:
            print("\nToo small!, Enter a Greater no.")

    else:
        print("\n\t*_*_*_*YOU WON_*_*_*_*")
        print(f"You have guessed the number in {i} guesses")
        break

    print(f"{9-i} guess are left.....")
    i += 1

else:
    print("\n\t-----!GAME OVER!-------")






