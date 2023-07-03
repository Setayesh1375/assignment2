
print("sanie ra vared konin")

sanie=int(input())
if sanie>=3600 :
   hours =int( sanie/3600)
   x= sanie % 3600
   if x>60 :
     minute = int(x/60)
     sanie = x % 60
     print(hours , ":" , minute , ":" , sanie)
   elif x<60 :
      minute = 00
      sanie = x
      print(hours , ":" , minute , ":" , sanie)  


elif sanie<3600 :
   if  sanie >= 60 :
        hours = 00
        minute = int(sanie/60)
        y = sanie % 60
        sanie = y
        print(hours , ":" , minute , ":" , sanie)  
   elif  sanie<60 :
        hours = 00
        minute = 00
        sanie =sanie 
        print(hours , ":" , minute , ":" , sanie)
  

   

