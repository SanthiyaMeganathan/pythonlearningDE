#set , here indexing is not possible and duplicate values are not allowed
#you cannot update
my_set={1,2,3,4,5,5}

print(my_set) #it will give only one 5 because duplicate values are not allowed

#union

uber_city={"chennai","bangalore","hyderabad"}
uber_city2={"mumbai","chennai","goa"}

union_uber_city=uber_city.union(uber_city2)
print(union_uber_city)
intersection_uber=uber_city.intersection(uber_city2)
print("intersection",intersection_uber)
diff_union=uber_city2.difference(uber_city)
print(diff_union)

