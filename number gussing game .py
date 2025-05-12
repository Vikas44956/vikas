#number gussing game 
import random
num =[1,2,3,4,5,6,7,8,9,10]
number = random.choice(num)
while True:
    user = int(input("Guess the number bettwen 1 to 10 :"))
    if user == number:
        print("great you are right.")
        print(number)
        break
    elif user <= number:
        print("too low")
    elif user >= number:
        print("too high")