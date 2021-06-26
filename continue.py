

counter = 0
bool = True

while bool:

    counter += 1

    print("Counter is at",counter)

    if counter < 100:
        continue # CTRL + C to stop endless loops

    elif counter == 100:
        break
