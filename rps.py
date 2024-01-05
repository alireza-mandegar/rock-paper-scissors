import random
from time import sleep

info = "!"
success = "+"
fail = "-"
done = "*"

def tree(p1, ch1, ch2):
    if ch1 == "paper" and ch2 == "rock":
        return p1.name
    elif ch1 == "rock" and ch2 == "scissors":
        return p1.name
    elif ch1 == "scissors" and ch2 == "paper":
        return p1.name
    else:
        return "draw"

# for Draw tree
# attributes
treeplayer1=[]
treeplayer2=[]
# function
def generate_tree(player1, player2, tree1, tree2):
    lenght = len(tree1)
    score = 0
    for i in range(lenght):
        print((lenght - i)*"\t", end="")
        print(f"{tree1[i]} : {tree2[i]}")
        sleep(0.2)
        if tree(player1, tree1[i], tree2[i]) == player1.name:
            score = score + 1
            print((lenght - i + 1)*"\t", end="")
            print(score)
        elif tree(player2, tree2[i], tree1[i]) == player2.name:
            score = score - 1
            print((lenght - i + 1)*"\t", end="")
            print(score)
        else:
            print((lenght - i + 1)*"\t", end="")
            print(score)
        sleep(0.2)

class Player:
    # attributes
    name = ""
    decision = ("rock", "paper", "scissors")
    score = 0

    #functions
    def __init__(self):
        pass

    def choice(self):
        return random.choice(list(self.decision))
    

def play(score, player1, player2, round):
    if player1.score >= score or player2.score >= score:
        return
    print(f"[{info}] round{round}")
    sleep(1)
    choice1 = player1.choice()
    treeplayer1.append(choice1)
    # print(treeplayer1)
    choice2 = player2.choice()
    treeplayer2.append(choice2)
    # print(treeplayer2)
    print(f"[{success}] Player1 choice is {choice1} and Player2 choice is {choice2} so ...")
    sleep(0.5)
    if tree(player1, choice1, choice2) == player1.name:
        player1.score += 1
        print(f"[{done}] player1 win! The score is {player1.score}:{player2.score}")
        sleep(0.1)
    elif tree(player2, choice2, choice1) == player2.name:
        player2.score += 1
        print(f"[{done}] player2 win! The score is {player1.score}:{player2.score}")
        sleep(0.1)
    else:
        print(f"[{fail}] draw! The score is {player1.score}:{player2.score}")
        sleep(0.1)
    play(score, player1, player2, round+1)

def main():
    player1 = Player()
    player1.name = "player1"
    player2 = Player()
    player2.name = "player2"

    score_limit = int(input(f"[{info}] Enter the Score Limit >> "))
    sleep(0.5)
    print(f"[{info}] Game Starting...")
    play(score_limit, player1, player2, 1)
    print(f"[{done}] Game has been done!")
    sleep(1)
    print(f"[{info}] {player1.name} do is : {treeplayer1} \n[{info}] {player2.name} do is : {treeplayer2}")
    sleep(0.5)
    print(f"[{info}] tree is generating...")
    sleep(2)
    print(f"[{success}] tree has been generated!")
    sleep(1.5)
    generate_tree(player1, player2, treeplayer1, treeplayer2)

if __name__ == "__main__":
    main()
