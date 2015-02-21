__author__ = 'matthewburleson'

def disemvowel(voweled_word):
    voweled_list = list(voweled_word.lower())
    vowels = list("aeiou")
    for vowel in vowels:
        while True:
            try:
                voweled_list.remove(vowel)
                continue
            except(ValueError):
                break

    return "".join(voweled_list)

voweled_word = input("What word would you like me to devowel? ")
print(disemvowel(voweled_word).capitalize())