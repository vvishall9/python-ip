list  = [8,5,55,44,44,41,104]
list.sort()
x = list[-1]
print("Largest integer is: ",x)

#or

largest = list[0]

for i in list:
    if largest < i:
        largest= i

print("largest: ", largest)

#smallest
small = list[0]
for i in list:
    if small > i:
        small= i

print ("smallest: ", small)