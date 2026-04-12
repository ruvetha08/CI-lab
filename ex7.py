def load_data(filename):
    data = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                p = [float(x) for x in line.strip().replace(',', ' ').split()]
                if len(p) == 3: data.append(p)
        return data
    except FileNotFoundError: return []

# User Inputs
w1 = float(input("Enter initial w1: "))
w2 = float(input("Enter initial w2: "))
b = float(input("Enter initial bias: "))
alpha = float(input("Enter alpha: "))
epochs = int(input("Enter number of epochs: "))

dataset = load_data("data.txt")

for epoch in range(1, epochs + 1):
    print(f"\n{'='*30} EPOCH {epoch} {'='*30}")
    header = f"{'x1,x2':<6} | {'T':<3} | {'Yin Calculation':<25} | {'Yin':<6} | {'Out':<4} | {'Weight Update (w+alpha*x*t)':<35} | {'New w1,w2,b'}"
    print(header)
    print("-" * len(header))

    for x1, x2, t in dataset:
        # 1. Yin Step
        calc_yin = f"{b:.1f} + ({x1}*{w1:.1f}) + ({x2}*{w2:.1f})"
        yin = b + (x1 * w1) + (x2 * w2)
        out = 1 if yin >= 0 else -1

        # 2. Update Step
        update_str = "None (Correct)"
        if out != t:
            # Show the calculation for the first weight and bias as an example
            update_str = f"w1:{w1:.1f}+({alpha}*{x1}*{t}) | b:{b:.1f}+({alpha}*{t})"
            w1 += (alpha * x1 * t)
            w2 += (alpha * x2 * t)
            b += (alpha * t)

        # 3. Print Row
        new_vals = f"{w1:.2f}, {w2:.2f}, {b:.2f}"
        print(f"{x1:>2},{x2:<2} | {t:<3} | {calc_yin:<25} | {yin:<6.2f} | {out:<4} | {update_str:<35} | {new_vals}")

print(f"\nFinal trained parameters: w1={w1:.2f}, w2={w2:.2f}, bias={b:.2f}")
