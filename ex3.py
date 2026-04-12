import math
import csv

# ---------------- DISTANCE FUNCTIONS ----------------
def get_euclidean_distance(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

def get_manhattan_distance(p1, p2):
    return sum(abs(a - b) for a, b in zip(p1, p2))

# ---------------- NORMALIZATION ----------------
def normalize_data(data):
    if not data: return []
    num_cols = len(data[0])
    normalized = [row[:] for row in data]

    for col in range(num_cols):
        col_values = [row[col] for row in normalized]
        min_v, max_v = min(col_values), max(col_values)
        for row in normalized:
            row[col] = (row[col] - min_v) / (max_v - min_v) if max_v != min_v else 0
    return normalized

# ---------------- WEIGHT ----------------
def calculate_weight(distance):
    return round(1 / (distance + 0.0001), 4)

def main():
    CSV_FILE = "data.csv"
    points, labels = [], []


    try:
        with open(CSV_FILE, "r") as file:
            reader = csv.reader(file)
            header = next(reader)
            features_names = header[:-1]
            for row in reader:
                if not row or len(row) < 2: continue
                points.append([float(x) for x in row[:-1]])
                labels.append(row[-1])
    except FileNotFoundError:
        print(f"Error: {CSV_FILE} not found.")
        return


    print(f"\nEnter the features for the new test point :")
    user_test_point = []
    for name in features_names:
        val = float(input(f" "))
        user_test_point.append(val)

    print("\nChoose Metric: 1. Euclidean | 2. Manhattan")
    metric_choice = input("Choice: ")
    print("Choose Voting Type: 1. Weighted | 2. Unweighted")
    vote_choice = input("Choice: ")

    # ---- NORMALIZATION ----
    all_pts = points + [user_test_point]
    norm_all = normalize_data(all_pts)
    norm_test = norm_all.pop()
    norm_train = norm_all

    # ---- DISTANCE CALCULATION ----
    results = []
    for i in range(len(norm_train)):
        dist = get_euclidean_distance(norm_test, norm_train[i]) if metric_choice == '1' else get_manhattan_distance(norm_test, norm_train[i])
        results.append({'point': points[i], 'label': labels[i], 'dist': round(dist, 4)})

    results.sort(key=lambda x: x['dist'])
    for i, r in enumerate(results): r['rank'] = i + 1

    k = int(input("\nEnter K value: "))

    # ---- PRINT FINAL TABLE (TOP K) ----
    print("\n" + "="*50)
    print(f"{'Rank':<5} | {'Point':<20} | {'Distance':<10} | {'Label':<10}")
    print("-" * 50)
    for i in range(min(k, len(results))):
        res = results[i]
        pt_str = str(res['point'])
        print(f"{res['rank']:<5} | {pt_str:<20} | {res['dist']:<10} | {res['label']:<10}")
    print("="*50)

    # ---- VOTING ----
    votes = {}
    for i in range(min(k, len(results))):
        lbl = results[i]['label']
        vote = calculate_weight(results[i]['dist']) if vote_choice == '1' else 1
        votes[lbl] = votes.get(lbl, 0) + vote

    print(f"\nFINAL PREDICTED CLASS: {max(votes, key=votes.get)}")

if __name__ == "__main__":
    main()
