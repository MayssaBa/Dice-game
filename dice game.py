import random

def roll():
    roll=random.randint(1,6)
    return roll

while True: 
    players=input("Enter the number of players (2-4): ")
    if players.isdigit():
        players=int(players)
        if 2<=players<=4:
            break
        else:
            print("number between 2-4 ")
    else:
        print("invalid!must be number")

max_score=50
player_scores=[0 for i in range(players)]
print("the players scores initialised to: ",player_scores)

while max(player_scores) < max_score:
    for i in range (players):
        print("\nPlayer num ",i+1,".Your turn has just started!\n")
        print("Your total score is: ",player_scores[i],"\n")
        current_score=0

        while True:
            should_roll=input("Would you like to roll ?press y: ")
            if should_roll.lower()!="y":
                break

            value=roll()
            if value==1:
                print ("\n!!You rolled a 1 ! Turn done")
                current_score=0
                break
            else:
                print ("You rolled a ",value)
                current_score+=value
                print("You current score is: ",current_score)
        player_scores[i]+=current_score
        print("\nYour total score is: ",player_scores[i],"\n")

max_score=max(player_scores)
winning_index=player_scores.index(max_score)+1
print("THE WINNER IS***PLAYER NUM ",winning_index,"*** with score= ",max_score)


                



