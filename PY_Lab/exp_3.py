# <----------------------------------- PART A ----------------------------------->

# n = int(input("Enter a number: "))
# if n % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

# <----------------------------------- PART B ----------------------------------->

# n = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"the table of {n} is", i*n)

# <----------------------------------- Practice ----------------------------------->

# n = int(input("Enter a number: "))
# if n % 5 == 0 and n % 11 == 0:
#     print("number is divisible by 5 and 11")
# elif n%5 == 0:
#     print("5 se divisible")
# elif n%11 == 0:
#     print("11 se divisible")
# else:
#     print("dono se divisible nahi")

# <----------------------------------- Practice ----------------------------------->

# for i in range(1, 101):
#     if(i % 2 == 0):
#         print(f"{i} number is even")

n = int(input("Enter the number you want to reverse: "))
reverse =0
while n != 0:
    remainder = n % 10
    reverse = reverse * 10 + remainder
    n = n // 10
print("reverse = ",reverse)

print("Reverse using function: ", n[::-1])