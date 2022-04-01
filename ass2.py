class Person:
    def _init_(self,name,last_name,birth_date):
        self.name = name 
        self.last_name = last_name
        self.birth_date = birth_date
    def get_age(self,age):
        self.age = age
    def can_vote(self):
        if(self.age>18):
            return True
        else:
            return False

    def display(self):
         print(f"Name :{self.name}")
         print(f"Last Name :{self.last_name}")
         print(f"Date of birth :{self.birth_date}")

obj = Person("Bob","Dylan","may 24, 1941")
obj.display()
obj.get_age(34)
print(obj.can_vote())