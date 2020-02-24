#a=2
#b=0
#print("execution1")
#try:
 #   c=a/b
#except ZeroDivisionError:
 #   print("error occured")
#print("execution2")

try:
    r=open("abc.txt","r")
    #print(r.read())

except:
    print("Error Occured")
else:
    print(r.read())


with open("abc.txt","a") as fopen:
    print(fopen.write("Shivam"))
