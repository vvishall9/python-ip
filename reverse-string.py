str = "abcdo"
b = str[::-1]
print(b)

#..........
rev = ""
for i in str:
    rev = i + rev
print(rev)

# Reverse a sentence

sen ="My name is Vishal"
spl = sen.split()
b= spl[::-1]
print(" ".join(b))


