import random
from english_words import get_english_words_set

Set_of_Word = get_english_words_set(['web2'], lower=True)
Random_word = random.choice(list(Set_of_Word))
Number_of_letter = len(Random_word)

revealed_word = ["_"] * Number_of_letter
Live = Number_of_letter

print ("The word :", " ".join(revealed_word))
print(Random_word)

while Live > 0:
    Ask_for_letter = input("Enter a letter or the word : ").lower()

    if Ask_for_letter == Random_word:
        print ("U win :", Random_word)
        break

    elif len(Ask_for_letter) == 1 and Ask_for_letter in Random_word:
        print("the letter", Ask_for_letter, "is in the word.")
        for i, letter in enumerate(Random_word):
            if letter == Ask_for_letter:
                revealed_word[i] = Ask_for_letter
        print("The word :", " ".join(revealed_word))

        if "_" not in revealed_word:
            print("U win :", Random_word)
            break

    else:
        Live -= 1
        print("The letter  ", Ask_for_letter, "isn't in the word")
        print("Live leftover :", Live)

        if Live == 0:
            print("U loose :", Random_word)