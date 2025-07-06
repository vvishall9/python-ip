vowel = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

def vowel_const(text):
    vowel_count =0
    cons_count = 0

    for i in text:
        if i in vowel:
            vowel_count += 1
        else:
            cons_count += 1
    print (f"Vowel count is : {vowel_count} and consonant count is {cons_count}")

vowel_const("My name is Vishal")