# Tuple elements

gender=("male", "female","other")
print(gender)
print(type(gender)) # Output: <class 'tuple'>
print(gender[0]) # Accessing the first element of the tuple/ indexing


a=('2')
b='b'
l=list(a) # Converts the string '2' into a list of characters
l.append(b) # Appends the string 'b' to the list
print(l) # Output: ['2', 'b']   


# combine tuple
a=(1,2,3)
b=(4,5,6)
c=a+b # Combines the two tuples
print(c) # Output: (1, 2, 3, 4, 5, 6)

# Tuple Repitation
d=(1,2,3)*3 # Repeats the tuple three times
print(d) # Output: (1, 2, 3, 1,

# Checking membership
fruits=("apple", "banana", "cherry")
print("apple" in fruits) # Checks if "apple" is in the tuple fruits


# count
e=(1,2,3,4,5,1,2,1)
print(e.count(1)) # Counts the number of occurrences of 1 in the tuple e

#index
f=(10,20,30,40,50)
print(f.index(30)) # Returns the index of the first occurrence of 30 in the tuple f


#     Sets:--------------------------
s={1, 2, 3, 4, 5}
s2=set((5,4,8))
print(s2)
print(type(s2)) # Output: <class 'set'>

g={}
print(type(g)) # Output: <class 'dict'> // donot blank the flower brackets.

h={1,2,3}
i={3,4,5}
print(h|i) # Union of sets h and i
print(h&i) # Intersection of sets h and i
print(h-i) # Difference of sets h and i

j=h^i
print(j) # Symmetric difference of sets h and i

h.add(6) # Adds the element 6 to the set h
print(h) # Output: {1, 2, 3, 6}

h.remove(2) # Removes the element 2 from the set h
print(h) # Output: {1, 3, 6}    

h.discard(3) # Removes the element 3 from the set h
print(h) # Output: {1, 6}       

h.pop() # Removes and returns an arbitrary element from the set h
print(h) # Output: {6} (the remaining element after popping one)    

h.clear() # Removes all elements from the set h
print(h) # Output: set() (an empty set) 