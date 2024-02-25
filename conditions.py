# n = int(input("Number: "))

# if n > 0:
#     print("n is positive.")
# elif n < 0:
#     print("n is negative.")
# else:
#     print("n is 0")

user_input = input("Enter a number: ")

try:
    num = float(user_input)
    if num.is_integer():
        num = int(num)
    print("Input number:", num)
except ValueError:
    print("Invalid")

