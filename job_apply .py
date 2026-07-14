name = input("enter your name: ")
age = int(input("enter your age: "))
height = int(input("enter your height: "))
strenght = int(input("enter your stenght from 1-10: "))
starter_pack = int(input("all the money your have : "))
print("from my decision you areeee!!!!")
if strenght  >= 8 and starter_pack >= 10000:
    print("you are accepted!")
else:
    print("your fail get outttttttttt")
print("your position is")
if strenght == 8:
   print("you are fatui harbinger class")
elif strenght == 9 :
    print("you are archon class")
elif strenght == 10:
    print("you are sovereign class")
