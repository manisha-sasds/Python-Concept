# Sets in Python- From Basics to Advanced Operations
# A set is a collection which is unordered, unchangeable*, and unindexed.

print ("\n----------------- 1. Firts way to Creating a set -----------------")

# 1.1 a Set of Integers
int_set = {1, 2, 3, 4, 5}
print("\nSet of integers:", int_set)

# 1.2 a Set of Strings
str_set = {"apple", "banana", "cherry", "date"}
print("\nSet of strings:", str_set)

# 1.3 a Mixed Set
mixed_set = {1, "hello", 3.14, True}
print("\nMixed set:", mixed_set)
# Note: True is treated as 1 → {1, 'hello', 3.14}

#1.4 Nested Sets (using frozenset because normal sets can't contain lists or sets)
nested_set = {1, 2, frozenset({3, 4}), frozenset({5, 6})}
print("\nNested set using frozenset:", nested_set)

# 1.5 Nested Mixed Set Example
nested_mixed_set = {
    frozenset({54, 87, 99}),
    frozenset({'Banana', 'Mango', 'Orange'}),
    frozenset({23.4, 67.8, 90.1}),
    frozenset({'age', 25, 'height', 5.7})
}
print("\n Nested Mixed Set (immutable inner sets):", nested_mixed_set)
   
print ("\n-----------------  Second way to Creating a  set in python set() constructor function -----------------")

# From Tuple
set_from_tuple = set((1, 2, 3))
print("\n Created Set from Tuple:", set_from_tuple)

# From String
set_from_string = set("hello")
print("\n Created Set from String:", set_from_string) # Each character becomes an element -> {'h', 'e', 'l', 'o'}

# From List
set_from_list = set(["apple", "banana", "apple", "grape"])
print("\n Created Set from List (duplicates removed):", set_from_list)  

print ("\n----------------- 2. How to access Set Elements -----------------")
# Sets are unordered and unindexed, so you cannot access elements by index.
print ("\n----------------- 2.1  Access Set Elements using a loop. -----------------")

# print("\n set_int " ,set_int[2]) # TypeError: 'set' object is not subscriptable
print("\n Iterating through int_set:")
for item in int_set:
    print(item, end=' ')    
print("\n\n Iterating through str_set:")
for item in str_set:
    print(item, end=' ')

print ("\n----------------- 2.2 Access Set Elements indirectly -----------------")

print("\n Is 3 in int_set?", 3 in int_set) # True
print("\n Is 'banana' in str_set?", "banana" in str_set) # True

print ("\n----------------- 2.3 Access Set Elements by converting set to listfor indexig -----------------")
# Sets are unordered and unindexed, so you cannot slice them so convert set to list.
int_set_list = list(int_set)
print("\n First element of int_set:", int_set_list[0])  # Accessing first element
str_set_list = list(str_set)
print("\n Second element of str_set:", str_set_list[1])  # Accessing second element




print ("\n----------------- 4. Python - Add Items to a set using methods like add(), update()-----------------")
print("\t   -----------------4.1 Add one items at the end of a set using methods like add()-----------------")

int_set.add(126)
print("\n\t After adding :", int_set) # only one item can be added

str_set.add("watermelon")
print("\n\t After adding:", str_set) 

mixed_set.add("Monika")
print("\n\t After adding:", mixed_set)


print("\t   -----------------4.2 Add Adds multiple elements from any iterable set using methods like add()-----------------")

int_set.update([99, 100, 101])
print("\n\t  int set after update:", int_set)  # multiple items can be added

str_set.update("grapes")  # adding characters from string
print("\n\t str set after update:", str_set)

mixed_set.update((2.17, False, "world"))
print("\n\t mixed set after update:", mixed_set)

print ("\n----------------- 5. Python - Remove Items from a set using methods like remove(),discard(), pop(), and clear(). -----------------")
print("\t   -----------------Remove items from a set using methods like remove()-----------------")

set_one= {'BMW','Audi','Benz','Tata','Ford','Benz','Honda','Hyundai'}
set_one.remove('Benz')  # Remove first occurrence of "Benz"
print("\n\t  After remove 'Benz':", set_one)

