user_sentence = input("Enter your words: ")

split_sentence = user_sentence.replace(',', '').lower().split()
word_count = {}

for word in split_sentence:
    if word in word_count.keys():
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
