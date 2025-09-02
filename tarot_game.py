deck = list(range(1, 24))
player_hand = []
dealer_hand = []
while True:
    print("the current deck is ", deck)
    while True:
        fcheck = []
        guess = int(input("card: "))

        M = guess
        if M not in deck:
            continue
        for N in range(1, M + 1):
            if M % N == 0:  # remainder is zero
                if N in deck:
                    if N not in player_hand:
                        if N not in dealer_hand:
                            if N != M:
                                fcheck.append(N)
        if fcheck == []:
            pass
        else:
            deck.remove(guess)
            player_hand.append(guess)
            print("your current hand is ", player_hand)
            break
    for N in range(1, M + 1):
        if M % N == 0:  # remainder is zero
            if N in deck:
                if N not in player_hand:
                    if N not in dealer_hand:
                        dealer_hand.append(N)
                        deck.remove(N)
    print("the dealers hand is ", dealer_hand)
    if deck == ():
        break

    EM = 0
    for i in deck:
        for N in deck:
            if i != N:
                if i % N == 0:
                    EM = EM + 1
    if EM > 0:
        pass
    else:
        dealer_hand.extend(deck)
        break


print("the dealers hand is ", dealer_hand)
playersum = sum(player_hand)
dealersum = sum(dealer_hand)
print("your score is ", playersum)
print("dealer score is ", dealersum)
if dealersum >= playersum:
    print("dealer wins")
else:
    if 6 in dealer_hand:
        print("you win and will soon meat the love of your life")
    elif 10 in dealer_hand:
        print("you win and you have gained untold fortune")
    elif 2 in dealer_hand:
        print("you win and the curse is broken")
    else:
        print("you win")
