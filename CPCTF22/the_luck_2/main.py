import random, os

while True:
    result = random.getrandbits(32)
    predict = input("Please predict the result: ")
    if not predict.isnumeric():
        print("Please input a number")
        continue
    if (int(predict) == result):
        print("Good luck!")
        print(os.getenv("FLAG"))
        break
    else:
        print("You are wrong!")
        print("The result is " + str(result) + "!")
        print("Do you wanna try again?")
        if (input("y/n: ") == "y"):
            continue
        else:
            break
print("good bye...")
