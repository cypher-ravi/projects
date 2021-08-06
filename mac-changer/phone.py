import re

file = open("contacts.txt", "r")

if file:
    print("file successfully opened")

contents = file.read()
x = re.findall(r"\d\d\d\d\d\d\d\d\d\d", contents)
y = '\n'.join(map(str, x))
print(y)


fileobj=open("phone_numbers.txt", "w")

fileobj.write(y)
if fileobj:
    print("file written successfully")


fileobj.close()


