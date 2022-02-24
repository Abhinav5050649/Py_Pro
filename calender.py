sr = input("Enter word: ")

sr = sr.casefold()
sr2 = reversed(sr)

if (list(sr2) ==list(sr)):
    print("Palindrome strings!")
else:
    print("Not palindrome strings!")