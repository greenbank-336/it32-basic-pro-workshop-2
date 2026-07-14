name = input("enter your name: ")
age = int(input("enter your age: "))
height = int(input("enter your height: "))
strength = int(input("enter your stenght from 1-10: "))
starter_pack = int(input("all the money your have : "))
print("from my decision you areeee!!!!")
if strength  >= 8 and starter_pack >= 10000:
    print("you are accepted!")
print("your position is")
if strength == 8:
   print("you are fatui harbinger class")
elif strength == 9 :
    print("you are archon class")
elif strength == 10:
    print("you are sovereign class")
else:
    print("sorry your fail there is no position for you now Getttttt outtttt")