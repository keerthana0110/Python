a=int(input("enter a year"))
if((a%400==0)or(a%4==0)and(a%100!=0)):
    print("the year is leap")
else:
    print("the year is not leap")
