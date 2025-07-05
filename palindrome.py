def palindrom(str):
    b=" ".join(str.strip("," " "))
    if b == b[::-1]:
        print("It is a palindrome")
    else:
        print("Not a palindrome")

palindrom("racecar")
palindrom("hello")
palindrom("A man, a plan, a canal, Panama")