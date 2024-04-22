#? else statement
#semi colon is very iomportant in if else
if 1==2:
    print("true")
else:
    print("not true")
    
    likes_chocolate=0 # we can use 0 or 1 as true or false here 
    if likes_chocolate :
        print("I like chocolates")
    else:
        print("I do not like chocolates")
        
        age=11
        name="Fred"
        if age<=12:
            print(f"{name} is a child")
        elif age<=19:
            print(f"{name} is a teen")
        else:
                print(f"{name} is a adult")
                
               #Modulous
        line_number = 6
        print(line_number % 3)
    if (line_number % 2 == 0):
        print("High light the line")
    else:
        print("Do not high light the line")
        
        #Write a Python program that classifies a given number into different categories.
# To classify the number into one of the following categories:
# If the number is even, print "The number [number] is even."
# If the number is odd, print "The number [number] is odd."
# If the number is zero, print "The number is zero."
# If the number is negative, print "The number [number] is negative."
number=-9
if number == 0:
        print("The number is zero.")
elif number % 2 == 0:
        print(f"The number {number} is even.")
else:
        print(f"The number {number} is odd.")
    
if number < 0:
        print(f"The number {number} is negative.")

    #another way 
if number == 0: 
    print("ZERO")
elif number > 0:
    if number % 2 ==0:
        print("EVEN")
    elif number % 2 == 1:
        print("ODD")
else: 
    print("NEGATIVE")
    
fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']
fruits_and_vegetables = "fruits_and_vegetables",fruits + vegetables
print(fruits_and_vegetables)
salad = 3 * vegetables
print(salad)
    
    
    #Lists 
drawers = ["documents", "envelopes", "pens"]

# access the drawer with index of 0 and print value
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


#and or
dessert="icer-Cream"
flavor="Starwberry"
if dessert=="icer-Cream" and flavor=="Starwberry":
    print("I will have ice Cream")
elif des=="cake" and (flavor=="chocolate" or flavor=="Strawberry"):
    print("I will have some cake")
else:
    print("No Dessert for you")
    