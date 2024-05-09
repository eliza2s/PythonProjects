import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)
    return roll


while True:
   players = input("how many players would like to play this game (2 to 5) ? ")
   if players.isdigit():
        players = int(players)
        if 2<=players<=4:
            break
        else:
            print("select a number between 2 to 5 only")
   else:
        print("type a number for gods sake")

max_score = 50
all_scores=[0 for _ in range(players)]
while max(all_scores) < max_score:
    for i in range(players):
        print("player ",i+1, " turn")
        current_score=0
        while True:
            ask = input("\n would you like to roll the dice ? (y/n)\n")
            if ask.lower() != "y":
                break
            value = roll()
            if value ==1:
                    print("you are out")
                    current_score=0
                    break
            else:
                current_score += value
                print("you rolled a", value)
                print("your current score is", current_score)
        all_scores[i]+=current_score
        print("your total score is", all_scores[i])

highest = max(all_scores)
winning_player = all_scores.index(highest)
print("player", winning_player+1, "is the winner with a score of ", highest)





