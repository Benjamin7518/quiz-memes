password='abc123'
# 1 lowercase
# 1 uppercases
# 1 number
# minimun 8 letters
# 1 special character
length=len(password)
uppercase=0
lowercase=0
specialcharacters=0
number=0
valid=False
for i in password:
    if i.isupper():
        uppercase+=1
    elif i.islower():
        lowercase+=1
    elif i.isdigit():
        number+=1
    else:
        specialcharacters+=1
    

if length>8 and length<=20:
    if uppercase>0 and lowercase>0 and specialcharacters>0 and number>0:
        valid=True
    else:
        valid=False
else:
    valid=False
print(valid)




