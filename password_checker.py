
correct_password = "correct123"
name = input("Enter name:")
surname = input("Enter surname:")
password = input("Enter password:")
print(password)

while correct_password != password:
    password = input("Wrong password! Enter the password again:")

print("Hi", name, ", you're Logged In!")
message = "Hi %s %s, you're logged in" % (name, surname)
print(message)
