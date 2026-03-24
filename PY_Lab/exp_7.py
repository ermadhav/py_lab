# ------------------- PART - 1 -------------------
# with open("C:\\Users\\madha\\OneDrive\\Desktop\\py_lab\\PY_Lab\\madhav.txt", "r") as file:    
#     text = file.read()

# freq = {}

# for ch in text:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1

# for key, value in freq.items():
#     print(f"'{key}' : {value}") 

# ------------------- PART - 2 -------------------

filename = "madhav.txt"

with open(filename, "r") as file:
    text = file.read()

# Frequency count (same as your code)
freq = {}
for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for key, value in freq.items():
    print(f"'{key}' : {value}")

# Detect file type using extension
if filename.endswith(".c"):
    print("\nThis is a C program file.")
elif filename.endswith(".py"):
    print("\nThis is a Python file.")
elif filename.endswith(".txt"):
    print("\nThis is a text file.")
else:
    print("\nUnknown file type.")