#attendance app that automatically takes student attendance
#how?
#Dream develop an app that uses AI to recognize student face.
#Get user data to recognize the user by an ID (password)
#Track arrival time with school schedule to decide if student is late.
#Student types in all the data.
#What data?

#Register Student
def studentRegistration():
    studentName = input("Enter your name")
    #Not a scalable approach, only one student or make 32 variable!!!

#Take attendance

def attendance():
    userInput = input ("What is your student ID?")
    #Check for random chars like - or . TOODO
    if userInput.isnumeric():
        userInput = int(userInput)
    else:
        print("Numbers only YO!")            
        attendance()


#Student Data
#Name
studentName = ""
#age or grade level
age = 0
#In class Present, Late, Not Present
attendance = ""
#Student ID
sid = 000
#Is the student late
#

isTakingAttendance = True

while isTakingAttendance:
    attendance()