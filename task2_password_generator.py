import random
print("----PASSWORD GENERATOR----\n")

length=int(input("Enter the desired length of the password you want : "))

s="abcdefghijklmnopqrstuvwxyz"
alpha=random.sample(s,random.randint(1,4))
# print(alpha)

count="1234567890"
number=random.sample(count,random.randint(1,10))
# print(number)

character="!@#*$%&?~'^"
char=random.sample(character,random.randint(1,10))
# print(char)

combine=alpha+char+number

final=random.sample(combine,length)

password="".join(final)
print(password)
