# Open file in read mode
with open("madhav.txt", "r") as file:
    text = file.read()

# Dictionary to store frequency
freq = {}

# Count frequency of each character
for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

# Print frequency
for key, value in freq.items():
    print(f"'{key}' : {value}")