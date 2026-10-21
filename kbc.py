Questions=["What is the National Animal of India",
           "What is the Chemical Formula of Gold",
           "How many sides are there in a Hexagon"]
options=[["A.Lion","B.Tiger","C.Peacock","D.Dinosaur"],
        ["A.Ag","B.Au","C.Pb","D.La"],
         ["A.5","B.6","C.6.0","D.8"] ]
answers=["B","A","B"]
prizes=[1000,10000,100000]
start_prize=0
for i in range(len(Questions)):
    print(Questions[i])

    for option in options[i]:
        print(option)

    answer=input("Enter your Answer (A/B/C/D):").upper()
    if answer==answers[i]:
        start_prize+=prizes[i]
        print("Correct Answer!")
        print("You Won $",start_prize)
    else:
        print("Wrong Answer!")
        break

print("Your total prize money is $",start_prize)
