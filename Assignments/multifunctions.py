class multiFunctions():
    def Subfields():
        data_list = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        print("Sub-fields in AI are:")
        for item in data_list:
            print(item)     

    def OddEven():
        num = int(input("Enter the number:"))
        if ((num%2) == 1):
            print("Odd Number")
            message = "Odd Number"
        else:
            print("Even Number")
            message = "Even Number"
    
        return message      

    def Elegible():
        gender=input("Your Gender: ")
        age=int(input("Your Age: "))
        if gender.lower() == 'male':
            if age >= 21:
                return "Eligible for marriage."
            else:
                return "NOT ELIGIBLE"
        elif gender.lower() == 'female':
            if age >= 18:
                return "Eligible for marriage."
            else:
                return "NOT ELIGIBLE"
        else:
            return "Invalid gender input. Please specify 'male' or 'female'."  

    def percentage():
        S1=float(input("Subject1: "))
        S2=float(input("Subject2: "))
        S3=float(input("Subject3: "))
        S4=float(input("Subject4: "))
        S5=float(input("Subject5: "))
    
        total_marks = S1+S2+S3+S4+S5
        print("Totel: ",total_marks)
    
        percentage = (total_marks / 5)
        print("Percentage : ",percentage)

    def triangle ():
        h=float(input("Height: "))
        b=float(input("Breadth: "))
        
        areaformula = (h*b)/2
        print("Area of Triangle: ", areaformula)
        
        h1=float(input("Height1: "))
        h2=float(input("Height2: "))
        b1=float(input("Breadth:: "))
    
        perimeterformula = h1+h2+b1
        print("Perimeter of Triangle: ", perimeterformula)
