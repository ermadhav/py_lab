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

filename = "madhav.c"

with open(filename, "r") as file:
    text = file.read()

freq = {}
for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for key, value in freq.items():
    print(f"'{key}' : {value}")

if filename.endswith(".c"):
    print("\nThis is a C program file.")
elif filename.endswith(".py"):
    print("\nThis is a Python file.")
elif filename.endswith(".txt"):
    print("\nThis is a text file.")
else:
    print("\nUnknown file type.")