
print ("mohasebe miyangin nomarat")
print("nomre khod ra vared konid" )
print("khoroj: 1")
i=0
sum=0

while True :
    grade=float(input())
    sum=sum+grade
    i=i+1
    if grade==1:
       a=sum/(i-1)
       print("miyangin = " , a)
       break
