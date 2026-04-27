target = int(input("Enter target sum: "))

count = 0

for i in range(1, 7):
    for j in range(1, 7):
        if i + j == target:
            print(f"({i}, {j})")
            count += 1

if count == 0:
    print("No possible outcomes")
else:
    probability = count / 36
    print("Total favorable outcomes:", count)
    print("Probability:", f"{probability:.2f}")
