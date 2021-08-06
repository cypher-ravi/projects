file=open("phone_numbers.txt", "w")
if file:
    file.write("phone numbers are:")

file.close()




f=open("phone_numbers.txt","r")

print(f.read())
