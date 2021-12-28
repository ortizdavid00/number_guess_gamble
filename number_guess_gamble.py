import random

# Task 1: Number Guess through User Input
def guess_random_num(tries, start, stop):
    x = random.randint(start, stop)
    print("There are", tries, "tries remaining!")
    while tries != 0:
        guess_input = int(input("Enter your guess: "))
        if guess_input < start or guess_input > stop:
            print("Enter a valid number!")
            continue

        if guess_input == x:
            print("You found the number!")
            return
        elif guess_input < x:
            print("Guess higher!")
            tries -= 1
        elif guess_input > x:
            print("Guess lower!")
            tries -= 1
        else:
            print("Enter a valid guess!")
            continue

    if tries == 0:
        print("Better luck next time!")

# guess_random_num(5, 0, 10)

# Task 2: Number Guess through Linear Search
def guess_random_num_linear(tries, start, stop):
    random_num = random.randint(start, stop)
    print("The number for the program to guess is", random_num)
    for x in range(start, stop):
        if x == random_num:
            print("The computer guessed:", x)
            print("The computer guessed the correct number!")
            return True
        elif x < random_num:
            print("The computer guessed:", x)
            print("Number of tries remaining:", tries)
            tries -= 1
            if tries == 0:
                print("The computer failed to guess the correct number...")
                return False
        elif x > random_num:
            print("The computer guessed:", x)
            print("Number of tries remaining:", tries)
            tries -= 1
            if tries == 0:
                print("The computer failed to guess the correct number...")
                return False
    return None

# guess_random_num_linear(5, 0, 10)


# Task 3: Number Guess through Binary Search
def guess_random_num_binary(tries, start, stop):
    random_num = random.randint(start, stop)
    lower_bound = start
    upper_bound = stop
    print("Random number to find:", random_num)

    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound) // 2

        if pivot == random_num:
            print("The computer guessed the correct number!")
            return pivot
        elif pivot > random_num:
            upper_bound = pivot - 1
            print("Guessing lower!")
            print("The computer guessed", pivot)
        elif pivot < random_num:
            lower_bound = pivot + 1
            print("Guessing lower!")
            print("The computer guessed", pivot)

        tries -= 1
        if tries <= 0:
            print("The computer could not guess the correct number...")
            return None
    return None

# guess_random_num_binary(15, 0, 100)

def gambling_game():
    user_money = 10
    while user_money > 0:
        print("")
        user_bet = int(input("Place you bet amount for this game: "))
        if user_bet <= 10 or user_bet >= 1:
            guess_random_num_linear(5, 0, 5)
        elif user_bet > 10:
            print("You cannot bet more than your total amount!")
            continue

        if guess_random_num_linear == True:
                user_money += user_bet
                print("You won the bet! You now have", user_money, "to bet with.")
                print("")
                continue
        elif guess_random_num_linear == False:
            user_money -= user_bet
            print("You lost the bet. You now have", user_money, "to bet with.")
            print("")
            continue

        if user_money <= 0:
            print("You lose! You have no more money to bet with...")
            return

gambling_game()