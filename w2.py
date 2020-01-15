#list and tuples:
# tuples are ordered sequences
# written as comma-separated elements within parehteses
# 3 types of tuples:
#strings int and floats
tuple1=('disco', 10, 1.2)
print(tuple1[-1])
tuple2= tuple1 + ('hard rock', 10)
print(tuple2)
# this is called slicing variable[:2] because it returns only a slice from index 0 to 1 (excluding 2)

# tuples are immutable
ratings = (10,9,6,5,10,8,9,6,2)
ratingssorted= sorted(ratings)
print(ratingssorted)
print(ratings)

NT=(1,2,("pop", "rock"), (3,4), ("disco", (1,2)))
print(NT[2][0])
