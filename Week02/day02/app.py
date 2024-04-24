from classes.student import Student
from classes.teacher import Teacher
from classes.human import Human

#create instance of student class 

john= Student("John",23,"Harvard University")
#get total number of people
print(Human.get_population())
print("\nTesting Student Class")
john.eat()
john.run()
john.sleep()
john.communicate("Hey, I am going to school" , "voice")
john.communicate("Hello, where are you going?")

maria=Teacher("Saba",34,"George Mason")
print(Human.get_population())
print("\nTesting Teacher Class")
maria.eat()
maria.run()
maria.work()
maria.sleep()
maria.teaching()

maria.communicate("Hey, Where are you going tooo?")