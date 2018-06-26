print("Think of a number between 1 and 1000")
lower = 1
upper = 1000
middle = (lower+upper)//2


print("Is your number between",lower,"and",upper,"?")
guess = input("Please type Yes or No")
print("Is your number between",middle,"and",upper,"?") 
while lower != upper: #!= not equal staticmethod
    guess = input("Please type Yes or No")
 
    if guess == "Yes":
        lower = middle+1
        middle = (lower+upper)//2
        print("Is your number between",middle,"and",upper,"?")
    elif guess =="No":
        upper = middle-1
        middle = (lower+upper)//2
        print("Is your number between",middle,"and",upper,"?")

print("Were you thinking of the number",middle,"?")


