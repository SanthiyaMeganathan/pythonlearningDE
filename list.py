playlist=["shapeofyou","naa ready","believer"]
fav_food=["dosa","pizza","biriyai"]
recent_locations=["home","airport","work"]


#maintains order based on index
#it has can mulitiple datatypes
#it is mutable

print(playlist)
print(fav_food)
print(recent_locations)

playlist.append("come on come on")
print("playlist after the append" ,playlist)

playlist.insert(1,"lalalalala")
print("after insert",playlist)

playlist.remove("naa ready")
print("after remove",playlist)

playlist.pop()
print("after pop",playlist)

playlist.reverse()
print("after reverse",playlist)

#to know position

print(playlist.count("believer"))

#list slicing

print("top 2 songs",playlist[0:2])

#last 

print("last two location",recent_locations[-2:])


#listIteration
for food in fav_food:
    print("all food", food.title())

for song in playlist:
    print("song is ", song )   


#searching in the list:

if "dosaaa" in fav_food:
    print("yes")

#updating the things in the list

fav_food[2]="shawarma"
print(fav_food)

#mixed

mixed=["gowtham",33,155,True]

for a in mixed:
    print(a)

