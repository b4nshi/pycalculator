n = input("Please enter your name:")
print("****************************************************")
print("                  welcome",n)
print("****************************************************")
choice = int (input("What do you want to do\n1.Age Calculate\n2.Height Calculate\n3.Time\n4.Numerical Calculation\n5.Temperature calculate\n6.Length "
                    "calculate\n7.Weight\n8.Discount\n"))
if choice == 1:
    import datetime
    birth_year = int(input("Enter tour birth year: "))
    y = datetime.datetime.now().year-birth_year
    birth_month = int(input("Enter your birth month: "))
    m = 12-birth_month
    birth_day = int(input("Enter your birth day: "))
    d = 30-birth_day
    print(n,"You are",y,"years",m,"months",d,"days old: ")


elif choice == 2:
    choice =int(input("1.Calculate your height in CM\n2.Calculate your height in Inches\n"))
    if choice == 1:
            ft = float(input("Enter your height in Feet:"))
            cm = round((ft*30.48),1)
            print("Your height is",cm,"cm")
    elif choice ==2:
            cm = int(input("Enter your Height in CM: "))
            ft = 0.0328*cm
            print("Your height is:",round(ft,2),"Feet")


elif choice == 3:
    choice = (int(input("1.Hour to Minute\n2.Hour to Second\n3.Minute to Second\n4.Minute to Hour\n5.Second to Minute\n6.Second to Hour\n")))
    if choice == 1:
       Hr = int(input("Enter the Hour: "))
       Min = Hr * 60
       print(Hr,"Hour = ",Min,"Minutes.")
    elif choice == 2:
        Hr = int(input("Enter the Hour: "))
        Sec = Hr* 3600
        print(Hr, "Hour = ", Sec,"Seconds.")
    elif choice == 3:
        Min = int(input("Enter the Minutes: "))
        Sec = Min* 60
        print(Min, "Minutes = ", Sec,"Seconds.")
    elif choice == 4:
        Min = int(input("Enter the Minutes: "))
        Hr=Min/ 60
        print(Min, "Minutes = ", Hr,"Hour.")
    elif choice == 5:
        Sec = int(input("Enter the Seconds: "))
        Min =Sec/ 60
        print(Sec, "Second = ", Min,"Minute.")
        Sec = int(input("Enter the Second: "))
        Hr =Sec/ 3600
        print(Sec, "Second = ", Hr,"Hour.")


elif choice == 4:
    print("Enter the 1st no:=")
    n1 = input()
    print("Enter the 2nd no:=")
    n2 = input()
    choice =(int(input("Choose which calculation you want to do-\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Remainder\n")))
    if choice == 1:
        a1 = (float(n1) +float(n2))
        print("Your ans is:",n1,"+",n2,"=", a1)
    elif choice == 2:
        a2 = (float(n1) - float(n2))
        print("Your ans is:",n1, "-", n2, "=", a2)
    elif choice==3:
        a3 = (float(n1) * float(n2))
        print("Your ans is:",n1, "*", n2, "=", a3)
    elif choice==4:
        a4 = (float(n1) / float(n2))
        print("Your ans is:",n1, "/", n2, "=", a4)
    elif choice == 5:
        a5 = (float(n1) % float(n2))
        print("Your ans is:",n1, "%", n2, "=", a5)


elif choice == 5:
    choice= (int (input("1.Celsius to Fahrenheit:\n2.Fahrenheit to Celsius:\n")))
    if choice == 1:
        C = int(input("Enter the temperature in Celsius:"))
        F = (C*1.8)+32
        print(C,"degree celsius=",F,"degree fahrenheit.")
    elif choice == 2:
        F =int(input( "Enter the temperature in fahrenheit:"))
        C = (F-32)*1/1.8
        print(F,"degree fahrenheit=",C,"degree celsius.")


elif choice ==6:
    choice =(int(input("1.Feet to CM\n2.CM to feet\n")))
    if choice == 1:
        ft = float(input("Feet: "))
        cm = round((ft * 30.48), 2)
        print(ft,"Feet =", cm, "cm")
    elif choice == 2:
        cm = float(input("CM: "))
        ft =round((0.0328 * cm),2)
        print(cm,"CM",ft, "Feet")


elif choice == 7:
    choice= int(input("1.gm to Kg \n 2.Kg to gm"))
    if choice == 1:
        gm =float(input("Enter the weight in gm: "))
        kg = gm/1000
        print(gm," gm = ",kg," kg")
    elif choice == 2:
        Kg =float(input("Enter the weight in Kg: "))
        gm=kg*1000
        print(kg," kg = ",gm," gm")


elif choice ==8:
    price=float(input("Enter original Price: "))
    discount=float(input("Enter discount(%): "))
    final_price= price - (price*discount/100)
    print("Price after discount = ",round(final_price, 2))