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
uber_city.add("karur")
print("newly add:", uber_city )
uber_city.remove("chennai")
print("removed", uber_city)

#impossible to get anything  by index. and cannot update directly , u need to remove and add
#print(uber_city[1])
#uber_city.remove("uber")
#it will cause erroe when you try to remove something that is not there
# to overcome with the discard.

uber_city.discard("jharkand")

