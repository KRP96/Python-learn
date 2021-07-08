# Create an empty set
s= set()

#Add some elements
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(4)       #set isn't allowed any duplicate values

print(s)

s.remove(3)      #remove number 3

print(s)

print(f"This set has {len(s)} elements.")    #count of elements