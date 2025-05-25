from art import logo
import random


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """
    Checks if 11 (Ace) and 10 in deck
    and switches the value of the Ace card from 11 to 1 if
    user goes above a score of 21
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(m_score, c_score):
    if m_score == c_score:
        return "It's a draw 🙃"
    elif c_score == 0:
        return "You lose, opponent has a Blackjack 🤑"
    elif m_score == 0:
        return "You win with a Blackjack 🤩"
    elif m_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😃"
    elif m_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😥"


def play_game():
    print(logo)
    is_game_over = False
    my_cards = []
    computer_cards = []
    computer_score = -1
    my_score = -1

    for card in range(2):
        my_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        my_score = calculate_score(my_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {my_cards}, current score: {my_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if my_score == 0 or computer_score == 0 or my_score > 21:
            is_game_over = True
        else:
            continue_or_pass = input("Type 'y' to get another card, type 'n' to pass: ")
            if continue_or_pass.lower() == "y":
                my_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {my_cards}, final score: {my_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(my_score, computer_score))


start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while start.lower() == "y":
    print("\n" * 20)
    play_game()
