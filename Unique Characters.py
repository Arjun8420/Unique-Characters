# Program to verify if the given string has all unique characters

data = input("Enter the String = ")

found = [False] * 127

for c in data:
    if found[ord(c)] == False:
        found[ord(c)] = True
    else:
        print("Duplicates present in String")
        break
else:
    print("All characters are unique")
