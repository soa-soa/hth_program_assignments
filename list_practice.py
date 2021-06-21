# Oakland, Atlanta, New York City, Seattle, Memphis, Miami, Boston, Los Angeles, Denver, and New Orleans

# from os import O_NDELAY
# from posix import EX_NOTFOUND


city_names = ["oakland", "altlanta", "new york city", "seattle", "memphis", "miami", "boston", "los angeles", "denver", "new orleans"]
three_cities = city_names[0:2]
city_names[0] = "san francisco"
city_names[1] = "orlando"
city_names[2] = "brooklyn"
city_names[5] = "tampa"
city_names[7] = "hollywood"

city_names.append("new jersey") # adds one to the end of the list
city_names.extend(["santa cruz", "selma", "chicago"]) # adds entire lists to the end of original list
city_names.insert(7,"washington, d.c.") # number in front tells var where to go

del city_names[3] #deleted seattle
city_names.pop(6) 
city_names.remove("hollywood")

print(city_names)

for city in city_names:
    print(city)
# useful to print all the names in a list on a single line

laptop_brands = ["lenovo", "dell", "apple", "hp", "acer", "huawei", "msi", "xiaomi", "samsung", "lg"]

print(laptop_brands[0]) 
print(laptop_brands[2]) 
print(laptop_brands[4]) 
# starts at 0 not 1 
# 0 = lenovo 1 = dell

three_laptops = laptop_brands[0:3]
print(three_laptops)


# lab 4 step 9

# while loop to access all valyes
# access value with index
# check to make sure index is less than list length


def print_city_names():
    counter = 0
    while counter < len(city_names):
        print(city_names[counter])
        counter += 1
    return"completed"

#print(city_names[0], city_names[1], city_names[2])
print_city_names()

# lab 4 step 10

# parameters help make the code reuseable (parameter):
# (longer names ... shorter names)

def organize_cities(cities_list):
    counter = 0
    for city in cities_list:
        if(len(cities_list[counter]) > len(cities_list[counter +1])):
            counter += 1
        else: 
            # pop - index value
            # remove - value
            cities_list.remove(city)
            cities_list.append(city)
            counter += 1
    return cities_list
    
print(organize_cities(city_names))
