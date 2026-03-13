driver_name="Gowtham"

print(driver_name.lower())
print(driver_name.upper())

mobile_number="1234567890"
masked=mobile_number[:2]+"******"+mobile_number[-2:]
print(masked)

#formating:

song_title="ShaPe oF yoU"
artist_name="Ed sheEren"

formatted=f"{song_title.title()} by {artist_name.title()}"
print(formatted)

#replacing

location = "chennai central"
fixed_location =location.replace("chennai central","ponneri")
print(fixed_location)

#

message ="Your uber booking id is: UB12345.Please keep it safe"
booking_id=message.split(":")[1].split(".")[0].strip()
#here we split things using what is inside the split , it can be anything

print(booking_id)

#when you know what to search for how to searc

promo_msg="Use code UBER20 to get 20% off on your next ride"

if "UBER20" in promo_msg:
    print("promo code is valid")


#to know the position of word
feedback="the driver was very friendly and the ride was comfortable"

print("Position is : ",(feedback.find("friendly")))

name="Santhiya Meganathan"
initials = "".join([word[0].lower() for word in name.split()])
print(initials)

dirty_input="   helo world     "
print(dirty_input)
clean=dirty_input.strip()
print(clean)

word1= "The trip was amazing and car is clean"
word_count=len(word1.split())
print(word_count)



