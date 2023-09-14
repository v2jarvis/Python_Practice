alpha=input("Type The Alphabet:-")
string=len(alpha)
if (string) == 1:
    print("Input is a single character.")
elif (" " and '.' not in alpha):
    print("Input is a word.")
else:
    print("Input is a sentence.")