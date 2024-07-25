import random

while True:
        choices = ['rock', 'paper', 'scissor']
        computer = random.choice(choices)

        player = None
        while player not in choices:
            player = input("rock, paper, or scissor? ").lower()

        def win(computer, player):
            print("computer", computer)
            print("player", player)
            print('Tie!')

        def lose(computer, player):
            print("computer", computer)
            print("player", player)
            print('You lose!')

        if player == computer:
            print("computer", computer)
            print("player", player)
            print('Tie!')

        elif player == "rock":
            if computer == "paper":
                lose(computer=computer,player=player)

            if computer == "scissor":
                win(computer=computer,player=player)

        elif player == "paper":
            if computer == "scissor":
                lose(computer=computer,player=player)

            if computer == "rock":
                win(computer=computer,player=player)

        elif player == "scissor":
            if computer == "rock":
                lose(computer=computer,player=player)
            
            if computer == "paper":
                win(computer=computer,player=player)

        play_again_choices = ["yes", "no"]

        while True:
            play_again = input('Would you like to play again? (yes/no) ').lower()
            if play_again not in play_again_choices:
                print('Please enter either yes or no!')
            else:
                if play_again == "no":
                    print('\nBye')
                    break
            break

        if play_again == "no":
            break