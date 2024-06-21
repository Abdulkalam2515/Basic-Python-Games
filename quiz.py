print("Let's play the game\n Make sure you type everything in lower case only !")

answer = input("Do you want to play? (yes/no)")
if answer != "yes":
    quit()

q1 = input("What is the full form of CPU? ")
if q1 == "central processing unit":
    print("Correct")
else:
    print("Incorrect")

q2 = input("What is the capital of India? ")
if q2 == "delhi":
    print("Correct")
else:
    print("Incorrect")

q3 = input("Which is the universal drink? ")
if q3 == "water":
    print("Correct")
else:
    print("Incorrect")

q4 = input("Name the independence year of india ? ")
if q4 == "1947":
    print("Correct")
else:
    print("Incorrect")

q5 = input("How many months have 28 days? ")
if q5 == "all":
    print("Correct")
else:
    print("Incorrect")

print("Thanks for playing!")
