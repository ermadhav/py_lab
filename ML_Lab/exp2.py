import csv

# -----------------------------
# STEP 1: Read CSV file
# -----------------------------
with open("weather.csv", "r") as file:
    reader = csv.reader(file)
    data = list(reader)

header = data[0]          # First row
examples = data[1:]       # Remaining rows
num_attr = len(header) - 1

# -----------------------------
# STEP 2: Initialize S and G
# -----------------------------
S = ['0'] * num_attr              # Specific Boundary
G = [['?'] * num_attr]            # General Boundary

print("Initial S:", S)
print("Initial G:", G)
print()

# -----------------------------
# STEP 3: Process each example
# -----------------------------
for row in examples:
    attributes = row[:-1]
    label = row[-1]

    # -------------------------
    # POSITIVE EXAMPLE
    # -------------------------
    if label == "Yes":
        # Generalize S
        for i in range(num_attr):
            if S[i] == '0':
                S[i] = attributes[i]
            elif S[i] != attributes[i]:
                S[i] = '?'

        # Remove inconsistent hypotheses from G
        new_G = []
        for g in G:
            consistent = True
            for i in range(num_attr):
                if g[i] != '?' and g[i] != attributes[i]:
                    consistent = False
                    break
            if consistent:
                new_G.append(g)
        G = new_G

    # -------------------------
    # NEGATIVE EXAMPLE
    # -------------------------
    else:
        new_G = []
        for g in G:
            covers_negative = True
            for i in range(num_attr):
                if g[i] != '?' and g[i] != attributes[i]:
                    covers_negative = False
                    break

            if not covers_negative:
                new_G.append(g)
            else:
                for i in range(num_attr):
                    if g[i] == '?' and S[i] != '?' and S[i] != attributes[i]:
                        new_hypothesis = g.copy()
                        new_hypothesis[i] = S[i]
                        if new_hypothesis not in new_G:
                            new_G.append(new_hypothesis)

        G = new_G

    # -------------------------
    # Remove overly specific hypotheses from G
    # -------------------------
    final_G = []
    for g in G:
        is_more_specific = False
        for h in G:
            if g != h:
                more_general = True
                for i in range(num_attr):
                    if h[i] != '?' and h[i] != g[i]:
                        more_general = False
                        break
                if more_general:
                    is_more_specific = True
                    break
        if not is_more_specific:
            final_G.append(g)

    G = final_G

# -----------------------------
# STEP 4: Final Output
# -----------------------------
print("\nFinal Result")
print("Final Specific Boundary (S):", S)
print("Final General Boundary (G):", G)
