
class Student():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.lessons = []
        self.grades = { "midterm":0 ,"final":0 ,"project":0 }        

    def welcomeStudent(self):
        print("Welcome",self.name)    
        
    def addLesson(self,new_lesson):
        print("Adding new lesson")
        self.lessons.append(new_lesson)

    def showInfo(self):
        print("{} {}".format(self.name,self.surname))
        print("student's lessons: ")
        for i in self.lessons:
              print(i)
student1 = list()
student1.append(Student("Merve", "Ayas"))
student1.append(Student("Aytaç", "Öztürk"))
student1.append(Student("Murat", "Akdeniz"))

all_lessons = ["Python", "AI", "ML", "NN", "DM"]

def percentage(grades):
    return (((30/100) * grades["midterm"]) + ((50/100) * grades["final"]) + ((20/100) * grades["project"]))

def search(name, surname):
    for i in range(len(student1)):
        if name == student1[i].name and surname == student1[i].surname :
            student1[i].welcomeStudent()
            return student1[i]
    return Student("-","-")    

def coursePass(grade):
    if grade >= 90:
        print("Your note is AA")
    elif 70 <= grade < 90:
        print("Your note is BB")
    elif 50 <= grade < 70:
        print("Your note is CC")
    elif 30 <= grade < 50:
        print("Your note is DD")
    else:
        print("Your note is FF. You are failed.")

for i in range(3):
    name = input("Please enter your name: ")
    surname = input("Please enter your surname: ")
    student = search(name,surname) 
    if name == student.name and surname == student.surname :
        enter = True
        break
if name != student.name or surname != student.surname :
    print("Please try again later.")
    enter = False

if enter == True:    
    for i in range(5):
        print("You have to take min: 3 max: 5 lessons {}".format(all_lessons)) 
        lesson = input("Enter the lesson name you want : ")
        if lesson != "" and lesson in all_lessons:
            all_lessons.remove(lesson)
            student.addLesson(lesson)
        else:
            print("The lesson that you choosed does not exist.")    
    student.showInfo()
    if len(student.lessons) < 3:
        print("You failed in class.")
    else:
        lesson = input("Enter the lesson for exam : ")
        if lesson not in student.lessons:
            print("It is not your lesson")
        else:
            coursePass(percentage(student.grades))
