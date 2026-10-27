swift = input("SWIFT: ")
print(f"Bank code: {swift[:4]}\nCountry code: {swift[4:6]}\nLocation code: {swift[6:8]}\nBranch code: {swift[8:11]}")