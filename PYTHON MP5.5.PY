print("\nName: BABIERA | ATIGA | PONCE | TENOLLAR")
print("School: FEU TECH")
print("Machine Problem - 5")

inList = [2, 5, 11, 2, 10, 1, 10, 4, 1, 8, 15, 13, 7, 5, 6, 5, 7, 
                6, 13, 12, 4, 12, 7, 3, 11, 11, 1, 11, 14, 12, 9, 4, 
                1, 7, 15, 8, 1, 5, 9, 3, 1, 15, 14, 2, 11, 1, 2, 3, 7, 
                12, 1, 1, 13, 10, 14, 10, 9, 1, 10, 9, 14, 3, 1, 13, 
                9, 9, 1, 9, 1, 12, 5, 2, 3, 9, 15, 9, 12, 10, 10, 2, 1, 
                11, 4, 12, 4, 2, 5, 9, 10, 6, 15, 6, 13, 13, 14, 7, 6, 
                15, 1, 14]

print("\nORIGINAL LIST", inList)
finList = list(set(inList))
print("\nFINAL LIST", finList)
removed = len(inList) - len(finList)
print("\nTotal number of removed elements:", removed, "\n")
