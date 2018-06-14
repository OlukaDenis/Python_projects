class Parent():
    def __init__(self, first_name, last_name, tel_no, eye_color):
        print("The parent has been called")
        self.first_name = first_name
        self.last_name = last_name
        self.tel_no = tel_no
        self.eye_color = eye_color

    def show_info(self):
        print("Last name: " +self.last_name)
        print("First name: " +self.first_name)
        print("Telephone number: " +str(self.tel_no))#converting figures to string
        print("Eye color: " +self.eye_color)
        
class Child(Parent):#inheritance
    def __init__(self,first_name, last_name, tel_no, eye_color, height, school):
        print("The child has been called")
        Parent.__init__(self,first_name, last_name,tel_no, eye_color)
        self.height = height
        self.school = school
        
        #method overriding
    def show_info(self):
        print("\nLast name: " +self.last_name)
        print("First name: " +self.first_name)
        print("Telephone number: " +str(self.tel_no))
        print("Eye color: " +self.eye_color)
        print("Height: " +str(self.height))
        print("School: " +self.school)
        
daddy = Parent("Michael", "Aloikin", 779275749, "Black")
daddy.show_info()
son = Child("Denis", "Aloikin", 773047940, "Black",  56 ,"Ndejje University")
son.show_info()
