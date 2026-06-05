import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','&',(',')]

print("welcome to password generator")
nr_letters=int(input("how many letters would you like in your password?\n"))
nr_symbols= int(input(f"how many symbols would you like"))
nr_numbers=int(input(f"how many numbers would you like"))


# passsword = ""

# for char in range(0, nr_letters):
#     password += random.choice(letters)

# for char in range(0,nr_symbols ):
#     password +=random.choice(symbols)

# for char in range(0,nr_numbers ):
#     password +=random.choice(numbers)

# print(password)            



password_list = []

for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password=""
for char in password_list:
    password+= char
print(f"your password is :{password}")    

