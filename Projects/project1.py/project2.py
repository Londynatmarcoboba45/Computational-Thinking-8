dicky_points = 0
nicky_points = 0 
ricky_points = 0

answer1 = input("what kind of birthday party do you want A science party, B roller skate, C vacation   ")
if answer1 == "A": 
    dicky_points += 1
elif answer1 == "B":
    nicky_points += 1
elif answer1 == "C":
    ricky_points += 1 

answer2 = input("Would you want to have A pizza, B tacos, C burgers   ")
if answer2 == "A":
    nicky_points += 1 
    dicky_points += 1
elif answer2 == "B":
    ricky_points += 2

answer3 = input("would you rather A wear blue, B wear red, C yellow   ")
if answer3 == "A" or answer3 == "B":
    nicky_points += 2
elif answer3 == "C":
    dicky_points += 1
    ricky_points += 1 

answer4 = input("Would you want A sister, B brother C sister and brother   ")
if answer4 == "A":
    nicky_points += 1
elif answer4 == "C":
    dicky_points += 1
    ricky_points += 1 

answer5 = input(" Would you rather have A dog, B cat, C pig   ")
if answer5 == "A":
    nicky_points += 1
elif answer5 == "B":
    dicky_points += 1
elif answer5 == "C":
    ricky_points += 1 

#End: determine results 
if dicky_points > nicky_points and dicky_points > ricky_points:
    print("You are a dicky person")
if nicky_points > dicky_points and nicky_points > ricky_points:
    print("You are a nicky person")
if ricky_points > nicky_points and ricky_points >dicky_points:
    print("You are a ricky person")