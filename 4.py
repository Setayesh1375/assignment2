print (" mohasebe zaman be sanie")

hour = int(input("saat ra vared konin : "))
minute = int (input("daghighe ra vared konin : "))
second = int (input("sanie ra vared konin : "))
print (hour ,":" , minute , ":" , second)

hour= hour*3600
minute = minute*60
sanie = hour + minute + second
print("sanie",sanie)