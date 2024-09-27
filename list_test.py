import random 

sweepstakers = [num for num in range(1,16)]
print(sweepstakers)

rand_sweepstaker = random.sample(sweepstakers, k=15)
print(rand_sweepstaker)

for num in rand_sweepstaker:
    print(num)

celebrities = [num for num in range(1,16) if num%2 == 0]
print(celebrities)

rand_celebrities = random.sample(celebrities, k=15)
print(rand_celebrities)

for num in rand_celebrities:
    print(num)

