#dict wont allow the duplicate:

trip = {
    "trip_id":"Ub1234",
    #you can have multiple value for sigle key and you can also access anything in that using the index.
    "pick_up":["chennai airport","medvakkam","thambharam"],
    "drop":"central railwaystation",
    "fare":450.89,
    "driver":"suresh",
    "status":"Completed",
    "trip_id":"1234"
}

#access
print(trip["pick_up"])
print(trip.get("chennai")) #safe way , if no key prints none

print(trip.keys())
print(trip.values())

for key,value in trip.items():
    print(key, ":" ,value)

#update: 
# if we are newly putting it , then it will get added, if we are putting the existing key then it will get updated

trip.update({"car_model":"swift"})
print(trip)
trip.update({"fare":500})
print(trip)

trip.pop("status") #it will remove the key and value and return the value

print(trip)

print("Trip id is entered twice , it will alwasy take the latest one.")
print(trip)

print("we are acessing the only one thing in the trip.")

print(trip["pick_up"][1])

for loc in trip["pick_up"]:
    print(loc)

#multuple dict in list  
#

print("learning to have a multiple lists")
 
trips=[
    {"trip_id":"ub1","pickup":"chennai","drop":"bangalore"},
    {"trip_id":"ub2","pickup":"covai","drop":"kk nagar"},
    {"trip_id":"ub3","pickup":"saidhapet","drop":"rs nagar"}
]

for trip in trips:
    print(trip)

for trip in trips:
    print(trip["trip_id"])   

#dict of dict


students={
    "student1":{"name":"gowtham","age":21,"edu":"cse"},
    "student2":{"name":"jeeva","age":22,"edu":"it"},
    "student3":{"name":"harith","age":19,"edu":"ece"},
    "student4":{"name":"vamshi","age":17,"edu":"csbs"}

}

print("student1 edu is ",students["student1"])

for stu_name ,age in students.items():
    print(stu_name, "age is" , age["age"])