import random
from art import logo, vs
from game_data import data
from replit import clear


def pullAccount():
    return random.choice(data)


def formatData(account):
    name = account["name"]
    description = account["description"]
    followerCount = account["follower_count"]
    country = account["country"]

    return (f"The description of {name} {description} with a follower count of {followerCount}, from {country}")


def checkAnswer(guess, aFollowers, bFollowers:
    if


aFollowers > bFollowers:
return guess == "a"
else:
return guess == "b"


def game():
    print
    logo
    score = 0
    continueGame = True
    accountA = pullAccount()
    accountB = pullAccount()

    while continueGame:
        accountA = accountB
        accountB = pullAccount()

        while accountA == accountB:
            accountB = pullAccount()

        print(f"Compare A: {formatData(accountA)}.")
        print(vs)
        print(f"Compare B: {formatData(accountB)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        aFollowerCount = accountA["follower_count"]
        bFollowerCount = accountB["follower_count"]
        accuracy = checkAnswer(guess, aFollowerCount, bFollowerCount)

        clear()
        print(logo)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()