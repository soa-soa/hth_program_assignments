
# for loop is for a specific range
# while loop can go infinitely, you use while if you don't know the amount of loops


the_list = [] # empty list

for i in range(1, 101): # for loop statement left is inclusive, right is exclusive
    the_list.append(i) # loop argument

counter = 0
print(the_list) 

counter = 0
bool = True

while bool:

    counter += 1

    print(counter)

    if counter == 100:
        bool = False