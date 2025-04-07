# create a tuple with  different data typles
tuplex = (1 , 2.5 , "hello" , True)

print(tuplex)

# create a tuple
tuplex = (1 ,2 ,3 ,4 ,5)
print(tuplex)

# tuples are immutablee , so you cannot chate its values
# using merge tuple with oprator + , you can add new tuple to existing one

tuplex = tuplex + (9,)
print(tuplex)

# count the number of time value repeats in tuple
tuplex = (1 ,2 ,3 ,4 ,5, 1,)
print(tuplex.count(1))#counting 1

# use [start:stop] to slice the tuple
tuplex = (1,3,3,4,5,6)
print(tuplex[1:4])

# start index not defined

print(tuplex[:4])