#PROGRAM TO REVERSE THE LIST GIVEN BY USER
"""
INPUT:[2,3,4,5]
OUTPUT:[5,4,3,2]
HERE WE HAVE TO DO IN THREE METHODS
"""
"""
BLUEPRINT:
FIRST METHID: RVERSE THE LIST FROM REVRSE FUNCTION
SECOND:LIST[::-1]
THIRD:TO SWAP THE LAST PLACE TO FIRST ONE , 
"""
print("THIS IS THE PROGRAM TO REVRSE THE LIST IN THREE WAYS\n")
print("PLEASE ENTER THE LIST BASED ON YOUR PREFERENCE\n")
food=list(map(int,input().split(",")))
food.reverse()
print(food)
food.reverse()
print(food[::-1])
food.reverse()
for i in range(len(food)):
    food[-i-1]
print(food)
food.reverse()
#for i in range(len(food/2)):
#    food[i],food[len(food)-i-1]=food[len(food)-i-1],food[i]
#print(food)
