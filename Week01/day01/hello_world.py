print("Hello World!")
#data types
x="Hello World again"
print(x)

y=45
print(y)

like_chocolate=True
print(like_chocolate)


#python syntax 
# indentation is very important in python

x=10
if x > 50:
    print("Bigger than 50")
else:
    print("smaller than 50")


    if x<25:
        print("x is greater than 5")
    else:
        pass
    #pass means we do not have anything to pass here and this wont give any error
    print("Here")

#if we want to check the data type of any variable we use "type"
    print(type(x))

    # String literal/concatenate

    first_name= "Fred"
    last_name= "Flinstone"
    print(first_name + " " + last_name)

    #comma after string comma creates a white space after string
    full_name=first_name + " " + last_name
    print("My name is ", full_name )
    print("My name is  "+ full_name )
    

    #type cast
    total=35
    user_val="26"
    #total=total+user_val

    #we get type error if we + string and int so convert 
    total = total + int(user_val)
    print(total)

    new_total=str(total) + user_val
    print(new_total)

    print(f"My name is  {first_name} {last_name}")#notice f here and place holder will do the concatenation

#string built in functions
lower_case="hello world"
print(lower_case.upper())
upper_case="HELLO WORLD"
print(upper_case.lower())
print(lower_case.count('l'))
print(lower_case.count('o'))