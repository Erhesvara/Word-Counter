# Where user will input the words
user_sentence = input("Enter your words: ")

split_sentence = user_sentence.replace(',', '').lower().split()
word_count1 = {}

for word in split_sentence:
    if word in word_count1.keys():
        word_count1[word] += 1
    else:
        word_count1[word] = 1

print(word_count1)

# Where there is a word ready

sentence = ("Let us buy a new collection of fish for our project aqua-scape, let's buy something unique fish with "
            "different color. this project will look good and nice with our new fish collection")

