# Decision Making
x=10
if x==10:
    print("x is equal to 10")

y=21
if y%10==0:
    print("y is divisible by 10")
else:
    print("y is not divisible by 10")



signal="yellow"
if signal=="red":
    print("stop") 
elif signal=="yellow":
    print("ready")
        
else:
    print("go")


# signals=input("what is the color of the signal:")
# if signals=="red":
#     print("stop") 
# elif signals=="yellow":
#     print("ready")
        
# else:
#     print("go")




age=19
if age<=18:
    print("you are eligible to vote.")
else:
    print("you are not eligible to vote.")


#logical Operators:--
attendence=80
is_teacher_frend=True

if attendence<=75 or is_teacher_frend==True:
    print("exam")
else :
    print("Not give exam")


gender=input("gender >>> ")
age=int(input("age >>> "))

if gender=="female":
    print("Ticket is free.")
else:
    if age<5:
        print("Ticket is free.")
    elif age<=12:
        print("You get a child discount.")
    elif age>=60:
        print("you get a senior citizen discount.")
    else:
        print("you pay the full fare.")



#Ne