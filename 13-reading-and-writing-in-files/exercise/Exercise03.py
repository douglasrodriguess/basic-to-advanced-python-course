with open("texto01.txt") as file:
    #list = file.readlines()
    list = file.read().splitlines()
    print(type(list))
    print(len(list))
    print(list)
    vet = []
    vogal = ['a', 'e', 'i', 'o', 'u']
    res = [vet.append(caract) if caract in vogal else print() for caract in list]
    #res = [[vet.append(caract) if caract in ["a", "e", "i", "o", "u"] else print("consoante") for caract in list] for  in vogal]
    # for caract in list:
    #     if str(caract) in vogal:
    #         vet.append(caract)
    print(vet)
    print(len(vogal))
