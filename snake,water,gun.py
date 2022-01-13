import random

def game(comp,you):
    if comp==you:
        return None
    elif comp=="s":
        if you=="w":
            return False
        elif you=="g":
            return True
    elif comp=="w":
        if you=="s":
            return True
        elif you=="g":
            return False
    elif comp=="g":
        if you=="s":
            return False
        elif you=="w":
            return True

randNo = random.randint(1,3)

print("Player 1: Snake(s) Water(w) or gun(g)?")
b=input("Player 2: Snake(s) Water(w) or gun(g)?\n")

if randNo==1:
    comp="s"
elif randNo==2:
    comp="w"
elif randNo==3:
    comp="g"

print(f"Computer chose {comp}")
print(f"You chose {b}")

a=game(comp,b)

if a==None:
    print("tie")
elif a==True:
    print("win")
else:
    print("lose")