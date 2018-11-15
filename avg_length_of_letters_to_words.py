# Average length of letters to words

sentence = "Hi my name is Gouri"
words = sentence.split()
print(sum(len(word) for word in words))
print(len(words))
average = sum(len(word) for word in words) / len(words)
print (average)

print(words)
print(type(words))

