__author__ = 'matthewburleson'
import random

guess_counter = 0
low_limit = 0
high_limit = 10
attempts = 0
allowed_attempts = 5
player_win = False


def ask_for_a_guess(low_int, high_int):
    return input("Can you guess my number? It's between {} and {}. ".format(low_int, high_int ))


def guess_legality_checker(guess, low_int, high_int):
    try:
        guess = int(guess)
        if guess > high_int:
            print("I'm sorry, that guess is too damn high.")
            return False
        if guess < low_int:
            print("I'm sorru, that guess is too freaking low.")
            return False
        print("Hey, that's a good guess...")
        return True
    except:
        print("No, that's either not a number, or it's a stupid fraction.")
        return False


def compare_numbers(target_int, guessed_int):
    if guessed_int < target_int:
        print("But my number is higher!")
        return False
    elif guessed_int > target_int:
        print("But my number is lower!")
        return False
    else:
        print("Holy crap, you got it!!")
        return True


random_int = random.randint(low_limit, high_limit)

guess = ask_for_a_guess(low_limit, high_limit)

while attempts < allowed_attempts:
    if guess_legality_checker(guess, 0, 10):
        attempts += 1
        if compare_numbers(random_int, int(guess)):
            print("Only took you {} tries!".format(attempts))
            player_win = True
            break
        else:
            guess = input("Try again:")
            continue
    else:
        guess = input("Try again:")
        continue

if False == player_win:
    print("Sorry, you've used all {} turns.  My number was {}".format(allowed_attempts, random_int))