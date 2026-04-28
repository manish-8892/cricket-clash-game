 import random

def toss():
    choice = input("Heads or Tails: ").lower()
    result = random.choice(["heads", "tails"])
    print("Toss:", result)
    return input("Bat or Bowl: ").lower() if choice == result else random.choice(["bat", "bowl"])

def get_num():
    while True:
        try:
            n = int(input("Enter (1-6): "))
            if 1 <= n <= 6:
                return n
        except:
            pass
        print("Invalid input!")

def play_innings(overs, role):
    score = wickets = 0
    for ball in range(overs * 6):
        print("\nBall", ball + 1)
        user = get_num()
        comp = random.randint(1, 6)

        if role == "bat":
            print("Computer:", comp)
            if user == comp:
                wickets += 1
                print("OUT!", "Wickets:", wickets)
            else:
                score += user
        else:
            print("Computer:", comp)
            if user == comp:
                wickets += 1
                print("Computer OUT!", "Wickets:", wickets)
            else:
                score += comp

        print("Score:", score)
        if wickets == 3:
            break
    return score

def play_game():
    overs = int(input("Overs: "))
    decision = toss()

    if decision == "bat":
        user = play_innings(overs, "bat")
        print("Target:", user + 1)
        comp = play_innings(overs, "bowl")
    else:
        comp = play_innings(overs, "bowl")
        print("Target:", comp + 1)
        user = play_innings(overs, "bat")

    print("\nFinal Score -> You:", user, "| Computer:", comp)
    print("You Win!" if user > comp else "Computer Wins!" if comp > user else "Draw")

def main():
    while True:
        print("\n1. Play\n2. Exit")
        ch = input("Choice: ")
        if ch == "1":
            play_game()
        elif ch == "2":
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
