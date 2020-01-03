with open("texto01.txt") as file:
    print(type(file.readlines()))
    print(len(file.readlines()))
    print(file.closed)
    file.close()
    print(file.closed)
