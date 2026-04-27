n = int(input("Enter number of variables: "))

names = []
for i in range(n):
    names.append(input(f"Enter name of variable {i+1}: ").strip())

total = 2 ** n
print("Total combinations:", total)

probs = []

print("Enter probabilities for each combination:")

for i in range(total):
    combo = input(f"Combination {i+1} (use {names}): ")
    p = float(input("Probability: "))

    values = {var: False for var in names}
    tokens = combo.split()

    for t in tokens:
        if t.startswith("~") or t.startswith("!"):
            values[t[1:]] = False
        else:
            values[t] = True

    probs.append((values, p))



def evaluate(expr, values):
    expr = expr.replace("^", " and ")
    expr = expr.replace("v", " or ")
    expr = expr.replace("|", " or ")
    expr = expr.replace("~", " not ")

    return eval(expr, {}, values)



query = input("Enter query: ")

result = 0

for values, p in probs:
    try:
        if evaluate(query, values):
            result += p
    except Exception as e:
        print("Invalid query format!")
        exit()

print("Answer:", result)
