def is_power_of_eight(n):
    if n > 0 and (n & (n - 1)) == 0:
        return (bin(n).count('0') - 1) % 3 == 0
    return False

number = int(input("Enter a number: "))
if is_power_of_eight(number):
    print(f"{number} is a power of 8.")
else:
    print(f"{number} is not a power of 8.")