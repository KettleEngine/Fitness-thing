import datetime, re

class Main():

    def __init__(self):
        
        self.getPersonalData()
        self.getPhysicalData()

        self.formatData()

    def getPersonalData(self):

        name = input("Full Name: ")

        DOB = self.getDOB()

        #while loops are to ensure that a valid email is being entered
        while True:
            email = input("What is your Email: ")
            if self.is_valid_email(email):
                break
            else:
                print("this is not a valid email format, please check the email")
        
        phoneNum = str(input("what is your prefered phone number to be called on: "))

        longTermGoal = input("What is your long term goal: ")

        while True:
            try:
                print("""
please select an option between 1 to 4 

1: Fat loss
2: Muscel gian
3: Lifestyle change
4: other
""")
                goalInput = int(input("option: "))

                if goalInput >= 1 and goalInput <=4:

                    match goalInput:

                        case 1:
                            goal = "Fat loss"

                        case 2:
                            goal = "Muscel gian"

                        case 3:
                            goal = "Lifestyle change"

                        case 4:
                            goal = input("other: ")

                    break
                else:
                    print("please enter a whole number between 1 and 4")
            except:
                print("please enter a whole number between 1 and 4")

        while True:
            try:
                print("""

Which Package are you interested in?
                      
1: Lifestyle Package
2: Advanced Package
""")
                packageChoice = int(input("package: "))

                if packageChoice == 1:
                    package = "Lifestyle Package"
                    break
                elif packageChoice == 2:
                    package = "Advanced Package"
                    break
                else:
                    print("please select a valid package, either enter 1 or 2")

            except:
                print("please select a valid package, either enter 1 or 2")

        planStart = input("When are you planning to start your plan: ")

        expectations = input("What do you expect from me as a coach: ")

        workingHours = input("what days and hours do you work: ")

        workingBreaks = input("what breaks do you get at work: ")
        
        self.personalData = {
            "name": name,
            "dateOfBirth": DOB,
            "email": email,
            "phone": phoneNum,
            "longTermGoal": longTermGoal,
            "package": package,
            "planStart": planStart,
            "expectations": expectations,
            "workingHours": workingHours,
            "workingBreaks":workingBreaks,
        }

    def getDOB(self):
        while True:
            print("When where you born?")

            while True:
                try:
                    year = int(input("Year: "))
                    now = datetime. datetime.now()
                    maxYear = int(now.year)
                    if year <= 1900 or year > maxYear:
                        print("please input a valid year, for example 2003")
                    else:
                        break
                except:
                    print("Please enter a valid number")

            while True:
                try:
                    month = int(input("Month: "))
                    if month > 12 or month < 1:
                        print("Please enter a valid month")
                    else:
                        break
                except:
                    print("Please enter a valid number")

            while True:
                try:
                    day = int(input("Day: "))
                    #if this fails then i know that the day was incorect regardless of the month as the datetime library will handle all of that calender stuff
                    self.DOB = datetime.datetime(year, month, day)

                    break

                except:
                    print("looks like that is not a valid day for that month, please try again.")

            break
        
    #calculates the age of the user so the user dosnt have to enter it
    def calculateAge(self):
        currentTime = datetime.datetime.now()
        
        diff = (currentTime - self.DOB) // 365

        age = diff.days
        
        return age

    def is_valid_email(self, email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.match(pattern, email):
            return True
        return False

    def getPhysicalData(self):
        
        #while loop is here to ensure the data is entered otherwise the program will just skip the entry of that peice of data
        while True:
            #try statments so if the user inputs something that is not valid the program will not crash
            try:
                weight = float(input("What is your weight in Kg: "))
                break
            except:
                print("Looks like you put in the weight wrong, please use numbers")

        while True:
            try:
                height = float(input("What is your height in cm: "))
                break
            except:
                print("looks like you put the hight value in wrong, please use numbers")

            
        age = self.calculateAge()
    

        gender = input("are you Male or Female: ")

        while True:
            try:
                print("""
on a scale of 1 to 5 how active are you per week?

1: inactive, little to no excercise 
2: light, exercise 1 to 3 times a week
3: moderate, exercise 4 to 5 times a week
4: active, dayly or intensive exercise 3 to 4 times a week
5: very active, intense exercise 6 to 7 times a week
""")
                activitylevel = int(input("activity level: "))

                if activitylevel >= 1 and activitylevel <=5:
                    break
                else:
                    print("please enter a whole number between 1 and 5")
            except:
                print("please enter a whole number between 1 and 5")

        caloriesPerDay = self.caloryCalculator(weight, height, age, gender, activitylevel)

        self.physicalData = {
            "weight": weight,
            "height": height,
            "age": age,
            "gender": gender,
            "calories": caloriesPerDay
        }

    #calculates the inital calory requirments
    def caloryCalculator(self, weight, height, age, gender, activity=1):

        if gender == "male":
            BMR = 13.397*weight + 4.799*height - 5.677*age + 88.362
        else:
            BMR = 9.24*weight + 3.098*height - 4.330*age + 447.593

        #this next bit of code to to do the activity modifyers to the BMR

        match activity:

            case 1:
                BMR = BMR * 1.2
            
            case 2:
                BMR = BMR * 1.375

            case 3:
                BMR = BMR * 1.55

            case 4:
                BMR = BMR * 1.725

            case 5:
                BMR = BMR * 1.9

        BMR = round(BMR, 3)
        print(BMR)
        return BMR

    def formatData(self):

        self.clientData = {
            "personalData": self.personalData,
            "physicalData": self.physicalData           
        }

main = Main()