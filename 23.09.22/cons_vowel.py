def cons_vowel(char):
    if char in ("a","A","e","E","i","I","o","O","u","U"):
        return (f"{char} is a vowel")
    elif not char.isalpha():
        return (f"{char} is not alphabet")
    else:
        return (f"{char} is a consonant")
char = input("Enter a character: ")
print(cons_vowel(char))
