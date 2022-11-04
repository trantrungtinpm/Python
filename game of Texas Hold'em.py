import random
import itertools


def get_player():
    while True:
        try:
            user_input = int(input("How many player there?").strip())
        except ValueError:
            print("You must enter integer")
        else:
            if user_input in range(2, 11):
                return user_input
            elif user_input < 2:
                print("You must have at least 2 players")
            else:
                print("You can have a maximum of 10 players")


def shuffle_deck(cards):
    deck = list(cards)
    random.shuffle(deck)
    return iter(deck)


def deal(card, number_of_player):
    deck = shuffle_deck(card)
    deal_to_player(deck, number_of_player)
    deal_to_table(deck)


def deal_to_player(deck, number_of_player):
    first_card = [next(deck) for _ in range(number_of_player)]
    second_card = [next(deck) for _ in range(number_of_player)]
    hands = zip(first_card, second_card)
    print()
    for i, (first_card, second_card) in enumerate(hands, start=1):
        print(f"Player {i} was dealt: {first_card}, {second_card}")


def deal_to_table(deck):
    next(deck)

    flop = ", ".join(str(next(deck)) for _ in range(3))
    print(f"The flop : {flop}")

    next(deck)
    print(f"The turn: {next(deck)}")

    next(deck)
    print(f"The river: {next(deck)}")


ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "ace")
suits = ("clubs", "diamonds", "hearts", "spades")
cards = list(itertools.product(ranks, suits))
deal(cards, get_player())
