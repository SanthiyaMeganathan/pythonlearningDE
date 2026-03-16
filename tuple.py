#same as list but immutable.means no add,delet,upadte
trip_summary=("ubergo","chennai","airport",450,"completed")
print(trip_summary)

print(trip_summary[1])

for item in trip_summary:
    print(item)

print(len(trip_summary))

print(trip_summary.count("completed")) #t counts how many times compelete appears
print(trip_summary.index("airport"))

trip_summary[1]='karuru'

