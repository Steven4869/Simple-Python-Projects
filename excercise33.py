class Student:
    pass
class Marks:
    pass
student1 = Student()
marks1 = Marks()
print("To check whether they are instances of class or not")
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks))
print(isinstance(student1, Marks))
print("\n To check whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))
