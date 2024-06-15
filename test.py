
import secrets

a = secrets.SystemRandom().randrange(1,10)
print(a)
option = input("Enter a number: ")
option = int(option)
print(option)

if a == option:
    print("Hello World")
else:
    print("Sucks to suck")
