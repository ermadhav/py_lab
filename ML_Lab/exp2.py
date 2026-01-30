# import csv
# # -----------------------------
# # STEP 1: Read CSV file
# # -----------------------------
# with open('weather.csv', 'r') as file:
# reader = csv.reader(file)
# data = list(reader)
# header = data[0]
# examples = data[1:]
# num_attr = len(header) - 1
# # -----------------------------
# # STEP 2: Initialize S and G
# # -----------------------------
# S = ['0'] * num_attr # Specific Boundary
# G = [['?'] * num_attr] # General Boundary
# print("Initial S:", S)
# print("Initial G:", G)
# print()
# # -----------------------------
# # STEP 3: Process each example
# # -----------------------------
# for row in examples:
# attributes = row[:-1]
# label = row[-1]
# # -------------------------
# # POSITIVE EXAMPLE
# # -------------------------
# if label == 'Yes':
# # Generalize S
# for i in range(num_attr):
# if S[i] == '0':
# S[i] = attributes[i]
# elif S[i] != attributes[i]:
# S[i] = '?'
# # Remove inconsistent hypotheses from G
# new_G = []
# for g in G:
# is_consistent = True
# for i in range(num_attr):
# if g[i] != '?' and g[i] != attributes[i]:
# is_consistent = False
# break
# if is_consistent:
# new_G.append(g)
# G = new_G
# # -------------------------
# # NEGATIVE EXAMPLE
# # -------------------------
# else:
# new_G = []
# for g in G:
# covers_negative = True
# for i in range(num_attr):
# if g[i] != '?' and g[i] != attributes[i]:
# covers_negative = False
# break
# # If hypothesis does NOT cover negative → keep it
# if not covers_negative:
# new_G.append(g)
# # Otherwise specialize the hypothesis
# else:
# for i in range(num_attr):
# if g[i] == '?' and S[i] != '?' and S[i] != attributes[i]:
# specialized = g.copy()
# specialized[i] = S[i]
# if specialized not in new_G:
# new_G.append(specialized)
# G = new_G
# # -------------------------
# # Remove overly specific hypotheses from G
# # -------------------------
# final_G = []
# for g in G:
# more_specific = False
# for h in G:
# if g != h:
# is_more_general = True
# for i in range(num_attr):
# if h[i] != '?' and h[i] != g[i]:
# is_more_general = False
# break
# if is_more_general:
# more_specific = True
# break
# if not more_specific:
# final_G.append(g)
# G = final_G
# # -----------------------------
# # STEP 4: Final Output
# # -----------------------------
# print("\nFinal Result")
# print("Final Specific Boundary (S):", S)
# print("Final General Boundary (G):", G)


import csv

# -----------------------------
# STEP 1: Read CSV file
# -----------------------------
with open('weather.csv', 'r') as file:

# with open('weather.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

header = data[0]
examples = data[1:]
num_attr = len(header) - 1

# -----------------------------
# STEP 2: Initialize S and G
# -----------------------------
S = ['0'] * num_attr                 # Specific Boundary
G = [['?'] * num_attr]               # General Boundary

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
    if label == 'Yes':
        # Generalize S
        for i in range(num_attr):
            if S[i] == '0':
                S[i] = attributes[i]
            elif S[i] != attributes[i]:
                S[i] = '?'

        # Remove inconsistent hypotheses from G
        new_G = []
        for g in G:
            is_consistent = True
            for i in range(num_attr):
                if g[i] != '?' and g[i] != attributes[i]:
                    is_consistent = False
                    break
            if is_consistent:
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

            # If hypothesis does NOT cover negative → keep it
            if not covers_negative:
                new_G.append(g)
            else:
                # Specialize hypothesis
                for i in range(num_attr):
                    if g[i] == '?' and S[i] != '?' and S[i] != attributes[i]:
                        specialized = g.copy()
                        specialized[i] = S[i]
                        if specialized not in new_G:
                            new_G.append(specialized)

        G = new_G

    # -------------------------
    # Remove overly specific hypotheses from G
    # -------------------------
    final_G = []
    for g in G:
        more_specific = False
        for h in G:
            if g != h:
                is_more_general = True
                for i in range(num_attr):
                    if h[i] != '?' and h[i] != g[i]:
                        is_more_general = False
                        break
                if is_more_general:
                    more_specific = True
                    break
        if not more_specific:
            final_G.append(g)

    G = final_G

# -----------------------------
# STEP 4: Final Output
# -----------------------------
print("\nFinal Result")
print("Final Specific Boundary (S):", S)
print("Final General Boundary (G):", G)
