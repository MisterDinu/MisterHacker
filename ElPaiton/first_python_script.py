
# this is a comment in a single line

# to comment several lines, use 3 times single quote: ''' and use another 3 to close '''

'''
Line 1
Line 2
Line 3
'''

my_number=3.1416

my_number_str=str(my_number)

print(f"Pi constant is about {my_number}")

print("Pi constant is about", my_number)

print("Pi constant is about " + my_number_str)

my_integer=1
print(type(my_integer))

my_integer=1.0
print(type(my_integer))

my_str="3.1416"
my_number=float(my_str)
print(type(my_number), my_number)

my_list=[my_str, my_number, my_integer]
print(my_list[0])
print(my_list[1])
print(my_list[2])

my_dic={"texto":my_str, "numero":my_number}
print(my_dic["texto"])
