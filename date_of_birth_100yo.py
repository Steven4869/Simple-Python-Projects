#to take input as age or dob and tell user when they will hundred years old
print("This program is to determine your 100th age in that particular year \n")
currentyear=2020
while(True):
    age=int(input("Please enter your birth year\n"))
    if len(str(age))==4:
        if age>currentyear:
            print("you are not born yet")
            print("please try again")
            continue
        elif age<1920:
            print("you are too old")
        elif age<currentyear +1:
            temp=age + 100
            print(f"you will turn 100 year old in {temp}th year")
        tellage=int(input("please enter a year to know your age in that year\n"))
        if tellage<age:
            print("you are not born yet")
        elif tellage>=age:
            temp1=tellage-age
            print(f"you will be {temp1} years old in {tellage}")
        else:
            print("wrong input")
    elif age>0 and len(str(age))<4:
        if age>120:
            print("you are too old")
        
