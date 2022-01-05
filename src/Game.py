import time
from termcolor import colored
import random2
import os


class Number_Guessing_Game:

    def __init__(self):
        self.attempts_list = []

    def show_score(self):
        if len(self.attempts_list) <= 0:
            print(colored("\nThere is Currently no High Score, it is for your Taking!\n", 'yellow'))
        else:
            print(colored(f"\nThe Current High Score is {min(self.attempts_list)}\n.", 'green'))

    def start_game(self, user_name):
        random_number = random2.randint(1, 10)
        print(colored(f"\nHey {user_name}!", 'green'))
        time.sleep(1)
        self.show_score()
        time.sleep(1)
        user_input = "yes"
        attempts = 0
        while user_input:
            try:
                guess = int(input(colored("\nEnter your guess between 1 to 10: ", 'yellow')))
                if 1 > guess > 10:
                    print(colored("\nPlease Enter the Number Between the specifies Range: ", 'red'))
                if guess == random_number:
                    print(colored("\nGreat! You have Guessed the Number Correctly!", 'green'))
                    attempts += 1
                    self.attempts_list.append(attempts)
                    print(colored("\nIt took you {} attempts".format(attempts), 'blue'))
                    play_again = input(colored("\nWould you like to play again? (Yes/No) ", 'yellow'))
                    attempts = 0
                    random_number = int(random2.randint(1, 10))
                    if play_again.lower() == 'n' or play_again.lower() == 'no':
                        print(colored("\nNo Problem! See you later!\n", 'yellow'))
                        break
                elif int(guess) > random_number:
                    print(colored("\nIt's lower", 'yellow'))
                    attempts += 1
                elif int(guess) < random_number:
                    print(colored("\nIt's higher", 'yellow'))
                    attempts += 1
            except ValueError as e:
                print(colored("Oh no!, that is not a valid value. Try again...\n", 'red'))
        else:
            print(colored("\nOkay then, I'll see you later!\n", 'red'))


class Hand_Cricket_Game:

    def __init__(self, u_name):
        self.numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.name_file = []
        self.score_file = []
        self.username = u_name
        self.import_score()

    @staticmethod
    def banner():
        print(colored("""
    '##::::'##::::'###::::'##::: ##:'########::::::'######::'########::'####::'######::'##:::'##:'########:'########:
     ##:::: ##:::'## ##::: ###:: ##: ##.... ##::::'##... ##: ##.... ##:. ##::'##... ##: ##::'##:: ##.....::... ##..::
     ##:::: ##::'##:. ##:: ####: ##: ##:::: ##:::: ##:::..:: ##:::: ##:: ##:: ##:::..:: ##:'##::: ##:::::::::: ##::::
     #########:'##:::. ##: ## ## ##: ##:::: ##:::: ##::::::: ########::: ##:: ##::::::: #####:::: ######:::::: ##::::
     ##.... ##: #########: ##. ####: ##:::: ##:::: ##::::::: ##.. ##:::: ##:: ##::::::: ##. ##::: ##...::::::: ##::::
     ##:::: ##: ##.... ##: ##:. ###: ##:::: ##:::: ##::: ##: ##::. ##::: ##:: ##::: ##: ##:. ##:: ##:::::::::: ##::::
     ##:::: ##: ##:::: ##: ##::. ##: ########:::::. ######:: ##:::. ##:'####:. ######:: ##::. ##: ########:::: ##::::
    ..:::::..::..:::::..::..::::..::........:::::::......:::..:::::..::....:::......:::..::::..::........:::::..:::::

                """, 'green'))

    def information(self):
        print(colored(f"\nWelcome", 'blue') + colored(f"to the game of Cricket, {self.username}. "
                                                      f"The Rules/Procedure are given Below: \n",
                                                      'blue'))
        print(colored("1) You have to Enter a Number between 1-10.\n", 'cyan'))
        print(colored("2) The Computer will Generate a Random Number within the Same Range.\n", 'cyan'))
        print(colored("3) If your Input is Equal to the Random Number Generated, ", 'cyan') +
              colored("YOU ARE OUT!!\n", 'red'))
        print(colored("4) After 3 Wrong inputs, the Game will be Terminated!\n", 'cyan'))
        if not self.score_file:
            print(colored(f"There is no High Score at The Moment. It is for Your Taking\n", 'yellow'))
        else:
            maximum = self.get_max()
            print(colored(f"The current High Score is: {maximum}. You can Break it!!\n", 'yellow'))

    def get_random_number(self):
        return random2.choice(self.numbers)

    def export_score(self, score):
        if os.path.exists("temp/Cricket_Score.txt"):
            with open("temp/Cricket_Score.txt", 'a') as file:
                file.write(f"{self.username}:{score}<sep>")
        else:
            with open("temp/Cricket_Score.txt", 'w') as file:
                file.write(f"{self.username}:{score}<sep>")

    def get_max(self):
        maximum = 0
        for i in self.score_file:
            if maximum < i:
                maximum = i
        return maximum

    def import_score(self):
        if os.path.exists("temp/Cricket_Score.txt"):
            with open("temp/Cricket_Score.txt", 'r') as file:
                score = file.read()
                if score.endswith("\n"):
                    score = score[:-2]
                if score.endswith("<sep>"):
                    score = score[:-5]
                score_list = score.split("<sep>")
                for listed in score_list:
                    name, scores = listed.split(":")
                    self.score_file.append(int(scores))
                    self.name_file.append(name)
        else:
            pass

    def main_game(self):
        score = 0
        c = 0
        while True:
            user_input = input(colored("\nEnter your Choice: ", 'yellow'))
            if user_input == "":
                print(colored("No Input! Enter Something!\n", 'red'))
                continue
            user_input = int(user_input)
            if user_input not in self.numbers:
                print(colored("\nWrong Input!\n", 'red'))
                c = c + 1
                if c == 3:
                    print(colored("You Have Entered Wrong Input Too Many Times! "
                                  "The Game has been Terminated! ", 'red'))
                    if score > int(self.get_max()):
                        print(colored(f"You have Achieved a new Score! Your Score is: {score}", 'green'))
                    else:
                        print(colored(f"Your Score is: {score}", 'cyan'))
                    self.export_score(score)
                    break
            else:
                if user_input == self.get_random_number():
                    print(colored(f"\nYou are Out!! The Computer also Generated {user_input}!!\n", "red"))
                    if score > int(self.get_max()):
                        print(colored(f"You have Achieved a new Score! Your Score is: {score}", 'green'))
                    else:
                        print(colored(f"Your Score is: {score}", 'cyan'))
                    self.export_score(score)
                    break
                else:
                    score = score + user_input
