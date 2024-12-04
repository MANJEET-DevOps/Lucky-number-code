lucky_no=42
i=1
while i<11:
    guess=int(input(f"Enter The Numbers{i}:"))
    if guess==lucky_no:
        print("Congratulation! You're Win")
        break
    else:
        print(f"Wrong Value Entered. Your Chances is{10-i} Left")
        i=i+1
else:
    print("You lose the game")