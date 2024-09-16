import random

CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = ["♥", "♦", "♠", "♦︎"]

deck_of_cards = [f"{card}{suit}" for card in CARDS for suit in SUITS]

# Implement a solution for shuffling a deck of cards without using random.shuffle()
# Using randint() is ok
def shuffle_deck(deck_of_cards):
    card_list = []

    for i in range(52):
        card_index = random.randint(0, len(deck_of_cards)-1)
        deck_of_cards.pop(card_index)
        card_list.append(deck_of_cards[card_index])

    print(card_list)

shuffle_deck(deck_of_cards)