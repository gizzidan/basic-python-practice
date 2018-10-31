bound_1 = int(input("Enter first number: "))
bound_2 = int(input("Enter second number: "))

bounds = [bound_1, bound_2]
bounds.sort()

primes = []
for x in range(bounds[0]+1, bounds[1]):
    if all(x%i!=0 for i in range(2,x)):
       primes.append(x)
    

if len(primes) > 1:
    for i in range(0, len(primes)-1, 3):
        primes[i] = str(primes[i])+":"

    for i in range(1, len(primes)-1, 3):
        primes[i] = str(primes[i])+"!"

    for i in range(2, len(primes)-1, 3):
        primes[i] = str(primes[i])+","
    print("".join(map(str,primes)))
elif len(primes) == 1:
    print("".join(map(str,primes)))
else:
    print("No Primes")








