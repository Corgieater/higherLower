import random
import data
import logo


def dereference(info):
    return f"{info['name']} from {info['country']} {info['description']}"


def compare(a, b):
    higher = a["name"]
    if a["follower_count"] < b["follower_count"]:
        higher = b["name"]
    return higher


print(logo.logo)


def game():
    again = True
    while again is True:
        is_game_over = False
        first = random.choice(data.data)
        score = 0
        while is_game_over is not True:
            second = random.choice(data.data)
            while second == first:
                second = random.choice(data.data)
            print(f"A : {dereference(first)}")
            print(logo.vs)
            print(f"B : {dereference(second)}\n")
            print(f"Your current score is {score}")
            player = input("which one has higher follower? A/B\n").upper()

            while player != "A" and player != "B":
                print("Invalid input")
                player = input("Which mountain is higher? A/B\n").upper()

            if player == "A":
                player_ans = first['name']
                print(f"You chose A: {player_ans}")
            else:
                player_ans = second['name']
                print(f"You chose B: {player_ans}")

            true_ans = compare(first, second)
            if player_ans == true_ans:
                print(f"Your are right! {true_ans} is higher\n")
                score += 1
                first = second
            elif player_ans != true_ans:
                print(f"You lose :( {true_ans} is higher\n")
                print(f"Your final score: {score}\n")
                is_game_over = True
        new_game = input("New game? Y/N\n").upper()
        if new_game != "Y":
            again = False


game()
print("OK, bye")
