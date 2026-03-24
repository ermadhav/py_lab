with open("madhav.txt", "r") as file:
    text = file.read()

freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for key, value in freq.items():
    print(f"'{key}' : {value}")