'''

my_string="python"

for each_element in my_string:
    print(each_element)

print(my_string, "has", len(my_string), "characters")

my_list=["a", "b", "c"]

for each_element in my_list:
    print(each_element)

my_list_lenght=len(my_list)

print("my list has", my_list_lenght, "elements")



my_numbers=[123, 12.4, 15, 152, 12.3333]
print(my_numbers)

my_numbers.append(34)
my_numbers.append(1)
my_numbers.append(69)

print(my_numbers)
print(len(my_numbers))

my_numbers.pop()
my_numbers.pop()
print(my_numbers)

print(my_numbers.index(15))

# my_numbers.remove(12.4) - Se debe especificar el nombre del elemento a borrar
# my_numbers.insert(0, 12000) - Se especifica posición y elemento para 
# insertarlo en una lista.


print(my_numbers)

my_chars=["a","b","c"]

# my_numbers.append(my_chars)

print(my_numbers)

two_dim_list=[my_numbers,my_chars]

print(two_dim_list)

print(two_dim_list[1][1])

nums1=[1, 2, 3]
nums2=[4, 5, 6]

fullnums = nums1 + nums2

print(fullnums)


# Number Chains


Conti=True
count = 0


while Conti == True:   
    num = input ("How many numbers?")

    if num.isdigit():
        num = float(num)
        while count < num:
            count+=1
            print(count)
        while Conti==True:
            Question=input("Would you like to continue? (Y/N)")
            if Question.upper()== "Y":
                count=0
                break
            elif Question.upper() == "N":
                Conti=False
                print("Goodbye")
                break
            else:
                print("Please insert a valid argument (Y/N)")
    else:
        print("Please, insert a valid number")

'''

'''
list_a=[1,2,3,4,5]
list_b=["1","2","3","4","5"]

len_list_a=len(list_a)

print(f"The list 'a' has {len_list_a} elements")

list_range=list(range(40, 10, -1)) #Se pueden usar distintos valores en range (range(4, 10))
print(f"List returned by range function: {list_range}")

print(list_a)


for each_index in range(len(list_a)):
    print(list_a[each_index], list_b[each_index])
'''

