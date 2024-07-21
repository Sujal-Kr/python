set={1,2,3,4}


# Define sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union (+): Combines unique elements from both sets
union_set = set1 + set2  # This will raise a TypeError, as '+' operator is not defined for sets

# Difference (-): Returns elements that are in the first set but not in the second set
difference_set = set1 - set2
# This will result in {1, 2, 3}, as elements 4 and 5 are present in both sets

# Intersection (&): Returns elements that are common to both sets
intersection_set = set1 & set2
# This will result in {4, 5}, as these elements are present in both sets

# Output

print("Difference:", difference_set)
print("Intersection:", intersection_set)



set3={8,9,10,11,11}
print(set3)