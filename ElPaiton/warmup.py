print("Hello user") 
nombre=input("Whats your name?")
print("Hello, ", nombre)
fav=input("Whats your favorite number")
num=float(fav)
if num> 27:
    print("Your number is higher than mine")
elif num<27:
    print("Your number is lower than mine")
elif num==27:
    print("Your number is the same than mine")