my_words = input("Enter sentence: ")

words = [word.lower() for word in my_words.split()]

words.sort()

for i in words:
    print(i)