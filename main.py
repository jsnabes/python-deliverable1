user_name = input("Welcome to GC mini golf! What is your name? ")
holes = int(input(f"Hi, {user_name}! Would you like to play 3 or 6 holes today? "))
if holes == 3:
    hole_1 = int(input("How many putts for hole 1? (par is 3) "))
    hole_2 = int(input("How many putts for hole 2? (par is 3) "))
    hole_3 = int(input("How many putts for hole 3? (par is 3) "))
    total_score = int(hole_1 + hole_2 + hole_3 - 9)
    if total_score == 0:
            print(f"Good game, {user_name}. Your total score was: {total_score}")
    elif total_score < 0:
            print(f"Great job, {user_name}! Your total score was: {total_score}")
    elif total_score > 0:
            print(f"Nice try, {user_name}...Your total par was: +{total_score}")

else:
    hole_1 = int(input("How many putts for hole 1? (par is 3) "))
    hole_2 = int(input("How many putts for hole 2? (par is 3) "))
    hole_3 = int(input("How many putts for hole 3? (par is 3) "))
    hole_4 = int(input("How many putts for hole 4? (par is 3) "))
    hole_5 = int(input("How many putts for hole 5? (par is 3) "))
    hole_6 = int(input("How many putts for hole 6? (par is 3) "))
    total_score = int(hole_1 + hole_2 + hole_3 + hole_4 + hole_5 + hole_6 - 18)
    if total_score == 0:
        print(f"Good game, {user_name}. Your total score was: {total_score}")
    elif total_score < 0:
        print(f"Great job, {user_name}! Your total score was: {total_score}")
    elif total_score > 0:
        print(f"Nice try, {user_name}...Your total par was: +{total_score}")












