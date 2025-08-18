import sys

print("Welcome to my computer quiz!")

playing = input("Do you want to play? ").strip().lower()
if playing != "yes":
    sys.exit() # Allows to quit

print("Okay! Let's play :)")

qa = [
    ("What does CPU stand for? ", "central processing unit"),
    ("What does GPU stand for? ", "graphics processing unit"),
    ("What does RAM stand for? ", "random access memory"),
    ("What does PSU stand for? ", {"power supply", "power supply unit"}),  
]
# qa is a list of tuples.

score = 0

for question, valid_ans  in qa:
    ans = input(question).strip().lower()
    if ans == valid_ans :
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

total = len(qa)
print(f"You got {score} out of {total} questions correct!")
print(f"Your score: {score/total:.0%}")