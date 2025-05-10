# to encode:
# if the string is > 3 characters then 
# 1. append the first letter in the end 
# 2. add 3 random characters in the start 
# 3. add 3 random characters in the end
# else the string is < 3 characters then reverse the string

# to dencode:
# if the string is > 3 characters then
# 1. remove 3 characters in the start 
# 2. remove 3 characters in the end 
# 3. append the last character to the start
# else the string is < 3 characters then reverse the string

# program should ask whether you want to encode or decode

def encode(normal):
    if(len(normal) > 3):
        step1 = normal[1:] + normal[0]
        step2 = "ahx"
        step3 = "zil"
        print(step2+step1+step3)

    else:
        print(normal[::-1])

def decode(normal):
    if(len(normal) > 3):
        step1 = normal[3:]
        step2 = step1[0:-3]
        step3 = step2[len(step2)-1] + step2[0:len(step2)-1]
        print(step3)

    else:
        print(normal[::-1])

normal = input("Enter a string: ")
operation = input("Do you want to encode or decode? ")
if operation == "encode":
    encode(normal)

elif operation == "decode":
    decode(normal)

else:
    print("Wrong choice, please select again!")