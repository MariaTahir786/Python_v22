"""
program taht use a loop to calculate the sum of all numbers from 1to 100
"""
total=0
for i in range(1,100):
    print(i)
    total +=i
print(total)


"""
program taht uctreate a list of squares of numbers fron 1-20
"""

square_num=[]
for i in range(1,21):
    square_num.append(i**2)
print(square_num)

"""
define a function that uses a loop to generate a list of even numbers from 2 upto a given number n
"""

def even_numbers(n):
    even_num = []
    for i in range(2, n + 1):
        if i % 2 == 0:
            even_num.append(i)
    return even_num
n = 16
EvenNo = even_numbers(n)
print("Even numbers from 2 to", n, ":", EvenNo)

"""
write a progran that classifies student grades into categories
90 and above :"excellent"
70 to 89" Good
50 to 69:"average
below 50: fail

"""
def grade_classification(grade):
    if grade>= 90 and grade <=100:
        print("Excellent")
        
    elif grade>= 70 and grade <=89:
        print("Good")
        
    elif grade>= 50 and grade <=69:
        print("average")
        
    elif grade<= 50 and grade >=0:
        print("fail")
        
grade_classification(90)
   
   
   
# def grade_classification(grade):
#     if grade >= 90 and grade <= 100:
#         return "Excellent"
        
#     elif grade >= 70 and grade <= 89:
#         return "Good"
        
#     elif grade >= 50 and grade <= 69:
#         return "Average"
        
#     elif grade >= 0 and grade <= 50:
#         return "Fail"
        
# grade_assigned = grade_classification(76)
# print("Grade assigned is", grade_assigned)