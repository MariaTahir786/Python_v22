#lists 
#array holds constant value if its string rest of items will also be string
shopping_list=["milk","bun","seeds","books"]
shopping_list[2]="pens"
print(shopping_list)
# access the drawer with index of 0 and print value
drawers = ["documents", "envelopes", "pens"]
print(drawers[0]) #prints documents
# access the drawer with index of 1 and print value

drawers[0] = "tchotchkes"
print(drawers)  # prints ["tchotchkes", "envelopes", "pens"]
# stores the value "tchotchkes" in a temporary variable.
top_contents = drawers[0]

# Replaces the value at index 1
# with whatever value is stored at index 0
drawers[1] = drawers[0]
print(drawers) # prints ["tchotchkes", "tchotchkes", "pens"]
################
#when we assign value get assigned from right to left side side


######
#append ,it will add the value at the end of list
#######
car_list=["Toyota","Honda","Ford","Chevy","BMW","Ford"]
# car_list.append("Mercedes Benz")
# print(car_list)

#####
#remove
#####
# car_list.remove("BMW")#it will remove first occurance
# print(car_list)

######
#delete 
# del car_list[1]
# print(car_list)

#######
#slicing
#syntex [:] we want copy of list ,array or we want to get portion of list/arraystart indx and ending idx should be separated by : strting idx is included and ending will be excluded
print(car_list[:])#will get whole copy
print(car_list[1:])
print(car_list[1:3])
print(car_list[0:5])

# copy of array 
original_array = [1, 2, 3, 4, 5]
copied_array = original_array[:]


#get length in python
print(len(car_list))

#Tuples
# mutable objects can be chand=ged onec created
# immutable can not be changed onec creadted we can create new truple with updated elements
#    access the value
my_tuple=(1,2,3,"Store",True)
print(my_tuple[2])
print(my_tuple[3])

#add an element in tuple middle of it 
# create new tuple with updated element
# Corrected slicing to update the third element
new_tuple = my_tuple[:2] + ("world",) + my_tuple[3:]

print(new_tuple)



