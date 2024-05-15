import random
import time

turns = 0
total = 0
total_comp = 0

print("Welcome to Blackjack!\n")


def ace(card1):
    if card1 == 11:
        change11 = input("Do you want an 11 or a 1? ")
        print("")
        if change11 == '1':
            card1 = 1
            print(card1)
        if change11 == '11':
            card1 = 11
    return card1


def draw_card():
    card = random.randint(1, 13)
    if card > 10:
        card = 10
    return card


def computer_game():
    global total_comp
    card_comp1 = draw_card()
    card_comp2 = draw_card()

    total_comp = card_comp1 + card_comp2
    while total_comp < 16:
        comp_card_twist = random.randint(1, 11)
        total_comp += comp_card_twist
        print("Computer twisted")
        time.sleep(1)
        print("")

    if total_comp == 21:
        print("The computer has Blackjack -", total_comp)
        print("")
    elif total_comp > 21:
        print("Computer went BUST with", total_comp)
    else:
        time.sleep(1)
        print("Computer's score is", total_comp)


def blackjack():
    global total, total_comp
    money = 100  # Starting money
    while money > 0:
        print(f"Current money: {money}")
        bet = int(input("Place your bet: "))
        if bet > money:
            print("You can't bet more than you have. Try again.")
            continue

        card1 = draw_card()
        card2 = draw_card()

        print("You drew", card1, "and", card2)

        card1 = ace(card1)

        total = card1 + card2

        print("Your score is", total)
        x = True
        while x:
            if total > 21:
                print("BUST")
                money -= bet
                print("")
                x = False
            elif total == 21:
                print("You win!")
                money += 2 * bet  # Earn twice the bet for winning
                print("")
                computer_game()
                x = False
            elif total < 21:
                stick_or_twist = input("Would you like to Stick or Twist? s/t: ")
                if stick_or_twist == 's':
                    print("")
                    print("Your overall score is", total)
                    print("")
                    computer_game()
                    x = False
                elif stick_or_twist == 't':
                    card_twist = random.randint(1, 11)
                    print("")
                    print("You drew a", card_twist)
                    print("")
                    total += card_twist
                    print("Your score is", total)
                    print("")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break

    print("Game over. You ran out of money.")


blackjack()
