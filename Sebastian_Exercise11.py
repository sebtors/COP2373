import random

# Deck Class from Section 11.5
class Deck:
    def __init__(self, size):
        self.card_list = [i for i in range(size)]
        self.cards_in_play_list = []
        self.discards_list = []
        random.shuffle(self.card_list)

    def deal(self):
        if len(self.card_list) < 1:
            random.shuffle(self.discards_list)
            self.card_list = self.discards_list
            self.discards_list = []
            print("Reshuffling...!!!")

        new_card = self.card_list.pop()
        self.cards_in_play_list.append(new_card)
        return new_card

    def new_hand(self):
        self.discards_list += self.cards_in_play_list
        self.cards_in_play_list.clear()


# Function to convert number to card name
def card_to_string(card_num):
    ranks = ['2', '3', '4', '5', '6', '7', '8',
             '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    rank = ranks[card_num % 13]
    suit = suits[card_num // 13]

    return f"{rank} of {suit}"


# Function to display a hand
def show_hand(hand):
    print("\nYour hand:")
    for i in range(len(hand)):
        print(f"{i + 1}: {card_to_string(hand[i])}")


# Function to replace selected cards
def draw_cards(deck, hand):
    replace = input("\nEnter positions to replace (example: 1,3,5) or press Enter to keep all: ")

    if replace.strip() == "":
        return hand

    positions = replace.split(",")

    for pos in positions:
        index = int(pos.strip()) - 1
        if 0 <= index < len(hand):
            hand[index] = deck.deal()

    return hand


# MAIN PROGRAM
def main():
    deck = Deck(52)

    # Deal initial hand
    hand = []
    for _ in range(5):
        hand.append(deck.deal())

    show_hand(hand)

    # Draw phase
    hand = draw_cards(deck, hand)

    # Show final hand
    print("\nFinal hand:")
    show_hand(hand)

    # End hand
    deck.new_hand()


if __name__ == "__main__":
    main()