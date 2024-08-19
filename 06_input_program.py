# name = input('Enter your name')

# print('Hello', name)


person_A_name=input("Enter your name:")
person_A_age=input("Enter your age:")

person_B_name=input("Enter your name:")
person_B_age=input("Enter your age:")

if person_A_age>person_B_age:
    print(person_A_name, "is older than ",person_B_name)
else:
    print(person_B_name, "is younger than ", person_A_name)