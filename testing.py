# lab 4 step 10

# parameters help make the code reuseable (parameter):
# (longer names ... shorter names)

city_names = ["oakland", "seattle", "altlanta", "new york city", "memphis", "miami", "los angeles", "new orleans"]

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
