"""
Student Name:
Course, Year, and Section:
Quiz No.:
Date:
"""

student = {
    "studentName": "Lewis Fonsi",
    "studentAddress": "City of Candon, Ilocos Sur",
    "studentFavNum1": 25,
    "studentAge": 25,
    "studentAllowance": 500
}
#Declaring a python as float
student["studentAllowance"] = float(student.get("studentAllowance"))

classmate = {
    "classmateName": "Andrea Andres",
    "classmateAddress": "City of Vigan, locos Sur",
    "classmateFavNum1": "18",
    "classmateAge": "21",
    "classmateAllowance": "700"
}

nameLength = []

sName_Length = len(student.get('studentName')) #get the length of the studentName in dictionary
cName_Length = len(classmate.get('classmateName'))  #get the length of the classmateNam

nameLength.append(int(sName_Length))
nameLength.append(int(cName_Length))


def info():
    if "Ilocos Sur" in student['studentAddress'] and classmate['classmateAddress']:
        print(student['studentName'].upper(), "is from", student['studentAddress'],) #Output: LEWIS FONS! is from City of Candon, !locos Sur - call and format your variables with concatenation techniques except fstring formatter
        print(classmate['classmateName'].lower(), "is from", classmate['classmateAddress']) #Output: andrea andres is from City of Vigan,Ilocos Sur - call and format your variables with concatenation techniques except fstring formatter
        if nameLength[0] > nameLength[1]:
            print(classmate['classmateName'].lower(), "has a longer name than", student['studentName'].upper(), "with", nameLength[1], "letters over", nameLength[0], "letters")
        else:
            print(student['studentName'].upper(), "has a shorter name than", classmate['classmateName'].lower(), "with", nameLength[0], "letters over",nameLength[1], "letters")
    
    elif "Ilocos Sur" in student['studentAddress'] and classmate['classmateAddress']:
        sName_Split = student.get('studentName').split(" ")
        cName_Split = classmate.get('classmateName').split(" ")
        print("One among", {sName_Split[-2]}, "or", {cName_Split[-2]}, "lives in Ilocos Sur")

    else:
        print("None of the Student live in ilocos Sur")
    print(f"The added age of {student['studentName']} and {classmate['classmateName']} is {int(student.get("studentAge")) + int(classmate.get('classmateAge'))}")  #print using the fstring format: the added age of studentAge and classmateAge, in addition to perform a mathematical
                                                                                                        #Output: "The added age of Lewis Fonsi and Andrea Andres is 43" The output is not 43 and instead 46.
    print(f"The subtracted value of favenum of {student['studentName']} and {classmate['classmateName']} is {int(student.get("studentFavNum1")) - int(classmate.get('classmateFavNum1'))}")

info()

combinedWeeklyAllowance = student["studentAllowance"] + float(classmate.get("classmateAllowance"))
print(f"The weekly allowance of {student['studentName']} and {classmate['classmateName']} is {(combinedWeeklyAllowance):.2f} pesos")

studentNameList = student.get('studentName')
classmateNameList = classmate.get('classmateName')

studentAddressList = student.get('studentAddress')
classmateAddressList = classmate.get('classmateAddress')


classList = [studentNameList, classmateNameList]
classList_Ext = [studentAddressList, classmateAddressList]


classList_Ext.extend(classList)

for classListInfoName in classList:
    print(classListInfoName)

classNumbers = [int(student.get("studentFavNum1")), int(student.get("studentAge")), int(student.get('studentAllowance'))]
classNumbers.append(int(classmate.get('classmateAge')))
classNumbers.append(int(classmate.get('classmateAllowance')))
classNumbers.sort(reverse=True) #Reverse the sort

for classListInfo in classNumbers:
    print(classListInfo)

def quizTwo(studentNameCS):
    print(f"Congratulations on Quiz 2 {studentNameCS}")

userFirstName = input("Please input your name: ")
quizTwo(userFirstName)