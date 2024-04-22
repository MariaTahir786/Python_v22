class User_hw:
    def __init__(self,first_name, last_name,email,age,is_reward_member=False,gold_points=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_reward_member = is_reward_member
        self.gold_points = gold_points 
    # Display info  
    def display_info(self):
        return f"\nFirst Name: {self.first_name} \nLast Name: {self.last_name} \nEmail {self.email}   \nAge :{self.age} \nIs reward member : {self.is_reward_member} \nGold points :{self.gold_points}"
    # ?Enroll
    def enroll(self):
     if self.is_reward_member == True:
         print("User already a member")
         self.is_reward_member = False
     else:
         self.is_reward_member = True
         self.gold_points=950
         
     
    #  ?Points deduction
    def spend_points(self, amount):
        if self.is_reward_member:
            if self.gold_points >= amount:
                self.gold_points -= amount
                print("Points applied successfully!")
                print(self.display_info())
            else:
                print("Insufficient points!")
        else:
            print("User is not a reward member and cannot spend points")

     
print("------------------------------------------------")

print("User1  ====> information")
User1=User_hw("Sara","Kabuo","abc@gamil.com",20)
print("User 1 before enrollment")
print(User1.display_info())
# after enrollment
User1.enroll()
print("User1 after enrollment")
User1.spend_points(50)
print(f"User1 \n {User1.display_info()}")

print("------------------------------------------------")

print("User2 ====> information")
User2=User_hw("Saba","Tariq","Dem@gmail.com",35)
User2.enroll()
User2.gold_points=500
User2.spend_points(400)
print(f"User2 \n {User2.display_info()}")        
     
print("------------------------------------------------")
print("User3 ====> information")
User3=User_hw("Zubia","Ali","zubi@hotmail.com",56)
User3.enroll()
User3.gold_points=200
User3.spend_points(300)
print(f"User3 \n {User3.display_info()}")