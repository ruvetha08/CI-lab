def nthPersonGetsNthSeat(n):
    if n == 1:
        return 1.0
    return 0.5
n = int(input("Enter number of passengers: "))
result = nthPersonGetsNthSeat(n)
print("Probability that nth person gets nth seat:", result)