print("\t   -----------------Remove items from a set using methods like discard()-----------------")
set_one.discard('Tata')  # Remove "Tata", no error if not found
print("\n\t After discard 'Tata':", set_one)


print("\t   -----------------Remove an random items from a set using methods like pop()-----------------")
set_one.pop()  
print("\n\t After pop :", set_one)

print("\t   -----------------Remove all items from a set using methods like clear()-----------------")
set_one.clear() 
print("\n\t After clear:", set_one)



print ("\n----------------- 6. Python - Joins on set  -----------------")
# Different methids are there to join two or more sets in python
print("\t   -----------------6.1  Union of two sets using union() method-----------------")
set_a = {1, 2, 3}
set_b = {"Jhon", "MEENA", "Aandy"}
union_set = set_a.union(set_b) # union returmn new set
print("\n\t Union of set_a and set_b:", union_set)  
print("\n\t Original set_a remains unchanged:", set_a)
print("\n\t Original set_b remains unchanged:", set_b)  


set_c = [12.34, 345.4, 56.78,78.98]
set_d = ('USA', 'India', 'UK')
muiltiple_union_set = set_a.union(set_b,set_c,set_d) # union returmn new set
print("\n\t muiltiple_union_set of set_c, set_a, set_d, set_b:", muiltiple_union_set)  

    
print("\t   -----------------6.2 Update set using update() method-----------------")


set_a.update(set_b)
print("\n\t set_a after update with set_b:", set_a)  
print("\n\t Original set_b remains unchanged:", set_b)      

print("\t   -----------------6.3  Intersection of two sets using intersection() method return commaon item in both set-----------------")

set_d = {'USA', 'India', 'UK', 'Germany'}
set_e = {'India', 'Germany', 'France'}
intersection_set = set_d.intersection(set_e) # intersection returmn new set
print("\n\t Intersection of set_d and set_e:", intersection_set)

print("\t   -----------------6.3  Intersection of two sets using intersection_update() method -----------------")
# intersection_update updates the original set with common items in both sets and wolln not create new set
set_d.intersection_update(set_e)
print("\n\t set_d after intersection_update with set_e:", set_d)  
print("\n\t Original set_e remains unchanged:", set_e)      
print("\t   -----------------6.4  Difference of two sets using difference() method-----------------")
set_f = {111, 112, 113, 4, 5,6}
set_g = {4, 5,6, 666, 777, 888}
difference_set = set_f.difference(set_g) # difference returmn new set
print("\n\t Difference of set_f and set_g (items in set_f not in set_g):", difference_set)      

print("\t   -----------------6.5  Difference of two sets using difference_update() method -----------------")
# difference_update updates the first set set_f by removing items found in the second set
set_f.difference_update(set_g)
print("\n\t ", set_f)  
print("\n\t Original set_g remains unchanged:", set_g)  


set_f = {111, 112, 113, 4, 5,6}
set_g = {4, 5,6, 666, 777, 888}

print("\t   -----------------6.6  Symmetric Difference of two sets using symmetric_difference() method-----------------")
set_f.symmetric_difference(set_g) # symmetric_difference returmn new set
sym_diff_set = set_f.symmetric_difference(set_g)
print("\n\t Symmetric Difference of set_f and set_g (items in either set but not in both):", sym_diff_set)  
print ("\n\t Original set_f remains unchanged:", set_f)
print("\t   -----------------6.7  Symmetric Difference of two sets using symmetric_difference_update() method -----------------")
# symmetric_difference_update updates the first set with items not common to both sets
set_f.symmetric_difference_update(set_g)
print("\n\t set_f after symmetric_difference_update with set_g:", set_f)  


print ("\n----------------- 7. Python - Frozenset on set -----------------")
# A frozenset is an immutable version of a set, meaning its elements cannot be changed after creation.
# Frozensets are hashable and can be used as keys in dictionaries or elements of other sets.    
frozen_set_one = frozenset([111, 222, 333,444, 555])
print("\n\t Frozen set a:", frozen_set_one)       
frozen_set_two = frozenset(["mango", "banana", "cherry","fig"])
print("\n\t Frozen set b:", frozen_set_two)
 