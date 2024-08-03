# Triangle of stars
n = int(input("Please enter an integer:"))

for i in range(n):
    print(" " * (n-i-1) + "*" * (2 * i + 1))
