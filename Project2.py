# project: guess the number
import random
n=random.randint(1,100)
a= -1
guesses=0
while a!=n:
    guesses+=1
    
    a=int(input("enter a number:"))
    if a>n:
        print("bhai aapki soch tou bohot badi hai")
    elif a<n:
        print("bhai aapki soch badi choti hai")
    else:
        print(f"congrats nigga you guessed it right in {guesses}guesses")


