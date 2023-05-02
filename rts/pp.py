# while True:
#     s = input('enter the string ')
#     t = s[::-1]
#     print("youre reversed string is ,=" , t)
#
#     if s == t:
#         print("entered string is palandrome")
#         break
#
#     else:
#         print("NOT PALANDROME")
#
#
#
#
# class s:
#     def test(self):
#         print("af")

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


# Create two instances of the Person class
person1 = Person("Alice", 25, "female")
person2 = Person("Bob", 30, "male")



# Access properties of the instances
print(person1.name)  # Output: Alice
print(person2.name)  # Output: 30

# # Call methods of the instances
# person1.eat()  # Output: Alice is eating.
# person2.sleep()  # Output: Bob is sleeping.
# person1.sleep()




