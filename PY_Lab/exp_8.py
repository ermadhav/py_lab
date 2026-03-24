with open("C:\\Users\\madha\\OneDrive\\Desktop\\py_lab\\PY_Lab\\madhav.txt", "r") as file:    
    text = file.read()

freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for key, value in freq.items():
    print(f"'{key}' : {value}")

reversed_text = text[::-1]

with open("C:\\Users\\madha\\OneDrive\\Desktop\\py_lab\\PY_Lab\\madhav.txt", "w") as file:
    file.write(reversed_text)