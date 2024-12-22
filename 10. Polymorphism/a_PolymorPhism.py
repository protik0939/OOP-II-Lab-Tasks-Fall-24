"""

Design the following code:

     _______________________
     |                     |
 2   |     Department      |
     |_____________________|
     |                     |
     |-- name              |
     |_____________________|
     |                     |
     |+ displayName()      |
     |_____________________|
               ^
               |
     _______________________                _______________________
     |                     |                |                     |
3    |      Teacher        |                |      Author         |
     |_____________________|                |_____________________|
     |                     |            2   |                     |
     |+ scheduleClass()    |                |+ writeArticle()     |
     |+ gradeStudent()     |                |+ publishBlog()      |
     |+ displayName()      |                |_____________________|
     |_____________________|                          ^
               ^                                      |
               |                                      |
               |                                      |
               |                                      |
               |        _______________________       |
               |        |                     |       |
               ---------|   TeachersAuthor    |--------
                        |_____________________|
                        |                     |
                    1   |                     |
                        |_____________________|

"""


# What is runtime polymorphism? give a code example

    # Runtime polymorphism occurs when a subclass provides a specific implementation
    # of a method that is already defined in the superclass. The method to call is 
    # determined at runtime based on the object's type.

        # Example of Runtime Polymorphism    
            # department = Department("Engineering")
            # teacher = Teacher("Maths")
            # author = Author("Literature")
            
            # department.displayName()
            # teacher.displayName()
            # author.displayName()



#Create and Instance of Teacher Author class and access the mentioned methods
class Department:
    def __init__(self, name):
        self.name = name

    def displayName(self):
        print(f"Department: {self.name}")


class Teacher(Department):
    def scheduleClass(self):
        print("Class has been scheduled.")

    def gradeStudent(self):
        print("Grading students.")

    def displayName(self):
        print("This is a Teacher.")


class Author(Department):
    def writeArticle(self):
        print("Writing an article.")

    def publishBlog(self):
        print("Blog published.")

    def displayName(self):
        print("This is an Author.")


class TeacherAuthor(Teacher, Author):
    def __init__(self, name):
        super().__init__(name)


# Example usage
ta = TeacherAuthor("Computer Science")
ta.displayName()  # Polymorphism in action
ta.scheduleClass()
ta.gradeStudent()
ta.writeArticle()
ta.publishBlog()


# What will happen if both class have same method profile() and you call it through TeacherA object?

    # If both Teacher and Author classes have a profile() method and 
    # you call it using a TeacherAuthor object, the method resolution 
    # order (MRO) determines which method is called. In this case, the 
    # Teacher class's profile() method will be called since it is the first parent class.