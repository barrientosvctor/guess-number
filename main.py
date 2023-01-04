from random import randint

def main():
    try:
        print("Welcome to Guess Number game!".center(50, "-"))
        print("1. Guess number with attempts count")
        print("2. Guess number with limited attempts")
        choose_game = int(input("Choose the game mode what you want to play: "))
        print("".center(50, "="))

        # Games selections
        while choose_game:
            # 1. Guess number with attempts count
            if choose_game == 1:
                # User attempts
                attempts_count: int = 0
                # Number range
                choose_number_range = input("Type the range of number to play (remember split every number with -. Example: 3-15): ")
                rand_number = randint(int(choose_number_range.split("-")[0]), int(choose_number_range.split("-")[1]))
                first_game = int(input(f"Attempts count: {attempts_count}.\nType a random number between {choose_number_range.split('-')[0]} - {choose_number_range.split('-')[1]}: "))

                while first_game != rand_number:
                    # Execute this if user input is greater or less than number range
                    if first_game > int(choose_number_range.split("-")[1]) or first_game < int(choose_number_range.split("-")[0]):
                        first_game = int(input(f"\n-- You've exceeded the limit of number range. --\n\nAttempts count: {attempts_count}.\nType a random number between {choose_number_range.split('-')[0]} - {choose_number_range.split('-')[1]}: "))
                    else:
                        # Else adds 1 attempt to attempts count
                        attempts_count += 1
                        first_game = int(input(f"\nAttempts count: {attempts_count}.\nType a random number between {choose_number_range.split('-')[0]} - {choose_number_range.split('-')[1]}: "))
                else:
                    print("You won!".center(50, "="))
                    print(f"You've guessed the number!\n\nAttempts count: {attempts_count + 1}")
                    print("Thanks for playing! :)")
                    break
            # 2. Guess number with limited attempts
            elif choose_game == 2:
                attempts_limit: int = int(input("Type the limit of attempts to play: "))
                if attempts_limit == 0:
                    print("Can't set attempts limit to 0.")
                    break

                choose_number_range_second_game = input("Type the range of number to play (remember split every number with -. Example: 3-15): ")
                random_number = randint(int(choose_number_range_second_game.split("-")[0]), int(choose_number_range_second_game.split("-")[1]))

                while attempts_limit != 0:
                    second_game = int(input(f"\nAttempts remaining: {attempts_limit}.\nType a random number between {choose_number_range_second_game.split('-')[0]} - {choose_number_range_second_game.split('-')[1]}: "))

                    # Execute this if user input is greater or less than number range
                    if second_game > int(choose_number_range_second_game.split("-")[1]) or second_game < int(choose_number_range_second_game.split("-")[0]):
                        # second_game = int(input(f"You've exceeded the limit of number range.\n\nAttempts remaining: {attempts_limit}.\nType a random number between {choose_number_range_second_game.split('-')[0]} - {choose_number_range_second_game.split('-')[1]}: "))
                        continue
                    # Else adds 1 attempt to attempts count
                    elif second_game != random_number:
                        attempts_limit -= 1
                        continue
                    # User input equal random number
                    else:
                        print("You won!".center(50, "="))
                        print(f"You've guessed the number!\n\nAttempts count: {attempts_limit}")
                        print("Thanks for playing! :)")
                        break
                else:
                    print("You lost!")
                    break
            # User input does not equal 1 or 2
            if choose_game > 2:
                print(f"The game mode '{choose_game}' does not exists.")
            break
    except ValueError as e:
        print(f"Type a number.")
    except KeyboardInterrupt as e:
        print("\nYou've leave the game. Thanks for playing! :)")
    except Exception as e:
        print(f"I've found an unexpected error: {e}")

# Run file as script
if __name__ == "__main__":
    main()
