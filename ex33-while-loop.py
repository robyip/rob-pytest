
def wloop(endloop: int, incrementby: int) -> None :

    # i = 0
    # numbers = []

    # while i < endloop:
    #     print(f"At the top i is {i}")
    #     numbers.append(i)

    #     i = i + incrementby
    #     print("Numbers now: ", numbers)
    #     print(f"At the bottom i is {i}")

    numbers = []

    for i in range(0, endloop, incrementby):
        print(f"At the top i is {i}")
        
        numbers.append(i)

        print("Numbers now: ", numbers)

        print(f"At the bottom i is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)

# call the while loop
wloop(9, 3)