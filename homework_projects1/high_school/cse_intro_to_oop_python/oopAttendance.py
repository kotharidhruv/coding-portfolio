#attendance app
#think about how
#--How do I verify they are there
#What data

#input for retrieving user
def attendance():
    id = input("Enter your user ID\n")
    #Todo, check in the list
    if id in roster:
        print("you're here")
        return False
        #mark them present in the data
    else:
        print("student not found")
        return True
    
def register():
    print("Welcome new user")
    newStudent = student()
    newStudent.uName = input("Please enter your name\n")
    student.addId( input("Please type your school ID Number\n")) # This needs to be generated, no two users can have the same ID!
    return newStudent


#store the user
class student:
#User ID int
    uid=0
#UserName String
    uName=""
#The time they showed up to class
    time=1.0

    def addId(num):
        if num.isnumeric():
            uid = int(num)
            #Should be a way to tell the user to retry


#Store data about the CS class
roster=[]


takingAttendance = True
while takingAttendance:
    if attendance():
        roster.append(register())
    