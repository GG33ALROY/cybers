import string

password = "hdnaknc!@#dASAKD3"

upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special_case = any([1 if c in string.punctuation else 0 for c in password])
digits_case = any([1 if c in string.digits else 0 for c in password])

print("Contains uppercase : ",upper_case)
print("Contains lowercase : ",lower_case)
print("Conatins special case : ",special_case)
print("Conatins digits : ",digits_case)

length = len(password)

score = 0

characters = [upper_case,lower_case,special_case,digits_case]

with open('common.txt','r') as f:
    common = f.read().splitlines()

if password in common:
    print("Password is common. Score: 0/7")
    exit()


if length > 8:
    score += 1

if length >12:
    score += 1

if length > 20:
    score += 2

print(f"Length of the password {str(length)} , adding {str(score)} points!")

if sum(characters) > 1:
    score +=1

if sum(characters) > 2:
    score +=1

if sum(characters) > 3:
    score +=1

print(f"Password has {str(sum(characters))} different character types, adding {str(sum(characters) -1)} points")

if score < 4:
    print(f"The password is quite weak! Score : {str(score)}/7")

elif score == 4:
    print(f"The password is ok! Score : {str(score)} /7")

elif score > 4 and score < 6:
    print(f"The password is good! Score : {str(score)} /7")

elif score >= 6 :
    print(f"The password is strong! Score : {str(score)} /7")


