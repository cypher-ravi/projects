# filename variables
import re


new_filename = "result.txt"
fileobj= open("contacts.txt", "r")
# regex = something@whatever.xxx
contents=fileobj.read()
r = re.compile(r'(\b[\w.]+@+[\w.]+.+[\w.]\b)')
results = r.findall(contents)
emails = ""
for x in results:
        emails += str(x)+"\n"

# function to write file
def writefile():
        f = open("new_filename", 'w')
        f.write(emails)
        f.close()
        print ("File written.")



p=open("new_filename","r")
if