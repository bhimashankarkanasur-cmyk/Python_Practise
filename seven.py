#Dictionaries:---

meanings={
    "hello": "a greeting",
    "goodbye": "a farewell",
    "bat": "a flying mammal"
}
print(meanings["hello"]) # Output: a greeting
print(meanings["goodbye"]) # Output: a farewell
print(meanings["bat"]) # Output: a flying mammal
print(type(meanings)) # Output: <class 'dict'>

karnataka_food={
    "bisi bele bath": "a spicy rice dish",
    "ragi mudde": "a traditional dish made from finger millet",
    "mysore pak": "a sweet made from gram flour, sugar, and ghee"
}
print(karnataka_food["bisi bele bath"]) # Output: a spicy rice dish
print(karnataka_food["ragi mudde"]) # Output: a traditional dish made from finger millet
print(karnataka_food["mysore pak"]) # Output: a sweet made from gram flour, sugar, and ghee
print(type(karnataka_food)) # Output: <class 'dict'>
print(karnataka_food.get("Jolada rotti","Dish not found")) # Output: Dish not found (since "Jolada rotti" is not a key in the dictionary)


# Adding and Updating Dictionary Elements:--
birthday={
    "Bhimashankar":"30-may-2004",
    "sachin":"09-jun-2008",
    "ravana":"12-jul-2012"
}
print(birthday) # Output: {'Bhimashankar': '30-may-2004', 'sachin': '09-jun-2008', 'ravana': '12-jul-2012'}
print("Adding new element to the dictionary")
birthday["siddharth"]="15-aug-2015" # Adding a new key-value pair to the dictionary
print(birthday) # Output: {'Bhimashankar': '30-may-200

#Updating:--
birthday={
    "Bhimashankar":"30-may-2004",
    "sachin":"09-jun-2008",
    "ravana":"12-jul-2012"
}
print(birthday)
print("updating  dictionary")
birthday["Bhimashankar"]="31-may-2004"
print(birthday) # Output: {'Bhimashankar': '31-may-2004', 'sachin': '09-jun-2008', 'ravana': '12-jul-2012'}


#Removing elements from a Dictionary:--
#pop:--
birthday.pop("sachin") # Removes the key-value pair with the key "sachin" from the dictionary
print(birthday) # Output: {'Bhimashankar': '30-may-200

# del
del birthday["ravana"] # Removes the key-value pair with the key "ravana" from the dictionary
print(birthday) # Output: {'Bhimashankar': '30-may-200

#clear:--
birthday.clear() # Removes all key-value pairs from the dictionary
print(birthday) # Output: {}





# Dictionary Methods:--
a= {
    "name": "Alice",
    "age": 30,
    "city": "New York"

}
print(a.keys()) # Output: dict_keys(['name', 'age', 'city']) (returns a view of the keys in the dictionary)
print(a.values()) # Output: dict_values(['Alice', 30, 'New York']) (returns a view of the values in the dictionary)
print(a.items()) # Output: dict_items([('name', 'Alice'), ('age',

b={
    "name": "Bob",
    "age": 25,
    "city": "Los Angeles"
}
a.update(b) # Updates the dictionary a with the key-value pairs from dictionary b
print(a) # Output: {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'} (the values for the keys in a are updated with the values from b)


c={
    "name": "Charlie",
    "age": 35,
    "number": 1234567890,
   
}
print(c.get("name")) # Output: Charlie (returns the value associated with the key "name")

item1= {
    "sugar": "1kg",
    "weight":2,
    "price":99.9
}

item2={
    "banana":"1kg",
    "weight":85,
    "price":100
}

items=[item1,item2]
print(items)

print(f"Total weight: {item1['weight']+item2['weight']} kg") # Output: Total weight: 87 kg (calculates the total weight of the two items)
print(f"Total price: {item1['price']+item2['price']}") # Output: Total price: 199.9 (calculates the total price of the two items)