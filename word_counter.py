# Where user will input the words
user_sentence = input("Enter your words: ")

split_sentence = user_sentence.replace(',', '').lower().split()
word_count1 = {}

for word in split_sentence:
    if word in word_count1.keys():
        word_count1[word] += 1
    else:
        word_count1[word] = 1

print(f"User words counter {word_count1}")

# Where there is a word ready
sentence = ("Let us buy a new collection of fish for our project aqua-scape, let's buy something unique fish with "
            "different color. this project will look good and nice with our new fish collection")

word_count2 = {}

own_sentence = sentence.replace(',', '').lower().split()
for word in own_sentence:
    if word in word_count2.keys():
        word_count2[word] += 1
    else:
        word_count2[word] = 1

print(f"Ready made sentence word count {word_count2}")
