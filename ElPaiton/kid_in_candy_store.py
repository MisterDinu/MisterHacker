# The list of candies to print to the screen
candy_list = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]
i=0
# The amount of candy the user will be allowed to choose
allowance = 5
# The list used to store all of the candies selected inside of
candy_cart = []
# Print out options

while allowance >0:
    print("Greetigns user! please select up to 5 candies, these are the available candies:")
    for candy in candy_list:
        print(f'[{i}]{candy}')
        i=i+1
    while allowance>0:
        add_candy=input("Select a candy")
        if add_candy.isdigit():
            add_candy=int(add_candy)
            if add_candy > 8 or add_candy < 0:
                print("Invalid option, select a candy in the index")
            else:
                candy_cart.append(candy_list[add_candy])
                allowance -= 1
                print(f"Your cart has:{candy_cart}")
                break
        else:
            print("Invalid option, select a candy in the index")
    if allowance==0:
        while True:
            more=input("Do you want more candies? Y/N")
            if more.upper() == "Y":
                allowance+=5
                print("You little piggy hahaha...")
                candy_cart = []
                break
            elif more.upper()== "N":
                print("See you later, alligator")
                break
            else:
                print("Please select a valid option")
    
    i=0

