print("Exercise 1")

# Rastin
# ================================
distance = int(input("please enter the number:"))
for star in range(6):
    print(" "*(distance-star)+"* "*(star))
# ================================

# Mohammad
# ================================
zel = int(input("Please write the size of the sides of the triangle"))
space = zel+1
for zel in range(1, zel+1):
    print((space-zel)*" ", zel*"* ")

# ================================


# Mehrad
# ================================
value = input("How Many Stars Do You Want?: ")
star = int(value)
for number in range(star):
    print(number*"*")
# ================================

# Pantea
# ================================
# your code
# ================================

# Hamed
# ================================
for number in range(1):
    print("", "", "", "", "", "", "*")
    for number in range(1):
        print("", "", "", "", "", "*", "*")
        for number in range(1):
            print("", "", "", "", "*", "*", "*")
            for number in range(1):
                print("", "", "", "*", "*", "*", "*")
                for number in range(1):
                    print("", "", "*", "*", "*", "*", "*")

# ================================

#####################################################################################################

print("Exercise 2")

# Rastin
# ================================
number = int(input("enter the number:"))
count = 2

while count <= number:
    print(count)
    count += 2

# ================================

# Mohammad
# ================================
number = int(input("plz enter the number:"))
start = 0
count = 0
while start <= number:
    # ya kolan bray adad zoj mitonim bnvisim start+=2
    start += 1
    if start % 2 == 0:
        print(start)
        count += 1
print(f"the amount is:{count}")
# ye moshkeli k dare vaghti adad fard vared mikonam yeki ezafe tar ham minevise
# ================================


# Mehrad
# ================================
user = input("Enter Your Number: ")
number = int(user)
even = 2
count = 0
while even <= number:
    if even % 2 == 0:
        count += 1
        print(even)
    even += 2
print(f'Number of Even Numbers: {count}')
# ================================

# Pantea
# ================================
x = int(input("Enter your number: "))
n = 0
while n <= x:
    if n % 2 == 0:
        print(n)
    n += 1

# (x // 2) + 1
# print(x)

# ================================

# Hamed
# ================================
# Your Code
# ================================

# Rahan
# ================================
# Your Code
# ================================

#####################################################################################################

print("Exercise 3")

# Rastin
# ================================
number = int(input("enter the number:"))
reverse = 0
while number > 0:
    num = number % 10
    reverse = reverse * 10 + num
    number = number // 10
# vase addad 2 raghami az num*10+number ham estefade mishe
print(reverse)
if (number == reverse):
    print(True)
else:
    print(False)
# ================================


# Mohammad
# ================================
def xx(number):
    num = str(number)
    return num[::-1] == str(number)


ex = xx(1221)
print(ex)
# ================================


# Mehrad
# ================================
def check_reverse():
    command = " "
    while command.upper() != "QUIT":
        command = input(">>> ")
        if command == command[::-1]:
            print("True")
        elif command.upper() == "QUIT":
            print("Have a Nice Day!")
        else:
            print("False")


check_reverse()
# ================================


# Pantea
# ================================
def is_palindrome(number):

    str_number = str(number)

    return str_number == str_number[::-1]


user_input = input("enter the number: ")

if is_palindrome(user_input):

    print("true ")

else:

    print("false ")
# ================================


# Rahan
# ================================
# Your Code
# ================================


#####################################################################################################

print("Exercise 4")

# Rastin
# ================================
# Your Code
# ================================


# Mohammad
# ================================
# Your Code
# ================================


# Mehrad
# ================================
def average(*points, name="Student"):

    total = 0
    for num in points:
        total += num
        avg = total // len(points)

    name = input("Enter Your Name: ") or name
    if 20 >= avg >= 18:
        print(f"Dear {name} Your Grade is \"A\"")
    elif 18 >= avg >= 14:
        print(f"Dear {name} Your Grade is \"B\"")
    else:
        print(f"Dear {name} Your Grade is \"C\"")


average(18, 17, 20, 16, 19)
# ================================


# Pantea
# ================================
# Your Code
# ================================


# Rahan
# ================================
# Your Code
# ================================
