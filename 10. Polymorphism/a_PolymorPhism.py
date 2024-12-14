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


#Create and Instance of Teacher Author class and access the mentioned methods

# What will happen if both class have same method profile() and you call it through TeacherA object?