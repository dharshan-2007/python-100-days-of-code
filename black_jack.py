import random


def pick_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    pck_crd = random.choice(cards)
    return pck_crd


def calculate(lst):
    total = sum(lst)
    if 11 in lst and total > 21:
        lst[lst.index(11)] = 1
        total = sum(lst)
    return total


def display(player, dck):
    print(f"{player}'s hand | score {calculate(dck)}")


def play_blackjack():
    user_deck = [pick_card(), pick_card()]
    sys_deck = [pick_card(), pick_card()]
    gameover = False

    while not gameover:
        display("your", user_deck)
        print(f"Dealers first card {sys_deck[0]}")

        if calculate(user_deck) == 21:
            print("black jack!")
            gameover = True
        elif calculate(user_deck) > 21:
            print("You are busted")
            gameover = True

        if not gameover:
            n = input("Do you want to Hit or Stand (h or s): ").lower()
            if n == "h":
                user_deck.append(pick_card())
            elif n == "s":
                gameover = True
            else:
                print("~~Invalid Choice~~")

    while calculate(sys_deck) < 17:
        sys_deck.append(pick_card())

    display("your", user_deck)
    display("dealer", sys_deck)

    your_score = calculate(user_deck)
    dealer_score = calculate(sys_deck)

    if your_score > 21:
        print("You are busted. Dealer wins!")
    elif dealer_score > 21:
        print("Dealer busted. You win!")
    elif dealer_score == your_score:
        print("Draw!")
    elif your_score > dealer_score:
        print("you won!!!")
    else:
        print("Dealer won!")


play_blackjack()
