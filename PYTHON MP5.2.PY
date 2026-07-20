print("NAMES: BABIERA | ATIGA | PONCE | TENOLLAR") 
print("School: FEU-TECH")
print("Machine Problem number - 2 ")


# Name: BABIERA | ATIGA | PONCE | TENOLLAR
# School: FEU-TECH 
# Machine Problem number - 3

# Initial list
numbers = [18, 19, 20]
print(f"Original list: {numbers}\n")

#a
numbers[1] = 17
print(f"a: {numbers}")

#b
numbers.extend([4, 5, 6])
print(f"b: {numbers}")

#c
numbers.pop(0)
print(f"c: {numbers}")

#d
numbers.sort()
print(f"d: {numbers}")

#e
numbers = numbers * 2
print(f"e: {numbers}")

#f
numbers.insert(3, 25)
print(f"f: {numbers}")
