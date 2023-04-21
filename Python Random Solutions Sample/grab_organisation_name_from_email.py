import re

istr=input()

special=re.match(r"[\w\._@]+",istr)

rep=re.findall(r"@",istr)
r1 = re.findall(r"@.+",istr)
if(len(r1) and len(rep)==1 and len(special.group(0))==len(istr) ):print(r1[0][1:])
else: print("invalid email")
  
  
  
  
#   input is    : example1.Name@gmail.com
# output is : gmail.com

#   input is    : example1.name@@gmail.com
# output is : invalid email

#   input is    : example.namegmail.com
# output is : invalid email

#   input is    : example.-!name@gmail.com
# output is : invalid email



  
  
  
  
  
  
