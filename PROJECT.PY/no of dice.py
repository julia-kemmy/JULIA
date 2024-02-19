#allow the user to rolling the dice
#this allows general random numbers
#defining roll function by using def
#lastly thats how we generate a random roll
# import random
# def roll():
#     min_value = 1
#     max_value = 6
#     roll = random.randint(min_value,max_value)
#     return roll
# value = roll()
# print(roll)
#reason of while loop is continuing to asking the user to input a number until is valid
while True:
    players = input("entre the number of players(2-4):")
    if players.isdigit():
        players = int(players)
    if 2<=players <= 4:
        break
    else:
        print("must be between 2-4 players.")
else:
    print("invalid try again.")
print(players)

#asking players to roll the dice
max_score = 50
player_scores = [2(players)]
print(player_scores)


# while max(player_scores) < max_score:



