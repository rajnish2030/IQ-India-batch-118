import random
import time

game = {"rock":3,"paper":2,"scissor":1}                              
item = ["rock","paper","scissor"]

your_score = 0
computer_score = 0

for i in range(1,4):
    user = input("Fill Your rock,paper,scissor :".lower())
    computer = random.choice(item)
    print("computer :",computer)
    if game[user] > game[computer]:
        print("WOOOOOOOW.....YOU ARE WINNER 1ST ROUND..😍😍")
        your_score += 1
    elif game[user] < game[computer]:
        print("😉😉😉......computer winner")
        computer_score += 1
    else:
        print("TIE 🫷🫷")
print("Final score")
print("Your Score : ",your_score)
print("Computer Score :",computer_score)

if your_score > computer_score:
    time.sleep(1)
    print("🤩🤩🤩😍 Congrate.....You Are Winner")
elif your_score < computer_score:
    time.sleep(1)
    print("Computer Winner\n")
    print("Next Time Better Luck")
else:
    time.sleep(1)
    print("OHHHHHHHOO.....TIE😎😎")