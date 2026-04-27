a = input("Enter name of event A: ")
b = input("Enter name of event B: ")

p_a = float(input(f"Enter P({a}): "))
p_b = float(input(f"Enter P({b}): "))
p_a_given_b = float(input(f"Enter P({a}|{b}): "))

p_b_given_a = (p_a_given_b * p_b) / p_a

print(f"P({b}|{a}) = {p_b_given_a}")
