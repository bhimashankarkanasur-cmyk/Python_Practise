# List in Python
items=["apple", "banana", "cherry", "date", "elderberry"]
print("Original list:", items)
print(items[0]) # Accessing the first item
print(items[-1]) # Accessing the last item

l=[1, 2, 3, 4, 5,"Bhimashankar"]
print(l)

# Remove
items.pop() # Removes the last item
print("List after pop:", items)

l.pop() # Removes the last item from l
print(l)

l.pop(0) # Removes the first item from l
print(l)

# ADD
items.append("fig") # Adds "fig" to the end of the list
print("List after append:", items)

l.append("Ganesh") # Adds "Ganesh" to the end of the list l
print(l)

# Add Perticular Place
items.insert(2, "coconut") # Inserts "coconut" at index 2
print("List after insert:", items)

# Remove all Lists
items.clear() # Removes all items from the list
print("List after clear:", items)


# Replace the Lists
l[0]="grape" # Replaces the first item with "grape"
print(l)


# Slicing the Lists
lm=[100,200,300,400,500,600,700]
lm[0:2] # Slices the list from index 0 to 1 (not including index 2)
print(lm[0:2]) # Output: [100, 200]


l1=[1,2,3,4,5,6,7,8,9]
l2=l1[2:5] # Slices the list from index 2 to 4 (not including index 5)
print(l2) # Output: [3, 4, 5]

# Common Funnctions of List:--
a=[1,2,3,4,5]
print(len(a)) # Length of the list

b=[100,10,50,800,70,60]
print(sorted(b)) # Returns a new sorted list

c=[5,2,9,1,5,6]
sorted_c=sorted(c) # Sorts the list and returns a new sorted list
print(sorted_c) # Output: [1, 2, 5, 5, 6, 9]

# Sum(list): Returns the sum of all items in the list
d=[1,2,3,4,5]
print(sum(d)) # Returns the sum of all items in the list    

# Index(element): Returns the index of the first occurrence of the specified element in the list
e=[10,20,30,40,50]
print(e.index(30)) 

#Count(element): Returns the number of occurrences of the specified element in the list
f=[1,2,3,4,5,1,2,1]
print(f.count(1)) # Returns the number of occurrences of 1 in the list

# Reverse(): Reverses the order of the list
g=[1,2,3,4,5]
g.reverse() # Reverses the order of the list
print(g)

g.sort() # Sorts the list in ascending order
print(g) # Output: [1, 2, 3, 4, 5]  


# Nested Lists:--
h=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(h)
print(h[0]) # Accessing the first sublist
print(h[1]) # Accessing the third element of the second sublist
print(type(h)) # Output: <class 'list'>