# step 1
word = input("Enter a word for us to count vowels:")

# I need to keep count of the vowels
vowel_count = 0
VOWEL_LETTERS = "aieou" # we don't do y around here.

# what I'm going to do  is loop over the words' letters
# remember that strings are character lists you can access each character
for letter in word:
    print(letter)
    # check if it's a vowel
    if letter in VOWEL_LETTERS:
        # add one to the vowel count
        vowel_count += 1 # vowel_count = vowel_count + 1

# outside of the loop
print(F"There are {vowel_count} vowels in the word {word}")