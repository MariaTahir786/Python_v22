
s_list=["string","string2"]
s_tuples=["string","string2"]


# dictionaries
name='fred'
hair_color='Brown'
age='34'


fred={
    "name":"Fred",
    "hair_color":"brown",
    "age":34
    
}
# //nedted dictionary
user_list= [
    {"name":"Maria","hair_color":"brown", "age":40,"is_student":True},
    {"name":"Nera","hair_color":"black", "age":40,"is_student":True},
    {"name":"nuzuk","hair_color":"brown", "age":40,"is_student":True}
    ]
    
# print(user_list[0]["name"])
# print(user_list[3]["name"])

for i in range(len(user_list)):   
    # range is used for range
    print(user_list[i]["name"])
    # for each loop
    for each_person in user_list:
        print(each_person["age"])
        
        
        for each_person in user_list:
            for key in each_person.keys():
                print(each_person[key])
                

# user_1=  {"name":"Maria","hair_color":"brown", "age":40,"is_student":True,"email":""}
# if "email" not in user_1:
#     user_1["email"]="abc@gmail.com"
# else:
#     print("would you like to update email")
#     # user_1["email"]="abc@gmail.com"
# print(user_1)

def simple_function():
    print("hello world")
simple_function()

# function with parameter 
def display_message(message):
    print(message)
    display_message("hello maria")



# function with default parameter and nemd parameter 
def display_message(message,is_student=True):
    if(is_student):
        print(message.upper())
    else:
        print(message)
        
display_message("hello world",False)
    

def do_calculate(num_1,num_2):
    return num_1 +num_2
result = do_calculate(5,9)
print(do_calculate(result,11))


#   A simple calculator function that performs basic arithmetic operations.

#     Args:
#     operation (str): The operation to perform. It can be 'add', 'subtract', 'multiply', or 'divide'.
#     x (int): The first number.
#     y (int): The second number.

#     Returns:
#     float: The result of the arithmetic operation.

def calculator(operation,x,y):
    # lower or uppercase will disregard and convert to upper or lower case when user types 
    if operation.lower()== "add":  
        return x+y
    elif operation=="subtract":
        return x-y
    elif operation=="multiply":
        return x*y
    elif operation=="divide":
        return x/y
    else:
        return "Invalid operation"
    
calculate_add=calculator('add',5,3)
subtract=calculator('subtract',5,3)
multiply=calculator('multiply',5,3)
division=calculator('divide',16,4)

print("Addition result: ",calculate_add)
print("subtraction result: ",subtract)
print("multiplication result: ",multiply)
print("division",division)

items={
    "fruits":{
        "apples":{"quantity":3},
         "banana":{"quantity":4},
          "grapes":{"quantity":5}
    },
     "vegetables":{
        "ladyFinger":{"quantity":13},
         "potato":{"quantity":14},
          "onion":{"quantity":55}
    }
}
#  we can not use dot notation in pyrhon we call directly by key in an object to object
print("Banana",items["fruits"]["banana"])
    # 8787878
items["fruits"]["Mango"] ={"quantity":100}   
price=13<-90
print(items)
if price < 10:
    print("A")
elif price > 15 and price <22:
    print("B")
elif price < 20:
    print("C")
elif int(price / 2) == 22:
    print("D")
elif price < 30 and price % 2 ==0:
    print("E")
elif price > 19:
    print("F")
else:
    print("oops")