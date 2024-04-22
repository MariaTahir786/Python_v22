#loops range can accept 3 arguments

# one argument
# for i in range(10):
    # print(i)
# two arguments will start print 2 until index 10 to 9
# for i in range(2,10):
#     print(i)
    
    
#     # three arguments ...3 will be added to i
#     print("printing 3 arguments")
#     for i in range(2,16,3): #2,5,8,11,14
#         print(i)
        
#         print("printing - arguments")
#     for i in range(16,3,-1): 
#         print(i)
        
        #iterating over lists
        # car_list=["Toyota","Honda","Ford","Chevy","BMW","Ford"]
        # for i in range(len(car_list)):
        #     print(car_list[i])
            
        #     # for each loop it will print all elements
        #     for i in car_list:
        #         print(i)
# for i in "String":
#     if i== "i":
#         print("This is ",i)
#     print(i)
    
# while loop
# loop whil ecertain condition is true
count= 0
while count<= 5:
    print("Looping -",count)
    count+=1
    
#     old_list = [3, 6, 8, 9, 2, 5, 6, 0, 1]
# new_list = []

# for num in old_list:
#     if num % 2 == 0:
#         new_list.append(num)

# print(new_list)  # Output: [6, 8, 2, 6, 0]

old_list = [3, 6, 8, 9, 2, 5, 6, 0, 1]
# new_list = [num for num in old_list if num % 2 == 0]
# print(new_list) 

new_list=[]
for num in old_list:
    if num % 2 == 0:
        new_list.append(num)
print(new_list) 

