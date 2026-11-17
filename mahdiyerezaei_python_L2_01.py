# python.py

# گرفتن نام کاربری و پسورد 
while True:
    username = input(" Enter username: ").strip()
    if username != "":
        break
    print(" Username cannot be empty. ")

while True:
    password = input(" Enter password: ").strip()
    if password != "":
        break
    print(" Password cannot be empty. ")

# امتیازدهی
score = 8
reasons = []

# بررسی‌ها
# طول بیشتر از 8
if len(password) <= 8:
    score -= 1
    reasons.append(" Password length must be more than 8 characters. ")

# حرف انگلیسی داشته باشد
has_letter = False
for char in password:
    if char.isalpha():
        has_letter = True
        break
if not has_letter:
    score -= 1
    reasons.append(" The password must contain at least one English letter. ")

# کاراکتر خاص داشته باشد
special = "!@$"
has_special = False
for char in password:
    if char in special:
        has_special = True
        break
if not has_special:
    score -= 1
    reasons.append(" The password must contain at least one special character (! or @ or $). ")

# حرف بزرگ داشته باشد
has_upper = False
for char in password:
    if char.isupper():
        has_upper = True
        break
if not has_upper:
    score -= 1
    reasons.append(" The password must contain at least one uppercase English letter. ")

# برابر با نام کاربری نباشد
if password == username:
    score -= 1
    reasons.append(" The password should not be the same as the username. ")

# swapcase نباشد
if password == username.swapcase():
    score -= 1
    reasons.append(" The password should not be the swapcase version of the username. ")

# جایگزینی خاص نباشد (a->@, i->!, s->$, o->0)
test_pass = password.lower().replace('a', '@').replace('i', '!').replace('s', '$').replace('o', '0')
if test_pass == username.lower().replace('a', '@').replace('i', '!').replace('s', '$').replace('o', '0'):
    score -= 1
    reasons.append(" The password should not be the same as the username but with special replacement characters. ")

# پسورد رایج نباشد
common = ["123456", "12345678", "12345", "111111", "qwerty", "asdfgh", "password", "admin"]
if password in common:
    score -= 1
    reasons.append(" Password is one of the most common and weak passwords. ")

# نمایش نتیجه
print("\n--- Security analysis result ---")
print(f" Final score : {score} از 8")
if score < 4:
    print(" Security level: Weak ")
elif score < 7:
    print(" Security level: medium ")
else:
    print(" Security level: strong ")

if reasons:
    print("\n List of improvements: ")
    for r in reasons:
        print(f"- {r}")
else:
    print(" The password is very strong. ")
